from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import csv

app = Flask(__name__)
app.secret_key = 'minha_vida_e_boa'


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
    
@app.route("/salvar_favorito", methods=['POST'])
def salvar_favorito():
    id_a = request.form['alimento-a']
    id_b = request.form['alimento-b']
    peso_a = int(request.form['peso_a'])
    existe_favorito = False

    with open('data/favoritos.csv', mode='r', newline='', encoding='utf-8') as favoritos_arquivo:
        leitor_favoritos = csv.reader(favoritos_arquivo)
        for linha in leitor_favoritos:
            if linha == [id_a, id_b, str(peso_a)]:
                existe_favorito = True
                flash('Comparação já está favoritada!')
                break

    if not existe_favorito:
        with open('data/favoritos.csv', mode='a', newline='', encoding='utf-8') as favoritos_arquivo:
            parametros = csv.writer(favoritos_arquivo)
            parametros.writerow([id_a, id_b, peso_a])
        flash('Comparação favoritada com sucesso!')
    return redirect(url_for('exibir_favoritos'))

@app.route("/exibir_favoritos")
def exibir_favoritos():
    favoritos = []

    with open('data/taco_adaptada.csv', newline='', encoding='utf-8') as tabela:
        leitor = csv.DictReader(tabela)
        taco_dict = {linha['id_alimento']: linha for linha in leitor}

    with open('data/favoritos.csv', newline='', encoding='utf-8') as favoritos_arquivo:
                leitor_favoritos = csv.reader(favoritos_arquivo)
                next(leitor_favoritos, None)

                for linha in leitor_favoritos:
                    if len(linha) < 3:
                        continue
                    id_favorito_a = linha[0]
                    id_favorito_b = linha[1]
                    peso_a = int(linha[2])
                    linha_a = taco_dict.get(id_favorito_a)
                    linha_b = taco_dict.get(id_favorito_b)

                    if linha_a and linha_b:
                        calorias_a = peso_a * float(linha_a['kcal']) / 100
                        favoritos.append({

                            'nome': linha_a['descricao'],
                            'tags': linha_a['tags'],
                            'peso_a': peso_a,
                            'calorias': round(calorias_a),
                            'proteinas': round(peso_a * float(linha_a['proteinas']) / 100),
                            'carboidratos': round(peso_a * float(linha_a['carboidratos']) / 100),
                            'lipideos': round(peso_a * float(linha_a['lipidios']) / 100),
                            
                            'nome_b': linha_b['descricao'],
                            'peso_b': round(calorias_a * 100 / float(linha_b['kcal']))
                        })



    return render_template('favoritos.html', favoritos=favoritos)

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