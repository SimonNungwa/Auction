from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recover')
def recover():
    return render_template('recover.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')