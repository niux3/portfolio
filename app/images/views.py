from flask import Blueprint, render_template, request, redirect, url_for
from app.portfolio.models import Portfolio
from app.images.models import Image
from app.images.forms import UploadImagesForm
from werkzeug.utils import secure_filename
from app import config, db
from app.config import basedir
import os
import uuid

bp = Blueprint('images', __name__)


@bp.route('/index-images')
def index():
    ctx = {
        'rows': Portfolio.query.all(),
    }
    return render_template('images/index.html', **ctx)


@bp.route('/create-images', methods=['GET', 'POST'])
def create():
    form = UploadImagesForm()
    if request.method == 'POST' and form.validate_on_submit():
        dir = form.portfolios.data.slug
        base_path = os.path.join(config['default'].UPLOAD_FOLDER, dir)
        if not os.path.isdir(base_path):
            os.mkdir(base_path)
        file = request.files['upload']
        name, ext = file.filename.split('.')
        name = uuid.uuid4()
        file.filename = f"{form.portfolios.data.id}__{name}.{ext.lower()}"
        path = os.path.join(base_path, secure_filename(file.filename))
        data = {
            'portfolios_id': form.portfolios.data.id,
            'url': path.replace(basedir, ''),
            'name': form.name.data,
            'description': form.description.data,
            'online': form.online.data,
            'thumbnail': form.thumbnail.data,
        }
        file.save(path)
        image = Image(**data)
        db.session.add(image)
        db.session.commit()
        return redirect(url_for('images.create'))
    ctx = {
        'form': form
    }
    return render_template('views/edit-images.html', **ctx)


@bp.route('/update-images-<int:id>', methods=['GET', 'POST'])
def update(id):
    return 'update images !'


@bp.route('/delete-images-<int:id>')
def delete(id):
    return 'delete images !'