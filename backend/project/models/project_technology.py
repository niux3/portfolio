from backend import db
from backend.core.libs.serializer_mixin import SerializerMixin


class ProjectTechnology(db.Model, SerializerMixin):
    __tablename__ = 'project_projects_technologies'

    id = db.Column(db.Integer, primary_key=True)
    technologies_id = db.Column(db.Integer, db.ForeignKey('project_technologies.id', onupdate='CASCADE', ondelete='CASCADE'))
    projects_id = db.Column(db.Integer, db.ForeignKey('project_projects.id', onupdate='CASCADE', ondelete='CASCADE'))

    project = db.relationship("Project", back_populates="project_technologies")
    technology = db.relationship("Technology", back_populates="project_technologies")

    def __str__(self):
        return self.id

    def __repr__(self):
        return "<ProjectTechnology %r %r %r>" % (self.id, self.technologies_id, self.projects_id)
