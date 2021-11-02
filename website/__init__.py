from os import path
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from enums import DB_NAME
from utils import generate_key

db = SQLAlchemy()

def create_app():
    app = Flask(__name__) # Creates instance of the flask class
    app.config["SECRET_KEY"] = generate_key()
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views.comments import comments
    from .views.posts import posts
    from .views.auth import auth
    from .views.home import home

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(posts, url_prefix="/")
    app.register_blueprint(comments, url_prefix="/")

    from website.models import User # Have to put here for circular import

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app: Flask) -> None:
    if not path.exists(f"website/{DB_NAME}"):
        db.create_all(app=app)
        print("Successfully created the database!")
