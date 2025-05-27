from sqlalchemy import desc
from flask import render_template, Blueprint
from backend.project.models import Project, Technology


prefix_bp = 'pages'
bp = Blueprint(prefix_bp, __name__)

@bp.route('/index.html')
def index():
    ctx = {
        "object_list": {
            "projects": Project.query.filter(Project.online == 1).order_by(desc('year')),
            "technologies": Technology.query.filter(Technology.online == 1).all()
        }
    }
    return render_template('pages/index.html', **ctx)
