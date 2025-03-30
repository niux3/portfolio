from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField


class ActivityForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    icon = StringField('icon', validators=[InputRequired()])
