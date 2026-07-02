from flask import Blueprint, render_template, flash, url_for, redirect, request
from backend.cv_ats.models import CvWork
from backend.cv_ats.forms import CvWorkForm
from backend.core.libs.base_views import BaseView
from backend import db


prefix_bp = 'cv_work'
bp = Blueprint(prefix_bp, __name__, url_prefix='/cv_work')


@bp.route('/backoffice/index.html')
def index():
    fields = {
        'Client': 'customer',
        'Année début': 'year_start',
        'Année fin': 'year_end',
    }
    return BaseView.index(CvWork.query.order_by(CvWork.year_end.desc()).all(), prefix_bp, fields, "expérience")


@bp.route('/backoffice/ajouter.html', methods=['GET', 'POST'])
def add():
    form = CvWorkForm()
    if form.validate_on_submit() and request.method == "POST":
        work = CvWork()
        form.populate_obj(work)
        db.session.add(work)
        db.session.commit()
        flash("Votre item a bien été ajouté", "success")
        return redirect(url_for(f'{prefix_bp}.index'))
    ctx = {
        'form': form
    }
    return render_template('project/edit.html', **ctx)


@bp.route('/backoffice/<int:id>-supprimer.html')
def destroy(id):
    instance = CvWork.query.get_or_404(id)
    db.session.flush()
    db.session.delete(instance)
    db.session.commit()
    flash("Votre item a bien été supprimé", "success")
    return redirect(url_for(f'{prefix_bp}.index'))


@bp.route('/backoffice/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    instance = CvWork.query.get_or_404(id)
    form = CvWorkForm(obj=instance)
    if form.validate_on_submit():
        form.populate_obj(instance)
        try:
            db.session.commit()
            flash("Votre item a bien été modifié", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Erreur lors de la mise à jour : {str(e)}", "danger")
            print("Erreur SQLAlchemy :", e)
        return redirect(url_for(f'{prefix_bp}.index'))
    ctx = {
        "instance": instance,
        "form": form
    }
    return render_template('project/edit.html', **ctx)
