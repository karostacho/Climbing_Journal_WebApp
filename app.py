from flask import Flask, render_template, request, flash, session, redirect, url_for
import re
from model.route import Route
from model.user import User
from database.route_db import add_route_to_db, remove_route_from_db
from database.sql_data import SqlData
from database.user_db import check_if_user_in_db, add_user_to_db, find_user_password, find_user_id, get_user
from werkzeug.security import check_password_hash, generate_password_hash
from variables import all_bouldering_grades, all_rock_grades, french, uiaa, usa, british, kurtyka, v_scale,font_scale
from database.password import secret_key


app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = secret_key
rock_climbing = 'rock_climbing_grades'
bouldering = 'bouldering_grades'

sql_data = SqlData()

 
def find_rock_grade_index(french_grade,kurtyka_grade, uiaa_grade, usa_grade,british_grade):
    if french_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "French", french_grade)
        
    elif kurtyka_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "Kurtyka(Poland)", kurtyka_grade)
       
    elif uiaa_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "UIAA", uiaa_grade)
       
    elif usa_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "USA", usa_grade)
    
    elif british_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "British", british_grade)
    return rock_grade_index

def convert_rock_grades(rock_grade_index):
    for row in all_rock_grades:
        if row[0] == rock_grade_index:
                rock_grades_by_index = row
    return rock_grades_by_index   

def find_bouldering_grade_index(v_scale_grade, font_scale_grade):
    if v_scale_grade:
        bouldering_grade_index = sql_data.get_index_by_grade(bouldering, "V_scale", v_scale_grade)
    elif font_scale_grade:
        bouldering_grade_index = sql_data.get_index_by_grade(bouldering, "Font_scale", font_scale_grade) 
    return bouldering_grade_index


def covert_bouldering_grades(bouldering_grade_index):
    for row in all_bouldering_grades:
        if row[0] == bouldering_grade_index:
            bouldering_grades_by_index = row
    return bouldering_grades_by_index
    

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
        if french_grade or kurtyka_grade or uiaa_grade or usa_grade or british_grade:
            rock_grade_index = find_rock_grade_index(french_grade,kurtyka_grade, uiaa_grade, usa_grade,british_grade)
            rock_grades_by_index = convert_rock_grades(rock_grade_index)
        else:
            bouldering_grade_index = find_bouldering_grade_index(v_scale_grade, font_scale_grade)
            bouldering_grades_by_index = covert_bouldering_grades(bouldering_grade_index)
   
    return render_template("home_page.html", french=french, uiaa=uiaa, usa=usa, british=british, kurtyka=kurtyka, v_scale=v_scale, font_scale=font_scale, rock_grades_by_index=rock_grades_by_index, bouldering_grade_index=bouldering_grade_index, bouldering_grades_by_index=bouldering_grades_by_index, rock_grade_index=rock_grade_index)


climbing_type = 'rock_climbing_grades'
routes_type = 'lead_climbing_routes'


@app.route("/view_routes", methods=["GET", "POST"])
def view_routes():
    rock_grade_index= None
    rock_grades_by_index = all_rock_grades[24]
    user_id = session.get('id')
    
    if request.method == "POST":
        date = request.form.get("date")
        comment = request.form.get("comment")
        french_grade = request.form.get("french")
        kurtyka_grade = request.form.get("kurtyka")
        uiaa_grade = request.form.get("uiaa")
        usa_grade = request.form.get("usa")
        british_grade = request.form.get("british")
        
        if french_grade or kurtyka_grade or uiaa_grade or usa_grade or british_grade:
            rock_grade_index = find_rock_grade_index(french_grade,kurtyka_grade, uiaa_grade, usa_grade,british_grade)

        route_name = request.form.get("route_name")
       
        route = Route(user_id, route_name, rock_grade_index, date, comment)
        add_route_to_db(route, "lead_climbing_routes")
    data = sql_data.get_rock_routes_of_user_by( user_id, 'date', 'DESC')
   
    return render_template("view_routes.html", data=data, french=french, uiaa=uiaa, usa=usa, british=british, kurtyka=kurtyka,rock_grades_by_index=rock_grades_by_index, rock_grade_index=rock_grade_index, user_id=user_id )


@app.route("/sortByDate/<sort_order>")
def sort_by_date(sort_order):
    user_id = session.get('id')
    if sort_order == 'desc':
        data = sql_data.get_rock_routes_of_user_by(user_id, 'lead_climbing_routes.date','DESC')
    else:
        data = sql_data.get_rock_routes_of_user_by(user_id, 'lead_climbing_routes.date','ASC')

    return render_template("view_routes.html", data=data, french=french, uiaa=uiaa, usa=usa, british=british, kurtyka=kurtyka, user_id=user_id, sort_order=sort_order)


@app.route("/sortByGrade/<sort_order>")
def sort_by_grade(sort_order):
    user_id = session.get('id')
    if sort_order == 'desc':
        data = sql_data.get_rock_routes_of_user_by(user_id, 'rock_climbing_grades."Index"','DESC')
    else:
        data = sql_data.get_rock_routes_of_user_by(user_id, 'rock_climbing_grades."Index"','ASC')

    return render_template("view_routes.html", data=data, french=french, uiaa=uiaa, usa=usa, british=british, kurtyka=kurtyka, user_id=user_id, sort_order=sort_order)


@app.route("/delete_route/<int:route_id>")
def delete_route(route_id):
    #create delete query as string
    remove_route_from_db(routes_type, route_id)
    return redirect(url_for('view_routes'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form and 'repeat_password' in request.form:
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        hashed_password = generate_password_hash(password)
        account = check_if_user_in_db(email)
    
        if account:
            flash('Account already exists!')
        else:
            user = User(None,name,hashed_password,email)
            add_user_to_db(user)
            new_user = get_user(email)
            if new_user:
                flash('You have successfully registered!', 'success')
            else:
                flash('Something went wrong', 'error')

    return render_template('register.html')



@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        email = request.form['email']
        password = request.form['password']
        account = check_if_user_in_db(email)
 
        if account:
            password_rs = find_user_password(email)
            if check_password_hash(password_rs, password):
                session['loggedin'] = True
                session['id'] = find_user_id(email)
                return redirect(url_for('view_routes'))
            else:
                flash('Incorrect username or password')
        else:
            flash('Incorrect username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   return redirect(url_for('home_page'))
   
if __name__ == "__main__":
    app.run()


