class RockClimbing:
    def __init__(self, index, usa, french, uiaa, british, kurtyka):
        self.index = int(index)
        self.usa = usa
        self.french = french
        self.uiaa = uiaa
        self.british = british
<<<<<<< HEAD
        self.kurtyka = kurtyka


    def get_grades(self, rating_system):
        rows = self.connector.execute_sql_query(f'''SELECT "{rating_system}" FROM rock_climbing_grades''')
        grades = [row[0] for row in rows]
        unique_grades = []
        for item in grades:
            if item not in unique_grades:
                unique_grades.append(item)
        return unique_grades
=======
        self.kurtyka = kurtyka
>>>>>>> e6c276d64157b8bb2104ce3b12a07a3996fcd3d5
