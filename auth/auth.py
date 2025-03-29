# from flask import Flask, render_template, request, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
# from werkzeug.security import generate_password_hash, check_password_hash


# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqllite:///db.sqlite"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SECRET_KEY"] = "supersecretkey"


# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"


# class Users(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(250), unique=True, nullable=False)
#     password = db.Column(db.String(250), nullable=False)

# with app.app_context():
#     db.create_all()

# @login_manager.user_loader
# def load_user(user_id):
#     return Users.query.get(int(user_id))

