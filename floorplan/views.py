from flask import Blueprint, send_from_directory, request, render_template, redirect, flash, session, url_for, g
from floorplan import *
from main import app
import boto
from boto.s3.key import Key
import os

floorplan = Blueprint('floorplan', __name__, template_folder="")

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = 'heaped'

@floorplan.route('/modify_floorplan', methods=["POST"])
def modify_floorplan():
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