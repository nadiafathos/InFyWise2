from sqlalchemy.orm import relationship

from dal.utils.enums import  Table
from dal.extensions import db
from dal.utils.dal_helper import get_fk

class Role(db.Model):
    __tablename__=Table.ROLE.value
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(50),unique=True,nullable=False)
    description = db.Column(db.String(150),nullable=True)

#relation bi directionnelle avec user et role .user donne le n om de tous les utiliszteurs ayant ce role
    #

    users = relationship("User",back_populates="role")

    def __repr__(self):
       return f"<Role {self.name}>"