from flask import Blueprint
from backend.project.models import Activity
from backend.project.forms import ActivityForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'activities'
bp = Blueprint(prefix_bp, __name__, url_prefix='/activites')

@bp.route('/backoffice/index.html')
def index():
    fields = {
        'Nom' : 'name',
    }
    return BaseView.index(Activity.query.all(), prefix_bp, fields, "une activité")

@bp.route('/backoffice/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(ActivityForm, Activity, prefix_bp)

@bp.route('/backoffice/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Activity, prefix_bp)

@bp.route('/backoffice/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, Activity, ActivityForm, prefix_bp)

