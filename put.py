from flask import Flask, jsonify, request

app = Flask(__name__)

# Fake database (stored in memory)
users = [
    {"id": 1, "name": "Lavanya"},
    {"id": 2, "name": "Arun"}
]

# ------------------------
# GET ALL USERS
# ------------------------
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# ------------------------
# CREATE USER (POST)
# ------------------------
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    users.append(data)

    return jsonify(data), 201


# ------------------------
# UPDATE USER (PUT)
# ------------------------
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404


# ------------------------
# RUN SERVER
# ------------------------
if __name__ == '__main__':
    app.run(debug=True)
