import psycopg2
from logger import Logger
from database.password import password
import psycopg2.extras


class Connector():
    def __init__(self):
        self.logger = Logger()
   
    def connect_to_database(self):
        try:
            connector = psycopg2.connect(
                host='snuffleupagus.db.elephantsql.com',
                port='5432',
                database='qpgrmemq',
                user='qpgrmemq',
                password=password
            )
            
            self.logger.log_message("Connected to database succesfully")
            return connector
        except psycopg2.OperationalError as error:
            self.logger.log_error(f"Something went wrong with the connection: {error}")
            return self.connect_to_database()
        

    def execute_sql_query(self, message):
        try:
            connector = self.connect_to_database()
            cursor = connector.cursor()
            cursor.execute(message)
            return cursor.fetchall()
        except psycopg2.errors.UndefinedColumn as error:
            self.logger.log_error(f"Column not found: {error}")
            quit()
        except psycopg2.errors.SyntaxError as error:
            self.logger.log_error(f"Syntax Error: {error}")
            quit()
