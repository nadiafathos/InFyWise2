from flask_sqlalchemy.session import Session

from dal.domain import User
from dal.extensions import db
from dal.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User, db.session)