import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'wLj5CIg15s2V11OsUkbF'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or "xaccaope2@gmail.com"
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or "naruto12345654321"
ADMINS = ['xaccaope2@gmail.com']
POST_PER_PAGE = 3

LANGUAGE = ['en', 'es', 'ru']