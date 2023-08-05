class RockClimbing:
    def __init__(self, index, usa, french, uiaa, british, kurtyka):
        self.index = index
        self.usa = usa
        self.french = french
        self.uiaa = uiaa
        self.british = british
        self.kurtyka = kurtyka


    @staticmethod
    def create_grades_list(data):
        grades = []
        for row in data:
            index = row[0]
            usa = row[1]
            french = row[2]
            uiaa = row[3]
            british = row[4]
            kurtyka = row[5]

            grade = RockClimbing(index, french,kurtyka,uiaa, usa, british)
            grades.append(grade)
        return grades