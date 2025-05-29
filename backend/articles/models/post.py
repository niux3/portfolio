from datetime import datetime
from slugify import slugify
from backend.articles.models import PostTag
from backend.core.libs.serializer_mixin import SerializerMixin
from backend import db


class Post(db.Model, SerializerMixin):
    __tablename__ = 'articles_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    status_id = db.Column(db.Integer, db.ForeignKey('articles_status.id', onupdate='CASCADE', ondelete='CASCADE'))

    post_tags = db.relationship('PostTag', back_populates='post', cascade="all, delete-orphan")

    @property
    def tags(self):
        return [pt.tag for pt in self.post_tags]

    @tags.setter
    def tags(self, tags_list):
        self.post_tags = [PostTag(tag=tag) for tag in tags_list]

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        self.slug = ''
        if self.title:
            self.slug = slugify(self.title)

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<Post %r>" % self.slug
