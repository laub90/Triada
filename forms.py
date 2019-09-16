from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email


class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message= "Please enter your name")])
    email = TextField('Email', validators=[DataRequired(message= "Please enter your email")])
    subject = TextField('Asunto', validators=[DataRequired(message= "Please enter your Asunto")])
    message = TextAreaField('Mensaje', validators=[DataRequired(message= "Please enter your mensaje")])
    submit = SubmitField('Enviar')

    