from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from ClassicoDecorator import ClassicoDecorator
from FamiliarDecorator import FamiliarDecorator
from TerrorDecorator import TerrorDecorator
from ConcreteEmailSender import ConcreteEmailSender

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form['email']
        topicos = request.form.getlist('topico')
        familia = 1 if "familiar" in topicos else 0
        terror = 1 if "terror" in topicos else 0
        classico = 1 if "classico" in topicos else 0

        # Conecta o banco de dados
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO user_info (email, familia, terror, classico) VALUES (?, ?, ?, ?)', (email, familia, terror, classico))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    return render_template('subscribe.html')

@app.route('/send')
def send():
    letter_type = request.args.get('type')
    sender = ConcreteEmailSender(username='newsl.lumiere@gmail.com', password='rvio zovh votm olth')
    if letter_type == 'FAMILIAR':
        familiar_sender = FamiliarDecorator(sender)
        familiar_sender.send()
        text = 'newsletter familiar enviada'
    if letter_type == 'CLASSICO':
        classico_sender = ClassicoDecorator(sender)
        classico_sender.send()
        text = 'newsletter classica enviada'
    if letter_type == 'TERROR':
        terror_sender = TerrorDecorator(sender)
        terror_sender.send()
        text = 'newsletter de terror enviada'
    return render_template('send.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
