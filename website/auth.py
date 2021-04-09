from flask import Blueprint, render_template, request, redirect, url_for
from .models import UserDetails
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from sqlalchemy import exc

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST", "GET"])
def mail():
    return render_template("login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        new_user = UserDetails(user_name=data.get("username"), email=data.get("email"),
                               password=generate_password_hash(data.get("password"), method="sha256"))
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("views.home"))
        except exc.IntegrityError:
            db.session.rollback()
            return redirect(url_for("auth.register"))

    return render_template("register.html")
