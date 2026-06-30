from backend.core.libs.serializer_mixin import SerializerMixin
from backend import db


class CvPosition(db.Model, SerializerMixin):
    __tablename__ = 'cv_positions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)

    def __str__(self):
        return self.name
