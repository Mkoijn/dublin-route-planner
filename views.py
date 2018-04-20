from app import app, login_manager
from models import User
from forms import AddressForm, LoginForm, RegisterForm
from flask import render_template, redirect, url_for, request
from helpers.bike_locations import closest_station, get_coordinates
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from models import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddressForm()
    return render_template('index.html', form=form)


@app.route('/map', methods=['GET', 'POST'])
def map():
    if request.method == 'POST':
        start_address = request.form['start']
        start_coordinates = get_coordinates(start_address)
        start_station = closest_station(start_address)
        finish_address = request.form['finish']
        finish_coordinates = get_coordinates(finish_address)
        finish_station = closest_station(finish_address)
        return render_template('map.html', start_station=start_station, finish_station=finish_station,
                               start_coordinates=start_coordinates, finish_coordinates=finish_coordinates)

    return render_template('index.html')


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
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

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
