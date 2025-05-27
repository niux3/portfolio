from flask import render_template, Blueprint
from markdown import markdown
from backend.core.config import config


bp = Blueprint('articles', __name__)

@bp.route('/article.html')
def show():
    print(config.BASEDIR / 'articles')
    with open(str(config.BASEDIR / 'articles'/ 'data_temp.md')) as f:
        obj = markdown(f.read(), extensions=['extra'])
    ctx = {
        'object': obj
    }
    return render_template('articles/show.html', **ctx)
