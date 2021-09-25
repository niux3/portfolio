from flask import Blueprint

bp = Blueprint('export', __name__)


@bp.route('/export')
def index():
    return "export method"