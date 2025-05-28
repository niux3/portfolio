import subprocess
import json
import pathlib
from datetime import datetime
from sqlalchemy import desc
from flask import render_template, Blueprint, jsonify, url_for, redirect, flash
from backend.core.config import config
from backend.project.models import Project, Technology, Activity, Function, ProjectTechnology
from backend import db


bp = Blueprint('backup_projects', __name__, url_prefix='/sauvegarde')
file_data_project_json = config.BASEDIR / 'core' / 'backup' / 'data-projects.json'

@bp.route('/projets-export-html.html')
def export_html():
    public_folder = config.BASEDIR.parent / 'public'
    static_folder = public_folder / 'static'
    path_manifest = public_folder / '.vite' / 'manifest.json'
    
    with open(str(path_manifest), encoding='utf-8') as f:
        manifest_data = json.load(f)
    pathlib.Path.unlink(public_folder / manifest_data.get('frontend/main.js').get('file'))
    pathlib.Path.unlink(public_folder / manifest_data.get('frontend/scss/index.scss').get('file'))

    result = subprocess.check_call('npm run build', shell=True)

    with open(str(path_manifest), encoding='utf-8') as f:
        manifest_data = json.load(f)

    ctx = {
        "layout_template": "base_export.html",
        "js_file": manifest_data.get('frontend/main.js').get('file'),
        "css_file": manifest_data.get('frontend/scss/index.scss').get('file'),
        "object_list": {
            "projects": Project.query.filter(Project.online == 1).order_by(desc('year')),
            "technologies": Technology.query.filter(Technology.online == 1).all(),
        }
    }
    html = render_template('pages/index.html', **ctx)
    with open(str(public_folder / 'index.html'), "w", encoding="utf-8") as f:
        f.write(html)
    flash("Votre export de la page accueil est réussi", "success")
    return redirect(url_for('projects.index'))

@bp.route('/projets-export-json.html')
def export_json():
    output = [{
        'id': project.id,
        'name': project.name,
        'slug': project.slug,
        'description': project.description,
        'color': project.color,
        'created': str(project.created),
        'modified': str(project.modified),
        'online': project.online,
        'url': project.url,
        'function': project.function.name,
        'technologies': [technology.name for technology in project.technologies],
        'year': project.year,
        'activity_icon': project.activity.icon,
        'activity_name': project.activity.name,
        'location': project.location,
        'customer': project.customer,
        'sort': project.sort,
    } for project in Project.query.all()]

    with open(str(file_data_project_json), 'w', encoding='utf-8') as f:
        f.write(json.dumps(output, indent=2))
    flash("Votre export en json est réussi", "success")
    return redirect(url_for('projects.index'))

@bp.route('/projets-import-json.html')
def import_json():
    with open(str(file_data_project_json), 'r', encoding='utf-8') as f:
        data = json.load(f)
    for row in data:
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
        ctx_data['created'] = datetime.strptime(row['created'][:row['created'].find('.')], '%Y-%m-%d %H:%M:%S')
        ctx_data['modified'] = datetime.strptime(row['modified'][:row['modified'].find('.')], '%Y-%m-%d %H:%M:%S')

        instance = Project(**ctx_data)
        db.session.add(instance)
        db.session.commit()
        db.session.refresh(instance)
        for tech in row['technologies']:
            instance_tech = ProjectTechnology(projects_id=instance.id, technologies_id=Technology.query.filter(Technology.name==tech).first().id)
            db.session.add(instance_tech)
            db.session.commit()
            db.session.refresh(instance_tech)
    flash("Votre import en json est réussi", "success")
    return redirect(url_for('projects.index'))

