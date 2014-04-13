from flask import Blueprint, send_from_directory, request, render_template, redirect, flash, session, url_for, g
from floorplan import *
from main import app
import boto
from boto.s3.key import Key
import os
from flask import jsonify

floorplan = Blueprint('floorplan', __name__, template_folder="templates")

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = 'heaped'


@floorplan.route('/save_floorplan', methods=["POST"])
def save_floorplan():
    contents = request.form['fileContents']
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(bucket_name)
    k = Key(bucket)
    k.key = "hello.svg"
    k.set_contents_from_string(contents)
    k.make_public()
    url = k.generate_url(expires_in=0, query_auth=False)
    print url
    return url

@floorplan.route('/edit')
def edit_floorplan():
    return render_template('edit.html')

@floorplan.route('/edit_tmp')
def edit_floorplan_tmp():
    return render_template('edit_old.html')

# @floorplan.route('/michael', methods=["POST"])
# def michael():
#     points = request.get_json().get('points')
#     userID = request.get_json().get('userID')
#     print points
#     print userID
#     return jsonify({'success': True})