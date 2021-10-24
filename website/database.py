# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy

# from .models import User

# from enums import DB_NAME

# db = SQLAlchemy()


# def init_db():
#     create_database(app)

#     login_manager = LoginManager()
#     login_manager.login_view = "auth.login"
#     login_manager.init_app(app)

#     @login_manager.user_loader
#     def load_user(id):
#         return User.query.get(int(id))

#     return app

# def create_database(app: Flask) -> None:
#     if not path.exists(f"website/{DB_NAME}"):
#         db.create_all(app=app)
#         print("Successfully created the database!")
