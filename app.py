from flask import Flask, render_template, send_file, session, redirect
from config import Config
from app.controller.comparador import comparador_bp
from app.controller.autenticacao import autenticacao_bp
from app.controller.favoritos import favoritos_bp



app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static')

app.config.from_object(Config)

@app.route('/app/data/taco_adaptada.csv')
def taco_adaptada():
    return send_file('app/data/taco_adaptada.csv')

@app.route('/')
def index():
    if 'usuario_logado' in session:
        return redirect('/comparador')
    
    return render_template('index.html')

@app.route('/comparador')
def comparador():
    if 'usuario_logado' not in session:
        return redirect('/')
    
    return render_template('comparador.html', erros={})

app.register_blueprint(comparador_bp, url_prefix='/comparador')

app.register_blueprint(autenticacao_bp)

app.register_blueprint(favoritos_bp)


import csv
@app.route("/tabela")
def tabela():
    with open('data/taco_adaptada.csv', encoding='utf-8') as tabela:
        leitor = csv.reader(tabela) 
        linhas = list(leitor)
        
    colunas = linhas[0][1:]
    dados = []
    for linha in linhas [1:]:
        dados.append(linha[1:])
    
    return render_template(
        'tabela.html',
        colunas = colunas,
        dados = dados
    )
    

@app.route("/perfil")
def perfil():
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(debug=True)
    #para atualizar depois das modificações

    
if __name__ == '__main__':
    app.run(debug=False)

