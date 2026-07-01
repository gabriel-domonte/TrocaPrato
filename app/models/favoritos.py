from app.models.carregar_alimentos import alimentos
from app.models.comparador import alimento_a, alimento_b

ARQUIVO = 'app/data/favoritos.csv'

def verificar_favorito(user_id, id_alimento_a, id_alimento_b, peso_a):
    with open(ARQUIVO, 'r') as favoritos:
        linhas = favoritos.readlines()
    if len(linhas) <= 1:
        return False
    for linha in linhas[1:]:
        linha = linha.strip().split(",")
        if len(linha) < 4: 
            continue

        if  linha[0] == user_id and linha[1] == id_alimento_a and linha[2] == id_alimento_b and linha[3] == peso_a:
            return True
    return False

def salvar_favorito(user_id, id_alimento_a, id_alimento_b, peso_a):
    if verificar_favorito(user_id, id_alimento_a, id_alimento_b, peso_a):
        return False
    else:
        with open(ARQUIVO, 'a') as favoritos:
            favoritos.write(f"{user_id},{id_alimento_a},{id_alimento_b},{peso_a}\n")
        return True


def listar_favoritos(user_id):
    lista_favoritos = []
    with open(ARQUIVO, 'r') as favoritos:
        next(favoritos)
        for linha in favoritos:
            linha = linha.strip().split(",")
            if len(linha) < 4:
                continue
            if user_id == linha[0]:
                id_alimento_a = linha[1]
                id_alimento_b = linha[2]
                peso_a = linha[3]

                if not id_alimento_a or not id_alimento_b or not peso_a:
                    continue 
                lista_favoritos.append((int(id_alimento_a), int(id_alimento_b), int(peso_a)))
    return lista_favoritos
        

def favoritos_detalhados(user_id):
    lista = listar_favoritos(user_id)
    resultado = []
    for item in lista:
        id_alimento_a = item[0]
        id_alimento_b = item[1]
        peso_a = item[2]
        resultado_a = alimento_a(alimentos, id_alimento_a, peso_a)
        resultado_b = alimento_b(alimentos, id_alimento_b, resultado_a)
        resultado.append({
            'id_alimento_a': id_alimento_a,
            'nome': resultado_a['nome'],
            'tags': resultado_a['tags'],
            'peso_a': resultado_a['peso'],
            'calorias': resultado_a['cal'],
            'proteinas': resultado_a['prot'],
            'carboidratos': resultado_a['carb'],
            'lipideos': resultado_a['lip'],

            'id_alimento_b': id_alimento_b,
            'nome_b': resultado_b['nome'],
            'tags_b': resultado_b['tags'],
            'peso_b': resultado_b['peso'],
            'calorias_b': resultado_b['cal'],
            'proteinas_b': resultado_b['prot'],
            'carboidratos_b': resultado_b['carb'],
            'lipideos_b': resultado_b['lip'],
        })
    return resultado

def remover(user_id, id_alimento_a, id_alimento_b, peso_a):
    favorito_removido = False
    with open(ARQUIVO, 'r') as favoritos:
        linhas = favoritos.readlines()
        if len(linhas) <= 1:
            return False
        favoritos_atualizado = [linhas[0]]
        for favorito in linhas[1:]:
            linha = favorito.strip().split(",")
            if len(linha) < 4: 
                continue

            if  linha[0] == user_id and linha[1] == id_alimento_a and linha[2] == id_alimento_b and linha[3] == peso_a:
                favorito_removido = True
                continue

            favoritos_atualizado.append(",".join(linha) + "\n")
    with open(ARQUIVO, 'w') as favoritos:
        favoritos.writelines(favoritos_atualizado)
    return favorito_removido
 