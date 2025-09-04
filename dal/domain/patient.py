

from dal.utils.enums import PostCol, ProfileCol, Table, Entity

from datetime import datetime, timezone
from sqlalchemy import Enum, DateTime, Date, ForeignKey
from dal.extensions import db

class Patient(db.Model):
    __tablename__ = Table.PATIENT.value
    id = db.Column(db.Integer,ForeignKey("users.id"),primary_key=True)
    birth_date= db.Column(Date,nullable=False)




#relationship
#relations one to many
symptoms = db.relationship('SymptomEntry',backref='patient',lazy="joined")
appointments = db.relationship('Appointment',backref='patient',lazy="joined")
testimonies = db.relationship('Testimony',backref='patient',lazy="joined")

def __repr__(self):


    return f"<Patient {self.id_patient}>"
