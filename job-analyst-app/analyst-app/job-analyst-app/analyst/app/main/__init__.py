from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .config.config import config_by_name
from ..main.database import insertion
from flask_jwt_extended import JWTManager
from flask_cors import CORS
db = SQLAlchemy()
flask_bcrypt = Bcrypt()



def create_app(config_name):
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}}, allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"])
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_object(config_by_name[config_name])
    app.config['JWT_SECRET_KEY']='JWT_SECRET_KEY'
    db.init_app(app)
    flask_bcrypt.init_app(app)
    JWTManager(app)
    return app
