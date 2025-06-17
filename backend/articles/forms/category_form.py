from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms.widgets import TextArea, CheckboxInput, ListWidget
from wtforms import StringField


class CategoryForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    slug = StringField('Slug', render_kw={"readonly": True})
    description = StringField('description', validators=[InputRequired()], render_kw={"maxlength": 255})
