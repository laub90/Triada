from flask import Flask, render_template, flash, redirect, request
from forms import ContactForm
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail()

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'laresidenciacordoba@gmail.com'
app.config["MAIL_PASSWORD"] = 'Amorsalud100000'

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
                          'laresidenciacordoba@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('home.html', success=True)
    elif request.method == 'GET':
        return render_template('home.html', form=form)
    
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/fotos')
def fotos():
    return render_template('fotos.html')


@app.route('/contacto')
def  contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)