from app import db
from slugify import slugify
from datetime import datetime


class Function(db.Model):
    __tablename__ = 'functions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Function %r>" % self.title


class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(128))
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    online = db.Column(db.SmallInteger, default=1)
    functions_id = db.Column(db.Integer, db.ForeignKey('functions.id'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Portfolio %r>" % self.title

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)