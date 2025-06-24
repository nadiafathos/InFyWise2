import sys

from flask import Flask
from sqlalchemy import create_engine, text

from dal.extensions import db
from il.enum.app_config import AppConfiguration
from il.enum.env import EnvironmentVariable
from utils import Logger

env = EnvironmentVariable
config = AppConfiguration

def get_pg_db_uri(db_name: str = env.DB_NAME.get()):
    """
    Retourne l'URL de connexion à PostgreSQL.
    """
    user = env.DB_USER.get()
    password = env.DB_PASSWORD.get()
    host = env.DB_HOST.get()
    port = env.DB_PORT.get()

    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

def get_pg_modif_tracker():
    """
    Indique si Flask-SQLAlchemy doit suivre les modifications des objets.
    Lit la variable TRACK_MODIFICATIONS dans l'env (true/false),
    sinon renvoie False par défaut.
    """
    return env.TRACK_MODIFICATIONS.get()

def create_db_if_doesnt_exists():
    """
        Se connecte d'abord à la base système 'postgres' en AUTOCOMMIT,
        vérifie si la base cible existe, et la crée si nécessaire.
    """

    try:
        engine = create_engine(
            get_pg_db_uri('postgres'),
            isolation_level='AUTOCOMMIT',
            connect_args={'options': '-c client_encoding=UTF8'}
        )

        with engine.connect() as conn :
            find_db_query = text("SELECT 1 FROM pg_database WHERE datname = :name")
            find_db_params = { 'name': env.DB_NAME.get() }

            db_exists = conn.execute(find_db_query, find_db_params).scalar() is not None

            if db_exists:
                Logger.info(f"Présence DB validée.")
            else:
                Logger.warn(f"DB : {env.DB_NAME.get()} inexistante. Début de la création...")

                create_db_query = text(f"CREATE DATABASE {env.DB_NAME.get()} ENCODING 'UTF8'")
                conn.execute(create_db_query)

                Logger.success("DB créée avec succès.")
    except Exception as e:
        Logger.error(f"Erreur lors de la création de la DB : {env.DB_NAME.get()} : {e}")
        sys.exit(1)

def config_app_db_context(app: Flask):
    create_db_if_doesnt_exists()
    app.config[config.SQLALCHEMY_DATABASE_URI.value] = get_pg_db_uri()
    app.config[config.SQLALCHEMY_TRACK_MODIFICATIONS.value] = get_pg_modif_tracker()

    db.init_app(app)

    with app.app_context():
        db.create_all()



