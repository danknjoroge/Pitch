from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField,SelectField
from wtforms.validators import DataRequired
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


# class AddPitch(FlaskForm):
#     title = TextAreaField('Tell us about you.',validators = [DataRequired()])
#     category = SelectField(u'Select Pitch Category', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
#     pitch = TextAreaField('Tell us about you.',validators = [DataRequired()])

#     submit = SubmitField('Submit')