from flask import Blueprint, render_template
from enums import Auth

auth = Blueprint("auth", __name__)

@auth.route(Auth.LOGIN.value)
def login():
    return "login"

@auth.route(Auth.SIGNUP.value)
def sign_up():
    return "signup"

@auth.route(Auth.LOGOUT.value)
def logout():
    return "logout"