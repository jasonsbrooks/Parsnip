from flask import (Flask, render_template, Response, request, flash,
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for)

advertisement = Blueprint('advertisement', __name__, template_folder="templates")