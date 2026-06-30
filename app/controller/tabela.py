from flask import Blueprint, render_template, redirect, session
from app.models.carregar_alimentos import alimentos

tabela_bp = Blueprint('tabela', __name__)

@tabela_bp.route('/tabela')
def exibir_tabela():
    #caso usuário não esteja logado, redireciona para página inicial
    if 'usuario_logado' not in session:
        return redirect('/')
    
    #renderiza a página html e envia a lista de alimentos criada por carregar_alimentos.py
    return render_template('tabela.html', alimentos=alimentos)