from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from ClassicoDecorator import ClassicoDecorator
from FamiliarDecorator import FamiliarDecorator
from TerrorDecorator import TerrorDecorator
from ConcreteEmailSender import ConcreteEmailSender
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def end():
    return render_template('end.html')


@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        topicos = request.form.getlist('topico')
        familia = 1 if "familiar" in topicos else 0
        terror = 1 if "terror" in topicos else 0
        classico = 1 if "classico" in topicos else 0

        # Conecta o banco de dados
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO user_info (email, familia, terror, classico, password) VALUES (?, ?, ?, ?, ?)', (email, familia, terror, classico, password))
        conn.commit()
        conn.close()

        return redirect(url_for('end'))
    return render_template('subscribe.html')

@app.route('/send')
def send():
    letter_type = request.args.get('type')
    sender = ConcreteEmailSender(username='newsl.lumiere@gmail.com', password='rvio zovh votm olth')

    # manda a newsletter familiar
    familiar_sender = FamiliarDecorator(sender)
    familiar_sender.send()
    # manda a newsletter clássica
    classico_sender = ClassicoDecorator(sender)
    classico_sender.send()
    # manda a newsletter de terror
    terror_sender = TerrorDecorator(sender)
    terror_sender.send()
    # manda a newsletter base
    sender.send()
    return render_template('send.html', text='Newsletter enviada')

@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    if request.method == 'POST':
        # Recebe os inputs do usuário
        emailtbc = request.form['email']
        passwordtbc = request.form['password']
        # Conecta ao banco de dados
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        # Procura a linha do email fornecido
        c.execute('SELECT password FROM user_info WHERE email=?', (emailtbc,))
        result = c.fetchone()
        if result:
            passwordtbt = result[0]
            # Compara a senha fornecida com a encontrada no banco de dados
            if passwordtbt == passwordtbc:
                # Deleta a linha da database
                c.execute('DELETE FROM user_info WHERE email = ?', (emailtbc,))
        conn.commit()
        conn.close()
        # Volta para a home
        return redirect(url_for('index'))
    return render_template('cancel.html')

if __name__ == '__main__':
    app.run(debug=True)
