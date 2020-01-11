from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators

class MusicForm(FlaskForm):
    # Для будущих версий (главное -- запомнить, что coerce=int)
    # For future versions (remenber that coerce=int)
    # input_mode = SelectField('Метод ввода', coerce=int, choices=[(0, 'табы (текст)'), (1, 'табы (графический ввод)'), (2, 'табы (png)'), (3, 'ноты (текст)')], render_kw={'class': 'custom-select'})
    music = StringField('Ваша песня', [validators.InputRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
