from app import db
import uuid
class Motivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=True)
    #RELACION DE 1 A MUCHOS
    #censo_persona_id = db.Column(db.Integer, db.ForeignKey('censo_persona.id'), nullable=False)
    censo_persona = db.relationship('CensoPersona', back_populates='motivo', lazy=True)
                                     #RELACION DE 1 
    #catalogos = db.relationship('Catalogo_Motivo', backref='motivo_censo', lazy=True) 
    
  