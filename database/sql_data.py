from database.connector import Connector


class SqlData():
    def __init__(self):
        self.connector = Connector()
    

    def get_grades(self, rating_system, climbing_type):
        rows = self.connector.execute_sql_query(f'''SELECT "{rating_system}" FROM {climbing_type}''')
        grades = [row[0] for row in rows]
        grades = SqlData.remove_duplicates(grades)
        return grades 

    def get_all_records(self, climbing_type):
        rows = self.connector.execute_sql_query(f'''SELECT * FROM {climbing_type}''')
        grades = [list(row) for row in rows]
        return grades

    def get_index_by_grade(self, climbing_type, rating_system, grade):
        rows = self.connector.execute_sql_query(f"""SELECT "Index" FROM {climbing_type} WHERE "{rating_system}" = '{grade}'""")
        possible_indexes = [row[0] for row in rows]
        index = SqlData.get_middle_value(possible_indexes)
        return index
    

    def get_grade_by_index(self, climbing_type, rating_system, index):
        rows = self.connector.execute_sql_query(f"""SELECT "{rating_system}" FROM {climbing_type} WHERE "Index" = {index}""")
        grade = [row[0] for row in rows]
        return grade

    #TODO: in final version remove rock_climbing_grades."French"
    def get_routes_of_user(self, user_id):
        rows = self.connector.execute_sql_query((f'''SELECT routes.route_name, rock_climbing_grades."French", routes.rating_system, routes.date 
                                                FROM routes
                                                LEFT JOIN rock_climbing_grades 
                                                ON rock_climbing_grades."Index" = routes.grade_index
                                                WHERE routes.user_id = {user_id};'''))
        return rows


    def get_grades_by_index(self, climbing_type, grade_index):
        rows = self.connector.execute_sql_query(f"""SELECT "French", "Kurtyka(Poland)", "UIAA", "USA","British"  FROM {climbing_type} WHERE "Index" = '{grade_index}'""")
        tuple = rows[0]
        grades = list(tuple)
        return grades 
    

    @staticmethod
    def get_middle_value(indexes):
        return indexes[len(indexes) // 2]
    

    @staticmethod
    def remove_duplicates(grades):
        unique_grades = []
        for item in grades:
            if item not in unique_grades:
                unique_grades.append(item)
        return unique_grades 