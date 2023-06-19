import psycopg2
import getpass
   
def connect_to_database():
    conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
    )
    cursor = conn.cursor()
    return cursor

host = 'snuffleupagus.db.elephantsql.com'
port = '5432'
database = 'qpgrmemq'
user = 'qpgrmemq'
password = password = getpass.getpass(prompt='Enter the database password: ')

cursor = connect_to_database()
cursor.execute('SELECT * FROM bouldering_grades LIMIT 0')
column_names = [desc[0] for desc in cursor.description[1:]]

