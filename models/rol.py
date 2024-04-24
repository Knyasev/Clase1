from app import db

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.String(60))
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), unique=True)
    persona = db.relationship("Persona", back_populates="rol")
