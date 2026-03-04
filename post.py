from flask import Flask, jsonify, request

app = Flask(__name__)

# -----------------------------------
# Fake Database (In-Memory)
# -----------------------------------
users = [
    {"id": 1, "name": "Lavanya"},
    {"id": 2, "name": "Karthi"}
]

# -----------------------------------
# GET ALL USERS
# -----------------------------------
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# -----------------------------------
# GET USER BY ID
# -----------------------------------
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200

    return jsonify({"message": "User not found"}), 404


# -----------------------------------
# CREATE NEW USER (POST)
# -----------------------------------
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()

    if not new_user:
        return jsonify({"message": "Invalid data"}), 400

    # Check duplicate ID
    for user in users:
        if user["id"] == new_user["id"]:
            return jsonify({"message": "User ID already exists"}), 400

    users.append(new_user)

    return jsonify({
        "message": "User created successfully",
        "user": new_user
    }), 201

if __name__=="__main__":
	app.run(debug=True)




