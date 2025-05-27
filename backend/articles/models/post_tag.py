from backend import db


class PostTag(db.Model):
    __tablename__ = 'articles_posts_tags'

    id = db.Column(db.Integer, primary_key=True)
    posts_id = db.Column(db.Integer, db.ForeignKey('articles_posts.id', onupdate='CASCADE', ondelete='CASCADE'))
    tags_id = db.Column(db.Integer, db.ForeignKey('articles_tags.id', onupdate='CASCADE', ondelete='CASCADE'))

    post = db.relationship('Post', backref="post")
    tag = db.relationship('Tag', backref="tag")

    def __str__(self):
        return self.id

    def __repr__(self):
        return "<PostTag %r %r %r>" % (self.id, self.posts_id, self.tags_id)
