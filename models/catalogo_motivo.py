from app import db
import uuid

class Motivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    estado = db.Column(db.Boolean, default=True)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
    catalogo_id = db.Column(db.Integer, db.ForeignKey('catalogo.id'), nullable=False)
    catalogo = db.relationship('Catalogo', backref=db.backref('motivos', lazy=True))
