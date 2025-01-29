from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp

class ContactForm(FlaskForm):
    name = StringField('Name')
    phone = StringField('Phone', validators=[ DataRequired(), 
    Regexp(r'^\+?\d+$', message="Phone number must contain only numbers and an optional '+' sign.")])
    email = StringField('Email')
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 