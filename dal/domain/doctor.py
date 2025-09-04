
from sqlalchemy.orm import relationship

from dal.utils.enums import PostCol, ProfileCol, Table, Entity


from sqlalchemy import Enum, DateTime, Date, ForeignKey
from dal.utils.enums import ProfileCol, Table, Entity
from dal.extensions import db

class Doctor(db.Model):
    """
    Table qui stocke les informations spécifiques aux docteurs.
    Chaque doctor est lié à un utilisateur existant dans la table User.
    """
    __tablename__ =Table.DOCTOR.value

    # Clé primaire et clé étrangère vers User
    id_doctor = db.Column(db.Integer, ForeignKey("users.id"), primary_key=True)

    # Données spécifiques au docteur
    speciality = db.Column(db.String(100))  # Spécialité médicale
    hospital = db.Column(db.String(100))    # Hôpital d'affectation

    # Relations
    # Un docteur peut gérer plusieurs rendez-vous
    appointments = relationship("Appointment", backref="doctor", lazy="joined")
    # Un docteur peut valider plusieurs entrées de symptômes
    validations = relationship("Validation", backref="doctor", lazy="joined")

    def __repr__(self):
        """
        Affichage lisible pour le debug.
        Exemple : <Doctor 2 (Cardiologue)>
        """
        return f"<Doctor {self.id_doctor} ({self.speciality})>"
