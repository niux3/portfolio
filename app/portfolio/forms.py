from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, ValidationError
from wtforms import StringField, BooleanField, SelectMultipleField, TextField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from wtforms.widgets import TextArea, CheckboxInput, ListWidget, Select, html_params
from app.portfolio.models import Technology, Function


class CommonForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()], render_kw={"class": "form-control", 'autofocus': 'true'})


class PortfolioForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()], render_kw={"class": "form-control name", 'autofocus': 'true', "autocomplete": "off"})
    slug = StringField('slug', validators=[InputRequired()], render_kw={"class": "form-control slug"})
    description = StringField('description', validators=[InputRequired()], widget=TextArea(), render_kw={"class": "form-control description"})
    color = StringField('couleur', validators=[InputRequired()], render_kw={"class": "form-control", "type": "color"})
    online = BooleanField('en ligne', render_kw={"class": "form-check-input", "value": "1"})
    functions = QuerySelectField(query_factory=lambda: Function.query.all())
    technologies = QuerySelectMultipleField('technologies', query_factory=lambda: Technology.query.all(), widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())