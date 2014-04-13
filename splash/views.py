from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from flask.ext.login import login_user, logout_user, current_user, login_required

splash = Blueprint('splash', __name__, template_folder="")

@splash.route('/')
def index():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('splash.dashboard'))
    return render_template('templates/home.html')

@splash.route('/dashboard')
@login_required
def dashboard():
    return render_template('templates/dashboard.html')

@splash.route('/visuals')
def visuals():
    return render_template('templates/visuals.html')

@splash.route('/heatmap')
def heatmap():
    return render_template('templates/heatmap.html')

@splash.route('/editor')
def editor():
    return render_template('templates/svg-edit-2.6/editor.html')
