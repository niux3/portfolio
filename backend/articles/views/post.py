from pprint import pprint
from urllib.parse import quote
from flask import render_template, Blueprint, flash, redirect, url_for
from markdown import markdown
from backend.core.config import config
from backend.core.libs.base_views import BaseView
from backend.articles.models import Post
from backend.articles.forms import PostForm
from backend import db


prefix_bp = 'posts'
bp = Blueprint(prefix_bp, __name__, url_prefix='/articles')

@bp.route('/<id>-<slug>.html')
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

@bp.route('/index.html')
def index():
    fields = {
        'slug' : 'slug',
        'status' : 'status',
    }
    return BaseView.index(Post, prefix_bp, fields, "un article")

@bp.route('/ajouter.html', methods=['GET', 'POST'])
def add():
    form = PostForm()
    if form.validate_on_submit():
        post = Post()
        form.populate_obj(post)
        post.generate_slug()
        post.tags = form.tags.data
        db.session.add(post)
        db.session.commit()
        flash("Votre item a bien été ajouté", "success")
        return redirect(url_for(f'{prefix_bp}.index'))
    ctx = {
        'form': form
    }
    return render_template('articles/edit.html', **ctx)

@bp.route('/<int:id>-supprimer.html')
def destroy(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    flash("Votre item a bien été supprimé", "success")
    return redirect(url_for(f'{prefix_bp}.index'))

@bp.route('/<int:id>-editer.html', methods=['GET', 'POST'])
def edit(id):
    post = Post.query.get(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        post.generate_slug()
        db.session.add(post)
        db.session.commit()
        flash("Votre item a bien été modifié", "success")
        return redirect(url_for(f'{prefix_bp}.index'))
    ctx = {
        'form': form
    }
    return render_template('articles/edit.html', **ctx)
