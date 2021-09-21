from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, ValidationError
from wtforms import StringField, BooleanField, SelectMultipleField
from wtforms.widgets import TextArea, CheckboxInput, ListWidget, Select, html_params


class CommonForm(FlaskForm):
    name = StringField('name', validators=[ InputRequired() ], render_kw={"class": "form-control", "maxlength": 128})