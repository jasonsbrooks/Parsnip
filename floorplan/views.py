from flask import Blueprint, send_from_directory, request, render_template, redirect, flash, session, url_for, g
# from floorplan import *
from floorplan.models import *
from main import app
import boto
from boto.s3.key import Key
import os
from flask import jsonify
import pdb
from splash.views import get_pending_users
from flask.ext.login import login_user, logout_user, current_user, login_required


floorplan = Blueprint('floorplan', __name__, template_folder="templates")

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = 'heaped'


@floorplan.route('/my-floorplans')
@get_pending_users
@login_required
def my_floorplans():
    user = g.user
    floorplans = user.company.floorplans.all()
    return render_template('my-floorplans.html', floorplans=floorplans)

@floorplan.route('/edit-floorplan/<fpid>')
@login_required
@get_pending_users
def edit_floorplan(fpid):
    fpID = fpid
    current_user = g.user
    if current_user.company.floorplans.filter(Floorplan.id == fpID).first() is None:
        return redirect(url_for('floorplan.my_floorplans'))
    fp = Floorplan.query.get(fpID)
    return render_template('edit.html', fp=fp)


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



@floorplan.route('/edit_tmp')
def edit_floorplan_tmp():
    return render_template('edit_old.html')
