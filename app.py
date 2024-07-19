from flask import Flask, render_template, request, redirect, url_for
import sqlite3

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


if __name__ == '__main__':
    app.run(debug=True)
