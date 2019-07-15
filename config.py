""" Configuration file """
import os

basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Logger path
LOG_PATH = os.path.join(basedir, 'dev.log')


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    """ DevelopmentConfig class """

    DEBUG = True


config_by_name = dict(

    dev=DevelopmentConfig
)
