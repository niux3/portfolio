from app import db
from slugify import slugify
from datetime import datetime


class Function(db.Model):
    __tablename__ = 'functions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Function %r>" % self.name


portfolio_technology = db.Table(
    'portfolios_technologies',

    db.Column('id', db.Integer, primary_key=True),
    db.Column('technologies_id', db.Integer, db.ForeignKey('technologies.id')),
    db.Column('portfolios_id', db.Integer, db.ForeignKey('portfolios.id'))
)


class Technology(db.Model):
    __tablename__ = 'technologies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Technology %r>" % self.name


class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(128))
    description = db.Column(db.Text)
    color = db.Column(db.String(8), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    online = db.Column(db.SmallInteger, default=1)
    url = db.Column(db.String(256), nullable=False)
    functions_id = db.Column(db.Integer, db.ForeignKey('functions.id'))
    technologies = db.relationship("Technology", secondary=portfolio_technology, backref=db.backref('portfolios', lazy="dynamic"))

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Portfolio %r>" % self.name