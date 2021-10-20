from os import path
from flask import Flask
from .auth import auth
from .views import views
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__) # Creates instance of the flask class
    app.config["SECRET_KEY"] = "isak's key"
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


