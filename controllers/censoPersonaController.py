from models.censo_persona import CensoPersona
from models.motivo import Motivo
from models.persona import Persona
from app import db
import uuid

class CensoPersonaController:
    def listar(self):
        return CensoPersona.query.all()
    
    def listar_censados(self):
        return CensoPersona.query.filter_by(estado=True).all()
    
    def guardar_censop(self, data):
    # Crear una nueva Persona
        persona = Persona()
        persona.nombre = data.get("nombre")
        persona.apellido = data.get("apellido")
        persona.external_id = uuid.uuid4()
        db.session.add(persona)
        db.session.commit()

    # Crear un nuevo Motivo
        motivo = Motivo()
        motivo.nombre = data.get("motivo")
        motivo.external_id = uuid.uuid4()
        db.session.add(motivo)
        db.session.commit()

    # Crear un nuevo CensoPersona
        censoPersona = CensoPersona()
        censoPersona.latitud = data.get("latitud")
        censoPersona.longitud = data.get("longitud")
        censoPersona.motivoc = data.get("motivoc")
    
        censoPersona.fecha = data.get("fecha")
        censoPersona.external_id = uuid.uuid4()
        db.session.add(censoPersona)
        db.session.commit()

        return censoPersona.id


    def buscar_external_motivo(self,external):
        return Motivo.query.filter_by(external_id=external).first()
    
