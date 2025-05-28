import subprocess
import json
import pathlib
from sqlalchemy import desc
from flask import render_template, Blueprint, jsonify, url_for, redirect, flash
from backend.core.config import config
from backend.project.models import Project, Technology


bp = Blueprint('backup_projects', __name__, url_prefix='/sauvegarde')
file_data_project_json = config.BASEDIR / 'core' / 'backup' / 'data-projects.json'

@bp.route('/projets-export-html.html')
def export_html():
    public_folder = config.BASEDIR.parent / 'public'
    static_folder = public_folder / 'static'
    path_manifest = static_folder / '.vite' / 'manifest.json'

    with open(str(path_manifest), encoding='utf-8') as f:
        manifest_data = json.load(f)
    pathlib.Path.unlink(static_folder / manifest_data.get('frontend/main.js').get('file'))
    pathlib.Path.unlink(static_folder / manifest_data.get('frontend/scss/index.scss').get('file'))

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
    return jsonify({
        "msg": html
    })

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
    print(data[0])
    flash("Votre import en json est réussi", "success")
    return redirect(url_for('projects.index'))

