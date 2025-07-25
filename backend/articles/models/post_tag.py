from backend import db
from backend.core.libs.serializer_mixin import SerializerMixin


class PostTag(db.Model, SerializerMixin):
    __tablename__ = 'articles_posts_tags'

    id = db.Column(db.Integer, primary_key=True)
    posts_id = db.Column(db.Integer, db.ForeignKey('articles_posts.id', onupdate='CASCADE', ondelete='CASCADE'))
    tags_id = db.Column(db.Integer, db.ForeignKey('articles_tags.id', onupdate='CASCADE', ondelete='CASCADE'))

    post = db.relationship('Post', back_populates='post_tags')
    tag = db.relationship('Tag', back_populates='post_tags')

    def __str__(self):
        return self.id

    def __repr__(self):
        return "<PostTag %r %r %r>" % (self.id, self.posts_id, self.tags_id)
