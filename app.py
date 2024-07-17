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
        # Envia o email recebido para o banco de dados
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO user_emails (email) VALUES (?)', (email,))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    return render_template('subscribe.html')


if __name__ == '__main__':
    app.run(debug=True)
