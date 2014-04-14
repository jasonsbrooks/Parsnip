from user.models import *
from floorplan.models import *
from datetime import datetime
from beacon.models import *
from company.models import *

db.drop_all()
db.create_all()

company1 = Company(name="Elm City Market", address1="777 Chapel St.", city="New Haven", state="Connecticut", zipcode="06520", profile_image="https://www.elmcitymarket.coop/wp-content/themes/elmcity/images/layout/header.logo.jpg", phone="12036240441", hoursmonday="8:00am - 9:00pm", hourstuesday="8:00am - 9:00pm", hourswednesday="8:00am - 9:00pm", hoursthursday="8:00am - 9:00pm", hoursfriday="8:00am - 9:00pm", hourssaturday="8:00am - 9:00pm", hourssunday="9:00am - 9:00pm")
db.session.add(company1)
db.session.commit()


u1 = User(firstname="Jason", lastname="Brooks", email="jason.brooks@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1)
u2 = User(firstname="Pranav", lastname="Maddi", email="pranav.maddi@yale.edu", profilepic="https://scontent-b-iad.xx.fbcdn.net/hphotos-prn2/t1.0-9/9749_10202200719724608_650155214_n.jpg", company=company1)
u1.hash_password("helloworld")
u2.hash_password("goodbyeworld")
u1.registered_on=datetime.utcnow()
u2.registered_on=datetime.utcnow()
db.session.add(u1)
db.session.add(u2)
db.session.commit()

floorplan1 = Floorplan(name="Floorplan 1", floorplan_url="http://www.google.com", company=company1)
db.session.add(floorplan1)
db.session.commit()

beacon1 = Beacon(name="Hello",major="3",minor="2",uuid="asdf34asdf2-asdf23",floorplan=floorplan1)
db.session.add(beacon1)
db.session.commit()

