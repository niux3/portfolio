import json
from pprint import pprint
from flask import Blueprint, url_for, redirect, flash
from backend.core.config import config
from backend.project.models import Project
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
    cv_data = CvData.query.first()
    basics = json.loads(cv_data.json_data) if cv_data else {}
    works_list = []
    for work in CvWork.query.order_by(CvWork.year_end.desc()).all():
        projects = Project.query.filter_by(
            customers_id=work.customers_id
        ).all()
        techs = set()
        for p in projects:
            for t in p.technologies:
                if t.online == 1:
                    techs.add(t.name)
        works_list.append({
            "company": work.customer.name,
            "position": work.position.name if work.position else None,
            "location": work.location,
            "startDate": str(work.year_start) if work.year_start else None,
            "endDate": str(work.year_end),
            "summary": work.summary,
            "highlights": [h.strip() for h in work.description.strip('- ').split('\n- ') if h.strip()],
            "technologies": sorted(techs) if work.customer.name != 'Eluv/IB Cegos' else ['JavaScript', 'Python', 'Svelte/SvelteKit'],
            "contract_type": work.contract_type.name if work.contract_type else None,
            "projects": [{"name": p.name, "url": p.url} for p in projects]
        })
    output = basics
    output["work"] = works_list
    with open(str(file_cv_api), 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    return True


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
    if export_cv_ats_frontend() and export_cv_ats_data_backend():
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
