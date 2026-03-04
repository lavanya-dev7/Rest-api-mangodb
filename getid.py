from flask import Flask, jsonify

app = Flask(__name__)

# Fake database (in-memory list)
users = [
    {"id": 1, "name": "Lavanya"},
    {"id": 2, "name": "Arun"}
]

# ----------------------------
# GET ALL USERS
# ----------------------------
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# ----------------------------
# GET USER BY ID
# ----------------------------
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404


# ----------------------------
# RUN SERVER
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)

