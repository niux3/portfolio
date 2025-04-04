from flask import Blueprint
from backend.project.models import Project
from backend.project.forms import ProjectForm
from backend.core.libs.base_views import BaseView

import json
from backend.core.config import config
from pprint import pprint
from backend.project.models import Activity, Function, ProjectTechnology, Technology
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
    return BaseView.add(ProjectForm, Project, prefix_bp)

@bp.route('/<int:id>-supprimer.html')
def destroy(id):
    return BaseView.destroy(id, Project, prefix_bp)

@bp.route('/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    return BaseView.edit(id, Project, ProjectForm, prefix_bp)

@bp.route('/import-project')
def import_data():
    src = config.BASEDIR / 'core' / 'backup' / 'data.json'
    with open(src, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i, row in enumerate(data):
        ctx_data = {k : v for k, v in row.items() if k != 'technologies' and not k.startswith('activi') and k != 'function' and k != 'id' and k != 'images'}
        ctx_data['activities_id'] = Activity.query.filter(Activity.name==row['activity_name']).first().id
        ctx_data['functions_id'] = Function.query.filter(Function.name==row['function']).first().id
        instance = Project(**ctx_data)
        db.session.add(instance)
        db.session.commit()
        db.session.refresh(instance)
        for tech in row['technologies']:
            print(Technology.query.filter(Technology.name==tech).first().id)
            instance_tech = ProjectTechnology(projects_id=instance.id, technologies_id=Technology.query.filter(Technology.name==tech).first().id)
            db.session.add(instance_tech)
            db.session.commit()
            db.session.refresh(instance_tech)

                # print(instance)
            # pprint(row, indent=2)
            # pprint(ctx_data, indent=2)
    return 'ok'
