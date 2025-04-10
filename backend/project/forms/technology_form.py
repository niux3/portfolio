from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, BooleanField


class TechnologyForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    online = BooleanField('en ligne', render_kw={"value": "1"})
