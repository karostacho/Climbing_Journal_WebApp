from flask import Flask, render_template, abort, request, redirect, url_for
from connector import column_names

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("home_page.html")


@app.route("/card/<int:index>")
def routes_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=(len(db)-1))
    except IndexError:
        abort(404)


@app.route("/add_route", methods=["GET"])
def add_route():
    bouldering_ratings = column_names
    climbing_types = ['bouldering', 'rock_climbing']
    routes = {
        'bouldering': bouldering_ratings,
        'rock_climbing': bouldering_ratings
    }
    return render_template('add_route.html', routes=routes, climbing_types=climbing_types)

@app.route('/submit_route', methods=['POST'])
def submit_route():
    selected_climbing_type = request.form.get('climbing_type')
    selected_rating = request.form.get('bouldering_ratings')
    return 'Route added successfully!'