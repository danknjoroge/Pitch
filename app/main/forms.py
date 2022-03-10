from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField, TextAreaField,SelectField
from wtforms.validators import DataRequired
from ..models import User

class UpdateProfile(FlaskForm):
    fullname = StringField('FullName.',validators = [DataRequired()])

    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Pitch Title.',validators = [DataRequired()])
    category = SelectField(u'Select Pitch Category', choices=[('....Select Category', 'Select Category.....'), ('Technology', 'Technology'), ('Business', 'Business'), ('Health', 'Health')])
    pitches = TextAreaField('Your Pitch .',validators = [DataRequired()])

    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Leave us a comment about the pitch',validators = [DataRequired()])
    submit = SubmitField('Submit')