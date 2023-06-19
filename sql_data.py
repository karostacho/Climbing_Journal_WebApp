from connector import Connector

class SqlData():
    def __init__(self):
        self.connector = Connector()

    def get_rating_system(self, climbing_type_table):
        self.connector.execute_sql_query(f'SELECT * FROM {climbing_type_table} LIMIT 0')
        rating_systems = [desc[0] for desc in self.connector.description[1:]]
        return rating_systems
    
    def get_grades(self, rating_system, climbing_type_table):
        self.connector.execute_sql_query(f'SELECT "{rating_system}" FROM {climbing_type_table}')

    
    