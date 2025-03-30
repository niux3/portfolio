from flask import Blueprint
from backend.project.models import Function
from backend.project.forms import CommonForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'functions'
bp = Blueprint(prefix_bp, __name__, url_prefix='/fonctions')

@bp.route('/index.html')
def index():
    fields = {
        'Nom' : 'name',
    }
    return BaseView.index(Function, prefix_bp, fields, "une fonction")

@bp.route('/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(CommonForm, Function, prefix_bp)

@bp.route('/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Function, prefix_bp)

@bp.route('/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, Function, CommonForm, prefix_bp)

