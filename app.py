from flask import Flask, render_template, send_file
from app.models.carregar_alimentos import alimentos
from app.controller.comparador import comparador_bp

app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static')

@app.route('/app/data/taco_adaptada.csv')
def csv_file():
    return send_file('app/data/taco_adaptada.csv')

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(comparador_bp)
    
if __name__ == '__main__':
    app.run(debug=False)