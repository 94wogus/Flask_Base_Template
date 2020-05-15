from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from mongoengine import connect
from dotenv import load_dotenv
from config import Config

load_dotenv()
login_manager = LoginManager()
cors = CORS()

app_config = Config()


def create_app(config=Config):
    app = Flask(__name__)

    app.config.from_object(config)

    connect(
        db=config.MONGODB_DATABASE,
        username=config.MONGODB_USER,
        password=config.MONGODB_PASSWORD,
        host=config.MONGODB_URI
    )

    from .api import api as v1
    app.register_blueprint(v1, url_prefix='/api/v1.0')

    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    login_manager.init_app(app)

    from app.model import User

    @login_manager.user_loader
    def load_user(uid):
        return User.objects(id=uid).first()

    return app