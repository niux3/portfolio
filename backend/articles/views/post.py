from flask import render_template, Blueprint
from markdown import markdown
from backend.core.config import config
from backend.core.libs.base_views import BaseView
from backend.articles.models import Post
from backend.articles.forms import PostForm


prefix_bp = 'posts'
bp = Blueprint(prefix_bp, __name__, url_prefix='/articles')

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

@bp.route('/index.html')
def index():
    fields = {
        'slug' : 'slug',
        'status' : 'status',
    }
    return BaseView.index(Post, prefix_bp, fields, "un article")

@bp.route('/ajouter.html', methods=['GET', 'POST'])
def add():
    form = PostForm()
    if form.validate_on_submit():
        return 'valide !'
    ctx = {
        'form': form
    }
    return 'ajouter'

@bp.route('/<int:id>-supprimer.html')
def destroy(id):
    return 'destoy ' + id

@bp.route('/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return 'edit ' + id
