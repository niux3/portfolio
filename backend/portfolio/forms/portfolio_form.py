from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from wtforms.widgets import TextArea, CheckboxInput, ListWidget
from backend.portfolio.models import Technology, Function, Activity

class PortfolioForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()], render_kw={'autofocus': 'true', "autocomplete": "off"})
    slug = StringField('slug', validators=[InputRequired()])
    url = StringField('url', validators=[InputRequired()])
    year = StringField('year', validators=[InputRequired()])
    description = StringField('description', validators=[InputRequired()], widget=TextArea())
    color = StringField('couleur', validators=[InputRequired()], render_kw={"type": "color"})
    customer = StringField('customer', validators=[InputRequired()])
    location = StringField('location', validators=[InputRequired()])
    online = BooleanField('en ligne', render_kw={"value": "1"})
    activities = QuerySelectField(query_factory=lambda: Activity.query.all())
    functions = QuerySelectField(query_factory=lambda: Function.query.all())
    technologies = QuerySelectMultipleField(
        'technologies',
        query_factory=lambda: Technology.query.all(),
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput()
    )
