from main import db
from floorplan.models import *

class Beacon(db.Model):
    __tablename__ = 'beacons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    major = db.Column(db.String(40))
    minor = db.Column(db.String(40))
    uuid = db.Column(db.String(40))
    floorplan_id = db.Column(db.Integer, db.ForeignKey('floorplans.id'))
    floorplan = db.relationship('Floorplan', backref="beacons")


    def __repr__(self):
        return '#%d: Name: %s, Major: %s, Minor: %s, UUID: %s, Floorplan: {{%s}}' % (self.id, self.name, self.major, self.minor, self.uuid, self.floorplan)
