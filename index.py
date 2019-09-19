from flask import Flask, render_template, flash, redirect, request
from forms import ContactForm
from flask_mail import Mail, Message
import os
import urllib.request 

x = urllib.request.urlopen('https://realemail.expeditedaddons.com/?api_key=TMF4RPB9I07GNH3K1L65XD10U5W2988YJ67OSZ43EVQA2C&email=email%40example.org&fix_typos=false')
print (x.read())

app = Flask(__name__)
mail = Mail()

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'lauriborra@gmail.com'
app.config["MAIL_PASSWORD"] = 'gyhinqpdstjihbls'

mail.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('home.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=[
                          'lauriborra@gmail.com'])
            msg.body = """
            From: %s &lt;%s&gt;
             %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('home.html', success=True)
    elif request.method == 'GET':
        return render_template('home.html', form=form)
    


if __name__ == '__main__':
    app.run(debug=True)