"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from sms import sendSMS
# from admin import setup_admin
# from models import db, User
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# MIGRATE = Migrate(app, db)
# db.init_app(app)
# CORS(app)
# setup_admin(app)
from datastructure import Queue
# from models import Person
from twilio.rest import Client
app = Flask(__name__)
app.url_map.strict_slashes = False
db = Queue();

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/new', methods=['POST'])
def new():
    guest = request.json
    size = db.size()
    db.enqueue(guest)
    responseBody = {
        "msg": f"Hello, {guest['name']} you've been added, currently there are {size} customers in front of you"
    }
    sendSMS(responseBody['msg'], guest['phone'])
    return jsonify(responseBody), 200

@app.route('/next', methods=['GET'])
def next():
    if db.size() > 0:
        guest = db.dequeue()
        responseBody = {
            "msg": f"Hello, {guest['name']} it is your turn!"
        }
        sendSMS(responseBody['msg'], guest['phone'])
    else:
        responseBody = {
            "msg": f"The queue is empy."
        }

    return jsonify(responseBody), 200

@app.route('/all', methods=['GET'])
def all():
    guestQueue = db.get_queue()
    return jsonify(guestQueue), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
