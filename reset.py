# importa all models
from user.models import *
from floorplan.models import *
from datetime import datetime
from beacon.models import *
from company.models import *
from advertisement.models import *

# recreate the database
db.drop_all()
db.create_all()

# create two companies
company1 = Company(name="Elm City Market", address1="777 Chapel St.", city="New Haven", state="Connecticut", zipcode="06520", profile_image="https://www.elmcitymarket.coop/wp-content/themes/elmcity/images/layout/header.logo.jpg", phone="12036240441", hoursmonday="8:00am - 9:00pm", hourstuesday="8:00am - 9:00pm", hourswednesday="8:00am - 9:00pm", hoursthursday="8:00am - 9:00pm", hoursfriday="8:00am - 9:00pm", hourssaturday="8:00am - 9:00pm", hourssunday="9:00am - 9:00pm")
company2 = Company(name="Gourmet Heaven", address1="15 Broadway", city="New Haven", state="Connecticut", zipcode="06520", profile_image="http://gourmetheaven.com/wp-content/uploads/2013/02/ghgh1.png", phone="12037874533", hoursmonday="12:00am - 11:59pm", hourstuesday="12:00am - 11:59pm", hourswednesday="12:00am - 11:59pm", hoursthursday="12:00am - 11:59pm", hoursfriday="12:00am - 11:59pm", hourssaturday="12:00am - 11:59pm", hourssunday="12:00am - 11:59pm")
db.session.add(company1)
db.session.add(company2)
db.session.commit()

