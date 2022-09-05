from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.util import text_type
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    active = db.Column(db.Boolean, default=False)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return text_type(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')


