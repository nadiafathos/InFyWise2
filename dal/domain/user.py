from dal.utils.enums import PostCol, ProfileCol, Table, Entity
from dal.extensions import db

class User(db.Model):
    __tablename__ = Table.USER.value

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # One-to-One
    profile = db.relationship(Entity.PROFILE.value, back_populates=ProfileCol.USER.value, uselist=False)

    # One-to-Many
    posts   = db.relationship(Entity.POST.value, back_populates=PostCol.AUTHOR.value, cascade='all, delete')
