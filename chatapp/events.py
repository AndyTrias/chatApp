from . import socketio
from flask_socketio import emit
from flask_login import current_user

@socketio.on('mensaje')
def handle_message(msg):
    # TODO - Save message to database
    # TODO - Send message to all users
    pass
