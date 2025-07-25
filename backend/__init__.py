import humps
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from backend.core.libs.filters import format_date_fr, random_delay_transition
from backend.core.config import config
from backend.core.libs.autoload import Autoload
from backend.core.context_processors import (
    inject_footer_flag,
    inject_canonical_url,
    inject_og_image
)


db = SQLAlchemy()


def create_app():
    app = Flask(
        __name__,
        static_folder=config.STATIC,
        template_folder=config.TEMPLATES
    )
    app.config.from_object(config)
    config.init_app(app)


    CORS(app)

    migrate = Migrate()

    db.init_app(app)
    migrate.init_app(app, db)

    Autoload.import_models()
    migrate.init_app(app, db, directory=config.BASEDIR / config.MIGRATIONS)

    Autoload.import_views(app)
    # Autoload.import_errors(app)

    # from app.auth import views as auth_views
    # app.register_blueprint(auth_views.bp, url_prefix='/auth')
    #context processor
    app.context_processor(inject_footer_flag())
    app.context_processor(inject_canonical_url())
    app.context_processor(inject_og_image())
    # filters
    app.jinja_env.filters['date_fr'] = format_date_fr
    app.jinja_env.filters['random_delay'] = random_delay_transition

    return app
