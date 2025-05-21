from flask import Blueprint, render_template, flash, request, url_for, redirect
from slugify import slugify
from backend.project.models import Project, ProjectTechnology
from backend.project.forms import ProjectForm
from backend.core.libs.base_views import BaseView
from backend import db


prefix_bp = 'projects'
bp = Blueprint(prefix_bp, __name__, url_prefix='/projets')

@bp.route('/index.html')
def index():
    fields = {
        'Nom' : 'name',
    }
    return BaseView.index(Project, prefix_bp, fields, "un projet")

@bp.route('/ajouter.html', methods=['GET', 'POST'])
def add():
    form = ProjectForm()
    if form.validate_on_submit() and request.method == "POST":
        cleared_data = {k:v for k, v in form.data.items() if k != 'csrf_token'}
        if 'online' in cleared_data.keys():
            cleared_data['online'] = 1 if cleared_data['online'] == True else 0
        project = Project(**{
            "name": cleared_data["name"],
            "slug": slugify(cleared_data["name"]),
            "url": cleared_data["url"],
            "year": cleared_data["year"],
            "description": cleared_data["description"],
            "color": cleared_data["color"],
            "customer": cleared_data["customer"],
            "location": cleared_data["location"],
            "online": cleared_data["online"],
            "activities_id": cleared_data["activities"].id,
            "functions_id": cleared_data["functions_id"].id,
        })
        db.session.add(project)
        db.session.commit()
        db.session.refresh(project)
        for tech in cleared_data['technologies']:
            project_technology = ProjectTechnology(**{
                "technologies_id": tech.id,
                "projects_id": project.id
            })
            db.session.add(project_technology)
            db.session.commit()

        flash("Votre item a bien été ajouté", "success")
        return redirect(url_for(f'{prefix_bp}.index'))
    ctx = {
        'form': form
    }
    return render_template('project/edit.html', **ctx)

@bp.route('/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Project, prefix_bp)

@bp.route('/<int:id>-editer.html', methods=['GET', 'POST'])
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
        project.slug = slugify(form.slug.data)
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

"""
import json
from backend.core.config import config
from pprint import pprint
from backend.project.models import Activity, Function, ProjectTechnology, Technology
from backend import db


@bp.route('/import-project')
def import_data():
    src = config.BASEDIR / 'core' / 'backup' / 'data.json'
    with open(src, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i, row in enumerate(data):
        if Activity.query.filter(Activity.name==row['activity_name']).count() == 0:
            activity = Activity()
            activity.name = row['activity_name']
            activity.icon = row['activity_icon']
            db.session.add(activity)
            db.session.commit()
            db.session.refresh(activity)
        else:
            activity = Activity.query.filter(Activity.name==row['activity_name']).first()
        if Function.query.filter(Function.name==row['function']).count() == 0:
            function = Function()
            function.name = row['function']
            db.session.add(function)
            db.session.commit()
            db.session.refresh(function)
        else:
            function = Function.query.filter(Function.name==row['function']).first()

        for tech in row['technologies']:
            if Technology.query.filter(Technology.name==tech).count() == 0:
                instance = Technology()
                instance.name = tech
                db.session.add(instance)
                db.session.commit()
        print(activity, activity.id)
        print(function, function.id)

        ctx_data = {k : v for k, v in row.items() if k != 'technologies' and not k.startswith('activi') and k != 'function' and k != 'id' and k != 'images'}
        ctx_data['activities_id'] = Activity.query.filter(Activity.name==row['activity_name']).first().id
        ctx_data['functions_id'] = Function.query.filter(Function.name==row['function']).first().id

        instance = Project(**ctx_data)
        db.session.add(instance)
        db.session.commit()
        db.session.refresh(instance)
        for tech in row['technologies']:
            instance_tech = ProjectTechnology(projects_id=instance.id, technologies_id=Technology.query.filter(Technology.name==tech).first().id)
            db.session.add(instance_tech)
            db.session.commit()
            db.session.refresh(instance_tech)

        pprint(row, indent=2)
        pprint(ctx_data, indent=2)
    return 'ok'
"""
