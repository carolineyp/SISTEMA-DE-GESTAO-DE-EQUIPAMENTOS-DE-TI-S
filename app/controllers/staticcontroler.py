from flask import render_template

class StaticController:
    @staticmethod
    def home():
        return render_template("index/home.html")

    @staticmethod
    def login_form():
        return render_template("index/formulario_log_in.html")
