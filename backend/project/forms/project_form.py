from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from wtforms.widgets import TextArea, CheckboxInput, ListWidget
from backend.project.models import Technology, Function, Activity

class ProjectForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()], render_kw={'autofocus': 'true', "autocomplete": "off"})
    slug = StringField('slug', render_kw={"readonly": True})
    url = StringField('url', validators=[InputRequired()])
    year = StringField('year', validators=[InputRequired()])
    description = StringField('description', validators=[InputRequired()], widget=TextArea())
    color = StringField('couleur', validators=[InputRequired()], render_kw={"type": "color"})
    customer = StringField('customer', validators=[InputRequired()])
    location = StringField('location', validators=[InputRequired()])
    online = BooleanField('en ligne', render_kw={"value": "1"})
    activity = QuerySelectField('Activity', query_factory=lambda: Activity.query.all(), get_label='name')
    function = QuerySelectField( 'Fonction', query_factory=lambda: Function.query.all(), get_label='name')
    technologies = QuerySelectMultipleField(
        'technologies',
        query_factory=lambda: Technology.query.all(),
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput()
    )
