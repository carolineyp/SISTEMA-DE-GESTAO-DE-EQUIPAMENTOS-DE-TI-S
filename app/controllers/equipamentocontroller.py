from flask import render_template, request, redirect, url_for
from app.models.Equipamentos import Equipamento

# exemplo simples: usando lista em memória
equipamentos = []

class equipamentoController:
    @staticmethod
    def listar():
        return render_template("equipamento/lista_equipamentos.html", equipamentos=equipamentos)

    @staticmethod
    def mostrar_form_cadastro():
        return render_template("equipamento/cadastro.html")

    @staticmethod
    def cadastrar():
        nome = request.form.get("nome")
        status = request.form.get("status")
        if nome and status:
            novo = Equipamento(len(equipamentos)+1, nome, status)
            equipamentos.append(novo)
        return redirect(url_for("equipamento_listar"))
