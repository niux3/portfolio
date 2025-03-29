from backend import db
from datetime import datetime
from backend.portfolio.models import PortfolioTechnology


class Portfolio(db.Model):
    __tablename__ = 'portfolio_portfolios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(128))
    description = db.Column(db.Text)
    color = db.Column(db.String(8), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    online = db.Column(db.SmallInteger, default=1)
    url = db.Column(db.String(256), nullable=False)
    functions_id = db.Column(db.Integer, db.ForeignKey('portfolio_functions.id', onupdate='CASCADE', ondelete='CASCADE'))
    technologies = db.relationship("Technology", secondary=PortfolioTechnology, backref=db.backref('portfolios', lazy="dynamic"))
    sort = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=True)
    activities_id = db.Column(db.Integer, db.ForeignKey('portfolio_activities.id', onupdate='CASCADE', ondelete='CASCADE'))
    customer = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)


    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Portfolio %r>" % self.name
