import os

DEBUG = True

SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:150556@localhost:3306/flask_second?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
