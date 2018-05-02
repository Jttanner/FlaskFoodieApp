"""
The flask application package.
"""

from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thepancake'

socketio = SocketIO(app)

loginManager = LoginManager()
loginManager.init_app(app)

import FoodieApp.views
