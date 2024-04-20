from app import db
import uuid

class Catalogo_Motivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
    estado = db.Column(db.Boolean, default=True)
    #RELACION  MUCHOS
    motivo_censo_id = db.Column(db.Integer, db.ForeignKey('motivo__censo.id'), nullable=False)
    motivo_censo = db.relationship('Motivo_Censo', backref=db.backref('catalogos', lazy=True))