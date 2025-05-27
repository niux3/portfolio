from flask import render_template, Blueprint
from markdown import markdown
from backend.core.config import config


bp = Blueprint('posts', __name__, url_prefix='/articles')

@bp.route('/voir.html')
def show():
    with open(str(config.BASEDIR / 'core'/ 'backup' / 'definir-le-langage-naturel.md')) as f:
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
