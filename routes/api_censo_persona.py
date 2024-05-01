from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from controllers.censoPersonaController import CensoPersonaController
from controllers.utils.errors import Error
from flask_expects_json import expects_json
api_censo_persona = Blueprint('api_censo_persona', __name__)

motivoC= CensoPersonaController()
schema = {
    'type': 'object',
    'properties': {
        "longitud" : {"type" : "number"},
        'latitud': {'type': 'number'},
        'motivoc': {'type': 'string'},

    },
    'required': ['longitud', 'latitud', 'motivoc']}


@api_censo_persona.route("/censo_persona")
def listar():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": ([i.serialize for i in motivoC.listar()])}),
        200
    )

@api_censo_persona.route("/censo_persona/censados")
def listar_activos():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": ([i.serialize for i in motivoC.listar_activos()])}),
        200
    )

@api_censo_persona.route(("/censo_persona/guardar"), methods=["POST"])
@expects_json(schema)
def guardar():
    data = request.get_json()
    motivo = motivoC.guardar_censop(data)
    if (motivo >=0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": ([i.serialize for i in motivoC.listar()])}),
            200
        )
    else:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(motivo)]}}), 
        )