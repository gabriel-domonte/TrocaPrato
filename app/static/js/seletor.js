export async function carregarAlimentos() {
    /* Transforma cada linha do .csv em um objeto, retorna uma lista de objetos */
    let optionsOriginal = [];

    const resposta = await fetch('/app/data/taco_adaptada.csv');
    const tabela = await resposta.text();
    const linhas = tabela.trim().split('\n');

    linhas.slice(1).forEach(linha => {
        const colunas = linha.split(',');

        optionsOriginal.push({
            value: colunas[0],
            categoria: colunas[1],
            text: colunas[3] === '' ? colunas[2] : `${colunas[2]} (${colunas[3]})`
        });
    });

    return optionsOriginal;
}

export function initTomSelect(select, optionsOriginal) {
    /* chama a classe TomSelect para criar um novo seletor*/
    return new TomSelect(select,{
        maxOptions: 559,
        options: optionsOriginal,
        valueField: 'value',
        labelField: 'text',
        searchField: ['text'],
        placeholder: 'Selecione um alimento...',
        render: {
            no_results: function() {
                return '<div class="no-results">Nenhum alimento encontrado</div>';
            }
        }       
    });
}

export function filtrar(tomSelectInstance, optionsOriginal, filtro) {
    /* utiliza o método filter() nos elementos do optionsOriginal e retorna apenas os elementos compatíveis com o filtro de categorias */
    const categoriaSelecionada = filtro.value;
    const optionsFiltrado = optionsOriginal.filter(item => {
        return categoriaSelecionada === 'todas' || item.categoria === categoriaSelecionada;
    });

    tomSelectInstance.clear();
    tomSelectInstance.clearOptions();
    tomSelectInstance.addOptions(optionsFiltrado);
}