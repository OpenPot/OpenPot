from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from util.util_sqlalchemy import ResourceMixin

from openpot.extensions import db


class Chef(UserMixin, ResourceMixin, db.Model):
    __tablename__ = 'chef'

    id = db.Column('chef_id', db.Integer(), primary_key=True)

    # Authentication
    username = db.Column('username', db.String(24),
                         unique=True, index=True, nullable=False)
    password = db.Column('password', db.String(128), nullable=False)
    email = db.Column('email', db.String(255), unique=True, nullable=False)

    def __init__(self, **kwargs):
        super(Chef, self).__init__(**kwargs)

        self.password = Chef.encrypt_password(kwargs.get('password', ''))

    @classmethod
    def find_by_identity(cls, identity):
        return Chef.query.filter(
            (Chef.username == identity) | (Chef.email == identity)
        ).first()

    @classmethod
    def encrypt_password(cls, plaintext_password):
        if plaintext_password:
            return generate_password_hash(plaintext_password)

        return None

    def authenticated(self, with_password=True, password=''):
        if with_password:
            return check_password_hash(self.password, password)
