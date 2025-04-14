from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/about')
def about():
    return render_template('about.html')

@routes.route('/recover')
def recover():
    return render_template('recover.html')

@routes.route('/signup')
def signup():
    return render_template('signup.html')

@routes.route('/search')
def search():
    return render_template('searchPage.html')

@routes.route('/services')
def services():
    return render_template('services.html')
