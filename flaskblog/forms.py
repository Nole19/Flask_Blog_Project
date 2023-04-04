from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=6, max=20, message="Should be between"
                                                                                                   " 6 and 20")])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = StringField('Password', validators = [DataRequired(), Length(min=6, message="Should be bigger than"
                                                                                                   " 6")])
    confirm_password = StringField('Confirm password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    """ Need to test Email"""
    email = StringField('Email', validators = [DataRequired(), Email(allow_empty_local='@gmail.com')])
    password = StringField('Password', validators = [DataRequired(), Length(min=6, max=20, message="Should be between"
                                                                                                   " 6 and 20")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


