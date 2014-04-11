from flask import (Flask, render_template, Response, request, 
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from user.models import *
from datetime import datetime

user = Blueprint('user', __name__, template_folder="templates")

@user.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	email = request.form['email']
	password = request.form['password']
	user = User(firstname=firstname, lastname=lastname, email=email)
	user.hash_password(password)
	user.registered_on=datetime.utcnow()
	db.session.add(user)
	db.session.commit()
	return "hello"