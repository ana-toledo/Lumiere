from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form['email']
        # Aqui você pode adicionar lógica para salvar o email, enviar um email de confirmação, etc.
        return redirect(url_for('index'))
    return render_template('subscribe.html')

if __name__ == '__main__':
    app.run(debug=True)
