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





