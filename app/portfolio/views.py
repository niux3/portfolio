from flask import Blueprint, render_template, request, redirect, url_for
from app.portfolio.forms import CommonForm
from app import db
from app.portfolio.models import Function

bp = Blueprint('portfolio', __name__)


@bp.route('/')
def index_portfolio():
    ctx = {
        'online': True,
        'suffixe_url': '_portfolio'
    }
    return render_template('portfolio/index.html', **ctx)


@bp.route('/create-portfolio')
def create_portfolio():
    ctx = {
        'suffixe_url': '_portfolio'
    }
    return render_template('portfolio/create.html')


@bp.route('/function')
def index_function():
    ctx = {
        'suffixe_url': '_function',
        'rows': Function.query.all()
    }
    return render_template('portfolio/index.html', **ctx)


@bp.route('/create-function')
def create_function():
    form = CommonForm()
    if request.method == 'POST' and form.validate_on_submit():
        db.session.add(Function(name=form.name.data.lower()))
        db.session.commit()
        return redirect(url_for('portfolio.index_function'))
    ctx = {
        'form': form,
    }
    return render_template('portfolio/create.html', **ctx)
