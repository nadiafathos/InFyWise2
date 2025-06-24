from flask import Blueprint
from dal.utils.enums import Table
import inspect

def define_blueprint(table_name: Table) -> Blueprint:
    '''
    Méthode généralisant la logique de définition d'un blueprint.

    :param table_name: Le nom de la table en DB
    :return: Blueprint qui représente une collection de routes déclarées sans passer par l'instanciation d'un objet.
    '''
    caller_module = inspect.stack()[1].frame.f_globals['__name__']
    return Blueprint(table_name.value, caller_module, url_prefix=f'/{table_name.value}')