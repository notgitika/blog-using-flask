from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):

    username = StringField('Username', 
        validators=[DataRequired(), Length(min=3, max=18)])

    email = StringField('Email',
        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
        validators=[DataRequired()])

    confirm_password = PasswordField('Password',
        validators=[DataRequired(), EqualTo('password')
        ])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):

    email = StringField('Email',
        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
        validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')
