import json
from flask import Blueprint, url_for, redirect, flash
from backend.core.config import config
from backend.cv_ats.models import (
    CvContractType,
    CvData,
    CvPosition,
    CvWork
)
from backend import db


bp = Blueprint('backup_cv', __name__, url_prefix='/sauvegarde')
file_data = config.BASEDIR / 'core' / 'backup' / 'data-cv.json'
public_folder = config.BASEDIR.parent / 'public'
api_cv_folder = public_folder / 'api-cv'
file_cv_api = api_cv_folder / 'cv.json'


def export_cv_ats_frontend():
    print('> ok')
    return True
    # output = [{
    #     "id": r.id,
    #     "name": r.name,
    #     "slug": r.slug,
    #     "url": r.url,
    #     "description": r.description,
    #     "year": r.year,
    #     "activity_name": r.activity.name if r.activity else None,
    #     "activity_icon": r.activity.icon if r.activity else None,
    #     "position": r.function.name if r.function else None,
    #     "location": r.location,
    #     "customer": r.customer.name if r.customer else None,
    #     "technologies": [t.name for t in r.technologies]
    # } for r in Project.query.filter(Project.online == 1).all()]
    #
    # with open(str(file_data_public), 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(output, indent=2))
    # return True


def export_cv_ats_data_backend():
    output = {
        'contracts': [r.to_dict() for r in CvContractType.query.all()],
        'json_data': [r.to_dict() for r in CvData.query.all()],
        'positions': [r.to_dict() for r in CvPosition.query.all()],
        'works': [r.to_dict() for r in CvWork.query.all()],
    }

    with open(str(file_data), 'w', encoding='utf-8') as f:
        f.write(json.dumps(output, indent=2))
    return True


@bp.route('/cv-ats-export-json.html')
def export_json():
    if export_cv_ats_frontend():
        flash("Votre export en json est réussi", "success")
        return redirect(url_for('projects.index'))


@bp.route('/cv-ats-import-json.html')
def import_json():
    with open(str(file_data), 'r', encoding='utf-8') as f:
        data = json.load(f)
    contracts = [CvContractType.from_dict(item) for item in data['contracts']]
    json_data = [CvData.from_dict(item) for item in data['json_data']]
    positions = [CvPosition.from_dict(item) for item in data['positions']]
    works = [CvWork.from_dict(item) for item in data['works']]

    db.session.add_all(contracts + json_data + positions + works)
    db.session.commit()
    flash("Votre import en json est réussi", "success")
    return redirect(url_for('projects.index'))
