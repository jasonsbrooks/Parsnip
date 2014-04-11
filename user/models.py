from main import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True, index=True)
    password = db.Column(db.String(15))
    registered_on = db.Column(db.DateTime)

    def __init__(self, firstname, lastname, email, password):
    	self.firstname = firstname
    	self.lastname = lastname
    	self.email = email
    	self.password = 
    	self.registered_on = datetime.utcnow()


    def __repr__(self):
        return '#%d: First Name: %s, Last Name: %s, Email: %s' % (self.id, self.firstname, self.lastname, self.email)