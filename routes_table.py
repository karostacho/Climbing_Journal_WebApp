from tabulate import tabulate
from database.sql_data import SqlData
from model.route import Route

class RoutesList():
    def __init__(self):
        self.routes = []

    def add_route_to_the_list(self, route):
         if isinstance (route, Route):
            self.routes.append(route)





def create_routes_table(routes):
    rows = []
    for route in routes:
        sql = SqlData()
        grade = sql.get_grade_by_index(route.rating_system, route.index)  
        rows.append([route.name,route.rating_system, grade, route.date])
        headers = ["Name", "Rating system", "Grade", "Date"] 
        table = tabulate(rows, headers=headers, tablefmt="fancy_grid")
        return table