from . import api

@api.before_request
def before_request():
    print("before request")