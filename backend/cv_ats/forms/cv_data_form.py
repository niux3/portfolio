from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms.widgets import TextArea
from wtforms import StringField


class CvDataForm(FlaskForm):
    data = StringField(
        'JSON du CV',
        validators=[InputRequired()],
        widget=TextArea(),
        render_kw={
            'style': 'min-height: 500px; font-family: monospace; tab-size: 4;',
            'autocomplete': 'off',
            'spellcheck': 'false'
        }
    )
