from flask import Blueprint
from backend.project.models import Project
from backend.project.forms import ProjectForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'projects'
bp = Blueprint(prefix_bp, __name__, url_prefix='/projets')

@bp.route('/index.html')
def index():
    fields = {
        'Nom' : 'name',
    }
    return BaseView.index(Project, prefix_bp, fields, "un projet")

@bp.route('/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(ProjectForm, Project, prefix_bp)

@bp.route('/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Project, prefix_bp)

@bp.route('/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, Project, ProjectForm, prefix_bp)

