from utils import Logger
from . import tools as config_manager
from il import EnvironmentVariable as Env

REQUIREMENTS = config_manager.requirements
FLASK = config_manager.flask

def run():
    if Env.INIT_REQUIREMENTS.get():
        Logger.warn(f"Le mode initialisation est activé. Vérification de la présence des dépendances projet :")
        REQUIREMENTS.install()
    FLASK.run()




if __name__ == "__main__":
    run()