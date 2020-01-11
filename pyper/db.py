from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(64), nullable=False)
    artist = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return '<Track {} -- {}>'.format(self.artist, self.title)
