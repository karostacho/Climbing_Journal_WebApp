
#column names from table

cursor.execute('SELECT * FROM bouldering_grades LIMIT 0')
column_names = [desc[0] for desc in cursor.description[1:]]