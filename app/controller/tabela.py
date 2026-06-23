# Pega a leitura do CSV já feita e cria a tabela

from flask import Blueprint, render_template
from app.models.carregar_alimentos import alimentos

tabela_bp = Blueprint('tabela', __name__)

@tabela_bp.route('/')
def exibir_tabela():
    return render_template(
        'tabela.html',
        alimentos=alimentos
    )