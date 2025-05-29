import subprocess
import json
import pathlib
from pprint import pprint
from datetime import datetime
from sqlalchemy import desc
from flask import render_template, Blueprint, jsonify, url_for, redirect, flash
from backend.core.config import config
from backend.articles.models import Post, PostTag, Tag, Status
from backend import db


bp = Blueprint('backup_articles', __name__, url_prefix='/sauvegarde')
file_data = config.BASEDIR / 'core' / 'backup' / 'data-posts.json'

@bp.route('/articles-export-json.html')
def export_json():
    output = {
        'post': [r.to_dict() for r in Post.query.all()],
        'tag': [r.to_dict() for r in Tag.query.all()],
        'posttag': [r.to_dict() for r in PostTag.query.all()],
        'status': [r.to_dict() for r in Status.query.all()],
    }

    with open(str(file_data), 'w', encoding='utf-8') as f:
        f.write(json.dumps(output, indent=2))
    flash("Votre export en json est réussi", "success")
    return redirect(url_for('projects.index'))

@bp.route('/articles-import-json.html')
def import_json():
    with open(str(file_data), 'r', encoding='utf-8') as f:
        data = json.load(f)
    post = [Post.from_dict(item) for item in data['post']]
    tag = [Tag.from_dict(item) for item in data['tag']]
    posttag = [PostTag.from_dict(item) for item in data['posttag']]
    status = [Status.from_dict(item) for item in data['status']]

    db.session.add_all(post + tag + posttag + status)
    db.session.commit()
    flash("Votre import en json est réussi", "success")
    return redirect(url_for('projects.index'))
