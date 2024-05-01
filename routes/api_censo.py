from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from controllers.censoController import CensoController
from controllers.utils.errors import Error
from flask_expects_json import expects_json
api_censo = Blueprint('api_censo', __name__)

censoC= CensoController()
schema = { 
    'type': 'object',
    'properties': {
        'fecha_inicio': {'type': 'string'},
        'fecha_fin': {'type': 'string'},
        'estado': {'type': 'boolean'},
        'motivo': {'type': 'string'},

        
    },
    'required': ['fecha_inicio', 'fecha_fin', 'estado' , 'motivo']}
censo_persona_schema = {
    "type": "object",
    'properties': {
        "latitud": {"type": "number"},
        "longitud": {"type": "number"},
        "motivo": {"type": "string"},
    },
    'required': ["latitud", "longitud", "motivo"]
}


@api_censo.route("/censo")
def listar():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": ([i.serialize() for i in censoC.listar()])}),
        200
    )


    
@api_censo.route(("/censo/guardar"), methods=["POST"])
@expects_json(schema)
def guardar():
    data = request.get_json()
    id = censoC.save(data)
    print(str(id))
    if (id >=0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": {"tag":"Datos Guardados"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
        )


@api_censo.route("/censo/<external>")
def buscar_external(external):
    search = censoC.buscar_external(external)
    if search is not None:
        search = search.serialize()
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": [] if search is None else search}),
        200
    )



@api_censo.route("/censo/modificar/<external>", methods=['POST'])
@expects_json(schema)
def modificar(external):
    data = request.get_json()
    data['external_id'] = external
    id = censoC.modificar(data)
    censo = censoC.buscar_external(external)
    if (id >=0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": "Datos Modificados"}),
            200
        )
    else:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
        )



@api_censo.route("/censo/<external_id>/desactivar", methods=['GET'])
def desactivar(external_id):
    censo = censoC.desactivar(external_id)
    if censo is None or censo == -1:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
        )

    censo = censoC.buscar_external(external_id)
    search = censo.serialize()
    return make_response(jsonify({"msg": "OK", "code": 200, "datos": search}), 200)


@api_censo.route("/censo/<external_id>/activar", methods=['GET'])
def activar (external_id):
    censo = censoC.activar(external_id)
    if censo is None or censo == -1:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
        )

    censo = censoC.buscar_external(external_id)
    search = censo.serialize()
    return make_response(jsonify({"msg": "OK", "code": 200, "datos": search}), 200)


@api_censo.route("/guardar/censo/persona", methods=["POST"])
@expects_json(censo_persona_schema)
def guardar_datos():
    data = request.json
    id_censo_persona = censoC.guardar_datos_censo(data)
    if id_censo_persona == -4:
        return make_response(
            jsonify({"msg": "Motivo no encontrado", "code": 404}),
            404
        )
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": id_censo_persona}),
        200
    )