from flask import Flask, render_template
import openpot.extensions as extensions
from openpot import index, auth


def create_app():

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')

    extensions.init_app(app)

    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)

    app.add_url_rule('/', endpoint='index')

    return app
