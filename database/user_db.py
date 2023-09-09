from database.connector import Connector


def check_if_user_in_db(email):
    connector = Connector()
    db_connector = connector.connect_to_database()
    cursor = db_connector.cursor()
    cursor.execute((f"SELECT * FROM users WHERE email = '{email}'"))
    account = cursor.fetchone()
    return account


def add_user_to_db(user):
    connector = Connector()
    db_connector = connector.connect_to_database()
    cursor = db_connector.cursor()
    cursor.execute(f"""INSERT INTO users ("id", "name", email, "password") VALUES (DEFAULT, '{user.name}','{user.e_mail}', '{user.password}')""" )
    db_connector.commit()


def find_user_password(email):
    connector = Connector()
    db_connector = connector.connect_to_database()
    cursor = db_connector.cursor()
    cursor.execute(f"""SELECT "password" from users where email = '{email}'""")
    tuple = cursor.fetchone()
    password = tuple[0]
    return password

def find_user_id(email):
    connector = Connector()
    db_connector = connector.connect_to_database()
    cursor = db_connector.cursor()
    cursor.execute(f"""SELECT "id" from users where email = '{email}'""")
    tuple = cursor.fetchone()
    id = tuple[0]
    return id
