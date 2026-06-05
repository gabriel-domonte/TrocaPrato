def alimento_a(alimentos, indice, peso_a):
    #retorna um dicionario com o valor nutricional do alimento a
    dict_alimento_a = {
        'categoria': alimentos[indice]['categoria'],
        'nome': alimentos[indice]['nome'],
        'tags': alimentos[indice]['tags'],
        'peso': peso_a,
        'cal': round(peso_a * float(alimentos[indice]['cal']) / 100),
        'carb': round(peso_a * float(alimentos[indice]['carb']) / 100),
        'prot': round(peso_a * float(alimentos[indice]['prot']) / 100),
        'lip': round(peso_a * float(alimentos[indice]['lip']) / 100),
        'fib': round(peso_a * float(alimentos[indice]['fib']) / 100)
    }

    return dict_alimento_a

def alimento_b(alimentos, indice, dict_alimento_a):
    #retorna um dicionario com o valor nutricional do alimento b
    cal = dict_alimento_a['cal']
    peso_b = round(cal * 100 / float(alimentos[indice]['cal']))

    dict_alimento_b = {
        'categoria': alimentos[indice]['categoria'],
        'nome': alimentos[indice]['nome'],
        'tags': alimentos[indice]['tags'],
        'peso': peso_b,
        'cal': cal,
        'carb': round(peso_b * float(alimentos[indice]['carb']) / 100),
        'prot': round(peso_b * float(alimentos[indice]['prot']) / 100),
        'lip': round(peso_b * float(alimentos[indice]['lip']) / 100),
        'fib': round(peso_b * float(alimentos[indice]['fib']) / 100)
    }

    return dict_alimento_b