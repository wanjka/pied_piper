from flask import Blueprint, render_template, redirect, url_for
from pyper.db import db
from pyper.track.models import Track
from pyper.track.forms import MusicForm
import pyper.track._seargine as seargine

bp = Blueprint('track', __name__, url_prefix='/')

@bp.route('/')
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
    title = 'Обработка результатов'
    results = []
    try:
        results = seargine.get_overlaps(form.music.data)
        return render_template('track/results.html', page_title=title, response=results)
    except Exception as e:
        print(e)
        return '1'
        #results = e
        #return render_template('track/results.html', page_title=title, response=results)

    # (previous version)
    # if form.validate_on_submit():
        # response = [('p', 'Ваша музыка'), ('pre', form.music.data)]
        # try:
            # results = seargine.get_overlaps(form.music.data)
        # except Exception as e:
            # results = e
        # response.append(('pre', results))
        # title = 'Обработка результатов'
        # return render_template(
                # 'track/results.html',
                # page_title=title,
                # response=response
        # )
    # else:
        # return 'You\'ve got error'

