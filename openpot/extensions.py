from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

debug_toolbar = DebugToolbarExtension()
db = SQLAlchemy()
login_manager = LoginManager()


def init_app(app):
    debug_toolbar.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
