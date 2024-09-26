# dashboard/dashboard_app.py

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import threading
import logging
from config import Config

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
socketio = SocketIO(app, async_mode='eventlet')

connected_clients = []

@app.route('/')
def index():
    return render_template('index.html')

def send_update(message):
    logging.info(f"Sending update: {message}")
    socketio.emit('update', {'data': message})

@socketio.on('connect')
def handle_connect():
    logging.info('Client connected')
    connected_clients.append(request.sid)
    emit('update', {'data': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    logging.info('Client disconnected')
    connected_clients.remove(request.sid)

@socketio.on('feedback')
def handle_feedback(feedback):
    logging.info(f"Received feedback: {feedback}")
    # Process feedback if needed

def run_dashboard():
    socketio.run(app, debug=False, use_reloader=False)

def start_dashboard():
    thread = threading.Thread(target=run_dashboard)
    thread.daemon = True
    thread.start()
