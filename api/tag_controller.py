from api.base import BaseController
from api.helpers import define_blueprint
from api.schemas.tag import TagResponseSchema, TagRequestSchema
from bll import TagService
from bll.schemas.tag import TagIn
from dal.utils.enums import Table

bp = define_blueprint(Table.TAG)

TagController = BaseController(
    blueprint=bp,
    service= TagService(),
    req_schema=TagRequestSchema,
    resp_schema=TagResponseSchema,
    dto_class=TagIn
)