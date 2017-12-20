import os
import inspect

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    ADMINS = ['']
    APPNAME = 'Flask-Boilerplate'
    SUPPORT_EMAIL = ''
    VERSION = '1.0.0'

    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET_KEY_ENV_VAR_NOT_SET'
        print('SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')

    HOST = 'localhost'
    PORT = int(os.environ.get('PORT', 5000))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_NATIVE_UNICODE = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    STATIC_FOLDER = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) + '/main/static'


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_POOL_RECYCLE = 240
    SQLALCHEMY_POOL_TIMEOUT = 60
    SQLALCHEMY_POOL_SIZE = 200
    SQLALCHEMY_MAX_OVERFLOW = 0
    DATABINDS = {}


class UnitTestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_POOL_RECYCLE = 240
    SQLALCHEMY_POOL_TIMEOUT = 60
    SQLALCHEMY_POOL_SIZE = 200
    SQLALCHEMY_MAX_OVERFLOW = 0
    DATABINDS = {}


class TestingConfig(Config):

    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_POOL_RECYCLE = 240
    SQLALCHEMY_POOL_TIMEOUT = 60
    SQLALCHEMY_POOL_SIZE = 200
    SQLALCHEMY_MAX_OVERFLOW = 0
    DATABINDS = {}


class ProductionConfig(Config):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_POOL_RECYCLE = 240
    SQLALCHEMY_POOL_TIMEOUT = 60
    SQLALCHEMY_POOL_SIZE = 200
    SQLALCHEMY_MAX_OVERFLOW = 0
    DATABINDS = {}


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'unittest': UnitTestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
