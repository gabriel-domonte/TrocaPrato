from werkzeug.security import generate_password_hash, check_password_hash
          
def username_disponivel (usuario):
    #retorna True se o nome de usuário escolhido estiver disponível
    with open ('app/data/usuarios.csv', encoding='utf-8') as tabela:
        for linha in tabela:
            colunas = linha.strip().split(',')
            if usuario == colunas[0]:
                return False
        
        return True

def username_valido (usuario):
    #retorna true se o nome de usuário escolhido conter apenas letras e números
    return usuario.isalnum()

def senha_valida (senha):
    #retorna true se a senha escolhida conter apenas letras e números, e no mínimo: 6 caracteres, uma letra maiuscula, uma letra minuscula e um numero.
    numero = any(i.isdigit() for i in senha)
    minuscula = any(i.islower() for i in senha)
    maiuscula = any(i.isupper() for i in senha)

    return senha.isalnum() and len(senha) > 5 and numero and minuscula and maiuscula

def erros_cadastro(usuario, senha1, senha2):
    #retorna um dicionário de erros que podem ocorrer durante o cadastro
    erros = {}

    if usuario == '':
        erros['usuario'] = 'Informe um nome de usuário'
    elif not username_disponivel(usuario):
        erros['usuario'] = 'Este nome de usuário já está em uso'
    elif not username_valido(usuario):
        erros['usuario'] = 'O nome de usuário pode conter apenas letras e/ou números'

    if senha1 == '':
        erros['senha1'] = 'Informe uma senha'
    elif not senha_valida(senha1):
        erros['senha1'] = 'Informe uma senha válida'

    if senha2 == '':
        erros['senha2'] = 'Confirme a senha'
    elif senha1 != senha2 and senha1 != '':
        erros['senha2'] = 'As senhas não iguais'

    return erros

def cadastrar (usuario, senha):
    #adiciona o usuário e sua respectiva senha ao arquivo usuarios.csv
    with open ('app/data/usuarios.csv', mode='a', encoding='utf-8') as tabela:
        tabela.write(f'{usuario},{generate_password_hash(senha)}\n')

def erros_login (usuario, senha):
    #retorna um dicionário de erros que podem ocorrer durante o login
    erros = {}

    if usuario == '':
        erros['usuario'] = 'Informe um usuário'

    if senha == '':
        erros['senha'] = 'Informe a senha'
    
    if usuario and senha and not logar(usuario, senha):
        erros['geral'] = 'Usuário ou senha incorretos'
    
    return erros

def logar (usuario, senha):
    #retorna true se o usuário e senha informados corresponderem a um usuário e senha em usuarios.csv
    with open ('app/data/usuarios.csv', encoding='utf-8') as tabela:
        for linha in tabela:
            colunas = linha.strip().split(',')
            if usuario == colunas[0] and check_password_hash(colunas[1], senha):
                return True
            
    return False

def erros_alterar_senha (usuario, senha_antiga, senha_nova, confirmar_senha):
    #retorna um dicionário de erros que podem ocorrer durante a mudança de senha
    erros = {}

    if not logar(usuario, senha_antiga):
        erros['senha_antiga'] = 'Senha atual incorreta'
    
    if senha_nova == '':
        erros['senha_nova'] = 'Informe uma nova senha'

    if not senha_valida(senha_nova):
        erros['senha_nova'] = 'Informe uma senha válida'

    if confirmar_senha == '':
        erros['confirmar_senha'] = 'Confirme a nova senha'

    if confirmar_senha != senha_nova and confirmar_senha != '':
        erros['confirmar_senha'] = 'As senhas não são iguais'

    return erros


def alterar_senha (usuario, senha_nova):
    #cria uma lista e adiciona as linhas de usuarios.csv uma a uma, alterando apenas a linha do usuário logado; ao final, reescreve usuários.csv com essa lista
    tabela_atualizada = []

    with open ('app/data/usuarios.csv', encoding='utf-8') as tabela:
        for linha in tabela:
            colunas = linha.strip().split(',')
            if usuario == colunas[0]:
                colunas[1] = generate_password_hash(senha_nova)
            tabela_atualizada.append(','.join(colunas) + '\n')
    
    with open ('app/data/usuarios.csv', 'w', encoding='utf-8') as tabela:
        tabela.writelines(tabela_atualizada)