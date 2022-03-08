from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


# class AddPitch(FlaskForm):
#     title = TextAreaField('Tell us about you.',validators = [DataRequired()])
#     category = TextAreaField('')
#     pitch = TextAreaField('Tell us about you.',validators = [DataRequired()])

#     submit = SubmitField('Submit')