class Route:
    def __init__(self, id, user_id, route_name, grade_index, rating_system):
        self.id = int(id)
        self.user_id = int(user_id)
        self.route_name = route_name
        self.grade_index = int(grade_index)
        self.rating_system = rating_system


    @staticmethod
    def create_route_list(data):
        routes = []
        for row in data:
            id = row[0]
            user_id = row[1]
            route_name = row[2]
            grade_index = row[3]
            rating_system = row[4]

            route = Route(id,user_id, route_name, grade_index, rating_system)
            routes.append(route)
        return routes