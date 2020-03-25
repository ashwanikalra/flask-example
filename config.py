""" Configuration file """
import os
import uuid

basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Logger path
LOG_PATH = os.path.join(basedir, 'dev.log')

APP_SECRET_KEY = uuid.uuid4().hex
DB_USER = os.getenv('mysql_username')
DB_PASS = os.getenv('mysql_password')
DB_HOST = os.getenv('mysql_host')
DB_NAME = os.getenv('mysql_db')

app_config_dict = {
    'SECRET_KEY': APP_SECRET_KEY,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}',
    'CACHE_TYPE': "simple",
    'CACHE_DEFAULT_TIMEOUT': 300,
    'DEBUG': True,
    'SQLALCHEMY_ENGINE_OPTIONS': {
        'max_overflow': 100,
        'pool_size': 50,
        'pool_pre_ping': True,
        'pool_recycle': 300
    }
}
