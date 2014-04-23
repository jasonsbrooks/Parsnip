"""
parsnip app setup
"""


from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import distinct, func
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from flask.ext.login import LoginManager
from flask_mail import Mail
# from user.models import *


app = Flask(__name__)
app.debug = True


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'

mail = Mail(app)


# app.debug = os.getenv["DEBUG"] in ('True', 'true')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEAPED_DATABASE_URL']
app.config.update(dict(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'theparsnipapp@gmail.com',
    MAIL_PASSWORD = os.environ['PARSNIP_MAIL_PW'],
    MAIL_DEFAULT_SENDER = 'theparsnipapp@gmail.com'
))

db = SQLAlchemy(app)

# for flaskext.auth -- secret key needed to use sessions
app.secret_key = os.environ['USER_AUTH_SECRET_KEY']