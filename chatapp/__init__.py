import os
from flask import Flask
from flask_session import Session
from flask_login import LoginManager
from flask_socketio import SocketIO
from .models import User, db


# Objet creation for flask login, database and user sessions(pin and opportunities)
# Initialize app
login_manager = LoginManager()
sess = Session()
DB_NAME = "database.db"
app = Flask(__name__)

# Flask sockets to send messages
socketio = SocketIO()


def create_app(debug=True):

    # Need to use sessions and sqlalchemy
    app.config["SECRET_KEY"] = os.environ["FLASK_SECRET_KEY"]
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.debug = debug

    # Set default view
    login_manager.init_app(app)
    login_manager.login_view = "views.start_page"
    login_manager.login_message = ""

    sess.init_app(app)
    db.init_app(app)
    socketio.init_app(app)

    # Import views of blueprint
    from .views import views
    from . import events
    app.register_blueprint(views, url_prefix="/")

    create_database(app)

    return app


# https://flask-login.readthedocs.io/en/latest/
def create_database(app):
    if not os.path.exists('app/' + DB_NAME):
        db.create_all(app=app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
