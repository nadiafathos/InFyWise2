from sqlalchemy.orm import relationship

from dal.utils.enums import PostCol, ProfileCol, Table, Entity

from datetime import datetime, timezone
from sqlalchemy import Enum, DateTime, Date, ForeignKey
from dal.utils.enums import ProfileCol, Table, Entity
from dal.extensions import db


class User(db.Model):

    __tablename__ = Table.USER.value
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    first_name =db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128),nullable= False)

    registration_date= db.Column(DateTime,default=lambda:datetime.now(timezone.utc),nullable=False)

    role_id = db.Column(db.Integer,ForeignKey("role.id"),nullable=False)
    role = relationship("Role",back_populates="users")

    def  __repr__(self):
        return f"<user {self.first_name} {self.last_name} ({self.role.name}"





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


class Doctor(User):

    __tablename__ = "doctor"

    id = db.Column(db.Integer,ForeignKey("users.id"),primary_key=True)
    speciality= db.Column(db.String(100))
    hospital = db.Column(db.String(100))

    __mapper_args__ ={
        "polymorphic_identity":"doctor",
    }
    # relationship

    appointments = db.relationship("Appointment",backref="doctor",lazy="joined")

    validations = db.relationship("Validation",backref="doctor",lazy="joined")


class Admin(User):
    __tablename__ ="admins"

    id_admin = db.Column(db.Integer,ForeignKey("users.id"),primary_key=True)

    __mapper_args__= {
        "polymorphic_identity":"admin",

    }


#RELATIONSHIP

disease_file = db.relationship("DiseaseFile",backref="admin",lazy="joined")
moderated_testimonies =db.relationship("Testimony",backref="moderator",lazy="joined",foreign_keys ="Testimony.moderated_by")
