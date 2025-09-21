from flask import render_template
from app.models.usuario import Usuario

usuarios = [
    Usuario(1, "Caroline", "caroline@email.com"),
    Usuario(2, "João", "joao@email.com")
]

class UsuarioController:
    @staticmethod
    def listar():
        return render_template("usuario/lista_usuarios.html", usuarios=usuarios)

    @staticmethod
    def perfil():
        usuario = usuarios[0]  # exemplo simples
        return render_template("usuario/perfil.html", usuario=usuario)
