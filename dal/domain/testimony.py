from dal.extensions import db
from dal.utils.enums import PostCol, Table, Entity


class Tag(db.Model):
    __tablename__ = Table.TAG.value
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50), unique=True, nullable=False)

    posts = db.relationship(Entity.POST.value, secondary=Table.POST_TAG.value, back_populates=PostCol.TAGS.value)