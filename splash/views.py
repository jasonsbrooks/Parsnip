from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)

splash = Blueprint('splash', __name__, template_folder="")

@splash.route('/')
def home():
    return render_template('templates/home.html')

@splash.route('/login')
def login():
    return render_template('templates/login.html')

@splash.route('/dashboard')
def dashboard():
    return render_template('templates/dashboard.html')

@splash.route('/visuals')
def visuals():
	return render_template('templates/visuals.html')