from . import socketio
from flask_socketio import emit
from flask_login import current_user
from .models import User
from .helpers import add_message


@socketio.on('chatMessage')
def handle_message(data):
    data = dict(data)
    print(User.query.get(data['receiver']))
    add_message(message=data['message'], sender=current_user, receiver=User.query.get(data['receiver']))
    emit("message", data["message"], broadcast=True, include_self=False)





