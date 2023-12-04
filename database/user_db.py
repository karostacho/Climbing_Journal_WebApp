from database.connector import Connector, get_cursor

def check_if_user_in_db(email):
    cursor = get_cursor()
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
    cursor = get_cursor()
    cursor.execute(f"""SELECT "password" from users where email = '{email}'""")
    tuple = cursor.fetchone()
    password = tuple[0]
    return password

def find_user_id(email):
    cursor = get_cursor()
    cursor.execute(f"""SELECT "id" from users where email = '{email}'""")
    tuple = cursor.fetchone()
    id = tuple[0]
    return id

def get_user(email):
    cursor = get_cursor()
    cursor.execute(f"""SELECT * from users where email = '{email}'""")
    user = cursor.fetchall()
    return user
