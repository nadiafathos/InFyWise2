import os
from enum import Enum
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class EnvironmentVariable(Enum):
    DB_USER = ('DB_USER', 'user', str)
    DB_PASSWORD = ('DB_PASSWORD', 'password', str)
    DB_HOST = ('DB_HOST', 'localhost', str)
    DB_PORT = ('DB_PORT', 00, int)
    DB_NAME = ('DB_NAME', 'db', str)
    TRACK_MODIFICATIONS = ('TRACK_MODIFICATIONS', False, bool)
    DEBUG_MODE = ('DEBUG_MODE', False, bool)
    RUN_AS_TESTING =  ('RUN_AS_TESTING', False, bool)
    INIT_REQUIREMENTS = ('INIT_REQUIREMENTS', False, bool)

    def __init__(self, key: str, default, cast_type):
        self._key = key
        self._default = default
        self._cast_type = cast_type

    def get(self):
        """
        Récupère la valeur depuis l'env (os.environ),
        ou le default si absent, puis caste si besoin.
        """
        raw = os.environ.get(self._key, None)
        if raw is None:
            return self._default
        if self._cast_type is bool:
            return str(raw).strip().lower() in ('1','true','yes','on')
        return self._cast_type(raw)

    @classmethod
    def get_all(cls) -> dict:
        """
        Renvoie un dict {clé: valeur} pour tous les membres de l'Enum,
        en lisant directement os.environ (après load_dotenv).
        """
        return {member._key: member.get() for member in cls}
