from flask import Flask
from flask_login import LoginManager
from models.models import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI 
app.config['SECRET_KEY'] = 'your-secret-key'  

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)