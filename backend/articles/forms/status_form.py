from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField


class StatusForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
