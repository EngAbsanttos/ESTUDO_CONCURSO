from flask import render_template
from . import db
from .models import Questao
from . import create_app

app = create_app()  # Cria a instância do aplicativo

@app.route('/')  # Corrigido para app.route
def index():
    questao = Questao.query.first()  # Exibe a primeira questão
    return render_template('index.html', questao=questao)
