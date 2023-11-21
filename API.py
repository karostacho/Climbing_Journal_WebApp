from flask import Flask, jsonify, request
from database.api_db import get_data_from_table
from database.user_db import add_user_to_db
from werkzeug.security import generate_password_hash
from model.user import User

app = Flask(__name__)
app.debug = True

@app.route('/users', methods=['GET'])
def get_users():
	users = get_data_from_table('users')
	return jsonify(users)

@app.route('/create-user', methods=['POST'])
def create_user():
	user_data = request.json
	if user_data is None:
		return jsonify({'error': 'No data provided'}), 400
	email = user_data.get('email')
	name = user_data.get('name')
	password = user_data.get('password')
	if not email or not name or not password:
		return jsonify({'error': 'Missing required fields'}), 400
	else:
		hashed_password = generate_password_hash(password)
		user = User(None, name, hashed_password, email)
		add_user_to_db(user)
		return jsonify({'message': 'User created successfully'})


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
	



@app.route('/routes', methods=['GET'])
def get_routes():
	routes = get_data_from_table('lead_climbing_routes')
	return jsonify(routes)


if __name__ == "__main__":
    app.run()