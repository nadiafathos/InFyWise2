from dal.utils.enums import UserCol, Table, Entity
from dal.utils.dal_helper import get_fk
from dal.extensions import db

class Profile(db.Model):
    __tablename__ = Table.PROFILE.value
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(200))
    user_id  = db.Column(db.Integer, db.ForeignKey( get_fk(Table.USER.value) ))

    user = db.relationship(Entity.USER.value, back_populates=UserCol.PROFILE.value)