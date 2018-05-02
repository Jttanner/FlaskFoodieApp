"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FoodieApp import app, loginManager, socketio
from ServerModels.User import User

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        doggo='dyay',
    )

@app.route('/login')
def login():
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        )

@app.route('/loginRequest')
def loginRequest():
    pass

@app.route('/register')
def register():
    return render_template(
    'register.html',
    title='Register',
    year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@login_manager.user_loader
def load_user(userID):
    return User.getUser(user_id)
