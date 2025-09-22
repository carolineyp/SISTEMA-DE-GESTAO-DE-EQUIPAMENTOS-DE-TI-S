
from flask import Flask

app = Flask(__name__)

# Importa os controllers (não o main!)
from app.controllers import staticcontroler
