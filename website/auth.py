from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User
from enums import Auth, Signup, Alerts

auth = Blueprint("auth", __name__) # this blueprint is then invoked in the init file


@auth.route(Auth.LOGIN.value, methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if not user:
            flash(Alerts.USERNAME_INV.value, category="error")
        else:
            print(user.username, user.email)
            if not check_password_hash(user.password, password): # The previuos hash is the first argument
                flash(Alerts.PASSWORD_INV.value, category="error")
            else:
                flash(Alerts.LOGGED_IN.value)
                login_user(user, remember=True)
                return redirect(url_for("views.home"))

    return render_template("login.html", user=current_user)


@auth.route(Auth.SIGNUP.value, methods = ["GET", "POST"])
def signup():
    if request.method == "POST":

        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first() # Will get the right row because email is unique
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash("Email is already in use.", category="error")
        elif username_exists:
            flash("Username is already in use.", category="error")
        elif password1 != password2:
            flash("The passwords don't match!", category="error")
        elif len(username) < Signup.USERNAME_LENGTH.value:
            flash("Username is too short.", category = "error")
        elif len(password1) < Signup.PASSWORD_LENGTH.value:
            flash("Password is too short.", category = "error")
        elif len(email) < Signup.EMAIL_LENGTH.value:
            flash("Email is too short.", category = "error")
        else:
            new_user = User(
                email=email,
                username=username,
                password=generate_password_hash(password1, method="sha256")
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("User created!")

            print("All users:")
            users = User.query.all()
            for user in users:
                print(user)

            return redirect(url_for("views.home"))
        
    return render_template("signup.html", user=current_user)

# This function redirects to the url that brings to the home page.
# This is an easier syntax for when projects get large.
@auth.route(Auth.LOGOUT.value)
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))
