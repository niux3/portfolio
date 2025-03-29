from backend import db


class Function(db.Model):
    __tablename__ = 'portfolio_functions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Function %r>" % self.name
