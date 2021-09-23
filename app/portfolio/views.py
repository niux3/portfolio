from flask import Blueprint, render_template, request, redirect, url_for
from app.portfolio.forms import CommonForm, PortfolioForm
from app import db
from app.portfolio.models import Function, Technology, Portfolio, portfolio_technology

bp = Blueprint('portfolio', __name__)


@bp.route('/')
def index_portfolio():
    ctx = {
        'rows': Portfolio.query.filter_by(online=1),
        'online': True,
        'suffixe_url': '_portfolio'
    }
    return render_template('portfolio/index.html', **ctx)


@bp.route('/create-portfolio', methods=['GET', 'POST'])
def create_portfolio():
    form = PortfolioForm()
    if request.method == "POST" and form.validate_on_submit():
        data = {
            'name': form.name.data,
            'slug': form.slug.data,
            'description': form.description.data,
            'color': form.color.data,
            'online': form.online.data,
            'functions_id': form.functions.data.id,
        }
        portfolio = Portfolio(**data)
        db.session.add(portfolio)
        db.session.commit()
        for row in form.technologies.data:
            data = portfolio_technology.insert().values(portfolios_id=portfolio.id, technologies_id=row.id)
            db.session.execute(data)
            db.session.commit()
        return redirect(url_for('portfolio.index_portfolio'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/update-portfolio-<int:id>', methods=['GET', 'POST'])
def update_portfolio(id):
    row = Portfolio.query.get_or_404(id)
    form = PortfolioForm(obj=row)
    if request.method == "POST" and form.validate_on_submit():
        return 'ok'
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/delete-portfolio-<int:id>')
def delete_portfolio(id):
    row = Portfolio.query.get_or_404(id)
    db.session.remove(row)
    db.session.commit()
    return redirect(url_for('portfolio.index_portfolio'))


@bp.route('/functions')
def index_function():
    ctx = {
        'suffixe_url': '_function',
        'rows': Function.query.all()
    }
    return render_template('portfolio/index.html', **ctx)


@bp.route('/create-function', methods=['GET', 'POST'])
def create_function():
    form = CommonForm()
    if request.method == 'POST' and form.validate_on_submit():
        db.session.add(Function(name=form.name.data.lower()))
        db.session.commit()
        return redirect(url_for('portfolio.index_function'))
    ctx = {
        'form': form,
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/update-function-<int:id>', methods=['GET', 'POST'])
def update_function(id):
    row = Function.query.get_or_404(id)
    form = CommonForm(obj=row)
    if request.method == 'POST' and form.validate_on_submit():
        row.name = form.name.data.lower()
        db.session.commit()
        return redirect(url_for('portfolio.index_function'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/delete-function-<int:id>')
def delete_function(id):
    row = Function.query.get_or_404(id)
    db.session.remove(row)
    db.session.commit()
    return redirect(url_for('portfolio.index_function'))


@bp.route('/technologies')
def index_technologies():
    ctx = {
        'suffixe_url': '_technologies',
        'rows': Technology.query.all()
    }
    return render_template('portfolio/index.html', **ctx)


@bp.route('/create-technology', methods=['GET', 'POST'])
def create_technologies():
    form = CommonForm()
    if request.method == 'POST' and form.validate_on_submit():
        db.session.add(Technology(name=form.name.data.lower()))
        db.session.commit()
        return redirect(url_for('portfolio.index_technologies'))
    ctx = {
        'form': form,
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/update-technologie-<int:id>', methods=['GET', 'POST'])
def update_technologies(id):
    row = Technology.query.get_or_404(id)
    form = CommonForm(obj=row)
    if request.method == 'POST' and form.validate_on_submit():
        row.name = form.name.data.lower()
        db.session.commit()
        return redirect(url_for('portfolio.index_technologies'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/delete-technologie-<int:id>')
def delete_technologies(id):
    row = Technology.query.get_or_404(id)
    db.session.remove(row)
    db.session.commit()
    return redirect(url_for('portfolio.index_technologies'))
