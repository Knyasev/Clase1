from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from controllers.personaController import PersonaController
from controllers.rolController import RolController
api_persona = Blueprint('api_persona', __name__)

personC = PersonaController()
@api_persona.route('/persona', methods=["GET"])
def listar():
    personaC = PersonaController()
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":([i.serialize() for i in personaC.listar()])}),
        200
    )
#API for persona   
@api_persona.route('/persona/post', methods=["POST"])
def create():
    data = request.json
    person_id = personC.save(data)
    return make_response(
        jsonify({"msg":"OK", "code":200, "data": person_id}),
        200
    )       


@api_persona.route('/rol', methods=["GET"])
def listarRol():
    rol = RolController()
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":([i.serialize() for i in rol.listarRol()])}),
        200
    )


