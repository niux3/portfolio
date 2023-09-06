from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.portfolio.models import Portfolio
from app.images.models import Image, Category
from app.portfolio.forms import CommonForm
from app.images.forms import UploadImagesForm, SelectViewForm, EditImgForm
from werkzeug.utils import secure_filename
from app import config, db
from app.config import basedir
import os
import uuid

bp = Blueprint('images', __name__)


@bp.route('/index-images')
def index():
    form = SelectViewForm()
    sql = """
        SELECT 
            i.id as id,
            p.name as portfolio,
            i.url as img,
            c.name as categorie
        FROM 
            portfolios as p,
            images as i,
            categories as c 
        WHERE 
            p.id = i.portfolios_id 
        AND 
            c.id = i.categories_id                   
    """
    rows = db.session.execute(sql)
    # rows = Image.query.all()
    if request.method == "GET" and request.args.get('send') == "ok":
        if request.args.get('portfolios') != '__None' and request.args.get('categories') != "__None":
            sql += "and p.id=:pid and c.id=:cid"
            params = {'pid': request.args.get('portfolios'), 'cid': request.args.get('categories')}
            # print(Portfolio.query.filter(Portfolio.id==request.args.get('portfolios')).join(Image).filter(Image.categories_id==request.args.get('categories')).all())
            # rows = Image.query.filter_by(categories_id=request.args.get('categories'), id=request.args.get('portfolios')).all()
        elif request.args.get('portfolios') != '__None' and request.args.get('categories') == "__None":
            sql += "and p.id=:pid"
            params = {'pid': request.args.get('portfolios')}
            # rows = Image.query.filter_by(id=request.args.get('portfolios')).all()
        elif request.args.get('portfolios') == '__None' and request.args.get('categories') != "__None":
            sql += "and c.id=:cid"
            params = {'cid': request.args.get('categories')}
            # rows = Image.query.filter_by(categories_id=request.args.get('categories')).all()
        rows = db.session.execute(sql, params)
    ctx = {
        'form': form,
        'rows': rows
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
        file.filename = f"{form.portfolios.data.id}--{form.categories.data.id}__{name}.{ext.lower()}"
        path = os.path.join(base_path, secure_filename(file.filename))
        data = {
            'categories_id': form.categories.data.id,
            'portfolios_id': form.portfolios.data.id,
            'url': path.replace(basedir, ''),
            'name': form.name.data,
            'description': form.description.data,
            'online': form.online.data,
        }
        file.save(path)
        image = Image(**data)
        db.session.add(image)
        db.session.commit()
        flash(f"création d'une image effectuée pour {dir}", "success")
        return redirect(url_for('images.index'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/update-images-<int:id>', methods=['GET', 'POST'])
def update(id):
    row = Image.query.get_or_404(id)
    form = EditImgForm(obj=row)
    if request.method == 'POST' and form.validate_on_submit():
        row.id = form.id.data
        row.categories_id = form.categories.data.id
        row.portfolios_id = form.portfolios.data.id
        row.name = form.name.data
        row.description = form.description.data
        row.online = form.online.data
        db.session.commit()
        flash("modification d'une image effectuée", "success")
        return redirect(url_for('images.index'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/delete-images-<int:id>')
def delete(id):
    row = Image.query.get_or_404(id)
    os.remove(os.path.join(basedir, row.url[1:]))
    db.session.delete(row)
    db.session.commit()
    flash("suppression d'une image effectuée", "warning")
    return redirect(url_for('images.index'))


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