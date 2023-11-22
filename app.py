from flask import Flask, render_template, request, flash, session, redirect, url_for
from model.route import Route
from model.user import User
from database.route_db import add_route_to_db, remove_data_from_db
from database.sql_data import SqlData
from database.user_db import check_if_user_in_db, add_user_to_db, find_user_password, find_user_id, get_user
from werkzeug.security import check_password_hash, generate_password_hash
from helper import convert_rock_grades, convert_bouldering_grades, get_fortmatted_routes_list, all_bouldering_grades, all_rock_grades, french, uiaa, usa, british, kurtyka, v_scale,font_scale, grade_column_index, date_column_index, sort_by_order
from database.password import secret_key


app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = secret_key
rock_climbing = 'rock_climbing_grades'
bouldering = 'bouldering_grades'


def find_rock_grade_index(french_grade, kurtyka_grade, uiaa_grade, usa_grade, british_grade):
    sql_data = SqlData()
    if french_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "French", french_grade)
    elif kurtyka_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "Kurtyka", kurtyka_grade)
    elif uiaa_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "UIAA", uiaa_grade)
    elif usa_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "USA", usa_grade)
    elif british_grade:
        rock_grade_index = sql_data.get_index_by_grade(rock_climbing, "British", british_grade)
    return rock_grade_index


def find_bouldering_grade_index(v_scale_grade, font_scale_grade):
    sql_data = SqlData()
    if v_scale_grade:
        bouldering_grade_index = sql_data.get_index_by_grade(bouldering, "V_scale", v_scale_grade)
    elif font_scale_grade:
        bouldering_grade_index = sql_data.get_index_by_grade(bouldering, "Font_scale", font_scale_grade)
    return bouldering_grade_index


def save_db_routes_list_to_session(user_id, column_to_sort, sort_order, selected_scale):
    sql_data = SqlData()
    routes_list = sql_data.get_rock_routes_of_user_by(user_id, column_to_sort, sort_order, selected_scale)
    session['routes_list'] = routes_list
    return routes_list


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
    rock_grade_index= rock_grades_by_index[0]
    bouldering_grades_by_index = all_bouldering_grades[18]
    bouldering_grade_index= bouldering_grades_by_index[0]

    if request.method == "GET":
        session.pop('current_rock_index', None)
        session.pop('current_bouldering_index', None)

    if request.method == "POST":
        if french_grade or kurtyka_grade or uiaa_grade or usa_grade or british_grade:
            rock_grade_index = find_rock_grade_index(french_grade,kurtyka_grade, uiaa_grade, usa_grade,british_grade)
            rock_grades_by_index = convert_rock_grades(rock_grade_index)
            session['current_rock_index'] = rock_grade_index
            if 'current_bouldering_index' in session and session['current_bouldering_index'] is not None:
                bouldering_grades_by_index = convert_bouldering_grades(session['current_bouldering_index'])
        else:
            bouldering_grade_index = find_bouldering_grade_index(v_scale_grade, font_scale_grade)
            bouldering_grades_by_index = convert_bouldering_grades(bouldering_grade_index)
            session['current_bouldering_index'] = bouldering_grade_index
            if 'current_rock_index' in session and session['current_rock_index'] is not None:
                rock_grades_by_index = convert_rock_grades(session['current_rock_index'])

    return render_template("home_page.html",
                           french=french, uiaa=uiaa, usa=usa, british=british, kurtyka=kurtyka,
                           v_scale=v_scale, font_scale=font_scale,
                           bouldering_grade_index=bouldering_grade_index,
                           bouldering_grades_by_index=bouldering_grades_by_index,
                           rock_grade_index=rock_grade_index,
                           rock_grades_by_index=rock_grades_by_index)


