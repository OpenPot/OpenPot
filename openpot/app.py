from flask import Flask, render_template
from itsdangerous import URLSafeTimedSerializer

import openpot.extensions as extensions
from openpot import index, auth
from openpot.models.chef import Chef


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')

    extensions.init_app(app)

    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)

    app.add_url_rule('/', endpoint='index')

    extensions.db.create_all(app=app)

    init_auth(app)

    return app


def init_auth(app):
    extensions.login_manager.login_view = 'auth.login'

    @extensions.login_manager.user_loader
    def load_user(uid):
        return Chef.query.get(uid)

    # @extensions.login_manager.token_loader
    # def load_token(token):
    #     duration = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
    #     serializer = URLSafeTimedSerializer(app.secret_key)

    #     data = serializer.loads(token, max_age=duration)
    #     uid = data[0]

    #     return Chef.query.get(uid)
