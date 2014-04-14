from flask import (Flask, render_template, Response, request, flash,
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from flask.ext.login import login_user, logout_user, current_user, login_required
from user.models import *
from datetime import datetime
from main import login_manager
from main import app
import boto
from boto.s3.key import Key
from werkzeug.utils import secure_filename
import hashlib
import os
import pdb
from splash.views import get_pending_users

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = 'heaped'

user = Blueprint('user', __name__, template_folder="templates")

@app.before_request
def before_request():
    g.user = current_user


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@user.route('/register', methods=['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('splash.dashboard'))
    if request.method == 'GET':
        return render_template('register.html')
    firstname = request.form['firstname'].capitalize()
    lastname = request.form['lastname'].capitalize()
    email = request.form['email'].lower()
    password = request.form['password']
    if User.query.filter(User.email == email).first() is not None:
        flash('Account already exists for this email address! Please try signing in.')
        return redirect(url_for('user.login', defaultEmail=email))
    user = User(firstname=firstname, lastname=lastname, email=email)
    user.hash_password(password)
    user.registered_on=datetime.utcnow()
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('user.login', defaultEmail=email))

@user.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('splash.dashboard'))
    if request.method == 'GET':
        email = request.args.get('defaultEmail')
        return render_template('login.html', defaultEmail=email)
    email = request.form['email'].lower()
    password = request.form['password']
    user = User.query.filter(User.email == email).first()
    if user is None:
        flash('Email is invalid!')
        return redirect(url_for('user.login'))
    if user.verify_password(password) is False:
        flash('Password is invalid!')
        return redirect(url_for('user.login'))
    if (user.account_approved is False) and (user.company is not None):
        return redirect(url_for('user.unvalidated'))
    login_user(user)
    return redirect(url_for('splash.dashboard'))

@user.route('/unvalidated')
def unvalidated():
    return "Your account has yet to be approved by a member of your team."

@user.route('/edit_account', methods=['POST'])
@login_required
def edit_account():
    firstname = request.form['firstname'].capitalize()
    lastname = request.form['lastname'].capitalize()
    password1 = request.form['password1']
    password2 = request.form['password2']
    u = g.user
    u.firstname = firstname
    u.lastname = lastname
    if password1 is not None:
        u.hash_password(password1)
    db.session.commit()
    flash('Account settings successfully changed!')
    return redirect(url_for('user.settings'))

@user.route('/logout')
@login_required
def logout():
    email = g.user.email
    logout_user()
    return redirect(url_for('user.login', defaultEmail=email))

@user.route('/approval_status', methods=["POST"])
@login_required
def change_approval_status():
    # pdb.set_trace()
    email = request.form['email']
    status = request.form['status']
    u = User.query.filter(User.email == email).first()
    if current_user.company != u.company:
        return jsonify({"success": "false"})
    if status == "approved":
        u.account_approved = True
    else:
        u.company = None
    db.session.commit()
    return jsonify({"success": "true"})

@user.route('/settings')
@login_required
@get_pending_users
def settings():
    return render_template('settings.html')

@user.route('/photo_upload/', methods=["POST"])
@login_required
def photo_upload():
    file = request.files['photo']
    filename = secure_filename(file.filename)
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(bucket_name)
    k = Key(bucket)
    extension = "." + filename.split('.')[-1]
    k.key =  hashlib.sha224(file.read()).hexdigest() + extension
    file.seek(0)
    k.set_contents_from_string(file.read())
    k.make_public()
    url = k.generate_url(expires_in=0, query_auth=False)
    u = g.user
    u.profilepic = url
    db.session.commit()
    return url


