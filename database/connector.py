import psycopg2
import getpass
from logger import Logger
from database.password import password
import psycopg2.extras


class Connector():
    def __init__(self):
        self.logger = Logger()
   
    def connect_to_database(self):
        try:
            conn = psycopg2.connect(
            host='snuffleupagus.db.elephantsql.com',
            port='5432',
            database='qpgrmemq',
            user='qpgrmemq',
            password=password
            )
            #cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

            
            self.logger.log_message("Connected to database succesfully")
            return conn
        except psycopg2.OperationalError as error:
            self.logger.log_error(error,"Wrong password" )
            return self.connect_to_database()
        

        

    def execute_sql_query(self, message):
        try:
            conn = self.connect_to_database()
            cursor = conn.cursor()
            cursor.execute(message)
            return cursor.fetchall()
        except psycopg2.errors.UndefinedColumn as error:
            self.logger.log_error(error,"Column not found")
            quit()
        except psycopg2.errors.SyntaxError as error:
            self.logger.log_error(error, "Syntax Error")
            quit()
