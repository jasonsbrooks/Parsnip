from flask import (Flask, render_template, Response, request, flash,
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from flask.ext.login import login_user, logout_user, current_user, login_required
from user.models import *
from datetime import datetime
from main import login_manager
from main import app

user = Blueprint('user', __name__, template_folder="templates")

@app.before_request
def before_request():
    g.user = current_user

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@user.route('/register', methods=['GET', 'POST'])
def register():
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
    print g.user
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('splash.dashboard'))
    if request.method == 'GET':
        email = request.args.get('defaultEmail')
        return render_template('login.html', defaultEmail=email)
    email = request.form['email'].lower()
    password = request.form['password']
    user = User.query.filter(User.email == email).first()
    if (user is None) or (user.verify_password(password) is False):
        flash('Username or Password is invalid')
        return redirect(url_for('user.login'))
    login_user(user)
    return redirect(url_for('splash.dashboard'))


@user.route('/logout')
def logout():
    if g.user is not None and g.user.is_authenticated():
        email = g.user.email
    logout_user()
    return redirect(url_for('user.login', defaultEmail=email)) 


