
from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

from config import app_config_dict
from myapp.main.core.logger_util import MyLogger

mycache = Cache()
db = SQLAlchemy()


def create_app(config_name):
    """
    Creates the Flask Application object
    :param config_name: configuration name - dev, test etc
    :return: Flask object
    """
    flask_app = Flask(__name__)

    log_ = MyLogger()

    flask_app.config.update(app_config_dict)
    flask_app.logger.setLevel(log_.info)
    flask_app.logger.addHandler(log_.logHandler)
    # flask_app.register_blueprint(zoo_blueprint)
    # request_started.connect(log_request, flask_app)
    # request_finished.connect(log_response, flask_app)
    db.init_app(flask_app)
    mycache.init_app(flask_app)

    return flask_app
