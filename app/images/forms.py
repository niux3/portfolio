from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, BooleanField, IntegerField, FileField, HiddenField
from wtforms.widgets import TextArea
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.portfolio.models import Portfolio


class UploadCreateForm(FlaskForm):
    portfolios = QuerySelectField(query_factory=lambda: Portfolio.query.all())
    name = StringField('name', validators=[InputRequired()], render_kw={"class": "form-control", 'autofocus': 'true', 'value': "bla"})
    description = StringField('description', validators=[InputRequired()], widget=TextArea(), render_kw={"class": "form-control description"}, default="blabla")
    online = BooleanField('en ligne', render_kw={"class": "form-check-input", "value": "1"})
    thumbnail = BooleanField('miniature', render_kw={"class": "form-check-input"})
    upload = FileField('upload')