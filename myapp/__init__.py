from flask import Blueprint
from flask_restplus import Api

from myapp.main.cats.cats_controller import cats_api, cats_cached_api
from myapp.main.core.logger_util import MyLogger
from myapp.main.dogs.dogs_controller import dogs_api

zoo_blueprint = Blueprint('Zoo Blue Print', __name__, url_prefix='/api/zoo')

api = Api(zoo_blueprint,
          title='Zoo API',
          version='1.0',
          description='Zoo API description',

          )

api.add_namespace(cats_api)
api.add_namespace(cats_cached_api)
api.add_namespace(dogs_api)
