from os import path
base_dir = path.abspath(path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(base_dir, '..', 'webapp.db')

SECRET_KEY = 'gu296hu8FDFYP224qwo439mlkj3l4HIH' # len() = 32