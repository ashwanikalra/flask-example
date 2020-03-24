""" Configuration file """
import os

basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Logger path
LOG_PATH = os.path.join(basedir, 'dev.log')


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    """ Configuration for Dev Environment """
    DEBUG = True

    # Flask-Caching related configs
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 300
    # get this from environment
    JWT_SECRET_KEY = '@#$%^@#$'


config_by_name = dict(
    dev=DevelopmentConfig
)
