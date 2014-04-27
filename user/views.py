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
from company.models import *
from flask_mail import Mail, Message

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
    newCompanyBool = False
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('splash.dashboard'))
    if request.method == 'GET':
        currentCompanies = Company.query.all()
        return render_template('register.html', currentCompanies=currentCompanies)
    testAccountApprove = False
    if request.form.get('testAccountApprove', None) == "ok":
        newCompanyBool = True
    firstname = request.form['firstname'].capitalize()
    lastname = request.form['lastname'].capitalize()
    email = request.form['email'].lower()
    company_id = request.form['company_id']
    password = request.form['password']
    if User.query.filter(User.email == email).first() is not None:
        flash('Account already exists for this email address! Please try signing in.')
        return redirect(url_for('user.login', defaultEmail=email))
    if company_id == '':
        company_id = create_company(request)
        newCompanyBool = True
    if Company.query.get(int(company_id)) is None:
        return "You hacked the system!"
    user = User(firstname=firstname, lastname=lastname, email=email, company=Company.query.get(int(company_id)))
    if newCompanyBool:
        user.account_approved = True
    else:
        user.account_approved = False
    user.hash_password(password)
    user.registered_on=datetime.utcnow()
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('user.login', defaultEmail=email))

def create_company(requestObj):
    companyname = request.form['companyname']
    address1 = request.form['address1']
    address2 = request.form['address2']
    city = request.form['city']
    state = request.form['state']
    zipcode = request.form['zipcode']
    phone = request.form['phone']
    hoursmonday = request.form['hoursmonday-start'] + ' - ' + request.form['hoursmonday-end']
    hourstuesday = request.form['hourstuesday-start'] + ' - ' + request.form['hourstuesday-end']
    hourswednesday = request.form['hourswednesday-start'] + ' - ' + request.form['hourswednesday-end']
    hoursthursday = request.form['hoursthursday-start'] + ' - ' + request.form['hoursthursday-end']
    hoursfriday = request.form['hoursfriday-start'] + ' - ' + request.form['hoursfriday-end']
    hourssaturday = request.form['hourssaturday-start'] + ' - ' + request.form['hourssaturday-end']
    hourssunday = request.form['hourssunday-start'] + ' - ' + request.form['hourssunday-end']

    comp = Company(name=companyname, address1=address1, address2=address2, city=city, state=state, zipcode=zipcode, phone=phone, hoursmonday=hoursmonday, hourstuesday=hourstuesday, hourswednesday=hourswednesday, hoursthursday=hoursthursday, hoursfriday=hoursfriday, hourssaturday=hourssaturday, hourssunday=hourssunday)
    db.session.add(comp)
    db.session.commit()
    return comp.id



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

@user.route('/new-company', methods=['GET', 'POST'])
def add_company():
    pass

@user.route('/unvalidated')
def unvalidated():
    return render_template('unvalidated.html')

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

@user.route('/edit_store_settings', methods=['POST'])
@login_required
def edit_store_settings():
    # firstname = request.form['firstname'].capitalize()
    # lastname = request.form['lastname'].capitalize()
    # password1 = request.form['password1']
    # password2 = request.form['password2']
    # u = g.user
    # u.firstname = firstname
    # u.lastname = lastname
    # if password1 is not None:
    #     u.hash_password(password1)
    # db.session.commit()
    # flash('Account settings successfully changed!')
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
    return jsonify({"success": "true", "email": email})

@user.route('/settings')
@login_required
@get_pending_users
def settings():
    return render_template('settings.html')

@user.route('/photo_upload/<ptype>', methods=["POST"])
@login_required
def photo_upload(ptype):
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
    if ptype == "user":
        u.profilepic = url
    if ptype == "company":
        u.company.profile_image = url
    db.session.commit()
    return url
