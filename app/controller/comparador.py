from flask import render_template, request, Blueprint
from app.models.carregar_alimentos import alimentos
from app.models.comparador import alimento_a, alimento_b

comparador_bp = Blueprint('comparador', __name__)

@comparador_bp.route('/resultado', methods=['POST'])
def comparador():
    #recebe dados do formulário, chama as funções do comparador e retorna uma comparação na forma de de dois dicionários
    id_a = int(request.form['alimento-a'])
    id_b = int(request.form['alimento-b'])
    peso_a = int(request.form['peso-a'])

    dict_alimento_a = alimento_a(alimentos, id_a, peso_a)
    dict_alimento_b = alimento_b(alimentos, id_b, dict_alimento_a)

    return render_template('resultado.html', dict_alimento_a=dict_alimento_a, dict_alimento_b=dict_alimento_b)

