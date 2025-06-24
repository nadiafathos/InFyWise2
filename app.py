from il.app_runner.run import run
if __name__ == "__main__":
    run()

try:
    from flask import Flask, Blueprint
    from il.enum.env import EnvironmentVariable as Env
    from il.postgres_manager.postgres_manager import config_app_db_context
    import pkgutil
    import importlib

    from utils import Logger

    app = Flask(__name__)

    def get_app_config():
        app.config.update(Env.get_all())
        config_app_db_context(app) #Vient de postgres_manager dans il

    def register_blueprints():
        import api  # doit être un package (avec __init__.py)

        for finder, name, ispkg in pkgutil.iter_modules(api.__path__):
            module = importlib.import_module(f"api.{name}")
            bp = getattr(module, "bp", None)

            if isinstance(bp, Blueprint):
                app.register_blueprint(bp)

    def get_endpoint_list():
        Logger.info("Liste des endpoints disponibles :")

        for rule in sorted(app.url_map.iter_rules(), key=lambda r: (r.endpoint, r.rule) ):
            methods = ",".join(sorted(rule.methods - {"HEAD", "OPTIONS"}))
            Logger.info(
                msg=f" → {rule.endpoint}",
                prf= f'{str.upper(str.split(rule.endpoint, '.')[0])} : {methods}'
            )


    def create_flask_app():
        get_app_config()
        register_blueprints()
        get_endpoint_list()
        return app
except ImportError:
    pass