from flask import Flask as flask, render_template, request, redirect, url_for



app = flask(__name__)


@app.route('/login.html')
def tela_login():
    return render_template('login.html')
if __name__ == '__redme__':
    app.run()


@app.route('/dologin', methods=['POST'])
def dologin():
    email = request.form['login']
    password = request.form['senha']
    # Aqui você pode adicionar a lógica de autenticação
    if email == 'carol@gmail.com' and password == '1234':
        return redirect(url_for('principal.html'))
    else:
        return "Credenciais inválidas, tente novamente ou recupere sua senha."
if __name__ == '__redme__':
    app.run(host="0.0.0.0", port=81)







@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')
if __name__ == '__redme__':
    app.run()


@app.route('/recuperarsenha.html')
def recuperar_senha():
    return render_template('recuperarsenha.html')
if __name__ == '__redme__':
    app.run()  


@app.route('/principal.html')
def principal():
    return render_template('principal.html')
if __name__ == '__redme__':

    app.run()