from urllib.parse import quote
from flask import render_template, Blueprint, flash, redirect, url_for
from sqlalchemy import desc
from sqlalchemy.orm import aliased
from markdown import markdown
from backend.core.config import config
from backend.core.libs.base_views import BaseView
from backend.articles.models import Post, Status, Tag, PostTag
from backend.articles.forms import PostForm
from backend import db


prefix_bp = 'posts'
bp = Blueprint(prefix_bp, __name__, url_prefix='/articles')

@bp.route('/<slug>-<id>.html')
def show(id, slug, export=None):
    obj = Post.query.get_or_404(id)
    obj.body = markdown(obj.body, extensions=['extra'])

    querystring_title = quote(obj.title)
    querystring_site = 'http://rb-webstudio.go.yj.fr'
    url = url_for(f'{prefix_bp}.show', id=obj.id, slug=obj.slug)
    querystring_url = quote(f'{querystring_site}{url}')

    ctx = {
        'object': obj,
        'shares': {
            'linkedin' : {
                'url' : f'https://www.linkedin.com/shareArticle?mini=true&url={querystring_url}&title={querystring_title}&source={quote(querystring_site)}',
                'icon' : 'fa-brands fa-linkedin',
            },
            'twitter': {
                'url': f'https://twitter.com/intent/tweet?url={querystring_url}&text={querystring_title}',
                'icon': 'fa-brands fa-square-x-twitter',
            },
            'facebook': {
                'url': f'https://www.facebook.com/sharer/sharer.php?u={querystring_url}',
                'icon': 'fa-brands fa-square-facebook',
            },
        }
    }
    if export is not None:
        ctx.update(export)
    return render_template('articles/show.html', **ctx)

@bp.route('/backoffice/index.html')
def index():
    fields = {
        'slug' : 'slug',
        'status' : 'status',
    }
    return BaseView.index(Post.query.order_by(desc('created')).all(), prefix_bp, fields, "un article")

@bp.route('/backoffice/ajouter.html', methods=['GET', 'POST'])
def add():
    form = PostForm()
    if form.validate_on_submit():
        post = Post()
        form.populate_obj(post)
        post.generate_slug()
        post.tags = form.tags.data
        db.session.add(post)
        db.session.commit()
        db.session.refresh(post)
        flash("Votre item a bien été ajouté", "success")
        return redirect(url_for(f'{prefix_bp}.edit', id=post.id))
    ctx = {
        'form': form
    }
    return render_template('articles/edit.html', **ctx)

@bp.route('/backoffice/<int:id>-supprimer.html')
def destroy(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    flash("Votre item a bien été supprimé", "success")
    return redirect(url_for(f'{prefix_bp}.index'))

@bp.route('/backofficee/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    post = Post.query.get(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        post.generate_slug()
        db.session.add(post)
        db.session.commit()
        flash("Votre item a bien été modifié", "success")
        return redirect(url_for(f'{prefix_bp}.edit', id=post.id))
    ctx = {
        'form': form,
        'object': post
    }
    return render_template('articles/edit.html', **ctx)

@bp.route('/index.html')
def index_articles(export=None):
    ctx = {
        'title': "Articles techniques - RB webstudio",
        'meta_description': "Découvrez nos articles récents sur le développement web, Python, JavaScript, frameworks modernes et bonnes pratiques techniques.",
        'h1': "Derniers articles & tutoriels de développement web",
        'object_list': Post.query.join(Status, Post.status_id == Status.id).filter(Status.name == 'online').order_by(desc(Post.created)).all()
    }
    if export is not None:
        ctx.update(export)
    return render_template('articles/index.html', **ctx)

@bp.route('/chercher-articles-par-<slug>.html')
def index_by_tags(slug, export=None):
    tag = Tag.query.filter(Tag.slug==slug).first()
    post_tag_alias = aliased(PostTag)
    posts = db.session.query(Post)\
        .join(post_tag_alias, Post.id == post_tag_alias.posts_id)\
        .join(Status, Post.status_id == Status.id)\
        .filter(post_tag_alias.tags_id == tag.id, Status.name == 'online')\
        .order_by(desc(Post.updated)).all()

    ctx = {
        'title': f"Chercher les articles par {tag.name} - RB webstudio",
        'meta_description': f"Découvrez nos articles sur {tag.name}",
        'h1': f"Chercher des articles avec le tag : {tag.name}",
        'object_list': posts
    }
    if export is not None:
        ctx.update(export)
    return render_template('articles/index.html', **ctx)
