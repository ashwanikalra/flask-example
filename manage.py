from flask_script import Manager
from app import create_app

app = create_app('dev')

manager = Manager(app)


@manager.command
def run():
    """ This will execute the application """
    app.run(host='localhost', port=5000)


if __name__ == '__main__':
    manager.run()
