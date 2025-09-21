from flask import Flask
from app.controllers.equipamentocontroller import equipamentoController
from app.controllers.staticcontroler import StaticController
# possivelmente UsuarioController também

app = Flask(__name__)

# Rotas (Front Controller centraliza aqui)
app.add_url_rule("/", view_func=StaticController.home)
app.add_url_rule("/login", view_func=StaticController.login_form)

app.add_url_rule("/equipamentos", view_func=equipamentoController.listar, methods=["GET"])
app.add_url_rule("/equipamentos/cadastrar", view_func=equipamentoController.mostrar_form_cadastro, methods=["GET"])
app.add_url_rule("/equipamentos/cadastrar", view_func=equipamentoController.cadastrar, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)
