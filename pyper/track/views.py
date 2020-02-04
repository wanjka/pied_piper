from flask import Blueprint, render_template, redirect, url_for, request
from pyper.db import db
from pyper.track.models import Track
from pyper.track.forms import MusicForm
import pyper.track._seargine as seargine

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from werkzeug import secure_filename

from music21 import converter

def parse_music_file(filename):
    pass

class UploadForm(FlaskForm):
    file = FileField()

bp = Blueprint('track', __name__, url_prefix='/')

@bp.route('/input-text')
def index():
    title = 'Пегий дудочник. Музыкальный антиплагиат'
    music_form = MusicForm()
    return render_template(
        'track/index.html',
        page_title=title,
        form=music_form
    )

@bp.route('/process_form', methods=['POST'])
def process_form():
    form = MusicForm()
    title = 'Результаты поиска'
    results = []
    try:
        results = seargine.get_overlaps(form.music.data)
        return render_template('track/results.html',
                #sample=form.music.data,
                page_title=title, response=results)
    except Exception as e:
        print(e)
        return 'You\'ve got error'

@bp.route('/', methods=['GET', 'POST'])
def process_file():
    form = UploadForm()
    title = 'Результаты поиска'
    if form.validate_on_submit():   # всё равно что method == 'POST'
# получить имя файла
        filename = secure_filename(form.file.data.filename)
# сохранить в папке uploads/
        music_file = 'uploads/' + filename
# приходится сохранить файл, чтобы иметь доступ к его содержимому
        form.file.data.save(music_file)

        results = seargine.get_overlaps_file(music_file)
        return render_template('track/results.html',
                page_title=title, response=results)
    else:
        return render_template('upload.html', form=form)
