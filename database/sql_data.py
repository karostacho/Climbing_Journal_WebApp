from connector import Connector


class SqlData():
    def __init__(self):
        self.connector = Connector()

    
    
    def get_grades(self, rating_system, climbing_type_table):
        grades = self.connector.execute_sql_query(f'SELECT "{rating_system}" FROM {climbing_type_table}')
        return grades    
    
sql = SqlData()


    