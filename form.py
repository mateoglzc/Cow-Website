from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class MooForm(FlaskForm):
    years = IntegerField('How old are you: ', validators=[DataRequired()])
    beef = IntegerField('Beef', validators=[DataRequired()])
    submit = SubmitField('MOO')