from app import db
import uuid
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    estado_civil = db.Column(db.Boolean, default=True)
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), unique=True)
    rol = db.relationship('Rol', back_populates='persona')
    cuenta = db.relationship('Cuenta', back_populates='persona')
    #relacion de 1 a muchos 
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    censo_persona =  db.relationship('CensoPersona', back_populates='persona', lazy=True)


    def serialize(self):
        return {
        'nombre': self.nombre,
        'apellido': self.apellido,
        'estado_civil': self.estado_civil,
        'external_id': self.external_id,
        'rol_external_id': self.rol.external_id if self.rol else None,
    }


 