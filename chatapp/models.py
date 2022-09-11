from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


# UserMixIn implements a few default methods required by flask
# To make sure user is active and logged
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    contacts = db.relationship("Contacts", backref="user", lazy=True)
    chats = db.relationship("Chat", backref="user", lazy=True)


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String, nullable=False)
    contact_id = db.Column(db.Integer, nullable=False)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chatWith = db.Column(db.Integer, db.ForeignKey("user.id"))
    messages = db.relationship("Message", backref="chat", lazy=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    sentBy = db.Column(db.Integer, db.ForeignKey("user.id"))
    sentTo = db.Column(db.Integer, db.ForeignKey("user.id"))
    sentAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"))

