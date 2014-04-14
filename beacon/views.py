from flask import (Flask, render_template, Response, request, flash,
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)
from flask.ext.login import login_user, logout_user, current_user, login_required
from main import login_manager
from main import app

beacon = Blueprint('beacon', __name__, template_folder="templates")
