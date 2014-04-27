#!flask/bin/python
import os
import unittest
import webstart
import flask.ext.testing

# from config import basedir
from main import app
import main

# from app import app, db
from user.models import *

from flask import g, url_for
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

    # def tearDown(self):
        # os.close(self.db_fd)
        # os.unlink(self.db_fd)

    def create_user(self, firstname, lastname, email, password, profilepic, company_id, account_approved):
        return self.app.post('/user/register', data=dict(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            profile_pic=profilepic,
            company_id=1
        ), follow_redirects=True)


    def login(self, email, password):
        return self.app.post('/user/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/user/logout', follow_redirects=True)

    def test_registration(self):
        company1 = Company(name="Elm City Market", address1="777 Chapel St.", city="New Haven", state="Connecticut", zipcode="06520", profile_image="https://www.elmcitymarket.coop/wp-content/themes/elmcity/images/layout/header.logo.jpg", phone="12036240441", hoursmonday="8:00am - 9:00pm", hourstuesday="8:00am - 9:00pm", hourswednesday="8:00am - 9:00pm", hoursthursday="8:00am - 9:00pm", hoursfriday="8:00am - 9:00pm", hourssaturday="8:00am - 9:00pm", hourssunday="9:00am - 9:00pm")
        db.session.add(company1)
        db.session.commit()
        rv = self.create_user('jason','brooks','jason.brooks@yale.edu', 'helloworld', 'https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg', 1, True)
        self.assertEquals(rv.status_code, 200)
        assert "User successfully registered" in rv.data
        rv = self.create_user('jason','brooks','jason.brooks@yale.edu', 'helloworld','https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg', 1, True)
        self.assertEquals(rv.status_code, 200)
        assert "Account already exists for this email address! Please try signing in." in rv.data
        rv = self.login('jason.brooks@yale.edu', 'helloworld')
        print rv.data

    # def test_approve_account(self):
    #     rv = self.login('jason.brooks@yale.edu', 'helloworld')
    #     print rv.data        

    # def register_user(self):
    #     rv = self.create_user('jason','brooks','jason.brooks@yale.edu', 'helloworld')
    #     pdb.set_trace()
    #     # self.assert_redirects(rv, url_for('user.asdfafasdffs'))
    #     # return
    #     # pdb.set_trace()
    #     self.assert_403(rv)

    # def test_login_logout(self):
    #     # print "potatos"
    #     # with main.app.test_request_context():
    #     #     g.user
    #     rv = self.login('jason.brooks@yale.edu', 'helloworld')
    #     return
    #     # pdb.set_trace()


    # def logout(self):
    #     return self.app.get('/logout', follow_redirects=True)

    # def test_homepage(self):
    #     response = self.app.get('/', follow_redirects=True)
    #     return

if __name__ == '__main__':
    unittest.main()