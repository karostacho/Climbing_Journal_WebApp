from flask import Flask, render_template, url_for, request, redirect
from model.route import Route
from database.route_db import add_route_to_db
from database.sql_data import SqlData


app = Flask(__name__)

climbing_types = ['Bouldering', "Rock_Climbing"]
rating_systems = ['French']
sql_data = SqlData()
grades = (sql_data.get_grades(rating_systems[0]))

french = sql_data.get_grades('French')
uiaa = sql_data.get_grades('UIAA')
usa = sql_data.get_grades('USA')
british = sql_data.get_grades('British')
kurtyka = sql_data.get_grades('Kurtyka(Poland)')

def get_index_by_grade(rating_system, grade):
    return sql_data.get_index_by_grade(rating_system, grade)



@app.route("/", methods= ["GET", "POST"])
def welcome():
    f_grade = request.form.get("french")
    uiaa_grade = request.form.get("uiaa")
    usa_grade = request.form.get("usa")
    british_grade = request.form.get("british")
    kurtyka_grade = request.form.get("kurtyka")
    grade_index = None


    if request.method == "POST":
        if f_grade:
            grade_index = get_index_by_grade("French", f_grade)
        elif kurtyka_grade:
            grade_index = get_index_by_grade("Kurtyka(Poland)", kurtyka_grade)
        elif uiaa_grade:
            grade_index = get_index_by_grade("UIAA", uiaa_grade)
        elif usa_grade:
            grade_index = get_index_by_grade("USA", usa_grade)
        elif british_grade:
            grade_index = get_index_by_grade("British", british_grade)
    data = sql_data.get_grades_by_index(grade_index) if grade_index else None

    return render_template("home_page.html", french=french, uiaa=uiaa, usa=usa, british=british, kurtyka=kurtyka, data=data)



@app.route("/add_route", methods=["GET", "POST"])
def add_route():
    if request.method == "POST":
        climgbing_type = request.form.get("climbing_type")
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
  
    


if __name__ == "__main__":
    app.run()


