from flask import Flask, jsonify, request
from database.api_db import get_data_from_table, get_data_by_id, update_data_by_id
from database.user_db import add_user_to_db, find_user_id, check_if_user_in_db
from werkzeug.security import generate_password_hash
from model.user import User
from database.route_db import remove_data_from_db


app = Flask(__name__)
app.debug = True


@app.route('/users', methods=['GET'])
def get_users():
	try:
		users = get_data_from_table('users')
		return jsonify(users)
	except:
		return jsonify({'error':'Internal Sever Error'}), 500


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
	try:
		user = get_data_by_id('users', user_id)
		if not user:
			return jsonify({'error':'User not found'}), 404
		return jsonify(user)
	except:
		return jsonify({'error':'Internal Sever Error'}), 500


@app.route('/users', methods=['POST'])
def create_user():
	user_data = request.json
	if user_data is None:
		return jsonify({'error': 'No data provided'}), 400
	email = user_data.get('email')
	name = user_data.get('name')
	password = user_data.get('password')
	if not email or not name or not password:
		return jsonify({'error': 'Missing required fields'}), 400
	account = check_if_user_in_db(email)
	if account:
		return jsonify({'error':'Account already exists'}), 400
	else:
		try:
			hashed_password = generate_password_hash(password)
			user = User(None, name, hashed_password, email)
			add_user_to_db(user)
			user_id = find_user_id(email)
			new_user = get_data_by_id('users', user_id)
			return jsonify({'message': 'User created successfully', 'user': new_user}), 201
		except:
			return jsonify({'error': 'Internal Server Error'}), 500
	

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
	user = get_data_by_id('users', user_id)
	if not user:
		return jsonify({'error':'User not found'}), 404
	else:
		user_data = request.json
		if user_data is None:
			return jsonify({'error': 'No data provided'}), 400
		email = user_data.get('email')
		name = user_data.get('name')
		password = user_data.get('password')
		try:
			hashed_password = generate_password_hash(password)
			update_data_by_id('users', user_id, email, name, hashed_password)
			updated_user = get_data_by_id('users', user_id)
			return jsonify({'message': 'User updated successfully', 'user': updated_user})
		except:
			return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
	user = get_data_by_id('users', user_id)
	if not user:
		return jsonify({'error':'User not found'}), 404
	else:
		try:
			remove_data_from_db('users', user_id)
			return jsonify({'message': 'User deleted successfully'})
		except:
			return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/routes', methods=['GET'])
def get_routes():
	routes = get_data_from_table('lead_climbing_routes')
	return jsonify(routes) #500


if __name__ == "__main__":
    app.run()