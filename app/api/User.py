from flask import request, jsonify
from app.api import api
from app.model import User
from datetime import datetime

@api.route("/users", methods=["GET"])
def get_user():
    users = User.objects().all()
    return jsonify({"result": [user.to_dict() for user in users]}), 200

@api.route("/user/create", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    if data.get("name", None) is None:
        return jsonify({"result": "Invaild Request"}), 400
    birthstr = data.get("birth", None)
    try:
        birth = datetime.strptime(birthstr, "%Y-%m-%d")
    except Exception as e:
        print(e)
        birth = datetime.now()

    newUser = User(
        name=data.get("name", None),
        gender=data.get("gender", None),
        birth=birth
    )
    newUser._create()

    return jsonify({"result": newUser.to_dict()}), 200