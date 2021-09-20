from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_blueprint import Blueprint
from app.config import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['default'])
    config['default'].init_app(app)

    db.init_app(app)
    migrate = Migrate()

    from app.portfolio.models import Function, Portfolio
    migrate.init_app(app, db)

    from app.portfolio import views as portfolio_views
    app.register_blueprint(portfolio_views.bp)

    return app
