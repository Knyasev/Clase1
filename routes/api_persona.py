from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from controllers.personaController import PersonaController
from controllers.utils.errors import Error
from flask_expects_json import expects_json
api_persona = Blueprint('api_persona', __name__)

personaC= PersonaController()
schema = {
    'type': 'object',
    'properties': {
        'nombre': {'type': 'string'},
        'apellido': {'type': 'string'},
        'estado_civil': {'type': 'string'},
        'fecha_nacimiento': {'type': 'string'},
        'id_rol': {'type': 'integer'},
        
    },
    'required': ['nombre', 'apellido', 'estado_civil', ]}

schema_censador= {
    'type': 'object',
    'properties': {
        'nombre': {'type': 'string'},
        'apellido': {'type': 'string'},
        'estado_civil': {'type': 'string'},
        'correo': {'type': 'string',
                   "pattern": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"},
        'clave': {'type': 'string'},
    },
    'required': ['nombre', 'apellido', 'estado_civil', 'correo', 'clave']
}
@api_persona.route("/persona")
def listar():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": ([i.serialize for i in personaC.listar()])}),
        200
    )

@api_persona.route(("/persona/guardar/censado"), methods=["POST"])
@expects_json(schema)
def guardar_censado():
    data = request.get_json()
    id = personaC.guardar_censado(data)
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
    
@api_persona.route(("/persona/guardar/censador"), methods=["POST"])
@expects_json(schema_censador)
def guardar_censador():
    data = request.get_json()
    id = personaC.guardar_censador(data)
    print(str(id))
    if (id >=0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": {"tag":"Datos Guardados"}}),
            200
        )
    else:
        return make_response(
           jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
            400
        )


@api_persona.route("/persona/<external>")
def buscar_external(external):
    search = personaC.buscar_external(external)
    if search is not None:
        search = search.serialize()
        search['estado_civil'] = search['estado_civil'].serialize()
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": [] if search is None else search}),
        200
    )


# Ruta para modificar un censo
@api_persona.route("/persona/<external_id>", methods=['POST'])
def modificar(external_id):
    data = request.get_json()  # Obtiene los datos del cuerpo de la solicitud HTTP
    if data is None:
        return make_response(jsonify({"msg": "Bad Request", "code": 400}), 400)

    persona = personaC.modificar(external_id, data)
    if persona is None:
        return make_response(jsonify({"msg": "Not Found", "code": 404}), 404)

    search = persona.serialize()
    search['estado_civil'] = search['estado_civil'].serialize()

    return make_response(jsonify({"msg": "OK", "code": 200, "datos": search}), 200)


@api_persona.route("/persona/<external_id>", methods=['PUT'])
def api_modificar_censador(external_id):
    data = request.get_json()  # Obtiene los datos del cuerpo de la solicitud HTTP
    if data is None:
        return make_response(jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
            400
        )

    persona = personaC.modificar_censador(external_id, data)
    search = persona.serialize()
    search['estado_civil'] = search['estado_civil'].serialize()
    

    if persona is None or persona == -1:
        return make_response(jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
            400
        )

    return make_response(jsonify({"msg": "OK", "code": 200, "datos": search}), 200)


@api_persona.route("/persona/<external_id>/copiar", methods=['POST'])
def api_copiar(external_id):
    persona = personaC.copiar(external_id)
    if persona is None or persona == -1:
        return make_response(jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Error.error[str(id)]}}), 
            400
        )

    search = persona.serialize()
    search['estado_civil'] = search['estado_civil'].serialize()

    return make_response(jsonify({"msg": "OK", "code": 200, "datos": search}), 200)


@api_persona.route("/persona/<external_id>/desactivar", methods=['GET'])
def desactivar(external_id):
    persona = personaC.desactivar(external_id)
    if persona is None or persona == -1:
        return make_response(jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : "Error desconocido"}}), 
        400
    )

    persona = personaC.buscar_external(external_id)
    search = persona.serialize()
    search['estado_civil'] = search['estado_civil'].serialize()


    return make_response(jsonify({"msg": "OK", "code": 200, "datos": search}), 200)


@api_persona.route("/persona/<external_id>/activar", methods=['GET'])
def activar_cuenta(external_id):
    persona = personaC.activar_cuenta(external_id)
    if persona is None or persona == -1:
        return make_response(jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : "Error desconocido"}}), 
        400
    )

    persona = personaC.buscar_external(external_id)
    search = persona.serialize()
    search['estado_civil'] = search['estado_civil'].serialize()
    return make_response(jsonify({"msg": "OK", "code": 200, "datos": search}), 200)

