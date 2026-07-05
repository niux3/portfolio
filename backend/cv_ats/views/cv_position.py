from flask import Blueprint
from backend.cv_ats.models import CvPosition
from backend.project.forms import CommonForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'cv_position'
bp = Blueprint(prefix_bp, __name__, url_prefix='/cv_postion')


@bp.route('/backoffice/index.html')
def index():
    fields = {
        'Nom': 'name',
    }
    return BaseView.index(CvPosition.query.all(), prefix_bp, fields, "une fonction")


@bp.route('/backoffice/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(CommonForm, CvPosition, prefix_bp)


@bp.route('/backoffice/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, CvPosition, prefix_bp)


@bp.route('/backoffice/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, CvPosition, CommonForm, prefix_bp)