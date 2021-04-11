from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("base.html", presentUser=current_user)


@views.route("/notes")
@login_required
def notes():
    return render_template("notes.html", presentUser=current_user)


@views.route("/createNote", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        data = request.form
        title = data.get("title")
        content = data.get("content")
        data = Note(title=title, content=content, user_id=current_user.id)
        try:
            db.session.add(data)
            db.session.commit()
            flash("Notes added successfully", "success")
            return redirect(url_for("views.notes"))
        except Exception:
            db.session.rollback()
            flash("Can't add notes", "error")
            return redirect(url_for("views.create"))

    return render_template("createNote.html", presentUser=current_user)


@views.route("/mail", methods=["POST", "GET"])
@login_required
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
    return render_template("mail.html", presentUser=current_user)


@views.route("/deleteNote", methods=["POST"])
def deleteNote():
    note = json.loads(request.data)
    print(request.data)
    noteId = note["noteId"]
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            print(Note.query.all())
    return jsonify({})
