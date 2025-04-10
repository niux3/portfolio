from flask import render_template, request, redirect, url_for, flash
from slugify import slugify
from backend import db


class BaseView:
    @staticmethod
    def index(obj, prefix_bp, fields, category="un item", add_filter_button=False):
        ctx = {action: f'{prefix_bp}.{action}' for action in ['add', 'edit', 'destroy']}
        if add_filter_button:
            ctx['url_filter_add'] = f'{prefix_bp}.filter_add'
        ctx['object_list'] = obj.query.all()
        ctx['category'] = category
        ctx['fields'] = fields
        return render_template('project/index.html', **ctx)

    @staticmethod
    def add(objForm, obj, prefix_bp):
        form = objForm()
        if form.validate_on_submit() and request.method == "POST":
            cleared_data = {k:v for k, v in form.data.items() if k != 'csrf_token'}
            if 'online' in cleared_data.keys():
                cleared_data['online'] = 1 if cleared_data['online'] == True else 0
            instance = obj(**cleared_data)
            db.session.add(instance)
            db.session.commit()
            db.session.refresh(instance)
            flash("Votre item a bien été ajouté", "success")
            return redirect(url_for(f'{prefix_bp}.index'))
        ctx = {
            'form': form
        }
        return render_template('project/edit.html', **ctx)

    @staticmethod
    def destroy(id, obj, prefix_bp):
        instance = obj.query.get_or_404(id)
        db.session.delete(instance)
        db.session.commit()
        flash("Votre item a bien été supprimé", "success")
        return redirect(url_for(f'{prefix_bp}.index'))

    @staticmethod
    def edit(id, obj, objForm, prefix_bp):
        instance = obj.query.get_or_404(id)
        form = objForm(obj=instance)
        if form.validate_on_submit() and request.method == "POST":
            print(form.data['online'])
            form.populate_obj(instance)
            if 'online' in form.data.keys():
                instance.online = 1 if form.data['online'] == True else 0
            slug_data = form.name.data
            instance.slug = slugify(slug_data)
            db.session.add(instance)
            db.session.commit()
            db.session.refresh(instance)
            flash("Votre item a bien été modifié", "success")
            return redirect(url_for(f'{prefix_bp}.index'))
        ctx = {
            'form': form
        }
        return render_template('project/edit.html', **ctx)
