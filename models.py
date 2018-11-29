"""
Dublin Route Planner Prototype
Author: Paul Durack
"""

from flask_login import UserMixin
from manage import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))
    leap_user = db.Column(db.String(15), unique=True)
    leap_pass = db.Column(db.String(15), unique=True)
    leap_balance = db.Column(db.Float)
    routes = db.relationship('Route', backref='likes', lazy=True)


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    __table_args__ = (db.UniqueConstraint('origin', 'destination'),
                 )
