from app import db
from models.rol import Rol
import uuid

class Cuenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100))
    clave = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    persona = db.relationship('Persona', backref='cuentas', lazy=True)

    def serialize(self):
        return {
        'usuario': self.usuario,
        'external_id': self.external_id,
        'estado': self.estado,
    }