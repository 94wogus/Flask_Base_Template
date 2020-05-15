from flask import Blueprint

api = Blueprint('api', __name__)

from . import request_hadler


@api.route('/', methods=['GET'])
def index():
    return "<h1>API V1.0<h1>"

