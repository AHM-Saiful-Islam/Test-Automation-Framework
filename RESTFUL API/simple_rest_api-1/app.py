from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (acting as a database)
users = [
    {"id": 1, "name": "Naima", "email": "naima@tu.com"},
    {"id": 2, "name": "Rasel", "email": "rasel@tu.com"}
]

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the simple rest api!"})

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if "name" not in new_user or "email" not in new_user:
        return jsonify({"error": "Name and email are required"}), 400
    new_user["id"] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

# Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    update_data = request.get_json()
    user.update(update_data)
    return jsonify(user)

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)

