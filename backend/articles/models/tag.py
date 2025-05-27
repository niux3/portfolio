from slugify import slugify
from backend import db


class Tag(db.Model):
    __tablename__ = 'articles_tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    slug = db.Column(db.String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.name:
            self.slug = slugify(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Tag %r>" % self.slug
