from flask import Blueprint
from backend.cv_ats.models import CvData
from backend.cv_ats.forms import CvDataForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'cv_data'
bp = Blueprint(prefix_bp, __name__, url_prefix='/cv_data')


@bp.route('/backoffice/index.html')
def index():
    fields = {
        'Nom': 'name',
    }
    return BaseView.index(CvData.query.all(), prefix_bp, fields, "base data")


@bp.route('/backoffice/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(CvDataForm, CvData, prefix_bp)


@bp.route('/backoffice/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, CvData, prefix_bp)


@bp.route('/backoffice/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, CvData, CvDataForm, prefix_bp)
