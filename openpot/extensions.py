from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

debug_toolbar = DebugToolbarExtension()
db = SQLAlchemy()


def init_app(app):
    debug_toolbar.init_app(app)
    db.init_app(app)
