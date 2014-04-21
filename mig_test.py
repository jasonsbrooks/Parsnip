#!flask/bin/python
import os
import unittest
import webstart

# from config import basedir
from main import app
import main

# from app import app, db
from user.models import *

from flask import g
import pdb
# usrs = User.query.all()
# print usrs
from floorplan.models import *
from datetime import datetime
from beacon.models import *
from company.models import *
import tempfile

class TestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, main.app.config['HEAPED_DATABASE_URL'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        # app.config['CSRF_ENABLED'] = False
        # webstart.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        # app.config['HEAPED_DATABASE_URL'] = os.environ['HEAPED_DATABASE_URL']
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        # self.seq = range(10)


    def create_user(self, firstname, lastname, email, password):
        return self.app.post('/user/register', data=dict(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password
        ), follow_redirects=True)


    def login(self, email, password):
        return self.app.post('/user/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def test_register_user(self):
        response = self.create_user('jason','brooks','jason.brooks@yale.edu', 'helloworld')
        self.assertEquals(response.status, "200 OK")

        # self.assert_redirects(rv, url_for('user.asdfafasdffs'))
        # return
        # pdb.set_trace()
        # self.assert_403(rv)

    def test_login_logout(self):
        # print "potatos"
        # with main.app.test_request_context():
        #     g.user
        response = self.login('jason.brooks@yale.edu', 'helloworld')
        self.assertEquals(response.status, "200 OK")
        # pdb.set_trace()


    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_homepage(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEquals(response.status, "200 OK")


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        return

if __name__ == '__main__':
    unittest.main()