from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message= "")])
    email = TextField('Email', validators=[DataRequired(message= "")])
    subject = TextField('Subject', validators=[DataRequired(message= "")])
    message = TextAreaField('Message', validators=[DataRequired(message= "")])
    submit = SubmitField('Send')

    