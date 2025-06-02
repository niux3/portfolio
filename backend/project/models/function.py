from backend import db
from backend.core.libs.serializer_mixin import SerializerMixin


class Function(db.Model, SerializerMixin):
    __tablename__ = 'project_functions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Function %r>" % self.name
