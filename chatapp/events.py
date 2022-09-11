from . import socketio
from flask_socketio import emit


@socketio.on('mensaje')
def handle_message(msg):
    # TODO - Save message to database
    # TODO - Send message to all users

    print(msg)
