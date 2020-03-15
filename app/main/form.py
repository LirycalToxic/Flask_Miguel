from flask import request
from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models import User


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140, message='_l(Text must be less then 140 symbols')],
                             render_kw={"cols": 50, 'rows': 4})
    submit = SubmitField(_l('Commit changes'))

    def __init__(self, original_name, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_name = original_name

    def validate_username(self, username):
        if username.data != self.original_name:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata'not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)
