from slugify import slugify
from backend.core.libs.serializer_mixin import SerializerMixin
from backend import db


class Category(db.Model, SerializerMixin):
    __tablename__ = 'articles_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    posts = db.relationship('Post', backref='category', lazy=True)

    def generate_slug(self):
        self.slug = ''
        if self.name:
            self.slug = slugify(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Category %r>" % self.slug
