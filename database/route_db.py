from database.connector import Connector


def add_route_to_db(route):
    connector = Connector()
    conn = connector.connect_to_database()
    cursor = conn.cursor()
    cursor.execute((f'''INSERT INTO routes ("id", user_id, route_name, grade_index, rating_system, "date") VALUES (DEFAULT, {route.user_id}, '{route.route_name}', {route.grade_index},'{route.rating_system}', '{route.date}')'''))
    conn.commit()

def remove_route_from_db(route):
    connector = Connector()
    conn = connector.connect_to_database()
    cursor = conn.cursor()
    cursor.execute((f'DELETE FROM routes WHERE "id"={route.id}'))

