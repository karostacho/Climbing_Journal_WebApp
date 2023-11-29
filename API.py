from flask import Flask, jsonify, request
from database.api_db import get_data_from_table, get_data_by_id, update_user_by_id, get_routes_of_user_by_id, get_all_routes_of_user, update_route_by_id
from database.user_db import add_user_to_db, find_user_id, check_if_user_in_db
from werkzeug.security import generate_password_hash
from model.user import User
from model.route import Route
from database.route_db import remove_data_from_db, add_route_to_db, find_route_id
from app import find_rock_grade_index
from database.sql_data import SqlData


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
			update_user_by_id(user_id, email, name, hashed_password)
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


@app.route('/users/<int:user_id>/routes', methods=['GET'])
def get_routes(user_id):
	try:
		routes = get_all_routes_of_user(user_id)
		return jsonify(routes)
	except:
		return jsonify({'error':'Internal Sever Error'}), 500


@app.route('/users/<int:user_id>/routes/<int:route_id>', methods=['GET'])
def get_route_by_id(user_id, route_id):
	try:
		route = get_routes_of_user_by_id(user_id, route_id)
		if not route:
			return jsonify({'error':'Route not found'}), 404
		return jsonify(route)
	except:
		return jsonify({'error':'Internal Sever Error'}), 500
	


@app.route('/users/<int:user_id>/routes', methods=['POST'])
def create_route(user_id):
	routes_data = request.json
	if routes_data is None:
		return jsonify({'error': 'No data provided'}), 400
	comment = routes_data.get('comment')
	date = routes_data.get('date')
	route_name = routes_data.get('route_name')
	grade_index = routes_data.get('grade_index')
	if not date or not route_name or not grade_index:
		return jsonify({'error': 'Missing required fields'}), 400
	else:
		try:
			route = Route(user_id, route_name, grade_index, date, comment)
			add_route_to_db(route, "lead_climbing_routes")
			new_route = {'comment':comment, 'route_name': route_name, 'date': date, 'grade_index': grade_index}
			return jsonify({'message': 'Route created successfully', 'route': new_route}), 201
		except:
			return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/users/<int:user_id>/routes/<int:route_id>', methods=['DELETE'])
def delete_route(user_id, route_id):
	user = get_data_by_id('users', user_id)
	if not user:
		return jsonify({'error':'User not found'}), 404
	route = get_routes_of_user_by_id(user_id, route_id)
	if not route:
		return jsonify({'error':'Route not found'}), 404
	else:
		try:
			remove_data_from_db('lead_climbing_routes', route_id)
			return jsonify({'message': 'Route deleted successfully'})
		except:
			return jsonify({'error': 'Internal Server Error'}), 500


@app.route('/users/<int:user_id>/routes/<int:route_id>', methods=['PUT'])
def update_route(user_id, route_id):
	user = get_data_by_id('users', user_id)
	if not user:
		return jsonify({'error':'User not found'}), 404
	route = get_routes_of_user_by_id(user_id, route_id)
	if not route:
		return jsonify({'error':'Route not found'}), 404
	else:
		route_data = request.json
		if route_data is None:
			return jsonify({'error': 'No data provided'}), 400
		comment = route_data.get('comment')
		date = route_data.get('date')
		route_name = route_data.get('route_name')
		grade_index = route_data.get('grade_index')
		try:
			update_route_by_id(route_id, user_id,comment,date,grade_index,route_name)
			updated_route = get_routes_of_user_by_id(user_id, route_id)
			return jsonify({'message': 'Route updated successfully', 'route': updated_route})
		except:
			return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == "__main__":
    app.run()