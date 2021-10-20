from enum import Enum

WEB_LINK = "http://127.0.0.1:5000"

class Auth(Enum):
    LOGIN = "/login"
    LOGOUT = "/logout"
    SIGNUP = "/sign-up"

