from flask import render_template, Blueprint
from backend.project.models import Project, Technology


bp = Blueprint('pages', __name__)

@bp.route('/')
def index():
    ctx = {
        "object_list": {
            "projects": Project.query.all(),
            "technologies": Technology.query.all()
        }
    }
    return render_template('pages/index.html', **ctx)
