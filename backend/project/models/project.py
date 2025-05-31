from datetime import datetime
from backend import db
from backend.core.libs.serializer_mixin import SerializerMixin
from backend.project.models.function import Function


class Project(db.Model, SerializerMixin):
    __tablename__ = 'project_projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(128))
    description = db.Column(db.Text)
    color = db.Column(db.String(8), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    online = db.Column(db.SmallInteger, default=1)
    url = db.Column(db.String(256), nullable=False)
    functions_id = db.Column(db.Integer, db.ForeignKey('project_functions.id', onupdate='CASCADE', ondelete='CASCADE'))
    function = db.relationship("Function", backref="projects")
    sort = db.Column(db.Integer, nullable=True)
    year = db.Column(db.String(16), nullable=True)
    activities_id = db.Column(db.Integer, db.ForeignKey('project_activities.id', onupdate='CASCADE', ondelete='CASCADE'))
    activity = db.relationship("Activity", back_populates="projects")
    customer = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)

    project_technologies = db.relationship(
        "ProjectTechnology",
        back_populates="project",
        overlaps="technologies,project_technologies"
    )

    technologies = db.relationship(
        'Technology',
        secondary='project_projects_technologies',
        backref=db.backref('projects', lazy='dynamic'),
        viewonly=True  # Solution clé : marque cette relation comme lecture seule
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Project %r>" % self.name

    @property
    def functions(self):
        return Function.query.get_or_404(self.functions_id)
