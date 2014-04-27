from main import db
from floorplan.models import *
from datetime import datetime

class Beacon(db.Model):
    __tablename__ = 'beacons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    major = db.Column(db.String(40))
    minor = db.Column(db.String(40))
    uuid = db.Column(db.String(40), default="B9407F30-F5F8-466E-AFF9-25556B57FE6D")
    xPos = db.Column(db.String(40))
    yPos = db.Column(db.String(40))
    
    floorplan_id = db.Column(db.Integer, db.ForeignKey('floorplans.id'))
    distances = db.relationship('Distance', backref='beacon', lazy='dynamic')

    def __repr__(self):
        return '#%d: Name: %s, Major: %s, Minor: %s, UUID: %s, Floorplan ID: %d' % (self.id, self.name, self.major, self.minor, self.uuid, self.floorplan_id)



class Distance(db.Model):
    __tablename__ = 'distances'
    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float)
    time = db.Column(db.DateTime)
    beacon_id = db.Column(db.Integer, db.ForeignKey('beacons.id'))
    userID = db.Column(db.String(40))

    def __repr__(self):
        return '#%d: Beacon: %d, Distance: %.2f, User ID: %s' % (self.id, self.beacon_id, self.distance, self.userID)

