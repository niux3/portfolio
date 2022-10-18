from flask import Blueprint, redirect, url_for, flash
from app import db
from app.config import basedir
from app.portfolio.models import Technology, portfolio_technology
from app.images.models import Image, Category
import json
import os


bp = Blueprint('export', __name__)


@bp.route('/export-json')
def index():
    sql = """
        SELECT
            p.id as pid,
            p.name as pname,
            p.slug as pslug,
            p.description as pdescription,
            p.url as purl,
            p.color as pcolor,
            p.year as pyear,
            a.name as aname,
            a.icon as aicon,
            f.name as fname
        FROM
            portfolios as p,
            functions as f,
            activities as a
        WHERE
            f.id = p.functions_id
        AND 
            a.id = P.activities_id 
        AND
            p.online = 1
        ORDER BY
            p.sort
    """

    rows = db.session.execute(sql)
    output_rows = []
    output_css = []
    root = os.path.dirname(basedir)
    for row in rows:
        technologies = []
        images = []
        for trow in db.session.execute(portfolio_technology.join(Technology).select().where(portfolio_technology.c.portfolios_id == row.pid)):
            technologies.append(trow.name)
        for irow in Image.query.join(Category).filter(Image.portfolios_id == row.pid, Image.online == 1).all():
            print('>> ', irow.name, irow.url)
            images.append(irow.url)
            # images = {
            #     'thumbnail': "miniature",
            #     'logo': 'logo',
            #     'standard': list(range(0, 10))
            # }
        output = {
            'id': row.pid,
            'name': row.pname,
            'slug': row.pslug,
            'url': row.purl,
            'description': row.pdescription,
            'color': row.pcolor,
            'year': row.pyear,
            'activity_name': row.aname,
            'activity_icon': row.aicon,
            'function': row.fname,
            'technologies': technologies,
            'images': images
        }
        output_rows.append(output)

        # css
        tpl = f"""
.univers-{row.pslug}{{
    > header{{
        background-color: {row.pcolor};
    }}

    > .global nav a:hover{{
        background-color: {row.pcolor};
    }}
}}
        """
        output_css.append(tpl)

    with open(os.path.join(root, 'frontoffice', 'src', 'data.js'), "w") as file:
        file.write(f"const data  = {json.dumps(output_rows)}; export default data;")
    # with open(os.path.join(root, 'docs', 'scripts', 'template', 'front', 'scss', 'atoms', '_export-univers.scss'), "w") as file:
    #     file.write("\n".join(output_css))
    flash("export réussi", "success")
    return redirect(url_for('portfolio.index_portfolio'))
