import os
import importlib
import inspect
from pathlib import Path
import humps
from dotenv import load_dotenv


load_dotenv()

class BaseConfig:
    FLASK_APP = os.getenv('FLASK_APP')
    SECRET_KEY = os.getenv('SECRET')
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = os.getenv('MAIL_PORT', 587)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_LOGIN = os.getenv('MAIL_LOGIN')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASEDIR = Path(__file__).resolve().parent.parent.parent
    TEMPLATES_EMAIL = os.getenv('TEMPLATES_EMAIL')
    STATIC = os.getenv('STATIC')
    TEMPLATES = os.getenv('TEMPLATES')
    MIGRATIONS = os.getenv('MIGRATIONS')

    @staticmethod
    def init_app(app):
        print(f">> config {os.getenv('FLASK_ENV')} loaded!")
