from flask import (Flask, render_template, Response, request, flash,
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from flask.ext.login import login_user, logout_user, current_user, login_required
from main import login_manager
from main import app
import pdb
from beacon.models import *

beacon = Blueprint('beacon', __name__, template_folder="templates")

@beacon.route('/get_store_information', methods=["POST"])
def get_store_information():
    major = int(request.get_json().get('major'))
    beacon = Beacon.query.filter(Beacon.major == major).first()
    if beacon is None:
        return jsonify({'success': False})
    company = beacon.floorplan.company
    return jsonify({'name': company.name, 'address1': company.address1, 'address2': company.address2, 'city': company.city, 'state': company.state, 'zipcode': company.zipcode, 'profile_image': company.profile_image, 'phone': company.phone, 'hoursmonday': company.hoursmonday, 'hourstuesday': company.hourstuesday, 'hourswednesday': company.hourswednesday, 'hoursthursday': company.hoursthursday, 'hoursfriday': company.hoursfriday, 'hourssaturday': company.hourssaturday, 'hourssunday': company.hourssunday})


@beacon.route('/add_coordinate_data', methods=["POST"])
def add_coordinate_data():
    major = request.get_json().get('major')
    points = request.get_json().get('points')
    uuid = request.get_json().get('UUID')
    # print major, points, uuid
    return jsonify({'success': True})