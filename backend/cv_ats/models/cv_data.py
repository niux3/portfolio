from datetime import datetime
from backend.core.libs.serializer_mixin import SerializerMixin
from backend import db


class CvData(db.Model, SerializerMixin):
    __tablename__ = 'cv_data'
    id = db.Column(db.Integer, primary_key=True)
    json_data = db.Column(db.Text, nullable=False)  # Le JSON brut
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )

    def __str__(self):
        return self.id

    def __repr__(self):
        return "<CvData %r>" % self.id