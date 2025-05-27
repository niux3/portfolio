import subprocess
import json
import pathlib
from sqlalchemy import desc
from flask import render_template, Blueprint, jsonify
from backend.core.config import config
from backend.project.models import Project, Technology


bp = Blueprint('export', __name__)

@bp.route('/export.html')
def export_project():
    dist_folder = config.BASEDIR.parent / 'dist'
    static_folder = dist_folder / 'static'
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
    with open(str(dist_folder / 'index.html'), "w", encoding="utf-8") as f:
        f.write(html)
    return jsonify({
        "msg": html
    })
