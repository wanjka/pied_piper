from os import path
base_dir = path.abspath(path.dirname(__file__))

#currently using SQLite, may be changed in production
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(base_dir, '..', 'pyper.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'This string will be replaced in production'
