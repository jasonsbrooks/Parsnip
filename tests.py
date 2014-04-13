from user.models import *
from floorplan.models import *
from datetime import datetime

db.drop_all()
db.create_all()

u = User(firstname="Jason", lastname="Brooks", email="jason.brooks@yale.edu")
u.hash_password("helloworld")
u.registered_on=datetime.utcnow()
db.session.add(u)
db.session.commit()