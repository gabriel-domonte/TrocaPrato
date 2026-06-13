from flask import Flask, render_template, send_file, session, redirect
from config import Config
from app.controller.comparador import comparador_bp
from app.controller.autenticacao import autenticacao_bp

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
    
if __name__ == '__main__':
    app.run(debug=False)