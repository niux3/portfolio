from flask import Blueprint, render_template, request, redirect, url_for
from app.portfolio.models import Portfolio
from app.images.forms import UploadCreateForm
from werkzeug.utils import secure_filename
from app import config
import os

bp = Blueprint('images', __name__)


@bp.route('/index-images')
def index():
    ctx = {
        'rows': Portfolio.query.all(),
        'prefixe_url': 'images',
        'suffixe_url': ''
    }
    return render_template('views/index.html', **ctx)


@bp.route('/create-images', methods=['GET', 'POST'])
def create():
    form = UploadCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        file = request.files['upload']
        path = os.path.join(config['default'].UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(path)
        return redirect(url_for('images.create'))
    ctx = {
        'form': form
    }
    return render_template('views/edit.html', **ctx)


@bp.route('/update-images', methods=['GET', 'POST'])
def update():
    return 'update images !'


@bp.route('/delete-images')
def delete():
    return 'delete images !'