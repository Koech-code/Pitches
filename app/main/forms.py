from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField, SubmitField
from wtforms.validators import Required

class postForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post =TextAreaField('Pitch', validators=[Required()])
    category =SelectField('Category', choices=[('INTERVIEW', 'INTERVIEW'), ('BUSINESS', 'BUSINESS'), ('FAMILY', 'FAMILY')], validators=[Required()])
    submit =SubmitField('post')

class commentForm(FlaskForm):
    title =StringField('Title', validators=[Required()])
    comment =TextAreaField('Comment', validators=[Required()])
    submit =SubmitField('post')

class vote(FlaskForm):
    submit =SubmitField('like')



