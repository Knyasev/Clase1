from models.persona import Persona
from models.rol import Rol
from models.cuenta import Cuenta
from app import db
import uuid

class PersonaController:
    def listPerson(self):
        return Persona.query.all()
    
    def save(self, data):
        persona = Persona()
        persona.apellido = data.get("apellido")
        persona.nombre = data.get("nombre")
        persona.estado_civil  = data.get("edad")
        persona.external_id = uuid.uuid4()
        db.session.add(persona)
        db.session.commit()
        return persona.id