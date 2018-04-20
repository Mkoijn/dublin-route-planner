# Dublin Route Planner

**A Mapping Application that gives Real Time Dublinbikes and public transport information for Dublin**

In this application the following plugins already configured:

* **Flask-Login** - Flask-Login provides user session management for Flask.
* **Flask-Bootstrap** - Ready-to-use Twitter-bootstrap for use in Flask.
* **Flask-Restless** - Flask-Restless provides simple generation of ReSTful APIs for database models defined using Flask-SQLAlchemy.
* **Flask-SQLAlchemy** - Adds SQLAlchemy support to Flask. Quick and easy.
* **Flask-WTF** - Using Flask-WTF, we can define the form fields in our Python script and render them using an HTML template. It is also possible to apply validation to the WTF field.

## Requirements

Python 2.5+, python-pip, virtualenv

## Installation

First, clone this repository.

    $ git clone http://github.com/berlotto/flask-app-template
    $ cd 'Dublin Route Planner'

Create a virtualenv, and activate this:

    $ virtualenv env
    $ source env/bin/activate

After, install all necessary to run:

    $ pip install -r requirements.txt

Then, run the application:

	$ python app.py

To see your application, access this url in your browser:

	http://localhost:5000

All configuration is in: `config.py`


## Author

* **Mkoijn** - https://github.com/Mkoijn
