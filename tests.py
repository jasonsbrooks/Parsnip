from user.models import *
from floorplan.models import *

db.drop_all()
db.create_all()

u = User(firstname="Jason", lastname="Brooks", email="jason.brooks@yale.edu")
u.hash_password("helloworld")
db.session.add(u)
db.session.commit()