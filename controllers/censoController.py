from models.censo import Censo
from models.censo_persona import CensoPersona
from models.motivo import Motivo
from app import db
import uuid

class CensoController:
    def listar(self):
        return Censo.query.all()
    
    def save(self, data):
        censo = Censo()
        censo.fecha_inicio = data.get("fecha_inicio")
        censo.fecha_fin = data.get("fecha_fin")
        censo.estado = data.get("estado")
        censo.motivo = data.get("motivo")
        censo.external_id = uuid.uuid4()
        db.session.add(censo)
        db.session.commit()
        return censo.id
    

    def modificar(self, data):
        censo = self.buscar_external(data.get("external_id"))
        if censo:
            censo.fecha_inicio = data.get("fecha_inicio")
            censo.fecha_fin = data.get("fecha_fin")
            censo.estado = data.get("estado")
            censo.external_id = uuid.uuid4()
            db.session.commit()
            return censo.id
        else:
            return -1

    def buscar_external(self, external):
        return Censo.query.filter_by(external_id=external).first()    

   
    def desactivar(self,external_id):
        censo = self.buscar_external(external_id)
        if censo:
            censo.estado = False
            db.session.commit()
            return censo.id
        else:
            return -1
        

    def activar(self,external_id):
        censo = self.buscar_external(external_id)
        if censo:
            censo.estado = True
            db.session.commit()
            return censo.id
        else:
            return -1


     # Metodo para guardar censo_persona
    def guardar_datos_censo(self, data):
        censo_persona = CensoPersona()
        censo_persona.lat = data.get('latitud')
        censo_persona.long = data.get('longitud')

        # Buscar motivos por nombre
        motivo_nombres = [nombre.strip() for nombre in data.get('motivo').split(',')]
        motivos = Motivo.query.filter(Motivo.nombre.in_(motivo_nombres)).all()
        if motivos:
            censo_persona.motivo = ', '.join(motivo.nombre for motivo in motivos)
        else:
            return -4

        db.session.add(censo_persona)
        db.session.commit()
        return censo_persona.id