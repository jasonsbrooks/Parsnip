from main import db
from passlib.apps import custom_app_context as pwd_context
# from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True, index=True)
    password = db.Column(db.String(15))
    profilepic = db.Column(db.String(100))
    registered_on = db.Column(db.DateTime)

    # def __init__(self, firstname, lastname, email, password):
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.email = email
    #     self.password = password
    #     self.registered_on = datetime.utcnow()

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '#%d: First Name: %s, Last Name: %s, Email: %s, Registered On: %s, Password: %s' % (self.id, self.firstname, self.lastname, self.email, self.registered_on.strftime('%m/%d/%Y at %H:%M:%S GMT'), self.password)

