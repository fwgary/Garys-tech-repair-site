from website import create_app, db
from website.models import User
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from flask_socketio import SocketIO, emit
import socket

app = create_app()
socketio = SocketIO(app)

if __name__ == '__main__':
  socketio.run(app,
                 host='0.0.0.0',
                 port=81,
                 debug=True,
                 use_reloader=True,
                 log_output=True)