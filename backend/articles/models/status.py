from slugify import slugify
from backend import db


class Status(db.Model):
    __tablename__ = 'articles_status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    posts = db.relationship('Post', backref='status', lazy=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Status %r>" % self.name
