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


    #GETTERS AND SETTERS
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = value

    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, value):
        if not value:
            raise ValueError("La descripcion no puede estar vacía")
        self._descripcion = value

    @property
    def external_id(self):
        return self._external_id
    
    @external_id.setter
    def external_id(self, value):
        if not value:
            raise ValueError("El external_id no puede estar vacío")
        self._external_id = value

    