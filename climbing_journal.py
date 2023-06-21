from flask import Flask, render_template, jsonify, url_for, request, redirect
from sql_data import SqlData

app = Flask(__name__)

#sql_data = SqlData()

@app.route("/", methods= ["GET", "POST"])
def welcome():
    if request.method == "POST":
        return redirect(url_for("add_route"))
    else:
        return render_template("home_page.html")



@app.route("/add_route")
def add_route():
    return render_template("add_route.html")


@app.route("/climbing_types")
def get_climbing_types():
    climbing_types = ['Bouldering', 'Rock Climbing']
    return jsonify(climbing_types)

@app.route("/rating_systems/<climbing_type>")
def get_rating_systems(climbing_type):
    rating_systems = {
        'Bouldering': ['V-scale', 'Fontainebleau'],
        'Rock Climbing': ['YDS', 'French', 'UIAA']
    }
    return jsonify(rating_systems.get(climbing_type, []))


    

