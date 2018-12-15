"""
Dublin Route Planner
Author: Paul Durack
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, DataRequired, EqualTo, ValidationError
from models import User


class AddressForm(FlaskForm):
    start = StringField('', validators=[InputRequired()])
    finish = StringField('', validators=[InputRequired()])


class LoginForm(FlaskForm):
    username = StringField('', validators=[InputRequired(), Length(min=4, max=15)], render_kw={"placeholder": "Username"})
    password = PasswordField('', validators=[InputRequired(), Length(min=8, max=80)], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember me')


class RegisterForm(FlaskForm):
    username = StringField('', validators=[InputRequired(), Length(min=4, max=15)], render_kw={"placeholder": "Username"})
    email = StringField('', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)], render_kw={"placeholder": "Email"})
    password = PasswordField('', validators=[InputRequired(), Length(min=8, max=80)], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    leap_user = StringField('', render_kw={"placeholder": "Leap Username"})
    leap_pass = StringField('', render_kw={"placeholder": "Leap Password"})


class RequestResetForm(FlaskForm):
    email = StringField('', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)], render_kw={"placeholder": "Email"})

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No account with that email.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('', validators=[InputRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
