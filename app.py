from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de filmes de exemplo
filmes = [
    {"titulo": "O Poderoso Chefão", "ano": 1972},
    {"titulo": "Um Sonho de Liberdade", "ano": 1994},
    {"titulo": "O Senhor dos Anéis: A Sociedade do Anel", "ano": 2001}
]

@app.route('/')
def index():
    return render_template('index.html', filmes=filmes)

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form['email']
        # Aqui você poderia adicionar lógica para salvar o email, enviar um email de confirmação, etc.
        return redirect(url_for('index'))
    return render_template('subscribe.html')

if __name__ == '__main__':
    app.run(debug=True)
