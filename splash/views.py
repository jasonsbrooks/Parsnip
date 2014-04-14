from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from flask.ext.login import login_user, logout_user, current_user, login_required
from user.models import *
from main import app
from functools import wraps



splash = Blueprint('splash', __name__, template_folder="")

def get_pending_users(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated():
            pending_users = current_user.company.users.filter(User.account_approved == False).all()
            g.pending_users = pending_users
        return f(*args, **kwargs)
    return decorated_function

@splash.route('/')
def index():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('splash.dashboard'))
    return render_template('templates/home.html')

@splash.route('/dashboard')
@login_required
@get_pending_users
def dashboard():
    return render_template('templates/dashboard.html')

@splash.route('/visuals')
@get_pending_users
def visuals():
    return render_template('templates/visuals.html')

@splash.route('/heatmap')
@get_pending_users
def heatmap():
    return render_template('templates/heatmap.html')

@splash.route('/editor')
@get_pending_users
def editor():
    return render_template('templates/svg-edit-2.6/editor.html')
