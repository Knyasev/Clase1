from app import db
import uuid

class Censo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.DateTime)
    fecha_fin = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    external_id = db.Column(db.String(60), default=str(uuid.uuid4()),nullable=False)
    censos = db.relationship('CensoPersona', backref='censo', lazy=True)

@property
def fecha_inicio(self):
        return self._fecha_inicio

@fecha_inicio.setter
def fecha_inicio(self, value):
        if not value:
            raise ValueError("La fecha de inicio no puede estar vacía")
        self._fecha_inicio = value

@property
def fecha_fin(self):
        return self._fecha_fin

@fecha_fin.setter
def fecha_fin(self, value):
        if not value:
            raise ValueError("La fecha de fin no puede estar vacía")
        self._fecha_fin = value


@property
def external_id(self):
        return self._external_id

@external_id.setter
def external_id(self, value):
        if not value:
            raise ValueError("El external_id no puede estar vacío")
        self._external_id = value

