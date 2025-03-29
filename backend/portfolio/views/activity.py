from flask import Blueprint
from backend.portfolio.models import Activity
from backend.portfolio.forms import ActivityForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'activities'
bp = Blueprint(prefix_bp, __name__, url_prefix='/activites')

@bp.route('/index.html')
def index():
    fields = {
        'Nom' : 'name',
    }
    print(Activity.query.all())
    # return BaseView.index(Activity, prefix_bp, fields, "une activité")
    return 'ok'

