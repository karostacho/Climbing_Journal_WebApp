from database.connector import get_cursor, Connector

def get_data_from_table(table):
    cursor = get_cursor()
    cursor.execute((f"SELECT * FROM {table}"))
    data = get_data_with_column_names(cursor)
    return data

def get_data_with_column_names(cursor):
    column_names = [desc[0] for desc in cursor.description]
    all_rows = cursor.fetchall()
    data = []
    for row in all_rows:
        formatted_row = {}
        for i, value in enumerate(row):
            formatted_row[column_names[i]] = value
        data.append(formatted_row)
    return data

def get_data_by_id(table, id):
    cursor = get_cursor()
    cursor.execute((f'SELECT * FROM {table} WHERE "id"={id}'))
    data = get_data_with_column_names(cursor)
    return data
    
def update_data_by_id(table, id, email, name, password):
    connector = Connector()
    db_connector = connector.connect_to_database()
    cursor = db_connector.cursor()
    cursor.execute((f'''UPDATE {table} SET email = '{email}', name = '{name}', password = '{password}' WHERE "id"={id}'''))
    db_connector.commit()
    
def test(table, email, name, password, id):
    print(f'''UPDATE {table} SET email = '{email}', name = '{name}', password = '{password}' WHERE "id"={id}''')	

