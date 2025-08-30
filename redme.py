from flask import flask, render_template

app = flask(__name__)


@app.route('/login')
def tela_login():
    return render_template('login.html')
if __name__ == '__redme__':
    app.run()