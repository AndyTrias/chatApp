from . import socketio
from flask_socketio import emit
from flask_login import current_user
from .models import Message, MessageRecipient


# Receive message from client
# Send message to proper client
# Update db
@socketio.on('chatMessage')
def handle_message(data):
    data = dict(data)
    # add_message(message=data['message'], sender=current_user, receiver=User.query.get(data['receiver']))
    msg = Message.create(content=data['message'], sender_id=current_user.id)
    MessageRecipient.create(message_id=msg.id, receiver_id=data['receiver'])
    emit("message", data["message"], broadcast=True, include_self=False)
