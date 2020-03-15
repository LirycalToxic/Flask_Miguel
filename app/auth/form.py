from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember me'))
    submit = SubmitField(_l('Sign in'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l("Password"), validators=[DataRequired(), Length(min=3, max=20,
                                                                                message=_l(
                                                                                    'Password must have more then 3 '
                                                                                    'symbols'))])
    password2 = PasswordField(_l("Repeat password"), validators=[DataRequired(),
                                                                 EqualTo('password',
                                                                         message=_l('Passwords must be equal'))])
    submit = SubmitField(_l('Sign in'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('This username have already used. Please enter other username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email have already used. Please enter other email.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l("Reset password"))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired(), Length(min=3, max=25)])
    password2 = PasswordField(_l('Repeat password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Reset'))
