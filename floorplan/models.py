from main import db
from company.models import *

class Floorplan(db.Model):
    __tablename__ = 'floorplans'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    floorplan_url = db.Column(db.String(500))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company = db.relationship('Company', backref="floorplans")

    def __repr__(self):
        return '#%d: Name: %s, URL: %s, Company: [ID: %s, Name: %s]' % (self.id, self.name, self.floorplan_url, self.company_id, self.company.name)

