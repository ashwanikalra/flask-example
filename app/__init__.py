from flask import Flask, request
from flask import request_finished
from flask import request_started

from app.core.logger_util import MyLogger
from app.zoo import api, zoo_blueprint
from config import config_by_name


def log_request(sender, **extra):
    """
    logs each api request
    :param sender:  flask app
    :param extra: any other additional prams
    :return: None
    """
    # sender.logger.debug('Request context is set up')
    if request.method == 'POST' and \
            request.path.startswith('/api/zoo/cats') \
            and (not request.path.endswith('.json')):
        sender.logger.info("Following JSON request posted\n")
        sender.logger.info(request.get_json())


def log_response(sender, response, **extra):
    """
    logs each api response
    :param sender: flask app
    :param response: response object
    :param extra: any additional params if needed
    :return: None
    """
    response_text = response.get_data(as_text=True)
    if not ('swagger' in response_text):
        sender.logger.info("Returning following response\n")
        sender.logger.info(response_text)


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

    flask_app.register_blueprint(zoo_blueprint)
    request_started.connect(log_request, flask_app)
    request_finished.connect(log_response, flask_app)

    return flask_app
