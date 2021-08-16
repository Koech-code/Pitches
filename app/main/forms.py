from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField, SubmitField
from wtforms.validators import Required

class postForm(FlaskForm):
    title = StringField()
    post =TextAreaField()
    category =SelectField()
    submit =SubmitField()



