from flask import Blueprint
from backend.portfolio.models import Activity
from backend.portfolio.forms import ActivityForm


prefix_bp = 'activities'
bp = Blueprint(prefix_bp, __name__, url_prefix='/activites')

@bp.route('/index.html')
def index():
    return 'ok activites'
