from . import socketio
from flask_socketio import emit


@socketio.on('evento')
def handle_message(msg):
    print('Message: ' + msg)
    emit('mensaje', 'holaaa')

