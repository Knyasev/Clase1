from app import db
import uuid

class Censo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.DateTime)
    fecha_fin = db.Column(db.DateTime)
    motivo = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
    censo_persona =  db.relationship('CensoPersona', backref='censo', lazy=True)
    
    
    def serialize(self):
        return {
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            'estado': self.estado,
            'external_id': self.external_id,
    }