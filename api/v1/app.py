#!/usr/bin/python3
"""The main app"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(error):
    """Cole the session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Return this if the request not have a match"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    port_d = '5000'
    host_d = '0.0.0.0'

    if os.getenv('HBNB_API_PORT'):
        port_d = os.getenv('HBNB_API_PORT')

    if os.getenv('HBNB_API_HOST'):
        host_d = os.getenv('HBNB_API_HOST')

    app.run(host=host_d, port=port_d, threaded=True, debug=True)
