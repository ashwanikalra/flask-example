from flask_script import Manager

from myapp import zoo_blueprint
from myapp.main import create_app

_flask_app = create_app('dev')
_flask_app.register_blueprint(zoo_blueprint)
# global cache object

manager = Manager(_flask_app)


@manager.command
def run():
    """ This will execute the application """
    _flask_app.run(host='localhost', port=5000)


if __name__ == '__main__':
    manager.run()
