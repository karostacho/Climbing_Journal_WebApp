from database.connector import Connector, get_cursor

def get_data_from_table(table):
    cursor = get_cursor()
    cursor.execute((f"SELECT * FROM {table}"))
    column_names = [desc[0] for desc in cursor.description]
    users = cursor.fetchall()
    users_data = []
    for row in users:
        formatted_row = {}
        for i, value in enumerate(row):
            formatted_row[column_names[i]] = value
        users_data.append(formatted_row)
    return users_data