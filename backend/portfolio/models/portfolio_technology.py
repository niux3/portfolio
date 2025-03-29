from backend import db


class PortfolioTechnology(db.Model):
    __tablename__ = 'portfolio_portfolios_technologies'

    id = db.Column(db.Integer, primary_key=True)
    technologies_id = db.Column(db.Integer, db.ForeignKey('portfolio_technologies.id', onupdate='CASCADE', ondelete='CASCADE'))
    portfolios_id = db.Column(db.Integer, db.ForeignKey('portfolio_portfolios.id', onupdate='CASCADE', ondelete='CASCADE'))

    def __str__(self):
        return self.id

    def __repr__(self):
        return "<PortfolioTechnology %r %r %r>" % ( self.id, self.technologies_id, self.portfolios_id )
