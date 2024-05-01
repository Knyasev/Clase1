from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from models.rol import Rol
from models.persona import Persona
from models.censo import Censo
from models.censo_persona import CensoPersona
from models.motivo import Motivo
from models.catalogo_motivo import Catalogo_Motivo
from models.cuenta import Cuenta
api = Blueprint('api', __name__)

@api.route("/")
def home ():
    return make_response(
        jsonify({"msg": "OK", "code": 200}),
        200
    )

@api.route("/suma/<a>/<b>")
def suma (a, b):
    c= float(a) + float(b)
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": {"suma": c}}),
        200     
    )

@api.route("/sumar", methods=["POST"])
def suma_post():
    data = request.json
    a = float(data["a"])
    b = float(data["b"])
    c = a + b
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": {"suma": c}}),
        200
    )