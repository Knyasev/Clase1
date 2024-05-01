from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from controllers.motivoController import MotivoController
from controllers.utils.errors import Error
from flask_expects_json import expects_json
api_motivo = Blueprint('api_motivo', __name__)

motivoC= MotivoController()
schema = {
    'type': 'object',
    'properties': {
        'nombre': {'type': 'string'},

    },
    'required': ['nombre']}


@api_motivo.route("/motivo")
def listar():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": ([i.serialize for i in motivoC.listar()])}),
        200
    )

@api_motivo.route(("/motivo/guardar/str"), methods=["POST"])
@expects_json(schema)
def guardar():
    data = request.get_json()
    motivo = motivoC.guardar_str(data['nombre'])
    if (motivo >=0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": ([i.serialize for i in motivoC.listar()])}),
            200
        )
    else:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(motivo)]}}), 
        )
    
@api_motivo.route(("/motivo/modificar/<external_id>"), methods=["POST"])
@expects_json(schema)
def modificar(external_id):
    data = request.get_json()
    motivo = motivoC.modificar(external_id, data)
    if (motivo >=0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": ([i.serialize for i in motivoC.listar()])}),
            200
        )
    else:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(motivo)]}}), 
        )