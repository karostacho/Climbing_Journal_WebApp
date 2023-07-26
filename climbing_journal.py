from flask import Flask, render_template, request
from model.route import Route
from database.route_db import add_route_to_db
from database.sql_data import SqlData


app = Flask(__name__)
app.debug = True


climbing_types = ['Bouldering', "Rock_Climbing"]
rating_systems = ['French']
rock_climbing = 'rock_climbing_grades'
bouldering = 'bouldering_grades'

sql_data = SqlData()
all_rock_grades = sql_data.get_all_records(rock_climbing)
all_bouldering_grades = sql_data.get_all_records(bouldering)
french = sql_data.get_grades('French', rock_climbing)
uiaa = sql_data.get_grades('UIAA', rock_climbing)
usa = sql_data.get_grades('USA', rock_climbing)
british = sql_data.get_grades('British', rock_climbing)
kurtyka = sql_data.get_grades('Kurtyka(Poland)', rock_climbing)
v_scale = sql_data.get_grades('V_scale', bouldering)
font_scale = sql_data.get_grades('Font_scale', bouldering)



def get_index_by_grade(climbing_type,rating_system, grade):
    return sql_data.get_index_by_grade(climbing_type, rating_system, grade)


@app.route("/", methods= ["GET", "POST"])
def home_page():
    french_grade = request.form.get("french")
    uiaa_grade = request.form.get("uiaa")
    usa_grade = request.form.get("usa")
    british_grade = request.form.get("british")
    kurtyka_grade = request.form.get("kurtyka")
    v_scale_grade = request.form.get("v_scale")
    font_scale_grade = request.form.get("font_scale")
    rock_grades_by_index = all_rock_grades[24]
    bouldering_grades_by_index = all_bouldering_grades[18]
    bouldering_grade_index= None
    rock_grade_index= None
 
    
    if request.method == "POST":
        
        if french_grade:
            rock_grade_index = get_index_by_grade(rock_climbing, "French", french_grade)
        elif kurtyka_grade:
            rock_grade_index = get_index_by_grade(rock_climbing, "Kurtyka(Poland)", kurtyka_grade)
        elif uiaa_grade:
            rock_grade_index = get_index_by_grade(rock_climbing, "UIAA", uiaa_grade)
        elif usa_grade:
            rock_grade_index = get_index_by_grade(rock_climbing, "USA", usa_grade)
        elif british_grade:
            rock_grade_index = get_index_by_grade(rock_climbing, "British", british_grade)
        
        for row in all_rock_grades:
            if row[0] == rock_grade_index:
                    rock_grades_by_index = row
    
        if v_scale_grade:
            bouldering_grade_index = get_index_by_grade(bouldering, "V_scale", v_scale_grade)
        elif font_scale_grade:
            bouldering_grade_index = get_index_by_grade(bouldering, "Font_scale", font_scale_grade) 

        for row in all_bouldering_grades:
            if row[0] == bouldering_grade_index:
                bouldering_grades_by_index = row
    
    #grades_by_index = sql_data.get_grades_by_index(grade_index) if grade_index else None
    return render_template("home_page.html", french=french, uiaa=uiaa, usa=usa, british=british, kurtyka=kurtyka, v_scale=v_scale, font_scale=font_scale, rock_grades_by_index=rock_grades_by_index, bouldering_grade_index=bouldering_grade_index, bouldering_grades_by_index=bouldering_grades_by_index, rock_grade_index=rock_grade_index)


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
        return render_template("add_route.html", climbing_types=climbing_types, rating_systems=rating_systems, grades=french)


@app.route("/view_routes")
def view_routes():
    headings = ("Name", "Grade", "Scale", "Date")
    data = sql_data.get_routes_of_user(1)
    return render_template("view_routes.html", headings=headings, data=data)


if __name__ == "__main__":
    app.run()
