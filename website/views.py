from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import User
from flask_socketio import SocketIO, emit
from . import db
import json
import requests

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("devTesting.html")

@views.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@views.route('/faq')
def faq():
    return render_template("FAQ.html")