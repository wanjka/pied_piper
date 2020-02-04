from flask import Flask, render_template, flash, redirect, url_for
from pyper.db import db
from pyper.track.views import bp as track_blueprint

# типа паттерн "фабрика"
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    # блюпринт всего один
    app.register_blueprint(track_blueprint)
    return app

if __name__ == '__main__':
    app.run(debug=True)
