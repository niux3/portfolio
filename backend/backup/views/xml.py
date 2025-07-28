from datetime import datetime
from flask import current_app, Blueprint, flash, redirect, url_for, render_template
from sqlalchemy import desc
from backend.core.config import config
from backend.articles.models import Post, Status, Tag


bp = Blueprint('backup_xml', __name__, url_prefix='/sauvegarde')
public_folder = config.BASEDIR.parent / 'public'


def get_sitemap():
    today = datetime.utcnow().date().isoformat()
    excludes_route = [
        'static',
        'backoffice',
        'sauvegarde'
    ]
    priorities = {
        'projects.index' : 1,
        'posts.index_articles': 0.9,
        'posts.index_by_tags': 0.8,
        'posts.show': 0.7
    }
    rows = []
    for rule in current_app.url_map.iter_rules():
        is_static_page = "GET" in rule.methods
        is_excluded = any(exclu in rule.rule for exclu in excludes_route)
        is_not_index_html = rule.rule != "/index.html"

        posts = Post.query.join(Status, Post.status_id == Status.id).filter(Status.name == 'online').order_by(desc(Post.created)).all()
        tags = Tag.query.all()

        if is_static_page and not is_excluded and is_not_index_html:
            if 'posts.show' == rule.endpoint:
                for post in posts:
                    rows.append({
                        'loc': f'{config.URL_PROJECT}{url_for(rule.endpoint, id=post.id, slug=post.slug)}',
                        'lastmod': today,
                        'changefreq': 'weekly',
                        'priority': priorities[rule.endpoint]
                    })
            elif 'posts.index_by_tags' == rule.endpoint:
                for tag in tags:
                    rows.append({
                        'loc': f'{config.URL_PROJECT}{url_for(rule.endpoint, slug=tag.slug)}',
                        'lastmod': today,
                        'changefreq': 'weekly',
                        'priority': priorities[rule.endpoint]
                    })
            else:
                rows.append({
                    'loc': f'{config.URL_PROJECT}{url_for(rule.endpoint)}',
                    'lastmod': today,
                    'changefreq': 'weekly',
                    'priority': priorities[rule.endpoint]
                })
    rows = list(sorted(rows, key=lambda r: r['priority'], reverse=True))
    sitemap_source = render_template('xml/sitemap.tpl', rows=rows)

    with open(str(public_folder / 'sitemap.xml'), mode='w', encoding='utf-8') as f:
        f.write(sitemap_source)


def get_rss():
    posts = Post.query.join(Status, Post.status_id == Status.id).filter(Status.name == 'online').order_by(desc(Post.created)).limit(20).all()
    for post in posts:
        post.url_article = f"{config.URL_PROJECT}{url_for('posts.show', id=post.id, slug=post.slug)}"
    ctx = {
        'object_list': posts,
        'today': datetime.utcnow().date().isoformat(),
        'title': "RB webstudio - spécialiste Python - Javascript/Typescript",
        'description': "RB webstudio - spécialiste Python - Javascript/Typescript",
        'url_site': config.URL_PROJECT
    }
    rss_source = render_template('xml/flux_rss.tpl', **ctx)
    with open(str(public_folder / 'rss.xml'), mode='w', encoding='utf-8') as f:
        f.write(rss_source)


@bp.route('/export-xml.html')
def export_xml():
    get_sitemap()
    get_rss()
    flash("Votre export xml est réussi", "success")
    return redirect(url_for('posts.index'))
