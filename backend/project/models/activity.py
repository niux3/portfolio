from backend import db
from backend.core.libs.serializer_mixin import SerializerMixin
from sqlalchemy.orm import relationship, backref


class Activity(db.Model, SerializerMixin):
    __tablename__ = 'project_activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    icon = db.Column(db.Text, nullable=True)

    activities = relationship('Project', backref=backref('activities'))

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Activity %r>" % self.name
