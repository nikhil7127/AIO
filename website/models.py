from . import db


class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
