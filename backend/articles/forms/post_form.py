from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, BooleanField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from wtforms.widgets import TextArea, CheckboxInput, ListWidget
from backend.articles.models import Tag, Status, Category


class PostForm(FlaskForm):
    status = QuerySelectField('Status', query_factory=lambda: Status.query.all(), get_label='name')
    category = QuerySelectField('Catégorie', query_factory=lambda: Category.query.all(), get_label='name')
    title = StringField('Titre', validators=[InputRequired()])
    slug = StringField('Slug', render_kw={"readonly": True})
    meta_description = StringField('Meta', validators=[InputRequired()])
    body = StringField('Contenu', validators=[InputRequired()], widget=TextArea(), render_kw={'class': 'markdownEdit'})

    tags = QuerySelectMultipleField(
        'Tags',
        query_factory=lambda: Tag.query.all(),
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput()
    )
