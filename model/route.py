class Route:
    def __init__(self, user_id, route_name, grade_index, date, comment):
        self.user_id = user_id
        self.route_name = route_name
        self.grade_index = grade_index
        self.date = date
        self.comment = comment


    @staticmethod
    def create_routes_list(data):
        routes = []
        for row in data:
            user_id = row[0]
            route_name = row[1]
            grade_index = row[2]
            date = row[3]
            comment = row[4]

            student = Route(user_id,route_name, grade_index, date, comment)
            routes.append(student)
        return routes