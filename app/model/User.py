from mongoengine import *
from .Base import _BaseDocument
from flask_login import UserMixin
import datetime


class User(_BaseDocument, UserMixin):
    name = StringField(required=True)
    gender = StringField(default=None, null=True, choices=["male", "female", None])
    birth = DateTimeField(default=None, null=True)

    def __repr__(self):
        return "<users: {}>".format(self.name)

    # Flask-Login 관련 Method
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def to_dict(self):
        data = {
            "id": str(self.id),
            "name": self.name,
            "gender": self.gender,
            "birth": self.birth.strftime("%Y-%m-%d")
        }

        return data