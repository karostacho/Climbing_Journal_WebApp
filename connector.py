import psycopg2
import getpass
from logger import Logger

class Connector():
    def __init__(self):
        self.logger = Logger()
        self.cursor = self.connect_to_database()
   
    def connect_to_database(self):
        try:
            conn = psycopg2.connect(
            host='snuffleupagus.db.elephantsql.com',
            port='5432',
            database='qpgrmemq',
            user='qpgrmemq',
            password=getpass.getpass(prompt='Enter the database password: ')
            )
            cursor = conn.cursor()
            self.logger.log_message("Connected to database succesfully")
            return cursor
        except psycopg2.OperationalError as error:
            self.logger.log_error(error,"Wrong password" )
            return self.connect_to_database()

    def execute_sql_query(self, message):
        try:
            self.cursor.execute(message)
            return self.cursor.fetchall()
        except psycopg2.errors.UndefinedColumn as error:
            self.logger.log_error(error)
            quit()
        except psycopg2.errors.SyntaxError as error:
            self.logger.log_error(error)
            quit()
