from password import password

import psycopg2
import itertools

conn = psycopg2.connect(
            host='snuffleupagus.db.elephantsql.com',
            port='5432',
            database='qpgrmemq',
            user='qpgrmemq',
            password=password
            )
            #cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCurso
cursor = conn.cursor()
climbing_type_table = 'rock_climbing_grades'
cursor.execute((f'SELECT * FROM {climbing_type_table} LIMIT 0'))
rating_systems = [desc[0] for desc in cursor.description[1:]]
#print(rating_systems)

cursor.execute(f'SELECT * FROM {climbing_type_table}')
data = [dict(zip(rating_systems, row)) for row in cursor.fetchall()]

cursor.close()
conn.close()
# Print the resulting list of dictionaries
print(data)