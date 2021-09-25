from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.portfolio.models import Portfolio
from app.images.models import Image, Category
from app.portfolio.forms import CommonForm
from app.images.forms import UploadImagesForm, SelectViewForm
from werkzeug.utils import secure_filename
from app import config, db
from app.config import basedir
import os
import uuid

bp = Blueprint('images', __name__)


@bp.route('/index-images')
def index():
    form = SelectViewForm()
    ctx = {
        'form': form,
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
        flash(f"création d'une image effectuée pour {dir}", "success")
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


@bp.route('/categories-images')
def index_categories():
    ctx = {
        'prefixe_url': 'images',
        'suffixe_url': '_categories',
        'rows': Category.query.all()
    }
    return render_template('portfolio/index.html', **ctx)


@bp.route('/create-categories-images', methods=['GET', 'POST'])
def create_categories():
    form = CommonForm()
    if request.method == 'POST' and form.validate_on_submit():
        db.session.add(Category(name=form.name.data.lower()))
        db.session.commit()
        flash("création d'une catégorie image effectuée", "success")
        return redirect(url_for('images.index_categories'))
    ctx = {
        'form': form,
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/edit-categories-images-<int:id>', methods=['GET', 'POST'])
def update_categories(id):
    row = Category.query.get_or_404(id)
    form = CommonForm(obj=row)
    if request.method == 'POST' and form.validate_on_submit():
        row.name = form.name.data.lower()
        db.session.commit()
        flash("mise à jour d'une catégorie image effectuée", "success")
        return redirect(url_for('images.index_categories'))
    ctx = {
        'form': form,
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/delete-categories-images-<int:id>')
def delete_categories(id):
    row = Category.query.get_or_404(id)
    db.session.delete(row)
    db.session.commit()
    flash("suppression d'une catégorie image effectuée", "warning")
    return redirect(url_for('images.index_categories'))