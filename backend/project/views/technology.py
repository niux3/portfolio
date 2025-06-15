from flask import Blueprint
from backend.project.models import Technology
from backend.project.forms import TechnologyForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'technology'
bp = Blueprint(prefix_bp, __name__, url_prefix='/technologies')

@bp.route('/index.html')
def index():
    fields = {
        'Nom' : 'name',
    }
    return BaseView.index(Technology.query.all(), prefix_bp, fields, "une technologie")

@bp.route('/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(TechnologyForm, Technology, prefix_bp)

@bp.route('/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Technology, prefix_bp)

@bp.route('/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, Technology, TechnologyForm, prefix_bp)

