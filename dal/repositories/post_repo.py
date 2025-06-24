from flask_sqlalchemy.session import Session

from dal.domain import Post
from dal.extensions import db
from dal.repositories.base import BaseRepository


class PostRepository(BaseRepository[Post]):
    def __init__(self):
        super().__init__(Post, db.session)