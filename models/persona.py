from app import db
import uuid
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    estado_civil = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)
    rol = db.relationship('Rol', backref=db.backref('personas', lazy=True))
    #relacion de 1 a muchos 
    censoPersona = db.relationship('Censo', backref='persona', lazy=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    