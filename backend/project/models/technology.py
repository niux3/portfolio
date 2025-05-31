from backend import db
from backend.core.libs.serializer_mixin import SerializerMixin


class Technology(db.Model, SerializerMixin):
    __tablename__ = 'project_technologies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    online = db.Column(db.SmallInteger, default=1, nullable=True)

    project_technologies = db.relationship(
        "ProjectTechnology",
        back_populates="technology",
        overlaps="projects,technology"  # Ajout explicite des overlaps
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Technology %r>" % self.name
