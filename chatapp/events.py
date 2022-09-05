from . import socketio
from flask_socketio import emit


@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    emit(msg, broadcast=True)