# assign three users, 1 who is not the first user for the company, and 2 who are the first users
u1 = User(firstname="Jason", lastname="Brooks", email="jason.brooks@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
u2 = User(firstname="Pranav", lastname="Maddi", email="pranav.maddi@yale.edu", profilepic="https://scontent-b-iad.xx.fbcdn.net/hphotos-prn2/t1.0-9/9749_10202200719724608_650155214_n.jpg", company=company1, account_approved=True)
u3 = User(firstname="Charles", lastname="Jin", email="charles.jin@yale.edu", profilepic="https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-ash2/t31.0-8/462503_10201093936700713_711489518_o.jpg", company=company2, account_approved=True)
# Extra data for when we want to test user approval
# u4 = User(firstname="Juan", lastname="Brooks", email="jason.brooksdasdfs@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
# u5 = User(firstname="Javier", lastname="Brooks", email="jason.brookasdfs@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
# u6 = User(firstname="Jermaine", lastname="Brooks", email="jason.brooasdfks@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
# u7 = User(firstname="Flan", lastname="Brooks", email="jason.brooasdgavcks@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
# u8 = User(firstname="Pottery", lastname="Brooks", email="jason.brook4543s@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
# u9 = User(firstname="Mosiah", lastname="Brooks", email="jason.brookc4s@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
# u10 = User(firstname="Naincheng", lastname="Brooks", email="jason.c425brooks@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
# u11 = User(firstname="Heroku", lastname="Brooks", email="jason.brook3245cs@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
# u12 = User(firstname="Hola", lastname="Brooks", email="jason.brookshdf89s@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)
# u13 = User(firstname="Tween", lastname="Brooks", email="jason.brook89asdfs@yale.edu", profilepic="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash2/t1.0-9/536283_218804554919317_1952113665_n.jpg", company=company1, account_approved=False)

# Hash passwords for database
u1.hash_password("helloworld")
u2.hash_password("goodbyeworld")
u3.hash_password("helloworld")
# u4.hash_password("helloworld")
# u5.hash_password("helloworld")
# u6.hash_password("helloworld")
# u7.hash_password("helloworld")
# u8.hash_password("helloworld")
# u9.hash_password("helloworld")
# u10.hash_password("helloworld")
# u11.hash_password("helloworld")
# u12.hash_password("helloworld")
# u13.hash_password("helloworld")
u1.registered_on=datetime.utcnow()
u2.registered_on=datetime.utcnow()
u3.registered_on=datetime.utcnow()
# u4.registered_on=datetime.utcnow()
# u5.registered_on=datetime.utcnow()
# u6.registered_on=datetime.utcnow()
# u7.registered_on=datetime.utcnow()
# u8.registered_on=datetime.utcnow()
# u9.registered_on=datetime.utcnow()
# u10.registered_on=datetime.utcnow()
# u11.registered_on=datetime.utcnow()
# u12.registered_on=datetime.utcnow()
# u13.registered_on=datetime.utcnow()

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
# db.session.add(u4)
# db.session.add(u5)
# db.session.add(u6)
# db.session.add(u7)
# db.session.add(u8)
# db.session.add(u9)
# db.session.add(u10)
# db.session.add(u11)
# db.session.add(u12)
# db.session.add(u13)

db.session.commit()

# Create three floorplans among the companies
floorplan1 = Floorplan(name="Main Floor", floorplan_url="https://s3.amazonaws.com/heaped/DFee.svg", company=company1)
floorplan2 = Floorplan(name="Main Floor", floorplan_url="https://s3.amazonaws.com/heaped/hello.svg", company=company2)
floorplan3 = Floorplan(name="Upstairs", floorplan_url="https://s3.amazonaws.com/heaped/hello.svg", company=company1)
db.session.add(floorplan1)
db.session.add(floorplan2)
db.session.add(floorplan3)
db.session.commit()

# Create three becons in the stores
beacon1 = Beacon(name="Elm City Market",major="33335",minor="27636", floorplan=floorplan1, xPos=0, yPos=0)
beacon2 = Beacon(name="Elm City Market",major="33334",minor="42933", floorplan=floorplan2, xPos=0, yPos=5)
beacon3 = Beacon(name="Elm City Market",major="33333",minor="52769", floorplan=floorplan1, xPos=5, yPos=0)
db.session.add(beacon1)
db.session.add(beacon2)
db.session.add(beacon3)
db.session.commit()

# Create 4 advertisements, 2 in each store
ad1 = Advertisement(name="Sale 30%% off", description="Summer is coming and we are trying to clear our winter items. Hats, gloves scarves, sweaters, and anything with a red tag are an extra 30%% off for up to 70%% off current-season stock.", details="Take an extra 30%% off all sale items for up to 70%% off", image_url="http://cdnd.lystit.com/photos/2013/10/08/urban-outfitters-pink-stone-cold-fox-x-uo-lacestrap-cami-product-1-13926596-249764859_large_flex.jpeg", company=company1)
ad2 = Advertisement(name="Spring shirting NOW $39", description="The lightweight, warm weather-ready Koto Breezy, available in new colors and prints, exclusively at UO. Limited time only.", details="We've got your MOST LOVED SHIRT.", image_url="http://www.luckymag.com/shopping/2013/06/urban-outfitters-stone-cold-fox/_jcr_content/par/cn_contentwell/par-main/cn_blogpost/cn_slideshow/item1.rendition.slideshowVertical.stone-cold-fox-uo-scallop-top.jpg", company=company2)
ad3 = Advertisement(name="JEANS for $29.99", description="The denim we're dreaming of this summer, from overall dresses and bodysuits or zip-front vests and the perfect cutoff jean shorts.", details="Warm evenings and cool drinks", image_url="http://picture-cdn.wheretoget.it/xov726-i.jpg", company=company1)
ad4 = Advertisement(name="10%% off STONE COLD FOX X UO", description="Introducing our newest exclusive collection from LA label Stone Cold Fox: Perfectly playful and vintage-inspired garments made for springtime fun.", details="Limited-time exclusive designer collab: 10%% off with this app", image_url="http://cdn-s3-3.wanelo.com/product/image/8866481/x200.jpg", company=company2)
db.session.add(ad1)
db.session.add(ad2)
db.session.add(ad3)
db.session.add(ad4)
db.session.commit()


