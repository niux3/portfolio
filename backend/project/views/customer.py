from flask import Blueprint
from backend.project.models import Customer
from backend.project.forms import CommonForm
from backend.core.libs.base_views import BaseView


prefix_bp = 'customers'
bp = Blueprint(prefix_bp, __name__, url_prefix='/customers')


@bp.route('/backoffice/index.html')
def index():
    fields = {
        'Nom': 'name',
    }
    return BaseView.index(Customer.query.all(), prefix_bp, fields, "un client")


@bp.route('/backoffice/ajouter.html', methods=['GET', 'POST'])
def add():
    return BaseView.add(CommonForm, Customer, prefix_bp)


@bp.route('/backoffice/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Customer, prefix_bp)


@bp.route('/backoffice/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, Customer, CommonForm, prefix_bp)
