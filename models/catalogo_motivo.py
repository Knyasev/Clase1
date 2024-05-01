from app import db
import uuid

class Catalogo_Motivo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(100)) 
    estado = db.Column(db.Boolean, default = True)
    external_id = db.Column(db.String(60),default = str(uuid.uuid4()),nullable=False)
    #Relacion de catalogo con motivo_censo
    #motivo_censo_id = db.Column(db.Integer,db.ForeignKey("motivo__censo.id"),nullable = False)
    #catalogo = db.relationship('Motivo_Censo', backref='catalogo_motivo', lazy=True)