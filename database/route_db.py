from database.connector import Connector


def add_route_to_db(route, table_name):
    connector = Connector()
    db_connector = connector.connect_to_database()
    cursor = db_connector.cursor()
    cursor.execute((f'''INSERT INTO {table_name} ("id", user_id, route_name, grade_index, "date", comment) VALUES (DEFAULT, {route.user_id}, '{route.route_name}', {route.grade_index}, '{route.date}', '{route.comment}')'''))
    db_connector.commit()


def remove_data_from_db(table_name, id):
    connector = Connector()
    db_connector = connector.connect_to_database()
    cursor = db_connector.cursor()
    cursor.execute((f'DELETE FROM {table_name} WHERE "id"={id}'))
    db_connector.commit()
