from user.models import *
from floorplan.models import *
from datetime import datetime

db.drop_all()
db.create_all()

u1 = User(firstname="Jason", lastname="Brooks", email="jason.brooks@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg")
u2 = User(firstname="Pranav", lastname="Maddi", email="pranav.maddi@yale.edu", profilepic="https://scontent-b-iad.xx.fbcdn.net/hphotos-prn2/t1.0-9/9749_10202200719724608_650155214_n.jpg")
u1.hash_password("helloworld")
u2.hash_password("goodbyeworld")
u1.registered_on=datetime.utcnow()
u2.registered_on=datetime.utcnow()
db.session.add(u1)
db.session.add(u2)
db.session.commit()

