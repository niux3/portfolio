from flask import render_template, Blueprint


bp = Blueprint('pages', __name__)

@bp.route('/')
def index():
    return render_template('pages/index.html')
