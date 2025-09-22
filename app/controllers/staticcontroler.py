from app import app
from flask import render_template

@app.route("/")
def home():
    return "<h1>Sistema de Gestão de Equipamentos de TI</h1><p>Rodando com sucesso 🚀</p>"


@app.route("/eqiuipamentos")
def equipamentos():
    return render_template("equipamento/lista_equipamentos.html")


@app.route("/cadastros")
def cadastros():
    return render_template("equipamento/cadastro.html")

# outras rotas estáticas podem ser adicionadas aqui
# mas a lógica de negócio deve ficar nos controllers
# e a definição dos modelos de dados deve ficar nos models

@app.route("/senha")
def senha():
    return render_template("equipamento/recuperarsenha.html")

@app.route("/logins")
def logins():
    return render_template("equipamento/login.html")

# lembre-se de registrar este controller no __init__.py do app
# para que o Flask saiba que ele existe
# e não esqueça de criar as views (templates) correspondentes
# em app/views/equipamento/

@app.route("/principal")
def principal():
    return render_template("equipamento/principal.html")

@app.route("/usuarios")
def usuarios():
    return render_template("equipamento/lista_usuario.html")

@app.route("/perfil")
def perfil():
    return render_template("equipamento/perfil.html")
