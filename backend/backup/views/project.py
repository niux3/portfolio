import subprocess
import json
import pathlib
from pprint import pprint
from datetime import datetime
from sqlalchemy import desc
from flask import render_template, Blueprint, jsonify, url_for, redirect, flash
from backend.core.config import config
from backend.project.models import Project, Technology, Activity, Function, ProjectTechnology
from backend import db


bp = Blueprint('backup_projects', __name__, url_prefix='/sauvegarde')
file_data = config.BASEDIR / 'core' / 'backup' / 'data-projects.json'
public_folder = config.BASEDIR.parent / 'public'
static_folder = public_folder / 'static'
file_data_public = static_folder / 'data-projects.json'


def export_project_data_frontend():
    output = [{
        "id": r.id,
        "name": r.name,
        "slug": r.slug,
        "url": r.url,
        "description": r.description,
        "year": r.year,
        "activity_name": r.activity.name if r.activity else None,
        "activity_icon": r.activity.icon if r.activity else None,
        "function": r.function.name if r.function else None,
        "location": r.location,
        "customer": r.customer,
        "technologies": [t.name for t in r.technologies]
    } for r in Project.query.filter(Project.online == 1).all()]

    with open(str(file_data_public), 'w', encoding='utf-8') as f:
        f.write(json.dumps(output, indent=2))
    return True


def export_project_data_backend():
    output = {
        'project': [r.to_dict() for r in Project.query.all()],
        'activity': [r.to_dict() for r in Activity.query.all()],
        'function': [r.to_dict() for r in Function.query.all()],
        'technology': [r.to_dict() for r in Technology.query.all()],
        'project_technology': [r.to_dict() for r in ProjectTechnology.query.all()],
    }

    with open(str(file_data), 'w', encoding='utf-8') as f:
        f.write(json.dumps(output, indent=2))
    return True


@bp.route('/projets-export-html.html')
def export_html():
    path_manifest = public_folder / '.vite' / 'manifest.json'

    with open(str(path_manifest), encoding='utf-8') as f:
        manifest_data = json.load(f)
    pathlib.Path.unlink(
        public_folder / manifest_data.get('frontend/js/main.js').get('file'))
    pathlib.Path.unlink(
        public_folder / manifest_data.get('frontend/scss/index.scss').get('file'))

    result = subprocess.check_call('npm run build', shell=True)

    with open(str(path_manifest), encoding='utf-8') as f:
        manifest_data = json.load(f)

    ctx = {
        "layout_template": "base_export.html",
        "js_file": manifest_data.get('frontend/js/main.js').get('file'),
        "css_file": manifest_data.get('frontend/scss/index.scss').get('file'),
        "object_list": {
            "projects": Project.query.filter(Project.online == 1).order_by(desc('year')),
            "technologies": Technology.query.filter(Technology.online == 1).all(),
        }
    }
    html = render_template('project/show.html', **ctx)
    with open(str(public_folder / 'index.html'), "w", encoding="utf-8") as f:
        f.write(html)
    flash("Votre export de la page accueil est réussi", "success")
    return redirect(url_for('projects.index'))


@bp.route('/projets-export-json.html')
def export_json():
    if export_project_data_backend() and export_project_data_frontend():
        flash("Votre export en json est réussi", "success")
        return redirect(url_for('projects.index'))


@bp.route('/projets-import-json.html')
def import_json():
    with open(str(file_data), 'r', encoding='utf-8') as f:
        data = json.load(f)
    projects = [Project.from_dict(item) for item in data['project']]
    activities = [Activity.from_dict(item) for item in data['activity']]
    functions = [Function.from_dict(item) for item in data['function']]
    technologies = [Technology.from_dict(item) for item in data['technology']]
    project_technologies = [ProjectTechnology.from_dict(
        item) for item in data['project_technology']]

    db.session.add_all(projects + activities + functions +
                       technologies + project_technologies)
    db.session.commit()
    flash("Votre import en json est réussi", "success")
    return redirect(url_for('projects.index'))
