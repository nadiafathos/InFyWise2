from flask_sqlalchemy.session import Session

from dal.domain import Tag
from dal.extensions import db
from dal.repositories.base import BaseRepository


class TagRepository(BaseRepository[Tag]):
    def __init__(self):
        super().__init__(Tag, db.session)