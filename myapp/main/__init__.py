from flask import Flask
from flask_caching import Cache

from config import config_by_name
from myapp.main.core.logger_util import MyLogger

mycache = Cache()


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

    # this is for json formatted logging. Not working properly.
    # json_logging.ENABLE_JSON_LOGGING = True
    # json_logging.init_flask()
    # json_logging.init_request_instrument(flask_app)

    # flask_app.register_blueprint(zoo_blueprint)
    # request_started.connect(log_request, flask_app)
    # request_finished.connect(log_response, flask_app)

    mycache.init_app(flask_app)

    return flask_app
