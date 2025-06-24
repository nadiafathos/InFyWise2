try:
    from il.enum.env import EnvironmentVariable
    from utils import Logger
    from . import tools as config_manager

    REQUIREMENTS = config_manager.requirements
    FLASK = config_manager.flask

    def run():
        if EnvironmentVariable.INIT_REQUIREMENTS.get():
            Logger.warn(f"Le mode initialisation est activé. Vérification de la présence des dépendances projet :")
            REQUIREMENTS.install()
        FLASK.run()




    if __name__ == "__main__":
        run()
except ImportError:
    from .tools.requirements_installer import install
    install()