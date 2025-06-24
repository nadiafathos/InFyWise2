import subprocess

from il import EnvironmentVariable as Env
from flask import Flask
from utils import Logger
from app import create_flask_app

from .init_project_helper import *
"""
flask_runner.py

Ce module permet d'activer automatiquement l'environnement virtuel et de lancer
une application Flask en mode développement sans avoir à passer manuellement
par l'activation du venv et l'appel à flask run.

Fonctions exposées :
  - define_flask_default_env() : définit les variables d'environnement Flask par défaut.
  - get_python() : retourne le chemin de l'exécutable Python dans le venv.
  - main() : point d'entrée principal qui construit et exécute la commande Flask.
"""

def define_flask_env():
    """
        Définit les variables d'environnement minimales pour Flask.

        FLASK_APP : nom du fichier python où est définie l'application Flask (par défaut "app.py").
        FLASK_ENV : mode d'exécution de Flask ("development" pour activer le debug et le rechargement).

        """
    os.environ.setdefault("FLASK_APP", "app.py")
    os.environ.setdefault("FLASK_ENV", "development")
    os.environ.setdefault("FLASK_TEST", "testing")
    os.environ.setdefault("APP_SETTINGS", "config.TestingConfig")
    os.environ["FLASK_APP"] = "app:create_flask_app()"

def run(testing: bool = Env.RUN_AS_TESTING.get()):
    """
        Point d'entrée principal du script.

        1. Définit les variables d'environnement Flask via define_flask_default_env().
        2. Détermine le bon exécutable Python dans le venv via get_python().
        3. Construit la commande ['python', '-m', 'flask', 'run'].
        4. Exécute cette commande et remonte toute erreur éventuelle.

        Usage python app_runner/flask_runner.py

        Le serveur Flask démarrera en mode développement sur http://127.0.0.1:5000/.
        """
    define_flask_env()

    try:
        if testing:
            cmd = [get_python(), "-m", "pytest", "--maxfail=1", "--disable-warnings"]
            Logger.info(f"Lancement de Flask en mode test via : {cmd}")
            subprocess.check_call(cmd, cwd=BASE_DIR)

        else:
            create_flask_app().run(
                host=Env.HOST.get(),
                port=Env.PORT.get(),
            )
    except subprocess.CalledProcessError as e :
        Logger.error(f"Flask s'est arrêté avec l'erreur : {e}")
        sys.exit(e.returncode)

if __name__ == "__main__":
    run()