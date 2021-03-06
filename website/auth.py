from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from sqlalchemy import exc
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        userName = request.form.get("email")
        password = request.form.get("password")
        currentUser = User.query.filter_by(username=userName).first()
        try:
            if check_password_hash(currentUser.password, password):
                flash("Logged in successfully", "success")
                login_user(currentUser,remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password doesn't match", "error")
                return redirect(url_for("auth.login"))
        except Exception:
            flash("Account doesn't exist", "error")
            return redirect(url_for("auth.login"))
    return render_template("login.html",presentUser=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        new_user = User(username=data.get("username").strip(), email=data.get("email").strip(),
                               password=generate_password_hash(data.get("password").strip(), method="sha256"))
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash("Logged in successfully", "success")
            return redirect(url_for("views.home"))
        except exc.IntegrityError:
            db.session.rollback()
            if User.query.filter_by(username=data.get("username").strip()).first():
                flash("Username already taken", "error")
            elif User.query.filter_by(email=data.get("email").strip()).first():
                flash("Email already taken", "error")
            else:
                flash("Account already exists", "error")
            return redirect(url_for("auth.register"))

    return render_template("register.html",presentUser=current_user)
