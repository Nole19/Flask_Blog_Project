from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User, Post


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20, message="Should be between"
                                                                                                   " 6 and 20")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min=6, message="Should be bigger than"
                                                                                                   " 6")])
    confirm_password = StringField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another one.')

    def validate_email(self, email):
        emai = User.query.filter_by(email=email.data).first()
        if emai:
            raise ValidationError('That username is taken. Please choose another one.')


class LoginForm(FlaskForm):
    """ Need to test Email"""
    email = StringField('Email', validators=[DataRequired(), Email(allow_empty_local='@gmail.com')])
    password = StringField('Password', validators=[DataRequired(), Length(min=6, max=20, message="Should be between"
                                                                                                   " 6 and 20")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20, message="Should be between"
                                                                                                   " 6 and 20")])
    email = StringField('Email', validators=[DataRequired(), Email()])

    confirm_password = StringField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose another one.')

    def validate_email(self, email):
        if email.data != current_user:
            emai = User.query.filter_by(email=email.data).first()
            if emai:
                raise ValidationError('That username is taken. Please choose another one.')
