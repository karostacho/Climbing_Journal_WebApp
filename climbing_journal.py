from flask import Flask, render_template, url_for, request, redirect
from model.route import Route
from database.route_db import add_route_to_db
from database.sql_data import SqlData
from routes_table import RoutesList, create_routes_table

app = Flask(__name__)

#sql_data = SqlData()

@app.route("/", methods= ["GET", "POST"])
def welcome():
    if request.method == "POST":
        if "add_route" in request.form:
            return redirect(url_for("add_route"))
        elif "view_routes" in request.form:
            return redirect(url_for("view_routes"))
    else:
        return render_template("home_page.html")

climbing_types = ['Bouldering', "Rock_Climbing"]
rating_systems = ['French']
sql_data = SqlData()
grades = (sql_data.get_grades(rating_systems[0]))


@app.route("/add_route", methods=["GET", "POST"])
def add_route():
    if request.method == "POST":
        climbing_type = request.form.get("climbing_type")
        rating_system = request.form.get("rating_system")
        grade = request.form.get("grade")
        route_name = request.form['route_name']
        grade_index = sql_data.get_index_by_grade(rating_system, grade)
        route = Route(1,route_name,grade_index, rating_system, "2023-06-23")
        add_route_to_db(route)
        return 'Route added to your climbing journal'
    else: 
        return render_template("add_route.html", climbing_types=climbing_types, rating_systems=rating_systems, grades=grades)


@app.route("/view_routes")
def view_routes():
    headings = ("Name", "Grade", "Scale", "Date")
    data = sql_data.get_routes_of_user(1)
    return render_template("view_routes.html", headings=headings, data=data)
    


