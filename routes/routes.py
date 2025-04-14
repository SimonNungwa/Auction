from flask import Flask, render_template, request, url_for, redirect
from auth import auth
from app import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/recover')
def recover():
    return render_template('recover.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/search')
def search():
    return render_template('searchPage.html')

@app.route('/services')
def services():
    return render_template('services.html')

# @app.route('/login')
# def login():
#     if 