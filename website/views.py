from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("base.html")


@views.route("/mail", methods=["POST", "GET"])
def mail():
    if request.method == "POST":
        data = request.form
        sender = (data.get("senderMail"), data.get("senderPassword"))
        receiver = data.get("receivers").split(";")
        subject = data.get("subject")
        body = data.get("body")
        files = data.get("files")
        from .templates.codes.mail import sendEmail
        sendEmail(sender, receiver, {"subject": subject, "message": body}, files)
        return redirect(url_for("views.home"))
    return render_template("mail.html")
