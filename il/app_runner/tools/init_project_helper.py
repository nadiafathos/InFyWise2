import os
import sys
import subprocess
import venv

from utils import Logger

BASE_DIR = os.path.abspath( os.path.join( os.path.dirname(__file__), "../../.." ) )
VENV_DIR = os.path.join(BASE_DIR, ".venv")

def get_python():
    """
    Détermine et retourne le chemin absolu de l'exécutable Python du venv.

    Le venv doit se trouver dans le répertoire parent du dossier contenant ce script,
    sous le nom ".venv".

    :return  str Chemin vers python.exe (Windows) ou python (macOS/Linux) dans le venv.
    :raise SystemExit Si le fichier Python n'est pas trouvé dans le venv.
    """
    if sys.platform == "win32":
        python = os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        python = os.path.join(VENV_DIR, "bin", "python")

    if not os.path.isfile(python):
        Logger.error(
            f"""
            Impossible de trouver python depuis le venv ({python})
            Assure-toi que le dossier {VENV_DIR} existe et contient un venv valide.
            """)
        sys.exit(1)

    return python

def get_pip():
    if sys.platform =="win32":
        pip_exe = os.path.join(VENV_DIR, "Scripts", "pip.exe")
    else:
        pip_exe = os.path.join(VENV_DIR, "bin", "pip")

    if not os.path.isfile(pip_exe):
        Logger.error(f"Impossible de trouver pip dans {pip_exe}")
        sys.exit(1)

    return pip_exe

def create_venv_if_doesnt_exist(path: str = VENV_DIR):
    """Crée un venv avec pip s'il n'existe pas déjà."""
    if not os.path.isdir(path):
        Logger.info(f"Création de l'env virtuel dans ./{path}...")
        venv.EnvBuilder(with_pip=True).create(path)
    else:
        Logger.info("L'environnement virtuel existe déjà.")