from flask import Flask

from app.core.logger_util import MyLogger
from app.zoo import api, zoo_blueprint
from config import config_by_name


def create_app(config_name):
    """
    Creates the Flask Application object
    :param config_name: configuration name - dev, test etc
    :return: Flask object
    """
    flask_app = Flask(__name__)
    log_ = MyLogger()
    flask_app.config.from_object(config_by_name[config_name])
    flask_app.logger.setLevel(log_.info)
    flask_app.logger.addHandler(log_.logHandler)
    flask_app.register_blueprint(zoo_blueprint)

    return flask_app
