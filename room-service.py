from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.hotel_management
rooms = db.rooms

@app.route('/room/<room_id>', methods=['GET'])
def get_room(room_id):
    room = rooms.find_one({'_id': ObjectId(room_id)})
    if room:
        room['_id'] = str(room['_id'])
        return jsonify(room), 200
    else:
        return jsonify({"error": "Room not found"}), 404

@app.route('/room/<room_id>/status', methods=['PUT'])
def update_status(room_id):
    status = request.json.get('status')
    result = rooms.update_one({'_id': ObjectId(room_id)}, {'$set': {'status': status}})
    if result.modified_count:
        return jsonify({"msg": "Room status updated"}), 200
    else:
        return jsonify({"error": "Update failed"}), 400

@app.route('/room/<room_id>/pricing', methods=['PUT'])
def update_pricing(room_id):
    new_price = request.json.get('price')
    result = rooms.update_one({'_id': ObjectId(room_id)}, {'$set': {'price': new_price}})
    if result.modified_count:
        return jsonify({"msg": "Room pricing updated"}), 200
    else:
        return jsonify({"error": "Update failed"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)
