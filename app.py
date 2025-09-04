from flask import Flask, Blueprint

from dal.extensions import db
from il import EnvironmentVariable as Env, config_app_db_context, app_runner, AppConfiguration as AppConfig
import pkgutil
import importlib

from utils import Logger

app = Flask(__name__)

def get_app_config():
    app.config.update(Env.get_all())
    app.config[AppConfig.ENVIRONMENT.value] = Env.ENVIRONMENT.get()
    app.config[AppConfig.DEBUG.value] = Env.DEBUG_MODE.get()
    config_app_db_context(app)

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
            msg=f" → {rule}",
            prf= f'{str.upper(str.split(rule.endpoint, '.')[0])} : {methods}'
        )

def register_models(package_name: str):
    """
    Parcourt récursivement tous les sous-modules du package donné
    et les importe, ce qui enregistre vos classes db.Model.
    """
    pkg = importlib.import_module(package_name)
    for finder, name, is_pkg in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        importlib.import_module(name)

def create_flask_app() -> Flask:
    register_models("dal.domain")
    get_app_config()
    register_blueprints()
    get_endpoint_list()
    return app

if __name__ == "__main__":
    app_runner.run()