"""
install_requirements.py

Ce script crée un environnement virtuel (si nécessaire) puis installe
toutes les dépendances listées dans requirements.txt.
"""
import subprocess
from .init_project_helper import *


REQ_DIR = os.path.join(BASE_DIR, "il", 'requirements.txt')
def install(requirements_file: str = REQ_DIR):
    """
    Crée le venv si nécessaire et installe les dépendances depuis requirements.txt.

    :param requirements_file: Chemin vers le fichier requirements.txt
    """

    if not os.path.isfile(requirements_file):
        Logger.error(f"Fichier '{requirements_file}' introuvable.")
        sys.exit(1)

    create_venv_if_doesnt_exist(VENV_DIR)

    pip_exe = get_pip()
    Logger.info(f"Installation des dépendances depuis '{requirements_file}'...")
    try:
        subprocess.check_call([pip_exe, 'install', '-r', requirements_file])
        Logger.success("Toutes les dépendances ont été installées avec succès !")
    except subprocess.CalledProcessError as e:
        Logger.error(f"Échec de l'installation : {e}")
        sys.exit(e.returncode)


