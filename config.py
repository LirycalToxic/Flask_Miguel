import os


SECRET_KEY = os.environ.get('SECRET_KEY') or 'wLj5CIg15s2V11OsUkbF'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
# 'mysql://root:1234@localhost/zpmerch'
# or 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or "xaccaope2@gmail.com"
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or "naruto12345654321"
ADMINS = ['xaccaope2@gmail.com']
POST_PER_PAGE = 10
MS_TRANSLATOR_KEY = '1018c4be87ad442eb5292625969f5ef6'
# 'trnsl.1.1.20200304T213148Z.31e74c48a6aacecf.bac1520af57fc54a56f88938197108fd65dee1c7'

LANGUAGES = ['en', 'es', 'ru']
# ELASTICSEARCH_URL = None
ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
# or 'http://167.99.206.94:9200'
