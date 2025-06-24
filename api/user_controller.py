from api.base import BaseController
from api.helpers import define_blueprint
from api.schemas.user import UserRequestSchema, UserResponseSchema
from bll import UserService
from bll.schemas.user import UserIn
from dal.utils.enums import Table

bp = define_blueprint(Table.USER)

UserController = BaseController(
    blueprint=bp,
    service= UserService(),
    req_schema=UserRequestSchema,
    resp_schema=UserResponseSchema,
    dto_class=UserIn
)