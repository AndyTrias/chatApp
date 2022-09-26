from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


# UserMixIn implements a few default methods required by flask
# To make sure user is active and logged
class BaseMixin(object):
    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

        return obj


class User(db.Model, UserMixin, BaseMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    contacts = db.relationship("Contact", backref="user", lazy=True)
    messages_sent = db.relationship("Message", backref="user", lazy=True)
    messages_received = db.relationship("MessageRecipient", backref="user", lazy=True)

    def get_user(self, phone):
        return self.query.filter_by(phone=phone).first()


class Contact(db.Model, BaseMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    contact_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)


class Message(db.Model, BaseMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    sentAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    message_recipient = db.relationship("MessageRecipient", backref="message", lazy=True, uselist=False)


class MessageRecipient(db.Model, BaseMixin):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey("message.id"))
    receiver_id = db.Column(db.Integer, db.ForeignKey("user.id"))



