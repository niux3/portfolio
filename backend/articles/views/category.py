from flask import Blueprint
from backend.articles.models import Category
from backend.articles.forms import CategoryForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'categories'
bp = Blueprint(prefix_bp, __name__, url_prefix='/categories')

@bp.route('/index.html')
def index():
    fields = {
        'Nom' : 'name',
        'Description' : 'description',
    }
    return BaseView.index(Category.query.all(), prefix_bp, fields, "une categorie")

@bp.route('/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(CategoryForm, Category, prefix_bp)

@bp.route('/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Category, prefix_bp)

@bp.route('/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, Category, CategoryForm, prefix_bp)

