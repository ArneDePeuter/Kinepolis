from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from . import kinepolis
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
def home():
    s = []
    kinepolis.getScreeningSystem().traverse(s.append)
    m = []
    kinepolis.getMovieSystem().traverse(m.append)
    return render_template("home.html", s=s, m=m)

@views.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == "POST":
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        lastname = request.form.get('lastName')

        users = kinepolis.getUserSystem().query(email, "email")
        if len(users)>0:
            flash("User already exists", category="error")
        else:
            kinepolis.getUserSystem().addUser(voornaam=firstname, achternaam=lastname, emailadres=email)
            flash("Added User!", category="succes")
        return redirect(url_for('views.users'))
            
    l = []
    kinepolis.getUserSystem().traverse(l.append)
    return render_template("users.html", l=l)

@views.route('/rooms', methods=['GET', 'POST'])
def rooms():
    if request.method == "POST":
        seats = int(request.form.get('seats'))
        if seats:
            kinepolis.getRoomSystem().addRoom(seats)
            flash("Added Room!", category="succes")
        else:
            flash("Enter amount of seats.", category="error")
            
        return redirect(url_for('views.rooms'))
            
    l = []
    kinepolis.getRoomSystem().traverse(l.append)
    return render_template("rooms.html", l=l)

@views.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == "POST":
        button = request.form.get('submit_button')
        if button=="addMovie":
            title = request.form.get('title')
            rating = round(float(request.form.get('rating')),2)

            succes = kinepolis.getMovieSystem().addMovie(title, rating)
            if succes:
                flash("Added movie.", category="succes")
            else:
                flash("Failed to add Movie.", category="error")
        elif button=="scrape":
            kinepolis.getMovieSystem().addIMBD()
            flash("Loaded IMBD top 250 movies.", category="succes")
        return redirect(url_for('views.movies'))
            
    l = []
    kinepolis.getMovieSystem().traverse(l.append)
    return render_template("movies.html", l=l)

@views.route('/reservations', methods=['GET', 'POST'])
def reservations():
    if request.method == "POST":
        userId = int(request.form.get('userId'))
        #timestamp = datetime.now()
        screeningId = int(request.form.get('screeningId'))
        seats = int(request.form.get('seats'))

        succes = kinepolis.getReservationSystem().reservate(userId, screeningId, seats)
        if succes:
            flash("Added reservation.", category="succes")
        else:
            flash("Failed to add reservation.", category="error")
        return redirect(url_for('views.reservations'))
    
    l = kinepolis.getEventSystem().getEventList()
    return render_template("reservation.html", l=l)

@views.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == "POST":
        button = request.form.get('submit_button')

        timestamp = request.form.get('timestamp')
        datetimeList = timestamp.split('-')
        year = int(datetimeList[0])
        month = int(datetimeList[1])
        datetimeList = datetimeList[2].split('T')
        day = int(datetimeList[0])
        datetimeList = datetimeList[1].split(':')
        hour = int(datetimeList[0])
        minute = int(datetimeList[1])
        timestamp = datetime(year=year, month=month, day=day, hour=hour, minute=minute)

        screeningId = int(request.form.get('screeningId'))
        seats = int(request.form.get('seats'))
        if button=="addReservationEvent":
            userid = int(request.form.get('userId'))
            succes = kinepolis.getEventSystem().addReservationEvent(userid, timestamp, screeningId, seats)
            if succes:
                flash("Added reservation event.", category="succes")
            else:
                flash("Failed to add reservation Event", category="error")
        elif button=="addTicketEvent":
            succes = kinepolis.getEventSystem().addTicketEvent(timestamp, screeningId, seats)
            if succes:
                flash("Added ticket event.", category="succes")
            else:
                flash("Failed to add ticket Event", category="error")
        return redirect(url_for('views.events'))
    
    l = kinepolis.getEventSystem().getEventList()
    return render_template("event.html", l=l)

@views.route('/screenings', methods=['GET', 'POST'])
def screenings():
    if request.method == "POST":
        roomnumber = int(request.form.get('roomNumber'))
        slot = int(request.form.get('slot'))
        date = request.form.get('date')
        #Convert to datetime obj
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        filmId = int(request.form.get('filmId'))
        freePlaces = int(request.form.get('freePlaces'))

        rooms = kinepolis.getRoomSystem().query(roomnumber, "roomNumber")
        movies = kinepolis.getMovieSystem().query(filmId, "id")

        if len(rooms)==0:
            flash("No room exists with this number", category="error")
        elif len(movies)==0:
            flash("No movie exists with this id.", category="error")
        elif date_obj < datetime.now():
            flash("No screening can be created in the past.", category="error")
        else:
            kinepolis.getScreeningSystem().addScreening(roomnumber, slot, date_obj, filmId, freePlaces)
            flash("Added screening.", category="succes")
        return redirect(url_for('views.screenings'))
            
    l = []
    kinepolis.getScreeningSystem().traverse(l.append)
    return render_template("screening.html", l=l)

@views.route('/run')
def run():
    return render_template("run.html")

@views.route('/feed')
def feed():
    action = request.args.get('action')
    if action=='start':
        kinepolis.running = True
    elif action=='stop':
        kinepolis.running = False
    elif action=="skip":
        kinepolis.skipToNextEvent()

    kinepolis.update()
    return Response(kinepolis.outputter.getLog(), mimetype='text')

@views.route('/load', methods=['GET', 'POST'])
def load():
    if request.method == "POST":
        filename = request.form.get('file')
        kinepolis.load(filename)
        flash("Loaded file", category="succes")
        return redirect(url_for('views.load'))
    return render_template("load.html")