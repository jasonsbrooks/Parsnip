from main import db

class Layout(db.Model):
    __tablename__ = 'layouts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    floorplan_url = db.Column(db.String(500))

    def __repr__(self):
        return '#%d: Name: %s  URL: %s' % (self.id, self.name, self.url)
