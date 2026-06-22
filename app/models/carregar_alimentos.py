#lê o arquivo .csv e retorna uma lista de alimentos

alimentos = []

with open ('app/data/taco_adaptada.csv', encoding='utf-8') as tabela:
    for linha in tabela:
        colunas = linha.strip().split(',')
        alimento = {
            'id_alimento': colunas[0],
            'categoria': colunas[1],
            'nome': colunas[2],
            'tags': colunas[3],
            'cal': colunas[4],
            'prot': colunas[5],
            'carb': colunas[6],
            'fib': colunas[7],
            'lip': colunas[8]
        }

        alimentos.append(alimento)