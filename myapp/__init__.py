from flask import request, Blueprint
from flask_restplus import Api

from myapp.main.cats.cats_controller import cats_api
from myapp.main.core.logger_util import MyLogger
from myapp.main.dogs.dogs_controller import dogs_api

zoo_blueprint = Blueprint('Zoo Blue Print', __name__, url_prefix='/api/zoo')
# zoo_blueprint = Blueprint('Zoo Blue Print', __name__)

api = Api(zoo_blueprint,
          title='Zoo API',
          version='1.0',
          description='Zoo API description',

          )

api.add_namespace(cats_api)
api.add_namespace(dogs_api)


def log_request(sender, **extra):
    """
    logs each api request
    :param sender:  flask myapp
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
    :param sender: flask myapp
    :param response: response object
    :param extra: any additional params if needed
    :return: None
    """
    response_text = response.get_data(as_text=True)
    if not ('swagger' in response_text):
        sender.logger.info("Returning following response\n")
        sender.logger.info(response_text)
