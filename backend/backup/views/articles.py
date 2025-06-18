import subprocess
import json
import pathlib
from urllib.parse import quote
from pprint import pprint
from datetime import datetime
from markdown import markdown
from sqlalchemy import desc
from flask import render_template, Blueprint, jsonify, url_for, redirect, flash
from backend.core.config import config
from backend.articles.views.post import prefix_bp, show, index_articles, index_by_tags
from backend.articles.models import Post, PostTag, Tag, Status, Category
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
        'category': [r.to_dict() for r in Category.query.all()],
    }

    with open(str(file_data), 'w', encoding='utf-8') as f:
        f.write(json.dumps(output, indent=2))
    flash("Votre export en json est réussi", "success")
    return redirect(url_for('posts.index'))

@bp.route('/articles-import-json.html')
def import_json():
    with open(str(file_data), 'r', encoding='utf-8') as f:
        data = json.load(f)
    post = [Post.from_dict(item) for item in data['post']]
    tag = [Tag.from_dict(item) for item in data['tag']]
    posttag = [PostTag.from_dict(item) for item in data['posttag']]
    status = [Status.from_dict(item) for item in data['status']]
    category = [Category.from_dict(item) for item in data['category']]

    db.session.add_all(post + tag + posttag + status + category)
    db.session.commit()
    flash("Votre import en json est réussi", "success")
    return redirect(url_for('projects.index'))


@bp.route('/articles-export-html')
def export_html():
    public_folder = config.BASEDIR.parent / 'public'
    path_manifest = public_folder / '.vite' / 'manifest.json'

    with open(str(path_manifest), encoding='utf-8') as f:
        manifest_data = json.load(f)
    items = []
    data_for_frontend = {
        "layout_template": "base_export.html",
        "js_file": manifest_data.get('frontend/js/main.js').get('file'),
        "css_file": manifest_data.get('frontend/scss/index.scss').get('file'),
    }
    for obj in Post.query.all():
        items.append({
            "url": url_for(f'{prefix_bp}.show', id=obj.id, slug=obj.slug),
            'content': show(obj.id, obj.slug, export=data_for_frontend)
        })
    items.append({
        "url": url_for('posts.index_articles'),
        "content": index_articles(export=data_for_frontend)
    })
    for tag in Tag.query.all():
        items.append({
            "url": url_for('posts.index_by_tags', slug=tag.slug),
            "content": index_by_tags(tag.slug, export=data_for_frontend)
        })
    for item in items:
        url = item.get('url')[item.get('url').rfind('/') + 1:]
        with open(str(public_folder / 'articles' / url), 'w', encoding='utf-8') as f:
            f.write(item.get('content'))
    flash("Votre export en html est réussi", "success")
    return redirect(url_for('posts.index'))
