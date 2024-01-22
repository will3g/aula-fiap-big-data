import os

from sqlalchemy import create_engine

MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_DC_HOSTNAME = os.environ.get('MYSQL_DC_HOSTNAME')

URL_CONNECT = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_DC_HOSTNAME}:3306/{MYSQL_DATABASE}'

MYSQL_CONNECTION = create_engine(URL_CONNECT)