from app import db
from datetime import datetime


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(128), nullable=False)
    online = db.Column(db.SmallInteger, default=1)
    description = db.Column(db.Text)
    thumbnail = db.Column(db.SmallInteger, default=1)
    portfolios_id = db.Column(db.Integer, db.ForeignKey('functions.id'))
    created = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Image %r>" % self.name