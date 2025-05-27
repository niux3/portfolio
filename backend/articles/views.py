from flask import render_template, Blueprint
from markdown import markdown
from backend.core.config import config


bp = Blueprint('articles', __name__)

@bp.route('/article.html')
def show():
    print(config.BASEDIR / 'articles')
    with open(str(config.BASEDIR / 'articles'/ 'definir-le-langage-naturel.md')) as f:
        obj = markdown(f.read(), extensions=['extra'])
    ctx = {
        'object': obj,
        'tags': [
            'accessibilité',
            'html',
            'seo',
            'ux'
        ],
        'shares': [
            'fa-brands fa-linkedin',
            'fa-brands fa-square-facebook',
            'fa-brands fa-square-x-twitter',
            'fa-solid fa-square-share-nodes',
        ]
    }
    return render_template('articles/show.html', **ctx)
