from flask import request, Blueprint, session, redirect, flash, render_template
from app.models.autenticacao import erros_login, cadastrar, erros_cadastro, alterar_senha, erros_alterar_senha

autenticacao_bp = Blueprint('autenticacao', __name__)

@autenticacao_bp.route('/login', methods=['GET','POST'])
def login():
    #se usuário já estiver logado, redireciona para página /comparador
    if 'usuario_logado' in session:
        return redirect('/comparador')
    
    erros = {}

    #recebe dados do formulário adiciona o usuário na sessão caso não haja erros
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        erros = erros_login(usuario, senha)

        if not erros:
            session['usuario_logado'] = usuario
            return redirect('/comparador')
    
    return render_template('login.html', erros=erros)

@autenticacao_bp.route('/cadastro', methods=['GET','POST'])
def cadastro():
    #se o usuário já estiver logado, redireciona para página /comparador
    if 'usuario_logado' in session:
        return redirect('/comparador')
    
    erros = {}

    #recebe dados do formulário e chama a função cadastrar caso não haja erros
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha1 = request.form['senha']
        senha2 = request.form['senha2']

        erros = erros_cadastro(usuario, senha1, senha2)
    
        if not erros:
            cadastrar(usuario, senha1)
            flash('Cadastro realizado com sucesso')
            return redirect('/login')
    
    return render_template('cadastro.html', erros=erros)

@autenticacao_bp.route('/logout')
def logout ():
    #remove o usuário da sessão e redireciona para página inicial
    session.pop('usuario_logado', None)
    return redirect('/')

@autenticacao_bp.route('/alterar-senha', methods=['GET','POST'])
def alteracao_senha():
    #se o usuário não estiver logado, redireciona para página inicial
    if 'usuario_logado' not in session:
        return redirect('/')
    
    erros = {}

    #rece os dados do formulário e chama a função alterar_senha caso não haja erros
    if request.method == 'POST':
        usuario = session['usuario_logado']
        senha_antiga = request.form['senha-antiga']
        senha_nova = request.form['senha-nova']
        confirmar_senha = request.form['confirmar-senha']

        erros = erros_alterar_senha(usuario, senha_antiga, senha_nova, confirmar_senha)

        if not erros:
            alterar_senha(usuario, senha_nova)
            flash('Senha alterada com sucesso')
            return redirect('/perfil')
    
    return render_template('alterar.html', erros=erros)
