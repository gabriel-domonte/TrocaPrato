from flask import Flask, render_template, send_file, session, redirect
from dotenv import load_dotenv, find_dotenv
import os
from app.controller.comparador import comparador_bp
from app.controller.autenticacao import autenticacao_bp
from app.controller.favoritos import favoritos_bp
from app.controller.tabela import tabela_bp

load_dotenv(find_dotenv())

app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

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

@app.route('/perfil')
def perfil():
    if 'usuario_logado' not in session:
        return redirect('/')
    
    return render_template('perfil.html')

app.register_blueprint(comparador_bp, url_prefix='/comparador')

app.register_blueprint(autenticacao_bp)

app.register_blueprint(favoritos_bp)
    
app.register_blueprint(tabela_bp)

if __name__ == '__main__':
    app.run(debug=True)