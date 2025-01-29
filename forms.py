from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Name is required.")])  # Ensures name is filled
    phone = StringField('Phone')
    email = StringField('Email', validators=[DataRequired(message="Email is required."), Email(message="Invalid email address.")])  # Ensures email is filled and valid
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 