from models.persona import Persona
from models.rol import Rol
from models.cuenta import Cuenta
from app import db
import uuid

class PersonaController:
    def listar(self):
        return Persona.query.all()
    
    def save(self, data):
        persona = Persona()
        persona.apellido = data.get("apellido")
        persona.nombre = data.get("nombre")
        persona.estado_civil  = data.get("estado_civil")
        persona.external_id = uuid.uuid4()
        persona.rol_id = data.get("rol_id")
        db.session.add(persona)
        db.session.commit()
        return persona.id
    
    def guardar_censado(self,data):
        rol = Rol.query.filter_by(nombre="CENSADO").first()
        persona = Persona()
        if rol:
            persona.external_id = uuid.uuid4()
            persona.apellido = data.get("apellido")
            persona.nombre = data.get("nombre")
            persona.estado_civil = data.get("estado_civil")
            persona.rol_id = rol.id
            db.session.add(persona)
            db.session.commit()
            return  persona.id
        else:
            return -1
        
    def guardar_censador(self,data):
        rol = Rol.query.filter_by(nombre="CENSADOR").first()
        persona = Persona()
        if rol:
            cuenta = Cuenta.query.filter_by(usuario=data.get("correo")).first()
            if cuenta:
                return -2
            else:

                persona.external_id = uuid.uuid4()
                persona.apellido = data.get("apellido")
                persona.nombre = data.get("nombre")
                persona.estado_civil = data.get("estado_civil")
                persona.rol_id = rol.id
                db.session.add(persona)
                db.session.commit()

                cuenta = Cuenta()
                cuenta.usuario = data.get("correo")
                cuenta.clave = data.get("clave")
                cuenta.persona_id = persona.id
                cuenta.external_id = str(uuid.uuid4())
                db.session.add(cuenta)
                db.session.commit()
            return  cuenta.id
        else:
            return -1

    def buscar_external(self, external):
        return Persona.query.filter_by(external_id=external).first()
    
    
    def modificar(self, external_id, data):
        persona = self.buscar_external(external_id)
        if persona:
            persona.apellido = data.get("apellido")
            persona.nombre = data.get("nombre") 
            persona.estado_civil = data.get("estado_civil")
            persona.fecha_nacimiento = data.get("fecha_nacimiento")

            db.session.add(persona)
            db.session.commit()
            return persona
        else:
            return -1
        

    def modificar_censador(self,external_id,data):
        persona = self.buscar_external(external_id)
        if persona:
            persona.apellido = data.get("apellido")
            persona.nombre = data.get("nombre")
            persona.estado_civil = data.get("estado_civil")
            persona.fecha_nacimiento = data.get("fecha_nacimiento")
            db.session.add(persona)
            db.session.commit()
            cuenta = Cuenta.query.filter_by(usuario=data.get("correo")).first()
            if cuenta:
                cuenta.usuario = data.get("correo")
                cuenta.clave = data.get("clave")
                cuenta.persona_id = persona.id
                db.session.add(cuenta)
                db.session.commit()
            return persona
        else:
            return -1