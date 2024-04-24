from app import db
import uuid

class CensoPersona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    longitud = db.Column(db.Numeric(), nullable=False)
    latitud = db.Column(db.Numeric(), nullable=False)
    motivo = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
        #RELACION DE 1 A MUCHOS
    censo_id =  db.Column(db.Integer, db.ForeignKey('censo.id'), nullable=False)
    persona_id =  db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    persona = db.relationship('Persona', back_populates='censo_persona')
    motivo_censo = db.relationship('Motivo_Censo', back_populates='censo_persona', lazy=True) 
    #RELACION DE 1
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    persona = db.relationship('Persona', back_populates='censo_persona')