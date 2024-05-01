import uuid 
from app import db
from models.motivo import Motivo
from tokenizer import split_into_sentences

class MotivoController():
    def listar (self):
        return Motivo.query.all()
    
    def listar_activos(self):
        return Motivo.query.filter_by(estado=True).all()
    

    def guardar_str(self,text):
        g = split_into_sentences(text)
        tokens = []
        for sentence in g:
            tokens = sentence.split()
            print (tokens)
            #guardar
        if len(tokens) > 0:
            for m in tokens:
                motivo = Motivo()
                motivo.nombre = m
                motivo.estado = True
                motivo.external_id = uuid.uuid4()
                db.session.add(motivo)
                db.session.commit()
                return 0
        else:
            return -3
        
        #mofiicar solo por nombre
