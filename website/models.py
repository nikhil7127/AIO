from . import db
from flask_login import UserMixin


class UserDetails(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
