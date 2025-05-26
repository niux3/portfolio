from flask import render_template, Blueprint


bp = Blueprint('articles', __name__)

@bp.route('/article.html')
def show():
    return render_template('articles/show.html')
