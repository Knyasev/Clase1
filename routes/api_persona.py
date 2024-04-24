from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from controllers.personaController import PersonaController
api_persona = Blueprint('api_persona', __name__)

personC = PersonaController()
@api_persona.route('/persona', methods=["GET"])
def list():
    persons = personC.listPerson()
    return make_response(
        jsonify({"msg":"OK", "code":200, "data":([person.serialize() for person in persons])}),
        200
    )
#API for persona   
@api_persona.route('/persona', methods=["POST"])
def create():
    data = request.json
    person_id = personC.save(data)
    return make_response(
        jsonify({"msg":"OK", "code":200, "data": person_id}),
        200
    )