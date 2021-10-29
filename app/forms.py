from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

