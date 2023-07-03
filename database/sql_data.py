from database.connector import Connector


class SqlData():
    def __init__(self):
        self.connector = Connector()
    
    def get_grades(self, rating_system):
        rows = self.connector.execute_sql_query(f'''SELECT "{rating_system}" FROM rock_climbing_grades''')
        grades = [row[0] for row in rows]
        unique_grades = []
        for item in grades:
            if item not in unique_grades:
                unique_grades.append(item)
        return unique_grades  

    def get_index_by_grade(self, rating_system, grade):
        rows = self.connector.execute_sql_query(f"""SELECT "Index" FROM rock_climbing_grades WHERE "{rating_system}" = '{grade}'""")
        indexes = [row[0] for row in rows]
        index = indexes[len(indexes) // 2]
        return index
    

    def get_grade_by_index(self, rating_system, index):
        rows = self.connector.execute_sql_query(f"""SELECT "{rating_system}" FROM rock_climbing_grades WHERE "Index" = {index}""")
        grade = [row[0] for row in rows]
        return grade


    def get_routes_of_user(self, user_id):
        rows = self.connector.execute_sql_query((f'''SELECT routes.route_name, rock_climbing_grades."French", routes.rating_system, routes.date 
                                                FROM routes
                                                LEFT JOIN rock_climbing_grades 
                                                ON rock_climbing_grades."Index" = routes.grade_index
                                                WHERE routes.user_id = {user_id};'''))
        #routes = [row[0] for row in rows]
<<<<<<< HEAD
        return rows

    def get_grades_by_index(self, grade_index):
        rows = self.connector.execute_sql_query(f"""SELECT "French", "Kurtyka(Poland)", "UIAA", "USA","British"  FROM rock_climbing_grades WHERE "Index" = '{grade_index}'""")
=======
>>>>>>> e6c276d64157b8bb2104ce3b12a07a3996fcd3d5
        return rows