from user.models import *
from floorplan.models import *
from datetime import datetime
from beacon.models import *
from company.models import *

db.drop_all()
db.create_all()

company1 = Company(name="Elm City Market", address1="777 Chapel St.", city="New Haven", state="Connecticut", zipcode="06520", profile_image="https://www.elmcitymarket.coop/wp-content/themes/elmcity/images/layout/header.logo.jpg", phone="12036240441", hoursmonday="8:00am - 9:00pm", hourstuesday="8:00am - 9:00pm", hourswednesday="8:00am - 9:00pm", hoursthursday="8:00am - 9:00pm", hoursfriday="8:00am - 9:00pm", hourssaturday="8:00am - 9:00pm", hourssunday="9:00am - 9:00pm")
company2 = Company(name="Gourmet Heaven", address1="15 Broadway", city="New Haven", state="Connecticut", zipcode="06520", profile_image="http://gourmetheaven.com/wp-content/uploads/2013/02/ghgh1.png", phone="12037874533", hoursmonday="12:00am - 11:59pm", hourstuesday="12:00am - 11:59pm", hourswednesday="12:00am - 11:59pm", hoursthursday="12:00am - 11:59pm", hoursfriday="12:00am - 11:59pm", hourssaturday="12:00am - 11:59pm", hourssunday="12:00am - 11:59pm")
db.session.add(company1)
db.session.add(company2)
db.session.commit()


u1 = User(firstname="Jason", lastname="Brooks", email="jason.brooks@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
u2 = User(firstname="Pranav", lastname="Maddi", email="pranav.maddi@yale.edu", profilepic="https://scontent-b-iad.xx.fbcdn.net/hphotos-prn2/t1.0-9/9749_10202200719724608_650155214_n.jpg", company=company1, account_approved=True)
u3 = User(firstname="Charles", lastname="Jin", email="charles.jin@yale.edu", profilepic="https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-ash2/t31.0-8/462503_10201093936700713_711489518_o.jpg", company=company2, account_approved=True)

u1.hash_password("helloworld")
u2.hash_password("goodbyeworld")
u3.hash_password("helloworld")
u1.registered_on=datetime.utcnow()
u2.registered_on=datetime.utcnow()
db.session.add(u1)
db.session.add(u2)
db.session.commit()

floorplan1 = Floorplan(name="Floorplan 1", floorplan_url="http://www.google.com", company=company1)
floorplan2 = Floorplan(name="Floorplan 2", floorplan_url="http://www.myspace.com", company=company2)
db.session.add(floorplan1)
db.session.commit()

beacon1 = Beacon(name="Elm City Market",major="33335",minor="27636", floorplan=floorplan1)
beacon2 = Beacon(name="Elm City Market",major="33334",minor="42933", floorplan=floorplan2)
beacon3 = Beacon(name="Elm City Market",major="33333",minor="52769", floorplan=floorplan1)
db.session.add(beacon1)
db.session.commit()

