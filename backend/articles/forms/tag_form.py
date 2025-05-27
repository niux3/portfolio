from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField


class TagForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
