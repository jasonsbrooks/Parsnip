"""
#heaped app setup
"""


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import distinct, func
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from flask.ext.login import LoginManager
# from user.models import *


app = Flask(__name__)
app.debug = True

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

# app.debug = os.getenv["DEBUG"] in ('True', 'true')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEAPED_DATABASE_URL']
db = SQLAlchemy(app)

# for flaskext.auth -- secret key needed to use sessions
app.secret_key = os.environ['USER_AUTH_SECRET_KEY']