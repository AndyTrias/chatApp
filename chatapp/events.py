from . import socketio
from flask_socketio import emit


@socketio.on('chatMessage')
def handle_message(msg):
    print('received message: ' + msg)
    emit("message", msg, broadcast=True, include_self=False)
    # TODO - Save message to database
    # TODO - Send message to all users
    pass
