from http import HTTPMethod, HTTPStatus
from typing import Type, Any

from flask import request, jsonify, abort, Blueprint
from marshmallow import ValidationError

from api.enum.endpoint_crud import EndpointCrud
from bll.base.base_service import BaseService


class BaseController:
    """
    Controller CRUD générique.
    - blueprint: instance de Blueprint
    - service: couche métier avec create, get, get_all, update, delete, get_by
    - req_schema: Schema Marshmallow pour requêtes
    - resp_schema: Schema Marshmallow pour réponses
    """
    def __init__(
        self,
        blueprint: Blueprint,
        service: BaseService,
        req_schema: Type,
        resp_schema: Type,
        dto_class: Type
    ):
        self.bp = blueprint
        self.svc = service
        self.req_schema = req_schema()
        self.resp_schema = resp_schema()
        self.dto_class = dto_class
        self.register_routes()

    def register_routes(self):
        prefix = self.bp.url_prefix or ''
        self.bp.add_url_rule(EndpointCrud.GET_ALL.value, endpoint='get_all', view_func=self.get_all, methods=[HTTPMethod.GET])
        self.bp.add_url_rule(EndpointCrud.CREATE.value, endpoint='create', view_func=self.create, methods=[HTTPMethod.POST])
        self.bp.add_url_rule(f'{EndpointCrud.GET.value}/<int:id>', endpoint='get', view_func=self.get, methods=[HTTPMethod.GET])
        self.bp.add_url_rule(f'{EndpointCrud.GET_BY.get()}/<string:column>/<string:value>',endpoint='get_by',view_func=self.get_by, methods=[HTTPMethod.GET])
        self.bp.add_url_rule(f'{EndpointCrud.UPDATE.value}/<int:id>', endpoint='update', view_func=self.update, methods=[HTTPMethod.PUT])
        self.bp.add_url_rule(f'{EndpointCrud.DELETE.value}/<int:id>', endpoint='delete', view_func=self.delete, methods=[HTTPMethod.DELETE])

    def get_all(self) -> Any:
        """Liste toutes les entités"""
        items = self.svc.get_all()
        return jsonify(self.resp_schema.dump(items, many=True)), HTTPStatus.OK

    def get(self, id: int) -> Any:
        """Récupère une entité par id"""
        item = self.svc.get(id)
        if item is None:
            abort(HTTPStatus.NOT_FOUND)
        return jsonify(self.resp_schema.dump(item)), HTTPStatus.OK

    def get_by(self, column: str, value: Any):
        """
        Recherche dynamique par nom de colonne et valeur.
        GET /by/<column>/<value>
        """
        item = self.svc.get_by(column, value)
        if item is None:
            abort(HTTPStatus.NOT_FOUND)
        return jsonify(self.resp_schema.dump(item)), HTTPStatus.OK

    def create(self) -> Any:
        """Crée une entité"""
        try:
            raw = request.get_json() or {}
            data_dict = self.req_schema.load(raw)
            dto = self.dto_class(**data_dict)
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST
        created = self.svc.create(dto)
        return jsonify(self.resp_schema.dump(created)), HTTPStatus.CREATED

    def update(self, id: int) -> Any:
        """Met à jour une entité"""
        try:
            data = self.req_schema.load(request.get_json() or {})
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.NOT_ACCEPTABLE
        updated = self.svc.update(id, data)
        if updated is None:
            abort(HTTPStatus.NOT_FOUND)
        return jsonify(self.resp_schema.dump(updated)), HTTPStatus.OK

    def delete(self, id: int) -> Any:
        """Supprime une entité"""
        success = self.svc.delete(id)
        if not success:
            abort(HTTPStatus.NOT_FOUND)
        return '', HTTPStatus.NO_CONTENT
