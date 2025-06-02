import os
from backend.core.config.base_config import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = os.getenv('FLASK_DEBUG')
    # postgresql://scott:tiger@localhost/project
    # SQLALCHEMY_DATABASE_URI = f"{os.getenv('DB_DRIVER')}{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_DATABASE_URI = f"{os.getenv('DB_DRIVER')}/core/backup/{os.getenv('DB_NAME')}.db"
