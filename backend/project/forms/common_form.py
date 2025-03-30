from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField


class CommonForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
