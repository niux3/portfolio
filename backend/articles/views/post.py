from flask import render_template, Blueprint, flash, redirect, url_for
from markdown import markdown
from backend.core.config import config
from backend.core.libs.base_views import BaseView
from backend.articles.models import Post
from backend.articles.forms import PostForm
from backend import db


prefix_bp = 'posts'
bp = Blueprint(prefix_bp, __name__, url_prefix='/articles')

@bp.route('/voir.html')
def show():
    obj = Post.query.get_or_404(1)
    obj.body = markdown(obj.body, extensions=['extra'])
    ctx = {
        'object': obj,
        'shares': {
            'linkedin' : {
                'url' : 'https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Ftonsite.com%2Fton-article&title=Le%20titre%20de%20ton%20article&summary=Un%20petit%20résumé&source=tonsite.com',
                'icon' : 'fa-brands fa-linkedin',
            },
            'twitter': {
                'url': 'https://twitter.com/intent/tweet?url=https%3A%2F%2Ftonsite.com%2Fton-article&text=Découvre%20cet%20article%20intéressant',
                'icon': 'fa-brands fa-square-x-twitter',
            },
            'facebook': {
                'url': 'https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Ftonsite.com%2Fton-article',
                'icon': 'fa-brands fa-square-facebook',
            },
        }
    }
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
