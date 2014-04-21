from main import db
from floorplan.models import *
from user.models import *
from advertisement.models import *

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    address1 = db.Column(db.String(60))
    address2 = db.Column(db.String(60))
    city = db.Column(db.String(60))
    state = db.Column(db.String(40))
    zipcode = db.Column(db.String(60))
    profile_image = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    hoursmonday = db.Column(db.String(50))
    hourstuesday = db.Column(db.String(50))
    hourswednesday = db.Column(db.String(50))
    hoursthursday = db.Column(db.String(50))
    hoursfriday = db.Column(db.String(50))
    hourssaturday = db.Column(db.String(50))
    hourssunday = db.Column(db.String(50))
    users = db.relationship('User', backref='company', lazy='dynamic')
    floorplans = db.relationship('Floorplan', backref='company', lazy='dynamic')
    advertisements = db.relationship('Advertisement', backref='company', lazy='dynamic')

    def __repr__(self):
        return '#%d: Name: %s, Address1: %s, Address2: %s, City: %s, State: %s, Zip: %s, Profile Image: %s, Phone: %s, Hours Monday: %s, Hours Tuesday: %s, Hours Wednesday: %s, Hours Thursday: %s, Hours Friday: %s, Hours Saturday: %s, Hours Sunday: %s' % (self.id, self.name, self.address1, self.address2, self.city, self.state, self.zipcode, self.profile_image, self.phone, self.hoursmonday, self.hourstuesday, self.hourswednesday, self.hoursthursday, self.hoursfriday, self.hourssaturday, self.hourssunday)



