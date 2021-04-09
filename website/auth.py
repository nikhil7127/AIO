from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import UserDetails
from sqlalchemy import exc

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        userName = request.form.get("email")
        password = request.form.get("password")
        print(UserDetails.query.all())
        currentUser = UserDetails.query.filter_by(username=userName).first()
        try:
            if check_password_hash(currentUser.password, password):
                flash("Logged in successfully", "success")
                return redirect(url_for("views.home"))
            else:
                flash("Password doesn't match", "error")
                return redirect(url_for("auth.login"))
        except Exception:
            flash("Account doesn't exist", "error")
            return redirect(url_for("auth.login"))
    return render_template("login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        new_user = UserDetails(username=data.get("username").strip(), email=data.get("email").strip(),
                               password=generate_password_hash(data.get("password").strip(), method="sha256"))
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully", "success")
            return redirect(url_for("views.home"))
        except exc.IntegrityError:
            db.session.rollback()
            if UserDetails.query.filter_by(username=data.get("username").strip()).first():
                flash("Username already taken", "error")
            elif UserDetails.query.filter_by(email=data.get("email").strip()).first():
                flash("Email already taken", "error")
            else:
                flash("Account already exists", "error")
            return redirect(url_for("auth.register"))

    return render_template("register.html")
