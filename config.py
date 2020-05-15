import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdl1230axcqaq24yr4'

    # DB Base Config
    MONGODB_DATABASE = os.environ.get('MONGODB_DATABASE')
    MONGODB_SERVER = os.environ.get('MONGODB_SERVER')
    MONGODB_PORT = os.environ.get('MONGODB_PORT')
    MONGODB_USER = os.environ.get('MONGODB_USER')
    MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')
    MONGODB_URI = os.environ.get('MONGODB_URI')

    # ES Base Config
    ES_ACCESS_KEY = os.environ.get('ES_ACCESS_KEY')
    ES_SECRET_KEY = os.environ.get('ES_SECRET_KEY')
    ELASTICSEARCH_URI = os.environ.get('ELASTICSEARCH_URI')

    # AWS Base Config
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')

    # FCM Base Config
    FCM_API_KEY = os.environ.get('FCM_API_KEY')
    FCM_END_POINT = os.environ.get('FCM_END_POINT')

    # CLOUD FRONT Base Config
    CLOUD_FRONT = os.environ.get('CLOUD_FRONT')
    RESIZE_CLOUD_FRONT = os.environ.get('RESIZE_CLOUD_FRONT')

    # S3 Base Config
    S3_BUCKET = os.environ.get('S3_BUCKET')
    PROFILE_DEFAULT = os.environ.get('PROFILE_DEFAULT')

    # Error Config
    SLACK_HOOK_URL = os.environ.get('SLACK_HOOK_URL')
    PROPAGATE_EXCEPTIONS = True

    # Time Format
    RFC3339_STRING = '%Y-%m-%dT%H:%M:%S.%fZ'
    KST = datetime.timezone(datetime.timedelta(hours=9))

    @staticmethod
    def init_app(app):
        pass
