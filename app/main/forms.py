from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField, TextAreaField,SelectField
from wtforms.validators import DataRequired
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Pitch Title.',validators = [DataRequired()])
    category = SelectField(u'Select Pitch Category', choices=[('....Select Category', 'Select Category.....'), ('Technology', 'Technology'), ('Business', 'Business'), ('Health', 'Health')])
    pitches = TextAreaField('Tell us about you.',validators = [DataRequired()])

    submit = SubmitField('Submit')