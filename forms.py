from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#  We created forms and accept user input. We will also learn how to validate that user input and notify the user if the input was invalid
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email=StringField('Email', validators=[DataRequired(), Email()])

    password= PasswordField('Password', validators=[DataRequired])

    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired, EqualTo('password')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    #This form will have a username,
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired])

    remember =BooleanField('Remember Me')

    submit = SubmitField('Log in')
