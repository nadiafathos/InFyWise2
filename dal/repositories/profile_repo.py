from flask_sqlalchemy.session import Session

from dal.domain import Profile
from dal.extensions import db
from dal.repositories.base import BaseRepository


class ProfileRepository(BaseRepository[Profile]):
    def __init__(self):
        super().__init__(Profile, db.session)