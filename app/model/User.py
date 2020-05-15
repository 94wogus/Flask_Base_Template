from mongoengine import *
from flask_login import UserMixin
from .Base import _BaseDocument


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
        data = self.to_mongo()
        return data