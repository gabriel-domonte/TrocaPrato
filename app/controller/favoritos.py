from flask import request, Blueprint, session, redirect, flash, render_template, url_for
from app.models.favoritos import salvar_favorito, favoritos_detalhados, remover

favoritos_bp = Blueprint('favoritos', __name__)

@favoritos_bp.route("/salvar_comparacao", methods=['POST'])
def salvar_comparacao():
    usuario = session.get('usuario_logado')
    if not usuario:
        return redirect('/')
    id_alimento_a = request.form['alimento-a']
    id_alimento_b = request.form['alimento-b']
    peso_a = request.form['peso_a']

    if salvar_favorito(usuario, id_alimento_a, id_alimento_b, peso_a):
        flash ("Comparação favoritada com sucesso!")
    else:
        flash ("Comparação já está favoritada!")
    return redirect(url_for('favoritos.exibir_favoritos'))

@favoritos_bp.route("/favoritos")
def exibir_favoritos():
    usuario = session.get('usuario_logado')
    if not usuario:
        return redirect('/')
    favoritos = favoritos_detalhados(usuario)
    return render_template('favoritos.html', favoritos=favoritos)

@favoritos_bp.route("/remover_favorito", methods=['POST'])
def remover_favorito():
    usuario = session.get('usuario_logado')
    if not usuario:
        return redirect('/')
    id_alimento_a = request.form['alimento-a']
    id_alimento_b = request.form['alimento-b']
    peso_a = request.form['peso_a']
    if remover(usuario, id_alimento_a, id_alimento_b, peso_a):
        flash('Comparação removida com sucesso!')
    else:
        flash('Comparação não encontrada.')
    return redirect(url_for('favoritos.exibir_favoritos'))