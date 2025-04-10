from flask import render_template, Blueprint
from backend.project.models import Project, Technology


bp = Blueprint('pages', __name__)

@bp.route('/')
def index():
    ctx = {
        "object_list": {
            "projects": Project.query.filter(Project.online == 1).all(),
            "technologies": Technology.query.filter(Technology.online == 1).all()
        }
    }
    return render_template('pages/index.html', **ctx)
