from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, BooleanField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from wtforms.widgets import TextArea, CheckboxInput, ListWidget
from backend.articles.models import Tag, Status


class PostForm(FlaskForm):
    status = QuerySelectField('Status', query_factory=lambda: Status.query.all(), get_label='name')
    title = StringField('Titre', validators=[InputRequired()])
    slug = StringField('Slug', render_kw={"readonly": True})
    body = StringField('Contenu', validators=[InputRequired()], widget=TextArea())
    online = BooleanField('en ligne', render_kw={"value": "1"})

    tags = QuerySelectMultipleField(
        'Tags',
        query_factory=lambda: Tag.query.all(),
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput()
    )
