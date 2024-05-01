from app import db
import uuid

class CensoPersona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    longitud = db.Column(db.Numeric(), nullable=False)
    latitud = db.Column(db.Numeric(), nullable=False)
    motivoc = db.Column(db.String(160), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
        #RELACION DE 1 A MUCHOS
    censo_id =  db.Column(db.Integer, db.ForeignKey('censo.id'), nullable=False)
    persona_id =  db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    persona = db.relationship('Persona', back_populates='censo_persona')
    motivo_id =  db.Column(db.Integer, db.ForeignKey('motivo.id'), nullable=False)
    motivo = db.relationship('Motivo', back_populates='censo_persona', lazy=True) 
    
    def serialize(self):
        return {
            'fecha': self.fecha,
            'longitud': str(self.longitud),
            'latitud': str(self.latitud),
            'motivoc': self.motivoc,
            'external_id': self.external_id,
        }