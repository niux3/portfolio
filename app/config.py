import os

basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)

class Config(object):
    SECRET_KEY = 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = '587'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = "administrator"
    MAIL_PASSWORD = "p@ssw0rd"
    MYBLOG_MAIL_SUBJECT_PREFIX = '[myblog]'
    MYBLOG_MAIL_SENDER = '<admin@example.com>'
    MYBLOG_ADMIN = "admin"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'img')

    @staticmethod
    def init_app(app):
        print('config loaded')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data", "data-dev.db")}'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data", "data.db")}'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}