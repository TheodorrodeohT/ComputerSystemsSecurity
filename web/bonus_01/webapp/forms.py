from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Length


class SearchForm(FlaskForm):
    choice = SelectField('Search by:', choices=[('1', 'login'), ('2', 'id')])
    field = StringField('Search for:', validators=[Length(min=1, max=256)])
    submit = SubmitField('Search')
