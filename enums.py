from enum import Enum

DB_NAME = "database.db"
WEB_LINK = "http://127.0.0.1:5000"

class Auth(Enum):
    LOGIN = "/login"
    LOGOUT = "/logout"
    SIGNUP = "/signup"

class Signup(Enum):
    EMAIL_LENGTH = 8
    USERNAME_LENGTH = 2
    PASSWORD_LENGTH = 6

class Alerts(Enum):
    USERNAME_INV = "Invalid Username"
    PASSWORD_INV = "Invalid Password"
    LOGGED_IN = "Logged in!"
    LOGGED_OUT = "You have been logged out."

