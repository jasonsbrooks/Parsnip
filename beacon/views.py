from flask import (Flask, render_template, Response, request, flash,
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from flask.ext.login import login_user, logout_user, current_user, login_required
from main import login_manager
from main import app
import pdb
from datetime import datetime
from beacon.models import *
from beacon import *
from advertisement.models import *

beacon = Blueprint('beacon', __name__, template_folder="templates")

@beacon.route('/get_store_information', methods=["POST"])
def get_store_information():
    major = int(request.json.get('major'))
    beacon = Beacon.query.filter(Beacon.major == major).first()
    if beacon is None:
        return jsonify({'success': False})
    company = beacon.floorplan.company
    advertisements = company.advertisements.all()
    deals = []
    details = []
    descriptions = []
    images = []
    for ad in advertisements:
        deals.append(ad.name)
        details.append(ad.details)
        descriptions.append(ad.description)
        images.append(ad.image_url)
    return jsonify({'deals': deals, 'details': details, 'descriptions': descriptions, 'images': images, 'name': company.name, 'address1': company.address1, 'address2': company.address2, 'city': company.city, 'state': company.state, 'zipcode': company.zipcode, 'profile_image': company.profile_image, 'phone': company.phone, 'hoursmonday': company.hoursmonday, 'hourstuesday': company.hourstuesday, 'hourswednesday': company.hourswednesday, 'hoursthursday': company.hoursthursday, 'hoursfriday': company.hoursfriday, 'hourssaturday': company.hourssaturday, 'hourssunday': company.hourssunday})


@beacon.route('/add_coordinate_data', methods=["POST"])
def add_coordinate_data():
    points = request.json.get('points')
    UUID = request.json.get('UUID')
    userID = request.json.get('userID')
    currenttime = datetime.utcnow()
    print points, userID
    xyDistList = []
    for dist in points:
        b = Beacon.query.filter(Beacon.major == dist[0]).filter(Beacon.minor == dist[1]).first()
        entry = Distance(distance=dist[2], time=currenttime, beacon=b, userID=userID)
        xyDistList.append([b.xPos, b.yPos, dist[2]])
        db.session.add(entry)
        db.session.commit()
    # print xyDistList
    intersect = intersection(xyDistList)
    print intersect
    if intersect is not False:
        p = Position(xPos=intersect[0],yPos=intersect[1], timeRegistered=currenttime, floorplan=b.floorplan)
        db.session.add(p)
        db.session.commit()
    return jsonify({'success': True})