@app.route("/journal_page", methods=["GET", "POST"])
def journal_page():
    rock_grade_index= None
    gradeFilter = request.form.get("gradeFilter")
    sort_date_order = request.form.get("sortDateOrder")
    sort_grade_order = request.form.get("sortGradeOrder")

    user_id = session.get('id')
    selected_scale = session.get('selected_scale', "French")
    sort_order= session.get("sort_order", "DESC")
    column_to_sort = session.get("column_to_sort", "date")

    if request.method == "GET":
        sql_data = SqlData()
        routes_list = session.get("routes_list", sql_data.get_rock_routes_of_user_by( user_id, 'date', 'DESC', selected_scale))
        routes_list = get_fortmatted_routes_list(routes_list)
        session['routes_list'] = routes_list

    if request.method == "POST":
        routes_list =  session.get("routes_list")
        routes_list = get_fortmatted_routes_list(routes_list)
        
        if 'gradeFilter' in request.form:
            sort_order =  session.get("sort_order")
            column_to_sort = session.get("column_to_sort")
            selected_scale = gradeFilter
            session['selected_scale'] = selected_scale
            routes_list = save_db_routes_list_to_session(user_id, column_to_sort, sort_order, selected_scale)
            
        elif 'sortDateOrder' in request.form:
            routes_list = sort_by_order(date_column_index, routes_list, sort_date_order)
            session['sort_order'] = sort_date_order
            session['column_to_sort'] = 'date'
            session['routes_list'] = routes_list

        elif 'sortGradeOrder' in request.form:
            routes_list = sort_by_order(grade_column_index, routes_list, sort_grade_order)
            session['sort_order'] = sort_grade_order
            session['column_to_sort'] = 'grade_index'
            session['routes_list'] = routes_list

        elif 'deleteRoute' in request.form:
            route_id = request.form.get("deleteRoute")
            remove_data_from_db("lead_climbing_routes", route_id)
            routes_list = save_db_routes_list_to_session(user_id, column_to_sort, sort_order, selected_scale)
        
        else:
            route_name = request.form.get("route_name")
            date = request.form.get("date")
            comment = request.form.get("comment")
            french_grade = request.form.get("french")
            kurtyka_grade = request.form.get("kurtyka")
            uiaa_grade = request.form.get("uiaa")
            usa_grade = request.form.get("usa")
            british_grade = request.form.get("british")

            if french_grade or kurtyka_grade or uiaa_grade or usa_grade or british_grade:
                rock_grade_index = find_rock_grade_index(french_grade, kurtyka_grade, uiaa_grade, usa_grade, british_grade)

                route = Route(user_id, route_name, rock_grade_index, date, comment)
                add_route_to_db(route, "lead_climbing_routes")
                sort_order= session.get("sort_order", "DESC")
                column_to_sort = session.get("column_to_sort", "date")
                routes_list = save_db_routes_list_to_session(user_id, column_to_sort, sort_order, selected_scale)
 
    return render_template("journal_page.html", routes_list=routes_list, french=french, uiaa=uiaa, usa=usa, 
                           						british=british, kurtyka=kurtyka, rock_grade_index=rock_grade_index, 
                                                user_id=user_id , selected_scale=selected_scale,  sort_grade_order=sort_grade_order,
                                                selected_sort_date_order=sort_date_order )


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST' :
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        hashed_password = generate_password_hash(password)
        account = check_if_user_in_db(email)

        if account:
            flash('Account already exists!')
        else:
            user = User(None, name, hashed_password, email)
            add_user_to_db(user)
            new_user = get_user(email)
            if new_user:
                return render_template('successful_register_page.html')
            else:
                flash('Something went wrong', 'error')

    return render_template('register_page.html')


@app.route('/successful_register', methods=['GET', 'POST'])
def successful_register():
    return render_template('successful_register_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST' :
        email = request.form['email']
        password = request.form['password']
        account = check_if_user_in_db(email)

        if account:
            password_rs = find_user_password(email)
            if check_password_hash(password_rs, password):
                session['loggedin'] = True
                session['id'] = find_user_id(email)
                return redirect(url_for('journal_page'))
            else:
                flash('Incorrect email or password', 'error')
        else:
            flash('Incorrect email or password', 'error')
    return render_template('login_page.html')


@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   return redirect(url_for('home_page'))


if __name__ == "__main__":
    app.run()
