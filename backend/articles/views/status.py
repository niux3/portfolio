from flask import Blueprint
from backend.articles.models import Status
from backend.articles.forms import StatusForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'status'
bp = Blueprint(prefix_bp, __name__, url_prefix='/status')

@bp.route('/backoffice/index.html')
def index():
    fields = {
        'Nom' : 'name',
    }
    return BaseView.index(Status.query.all(), prefix_bp, fields, "un status")

@bp.route('/backoffice/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(StatusForm, Status, prefix_bp)

@bp.route('/backoffice/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Status, prefix_bp)

@bp.route('/backoffice/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, Status, StatusForm, prefix_bp)

