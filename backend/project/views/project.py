from flask import Blueprint, render_template, flash, request, url_for, redirect
from slugify import slugify
from sqlalchemy import desc
from backend.project.models import Project, ProjectTechnology, Technology
from backend.project.forms import ProjectForm
from backend.core.libs.base_views import BaseView
from backend import db


prefix_bp = 'projects'
bp = Blueprint(prefix_bp, __name__)

@bp.route('/')
def index():
    fields = {
        'Nom' : 'name',
    }
    return BaseView.index(Project, prefix_bp, fields, "un projet")

@bp.route('/projets/ajouter.html', methods=['GET', 'POST'])
def add():
    form = ProjectForm()
    if form.validate_on_submit() and request.method == "POST":
        project = Project()
        form.populate_obj(project)
        project.slug = slugify(project.name)
        project.online = 1 if form.online.data else 0
        project.technologies = form.technologies.data
        db.session.add(project)
        db.session.commit()
        flash("Votre item a bien été ajouté", "success")
        return redirect(url_for(f'{prefix_bp}.index'))
    ctx = {
        'form': form
    }
    return render_template('project/edit.html', **ctx)

@bp.route('/projets/<int:id>-supprimer.html')
def destroy(id):
    instance = Project.query.get_or_404(id)
    instance.technologies.clear()

    db.session.flush()
    db.session.delete(instance)
    db.session.commit()
    flash("Votre item a bien été supprimé", "success")
    return redirect(url_for(f'{prefix_bp}.index'))

@bp.route('/projets/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)

    if request.method == 'GET':
        form.technologies.data = project.technologies

    if form.validate_on_submit():
        form.populate_obj(project)
        if 'online' in form.data.keys():
            project.online = 1 if form.data['online'] == True else 0
        project.technologies = form.technologies.data
        project.slug = slugify(form.name.data)
        try:
            db.session.commit()
            flash("Votre item a bien été modifié", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Erreur lors de la mise à jour : {str(e)}", "danger")
            print("Erreur SQLAlchemy :", e)
        return redirect(url_for(f'{prefix_bp}.index'))
    ctx = {
        "project": project,
        "form": form
    }
    return render_template('project/edit.html', **ctx)

@bp.route('/index.html')
def show():
    ctx = {
        "object_list": {
            "projects": Project.query.filter(Project.online == 1).order_by(desc('year')),
            "technologies": Technology.query.filter(Technology.online == 1).all()
        }
    }
    return render_template('project/show.html', **ctx)
