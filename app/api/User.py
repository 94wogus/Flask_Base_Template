from flask import request
from app.api import api
from app.model import User


@api.route("/user", methods=["GET"])
def get_user():
    uid = request.args.get('id', None)
    user = User.objects(id=uid).first()
    return user.to_dict()