from app import db
import uuid

class CensoPersona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    longitud = db.Column(db.Numeric(), nullable=False)
    latitud = db.Column(db.Numeric(), nullable=False)
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

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        if not value:
            raise ValueError("La fecha no puede estar vacía")
        self._fecha = value

    @property
    def longitud(self):
        return self._longitud
    
    @longitud.setter
    def longitud(self, value):
        if not value:
            raise ValueError("La longitud no puede estar vacía")
        self._longitud = value

    @property
    def latitud(self):
        return self._latitud
    
    @latitud.setter
    def latitud(self, value):
        if not value:
            raise ValueError("La latitud no puede estar vacía")
        self._latitud = value

    @property
    def external_id(self):
        return self._external_id
    
    @external_id.setter
    def external_id(self, value):
        if not value:
            raise ValueError("El external_id no puede estar vacío")
        self._external_id = value