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
        self.db_fd, main.app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        # app.config['CSRF_ENABLED'] = False
        # webstart.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        # app.config['HEAPED_DATABASE_URL'] = os.environ['HEAPED_DATABASE_URL']
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

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

    def register_user(self):
        rv = self.create_user('jason','brooks','jason.brooks@yale.edu', 'helloworld')
        # self.assert_redirects(rv, url_for('user.asdfafasdffs'))
        # return
        # pdb.set_trace()
        self.assert_403(rv)

    def test_login_logout(self):
        # print "potatos"
        # with main.app.test_request_context():
        #     g.user
        rv = self.login('jason.brooks@yale.edu', 'helloworld')
        return
        # pdb.set_trace()


    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_homepage(self):
        response = self.app.get('/', follow_redirects=True)
        return
        # self.assertEquals(response.status, "200 OK")


        # print usrs
        # assert 'You were logged in' in rv.data
        # rv = self.logout()
        # assert 'You were logged out' in rv.data
        # rv = self.login('adminx', 'default')
        # assert 'Invalid username' in rv.data
        # rv = self.login('admin', 'defaultx')
        # assert 'Invalid password' in rv.data
        # pass


    # def test_avatar(self):
    #     u = User(firstname = 'john', lastname = 'doe', email = "jon.doe@gmail.com")
    #     db.session.add(u)
    #     db.session.commit()
    #     # avatar = u.avatar(128)
    #     # expected = 'http://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'
    #     # assert avatar[0:len(expected)] == expected
    #     assert True

    # def test_make_unique_nickname(self):
    #     u = User(nickname = 'john', email = 'john@example.com')
    #     db.session.add(u)
    #     db.session.commit()
    #     nickname = User.make_unique_nickname('john')
    #     assert nickname != 'john'
    #     u = User(nickname = nickname, email = 'susan@example.com')
    #     db.session.add(u)
    #     db.session.commit()
    #     nickname2 = User.make_unique_nickname('john')
    #     assert nickname2 != 'john'
    #     assert nickname2 != nickname

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        return

if __name__ == '__main__':
    unittest.main()