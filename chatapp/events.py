from . import socketio
from flask_socketio import emit
from flask import request


@socketio.on('chatMessage')
def handle_message(msg):
    print('received message: ' + msg)
    emit("message", msg, to=request.sid)
    # TODO - Save message to database
    # TODO - Send message to all users
    pass
