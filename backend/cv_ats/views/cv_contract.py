from flask import Blueprint
from backend.cv_ats.models import CvContractType
from backend.project.forms import CommonForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'cv_contract'
bp = Blueprint(prefix_bp, __name__, url_prefix='/cv_contract')


@bp.route('/backoffice/index.html')
def index():
    fields = {
        'Nom': 'name',
    }
    return BaseView.index(CvContractType.query.all(), prefix_bp, fields, "un contrat")


@bp.route('/backoffice/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(CommonForm, CvContractType, prefix_bp)


@bp.route('/backoffice/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, CvContractType, prefix_bp)


@bp.route('/backoffice/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, CvContractType, CommonForm, prefix_bp)
