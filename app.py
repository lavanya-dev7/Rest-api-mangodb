
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (acting like database)
users = [
    {"id": 1, "name": "Lavanya"},
    {"id": 2, "name": "Karthi"}
]

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)
