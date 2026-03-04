from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

# -------------------------
# GET ALL USERS
# -------------------------
@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return jsonify(users), 200

# -------------------------
# ADD USER
# -------------------------
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
