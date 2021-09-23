from flask import Blueprint, render_template

bp = Blueprint('images', __name__)


@bp.route('/index-images')
def index():
    return 'index images !'


@bp.route('/create-images', methods=['GET', 'POST'])
def create():
    return 'create images !'


@bp.route('/update-images', methods=['GET', 'POST'])
def update():
    return 'update images !'


@bp.route('/delete-images')
def delete():
    return 'delete images !'