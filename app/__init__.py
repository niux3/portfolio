from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['default'])
    config['default'].init_app(app)

    db.init_app(app)
    migrate = Migrate()

    from app.portfolio.models import Function, Portfolio
    from app.images.models import Image, Category
    migrate.init_app(app, db)

    from app.portfolio import views as portfolio_views
    app.register_blueprint(portfolio_views.bp)

    from app.images import views as images_views
    app.register_blueprint(images_views.bp)

    from app.export import views as export_views
    app.register_blueprint(export_views.bp)

    return app
