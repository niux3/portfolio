from flask import Blueprint
from backend.articles.models import Tag
from backend.articles.forms import TagForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'tags'
bp = Blueprint(prefix_bp, __name__, url_prefix='/tags')

@bp.route('/index.html')
def index():
    fields = {
        'Nom' : 'name',
    }
    return BaseView.index(Tag, prefix_bp, fields, "un tag")

@bp.route('/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(TagForm, Tag, prefix_bp)

@bp.route('/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Tag, prefix_bp)

@bp.route('/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, Tag, TagForm, prefix_bp)

