from flask import Flask, render_template, request, send_file
import csv
import pandas as pd

app = Flask(__name__)



@app.route('/data/taco_adaptada.csv')
def csv_file():
    return send_file('data/taco_adaptada.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():

    cal_porcao = 0

    dic_alimento_a = {}
    dic_alimento_b = {}

    id_a = request.form['alimento-a']
    id_b = request.form['alimento-b']
    peso_a = int(request.form['peso_a'])

    with open('data/taco_adaptada.csv', newline='', encoding='utf-8') as tabela:
        leitor = csv.DictReader(tabela)
        for linha in leitor:
            if linha['id_alimento'] == id_a:
                cal_porcao = peso_a * float(linha['kcal']) / 100
                dic_alimento_a = {
                    'nome': f'{linha['descricao']} ({linha['tags']})' if linha['tags'] else f'{linha['descricao']}',
                    'peso': round(peso_a),
                    'cal': round(cal_porcao),
                    'carb': round(peso_a * float(linha['carboidratos']) / 100),
                    'prot': round(peso_a * float(linha['proteinas']) / 100),
                    'lip': round(peso_a * float(linha['lipidios']) / 100),
                    'fib': round(peso_a * float(linha['fibras']) / 100)
                }
                break

    with open('data/taco_adaptada.csv', newline='', encoding='utf-8') as tabela:
        leitor = csv.DictReader(tabela)
        for linha in leitor:
            if linha['id_alimento'] == id_b:
                peso_b = cal_porcao * 100 /float(linha['kcal'])
                dic_alimento_b = {
                    'nome': f'{linha['descricao']} ({linha['tags']})' if linha['tags'] else f'{linha['descricao']}',
                    'peso': round(peso_b),
                    'cal': round(cal_porcao),
                    'carb': round(peso_b * float(linha['carboidratos']) / 100),
                    'prot': round(peso_b * float(linha['proteinas']) / 100),
                    'lip': round(peso_b * float(linha['lipidios']) / 100),
                    'fib': round(peso_b * float(linha['fibras']) / 100)
                }
                break

    return render_template('resultado.html', alimento_a=dic_alimento_a, alimento_b=dic_alimento_b)
    
@app.route("/favoritos")
def favoritos():
    return render_template('favoritos.html')

@app.route("/tabela")
def tabela():
    df = pd.read_csv("dados.csv")
    
    colunas = df.columns.tolist()
    dados = df.values.tolist()
    
    return render_template(
        "tabela.html",
        colunas =colunas,
        dados= dados
    )
    return render_template('tabela.html')

@app.route("/perfil")
def perfil():
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(debug=True)
    #para atualizar depois das modificações