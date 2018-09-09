# project/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    SECRET_KEY = 'socialmetric'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://www:[pass]@/socialmetric?host=localhost'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
