from models.censo import Censo
from models.rol import Rol
from models.cuenta import Cuenta
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

