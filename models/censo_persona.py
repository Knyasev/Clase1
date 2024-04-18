from app import db
import uuid

class CensoPersona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
        #RELACION DE 1 A MUCHOS
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    persona = db.relationship('Persona', backref=db.backref('censoPersona'))
    censo_id = db.Column(db.Integer, db.ForeignKey('censo.id'), nullable=False)
    censo = db.relationship('Censo', backref=db.backref('censos'))
    #RELACION DE 1
    motivo_censos = db.relationship('Motivo_Censo', backref='censo_persona', lazy=True)