from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional
from wtforms import StringField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.widgets import TextArea
from backend.project.models import Customer
from backend.cv_ats.models import CvPosition, CvContractType


class CvWorkForm(FlaskForm):
    customer = QuerySelectField(
        'Client',
        query_factory=lambda: Customer.query.order_by(Customer.name).all(),
        get_label='name',
        validators=[InputRequired()]
    )
    position = QuerySelectField(
        'Fonction',
        query_factory=lambda: CvPosition.query.all(),
        get_label='name'
    )
    contract_type = QuerySelectField(
        'Contrat',
        query_factory=lambda: CvContractType.query.all(),
        get_label='name'
    )
    location = StringField(
        'location',
        validators=[InputRequired()],
        render_kw={
            'autofocus': 'true',
            "autocomplete": "off"
        }
    )
    year_start = IntegerField('year_start', validators=[Optional()])
    year_end = IntegerField('year_end', validators=[InputRequired()])
    description = StringField(
        'description',
        validators=[InputRequired()],
        widget=TextArea(),
        render_kw={
            'style': 'min-height: 200px; resize: vertical;'
        }
    )
