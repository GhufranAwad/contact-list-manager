from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp

class ContactForm(FlaskForm):
    name = StringField('Name', 
        validators=[DataRequired(message="Name is required."),
                    Regexp(r'^[A-Za-z0-9 ]+$', message="Name can only contain letters, numbers, and spaces.")])  # No special chars
    #name = StringField('Name', validators=[DataRequired(message="Name is required.")])  # Ensures name is filled
    phone = StringField('Phone', 
        validators=[DataRequired(message="Phone number is required."),
                    Regexp(r'^[0-9+\- ]+$', message="Phone number can only contain numbers, spaces, plus signs, and hyphens.")])  # No special chars
   # phone = StringField('Phone')
    email = StringField('Email', validators=[DataRequired(message="Email is required."), Email(message="Invalid email address.")])  # Ensures email is filled and valid
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 