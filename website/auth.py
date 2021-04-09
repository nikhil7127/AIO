from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST", "GET"])
def mail():
    return render_template("login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print(request.form)
        return redirect(url_for("auth.register"))
    return render_template("register.html")
