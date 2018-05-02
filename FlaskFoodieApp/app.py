"""
This script runs the FlaskTest application using a development server.
"""

from os import environ
from FoodieApp import app, socketio

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    #app.run(HOST, PORT)
    #print('test')
    socketio.run(app, HOST, PORT)
