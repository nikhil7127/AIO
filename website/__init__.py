from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
db_name = "userDetails.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "nikhilvarma7127"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    from .views import views
    from .auth import auth
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    from .models import UserDetails
    create_database(app)
    manager = LoginManager()
    manager.login_view = "auth.login"
    manager.init_app(app)

    @manager.user_loader
    def loader(ids):
        return UserDetails.query.get(int(ids))

    return app


def create_database(app):
    if not path.exists("website/" + db_name):
        db.create_all(app=app)
        print("successfully Created")
