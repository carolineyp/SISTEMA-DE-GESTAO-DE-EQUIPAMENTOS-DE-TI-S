from flask import flask, render_template

app = flask(__name__)


@app.route('/login.html')
def tela_login():
    return render_template('login.html')
if __name__ == '__redme__':
    app.run()


@app.route('/cadastro.html')
def login():
    return render_tamplate('cadastro.html')
if __name__ == '__redme__':
    app.run()


@app.route('/recuperarsenha.html')
def login():
    return render_tamplate('recuperarsenha.html')
if __name__ == '__redme__':
    app.run()  


 @app.route('/principal.html')
def login():
    return render_tamplate('principal.html')
if __name__ == '__redme__':
    app.run()