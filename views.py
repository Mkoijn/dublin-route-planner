"""
Dublin Route Planner Prototype
Author: Paul Durack
"""

from app import app, login_manager
from models import User
from forms import AddressForm, LoginForm, RegisterForm
from flask import render_template, redirect, url_for, request
from helpers.bike_locations import closest_stations, get_coordinates
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from models import db
from urllib.request import Request, urlopen
from json import loads
import json


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddressForm()
    return render_template('index.html', form=form)


@app.route('/map', methods=['GET', 'POST'])
def map():
    # Bike data URL API
    form = AddressForm()
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=7453c07d7cf230540911a81515a937d8963cbdfe'
    req = Request(url, None, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows\
                            NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    bike_data = loads(urlopen(req).read().decode("utf-8"))

    # clean the data, extract coordinates
    for item in bike_data:
        item['lat'] = item['position']['lat']
        item['lng'] = item['position']['lng']
        item.pop('position', None)  # extract lat and lng

    if request.method == 'POST':
        # User Inputs
        start_address = request.form['start']
        start_coordinates = get_coordinates(start_address)
        finish_address = request.form['finish']
        finish_coordinates = get_coordinates(finish_address)

        # Check that User entered a valid address
        if (start_coordinates is None) or (finish_coordinates is None):
            return redirect(url_for('index'))
        # Check for the stations closest to User's inputs
        start_stations = json.dumps(closest_stations(start_address, bike_data))
        finish_stations = json.dumps(closest_stations(finish_address, bike_data))
        return render_template('map.html', start_coordinates=start_coordinates,
                                           finish_coordinates=finish_coordinates,
                                           starting_stations=start_stations,
                                           finishing_stations=finish_stations,
                                           start_address=start_address,
                                           finish_address=finish_address,
                                           form=form)

    return return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))

        return '<h1>Invalid username or password</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
