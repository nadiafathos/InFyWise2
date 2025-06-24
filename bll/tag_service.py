from bll.base.base_service import BaseService
from bll.schemas.tag import TagIn, TagOut
from dal.repositories import TagRepository
from dal.utils.enums import Entity


class TagService(BaseService[TagIn, TagOut, Entity.TAG]):
    def __init__(self):
        super().__init__(TagRepository())

    def _to_out(self, model) -> TagOut:
        return TagOut(id=model.id, name=model.name)