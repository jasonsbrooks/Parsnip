from main import db
from company.models import *
from beacon.models import *

class Floorplan(db.Model):
    __tablename__ = 'floorplans'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    floorplan_url = db.Column(db.String(500))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    beacons = db.relationship('Beacon', backref='floorplan', lazy='dynamic')
    positions = db.relationship('Position', backref='floorplan', lazy='dynamic')
    
    def __repr__(self):
        return '#%d: Name: %s, URL: %s, Company: [ID: %s, Name: %s]' % (self.id, self.name, self.floorplan_url, self.company_id, self.company.name)

