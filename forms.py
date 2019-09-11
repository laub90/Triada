from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email


class ContactForm(Form):
    name = StringField('Nombre', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired()])
    subject = TextField('Asunto', validators=[DataRequired()])
    message = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar', validators=[DataRequired()])