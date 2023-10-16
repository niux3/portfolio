from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.portfolio.forms import CommonForm, PortfolioForm, ActivityForm
from app import db
from app.portfolio.models import Function, Technology, Portfolio, portfolio_technology, Activity

bp = Blueprint('portfolio', __name__)


@bp.route('/')
def index_portfolio():
    ctx = {
        'rows': Portfolio.query.order_by('sort'),
        'online': True,
        'prefixe_url': 'portfolio',
        'suffixe_url': '_portfolio',
        'sortable': True,
    }
    return render_template('portfolio/index.html', **ctx)


@bp.route('/update-portfolio-sort', methods=['POST'])
def update_portfolio_sort():
    if request.method == "POST":
        for row_ajx in request.get_json():
            row = Portfolio.query.get(row_ajx['id'])
            row.sort = row_ajx['sort']
            db.session.commit()
        return 'ok'


@bp.route('/create-portfolio', methods=['GET', 'POST'])
def create_portfolio():
    form = PortfolioForm()
    if request.method == "POST" and form.validate_on_submit():
        if Portfolio.query.order_by(Portfolio.id.desc()).first() is not None:
            last_id = int(Portfolio.query.order_by(Portfolio.id.desc()).first().id)
        else:
            last_id = 0

        data = {
            'name': form.name.data,
            'slug': form.slug.data,
            'url': form.url.data,
            'description': form.description.data,
            'color': form.color.data,
            'online': form.online.data,
            'functions_id': form.functions.data.id,
            'sort': last_id + 1,
            'year': form.year.data,
            'activities_id': form.activities.data.id,
            'customer': form.customer.data,
            'location': form.location.data,
        }

        portfolio = Portfolio(**data)
        db.session.add(portfolio)
        db.session.commit()
        for row in form.technologies.data:
            data = portfolio_technology.insert().values(portfolios_id=portfolio.id, technologies_id=row.id)
            db.session.execute(data)
            db.session.commit()
        flash("creation d'un portofolio effectuée", "success")
        return redirect(url_for('portfolio.index_portfolio'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/update-portfolio-<int:id>', methods=['GET', 'POST'])
def update_portfolio(id):
    row = Portfolio.query.filter(portfolio_technology.c.portfolios_id == id, Portfolio.id == id).first()
    form = PortfolioForm(obj=row)
    if request.method == "POST" and form.validate_on_submit():
        row.name = form.name.data
        row.slug = form.slug.data
        row.url = form.url.data
        row.year = form.year.data
        row.description = form.description.data
        row.online = form.online.data
        row.functions_id = form.functions.data.id
        row.activities_id = form.activities.data.id
        row.location = form.location.data
        row.customer = form.customer.data
        db.session.commit()

        rows = portfolio_technology.delete().where(portfolio_technology.c.portfolios_id == row.id)
        db.session.execute(rows)
        db.session.commit()
        for pt in form.technologies.data:
            cp = portfolio_technology.insert().values(portfolios_id=row.id, technologies_id=pt.id)
            db.session.execute(cp)
            db.session.commit()

        flash("mise à jour d'un portofolio effectuée", "success")
        return redirect(url_for('portfolio.index_portfolio'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/delete-portfolio-<int:id>')
def delete_portfolio(id):
    row = Portfolio.query.get(id)
    db.session.delete(row)
    db.session.commit()

    flash("suppression d'un portofolio effectuée", "warning")
    return redirect(url_for('portfolio.index_portfolio'))


@bp.route('/activites')
def index_activities():
    ctx = {
        'prefixe_url': 'portfolio',
        'suffixe_url': '_activity',
        'rows': Activity.query.all()
    }
    return render_template('portfolio/index.html', **ctx)


@bp.route('/create-activity', methods=['GET', 'POST'])
def create_activity():
    form = ActivityForm()
    if request.method == 'POST' and form.validate_on_submit():
        db.session.add(Activity(name=form.name.data.lower(), icon=form.icon.data))
        db.session.commit()
        flash("creation d'une activité effectuée", "success")
        return redirect(url_for('portfolio.index_activities'))
    ctx = {
        'form': form,
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/update-activity-<int:id>', methods=['GET', 'POST'])
def update_activity(id):
    row = Activity.query.get_or_404(id)
    form = ActivityForm(obj=row)
    if request.method == 'POST' and form.validate_on_submit():
        row.name = form.name.data.lower()
        row.icon = form.icon.data.lower()
        db.session.commit()
        flash("mise à jour d'une activité effectuée", "success")
        return redirect(url_for('portfolio.index_activities'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/delete-activity-<int:id>')
def delete_activity(id):
    row = Activity.query.get_or_404(id)
    db.session.delete(row)
    db.session.commit()
    flash("suppression d'une activitée effectuée", "warning")
    return redirect(url_for('portfolio.index_activities'))


@bp.route('/functions')
def index_function():
    ctx = {
        'prefixe_url': 'portfolio',
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
        flash("creation d'une function effectuée", "success")
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
        flash("mise à jour d'une function effectuée", "success")
        return redirect(url_for('portfolio.index_function'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/delete-function-<int:id>')
def delete_function(id):
    row = Function.query.get_or_404(id)
    db.session.delete(row)
    db.session.commit()
    flash("suppression d'une function effectuée", "warning")
    return redirect(url_for('portfolio.index_function'))


@bp.route('/technologies')
def index_technologies():
    ctx = {
        'prefixe_url': 'portfolio',
        'suffixe_url': '_technologies',
        'rows': Technology.query.all()
    }
    return render_template('portfolio/index.html', **ctx)


@bp.route('/create-technology', methods=['GET', 'POST'])
def create_technologies():
    form = CommonForm()
    if request.method == 'POST' and form.validate_on_submit():
        db.session.add(Technology(name=form.name.data))
        db.session.commit()
        flash("création d'une technologie effectuée", "success")
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
        row.name = form.name.data
        db.session.commit()
        flash("mise à jour d'une technologie effectuée", "success")
        return redirect(url_for('portfolio.index_technologies'))
    ctx = {
        'form': form
    }
    return render_template('portfolio/edit.html', **ctx)


@bp.route('/delete-technologie-<int:id>')
def delete_technologies(id):
    row = Technology.query.get_or_404(id)
    db.session.delete(row)
    db.session.commit()
    flash("suppression d'une technologie effectuée", "warning")
    return redirect(url_for('portfolio.index_technologies'))


@bp.route('/toggle-online-<int:id>.html')
def toggle_online_portfolio(id):
    row = Portfolio.query.get_or_404(id)
    row.online = not row.online
    db.session.commit()
    flash(f"{row.name} est {'en' if row.online else 'hors'} ligne", "success" if row.online else "danger")
    return redirect(url_for('portfolio.index_portfolio'))


@bp.route('/get-data-select')
def get_data_function():
    print(request.args.get('id_portfolio'))
    row = Portfolio.query.get(request.args.get('id_portfolio'))
    print(row.functions_id)
    return jsonify({
        "activities": row.activities_id,
        "functions": row.functions_id,
    })
