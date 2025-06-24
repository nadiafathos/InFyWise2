import inspect
import os
from sys import prefix


class Logger:
    """
    Logger simple pour la console avec couleurs ANSI.

    Méthodes disponibles :
      - info(msg)
      - warn(msg)
      - error(msg)
      - success(msg)
      - debug(msg)
      
      # from logging import Logger notez qu'il existe déjà un logger tout fait en python
    """

    # Codes ANSI pour les couleurs
    RESET   = '\033[0m'
    COLORS  = {
        'info': '\033[34m',  # bleu
        'warn': '\033[33m',  # jaune
        'error': '\033[31m',  # rouge
        'success': '\033[32m',  # vert
        'debug': '\033[35m',  # magenta
    }

    @classmethod
    def _get_caller(cls) -> str:
        """
        Récupère le fichier ou module ayant appelé la méthode de log.
        """
        # inspect.stack()[3] : 0=_get_caller,1=_log,2=info()/warn()/...,3=appelant réel
        try:
            frame = inspect.stack()[3].frame
            filename = frame.f_globals.get('__file__', frame.f_code.co_filename)
            return os.path.basename(filename)
        except IndexError:
            return ''

    @classmethod
    def _log(cls, level: str, msg: str, prf: str = '') -> None:
        color = cls.COLORS.get(level, '')
        caller = cls._get_caller()

        if prf != '':
            prefix = f"[{prf}]"
        else:
            if caller:
                prefix = f"[{level.upper()} {caller}]"
            else:
                prefix = f"[{level.upper()}]"

        print(f"{color}{prefix} {msg}{cls.RESET}")

    @classmethod
    def info(cls, msg: str, prf: str = '') -> None:
        """Message d'information (bleu)"""
        cls._log('info', msg, prf)

    @classmethod
    def warn(cls, msg: str, prf: str = '') -> None:
        """Message d'avertissement (jaune)"""
        cls._log('warn', msg, prf)

    @classmethod
    def error(cls, msg: str, prf: str = '') -> None:
        """Message d'erreur (rouge)"""
        cls._log('error', msg, prf)

    @classmethod
    def success(cls, msg: str, prf: str = '') -> None:
        """Message de succès (vert)"""
        cls._log('success', msg, prf)

    @classmethod
    def debug(cls, msg: str, prf: str = '') -> None:
        """Message de debug (magenta)"""
        cls._log('debug', msg, prf)
