from dal.utils.enums import PostTagCol,UserCol, Table, Entity
from dal.extensions import db
from dal.utils.dal_helper import get_fk

# Association table for Many-to-Many Post<->Tag
post_tags = db.Table(
    Table.POST_TAG.value,

    db.Model.metadata,

    db.Column(
        PostTagCol.FK_POST.value,
        db.Integer,
        db.ForeignKey( get_fk(Table.POST.value) ), primary_key=True),

    db.Column(
        PostTagCol.FK_TAG.value,
        db.Integer,
        db.ForeignKey( get_fk(Table.TAG.value) ), primary_key=True)
)

class Post(db.Model):
    __tablename__ = Table.POST.value
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey(get_fk(Table.USER.value)))

    author = db.relationship(Entity.USER.value, back_populates=UserCol.POSTS.value)
    tags = db.relationship(Entity.TAG.value, secondary=post_tags, back_populates=UserCol.POSTS.value)