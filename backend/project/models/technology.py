from backend import db


class Technology(db.Model):
    __tablename__ = 'project_technologies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    online = db.Column(db.SmallInteger, default=1, nullable=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Technology %r>" % self.name
