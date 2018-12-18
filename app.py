"""
Dublin Route Planner Prototype
Author: Paul Durack
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_heroku import Heroku
from flask_mail import Mail


app = Flask(__name__)

app.config.from_pyfile('config.py')

Bootstrap(app)
heroku = Heroku(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'loserwinner6666@gmail.com'
app.config['MAIL_PASSWORD'] = 'Loserwinner21'
mail = Mail(app)

from views import *
from errors.handlers import errors
app.register_blueprint(errors)


if __name__ == '__main__':
    app.run()
