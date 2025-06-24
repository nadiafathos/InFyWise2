from api.base import BaseController
from api.helpers import define_blueprint
from api.schemas.post import PostRequestSchema, PostResponseSchema
from bll import PostService
from bll.schemas.post import PostIn
from dal.utils.enums import Table

bp = define_blueprint(Table.POST)

PostController = BaseController(
    blueprint=bp,
    service= PostService(),
    req_schema=PostRequestSchema,
    resp_schema=PostResponseSchema,
    dto_class=PostIn
)