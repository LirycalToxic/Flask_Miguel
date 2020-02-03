import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'wLj5CIg15s2V11OsUkbF'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False