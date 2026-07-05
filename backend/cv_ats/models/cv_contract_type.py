from backend.core.libs.serializer_mixin import SerializerMixin
from backend import db


class CvContractType(db.Model, SerializerMixin):
    __tablename__ = 'cv_contracts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)

    def __str__(self):
        return self.name