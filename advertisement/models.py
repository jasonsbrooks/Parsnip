from main import db
from floorplan.models import *
from datetime import datetime
from company.models import *

class Advertisement(db.Model):
    __tablename__ = 'advertisements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(1000))
    details = db.Column(db.String(1000))
    image_url = db.Column(db.String(150))
    
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

    def __repr__(self):
        return '#%d: Name: %s, Description: %s, Details: %s, Image URL: %s, Store Name: %s' % (self.id, self.name, self.description, self.details, self.image_url, self.company.name)
