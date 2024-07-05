from flask import Flask, request, jsonify
from pymongo import MongoClient, errors
from bson import ObjectId
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app = Flask(__name__)

try:
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
    client.server_info()
    db = client.hotel_management
    rooms = db.rooms
    logger.info("MongoDB connected successfully")
except errors.ServerSelectionTimeoutError as err:
    logger.error("Failed to connect to MongoDB: %s", err)

@app.before_request
def log_request_info():
    logger.info('Received %s request to %s', request.method, request.path)

@app.after_request
def log_response_info(response):
    logger.info('Responded with status %s', response.status)
    return response

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/room/<room_id>', methods=['GET'])
def get_room(room_id):
    try:
        room = rooms.find_one({'_id': ObjectId(room_id)})
        if room:
            room['_id'] = str(room['_id'])
            return jsonify(room), 200
        else:
            return jsonify({"error": "Room not found"}), 404
    except Exception as e:
        logger.error("Error fetching room data: %s", e)
        return jsonify({"error": "Server error"}), 500

@app.route('/room/<room_id>/status', methods=['PUT'])
def update_status(room_id):
    try:
        status = request.json.get('status')
        result = rooms.update_one({'_id': ObjectId(room_id)}, {'$set': {'status': status}})
        if result.modified_count:
            return jsonify({"msg": "Room status updated"}), 200
        else:
            return jsonify({"error": "Update failed or no change made"}), 404
    except Exception as e:
        logger.error("Error updating room status: %s", e)
        return jsonify({"error": "Server error"}), 500

@app.route('/room/<room_id>/pricing', methods=['PUT'])
def update_pricing(room_id):
    try:
        new_price = request.json.get('price')
        result = rooms.update_one({'_id': ObjectId(room_id)}, {'$set': {'price': new_price}})
        if result.modified_count:
            return jsonify({"msg": "Room pricing updated"}), 200
        else:
            return jsonify({"error": "Update failed or no change made"}), 404
    except Exception as e:
        logger.error("Error updating room pricing: %s", e)
        return jsonify({"error": "Server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)
