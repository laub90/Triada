from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email


class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message= "Ingresa tu nombre")])
    email = TextField('Email', validators=[DataRequired(message= "Ingresa tu email")])
    subject = TextField('Celular/ Whatsapp', validators=[DataRequired(message= "Ingresa tu telefono")])
    message = TextAreaField('Mensaje', validators=[DataRequired(message= "Ingresa tu mensaje")])
    submit = SubmitField('Enviar')

    