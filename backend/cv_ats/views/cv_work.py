from flask import Blueprint, render_template
from backend.cv_ats.models import CvWork
from backend.cv_ats.forms import CvWorkForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'cv_work'
bp = Blueprint(prefix_bp, __name__, url_prefix='/cv_work')


@bp.route('/backoffice/index.html')
def index():
    fields = {
        'Nom': 'name',
    }
    return BaseView.index(CvWork.query.all(), prefix_bp, fields, "expérience")


@bp.route('/backoffice/ajouter.html', methods=['GET', 'POST'])
def add():
    form = CvWorkForm()
    ctx = {
        'form': form
    }
    return render_template('project/edit.html', **ctx)


@bp.route('/backoffice/<int:id>-supprimer.html')
def destroy(id):
    return 'destroy'


@bp.route('/backoffice/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return 'edit'
