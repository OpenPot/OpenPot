import os
from datetime import timedelta

DEBUG = True
DEBUG_TB_INTERCEPT_REDIRECTS = False

REMEMBER_COOKIE_DURATION = timedelta(days=90)

SECRET_KEY = 'insecurekeyfordevelopment'

# SQL Alchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://{usr}:{pwd}@database:5432/{db}'.format(
    usr=os.environ['POSTGRES_USER'],
    pwd=os.environ['POSTGRES_PASSWORD'],
    db=os.environ['POSTGRES_DB']
)
