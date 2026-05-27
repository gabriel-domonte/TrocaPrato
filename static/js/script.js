const form = document.getElementById('comparador')

const bntProx1 = document.getElementById('btn-prox-1');
const bntProx2 = document.getElementById('btn-prox-2');
const btnSubmit = document.getElementById('btn-submit');

const divPeso = document.getElementById('div-peso');
const divAlimentoB = document.getElementById('div-alimento-b')

const selectAlimentoA = document.getElementById('select-alimento-a');
const selectAlimentoB = document.getElementById('select-alimento-b');

const filtroCategoriasA = document.getElementById('filtro-a');
const filtroCategoriasB = document.getElementById('filtro-b');

const pesoAlimentoA = document.getElementById('peso-a');

const labelAlimento = document.getElementById('label-alimento');

const msgErro1 = document.getElementById('msg-erro-1');
const msgErro2 = document.getElementById('msg-erro-2');
const msgErro3 = document.getElementById('msg-erro-3');

let optionsOriginal = []

let tomSelectInstanceA;
let tomSelectInstanceB;

fetch('data/taco_adaptada.csv')
    .then(r => r.text())
    .then(texto => {
        const linhas = texto.trim().split('\n');
        linhas.slice(1).forEach(linha =>{
            const colunas = linha.split(',');
            optionsOriginal.push({
                value: colunas[0],
                categoria: colunas[1],
                text: colunas[3] === '' ? colunas[2] : `${colunas[2]} (${colunas[3]})`
            });
        });
        tomSelectInstanceA = initTomSelect(selectAlimentoA);
        tomSelectInstanceB = initTomSelect(selectAlimentoB);
    });


function initTomSelect(select) {
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

function filtrar(tomSelectInstance, filtro) {
    const categoriaSelecionada = filtro.value;
    const optionsFiltrado = optionsOriginal.filter(item => {
        return categoriaSelecionada === 'todas' || item.categoria === categoriaSelecionada;
    });

    tomSelectInstance.clear();
    tomSelectInstance.clearOptions();
    tomSelectInstance.addOptions(optionsFiltrado);
}

function limitarPesoA() {
    if (pesoAlimentoA.value.length > 3){
        pesoAlimentoA.value = pesoAlimentoA.value.slice(0,3);
    }
}

function comparadorStep1() {
    if (!selectAlimentoA.checkValidity()) {
        msgErro1.classList.remove('escondido');
    } else {
        msgErro1.classList.add('escondido')
        divPeso.classList.remove('escondido');
        bntProx2.classList.remove('escondido');
        bntProx1.classList.add('escondido');
    }
}

function comparadorStep2() {

    msgErro1.classList.add('escondido')
    msgErro2.classList.add('escondido')

    if (!selectAlimentoA.checkValidity()) {
        msgErro1.classList.remove('escondido')
    }

    if (!pesoAlimentoA.checkValidity()) {
        msgErro2.classList.remove('escondido');
    }

    if (selectAlimentoA.checkValidity() && pesoAlimentoA.checkValidity()) {
        divAlimentoB.classList.remove('escondido');
        btnSubmit.classList.remove('escondido');
        bntProx2.classList.add('escondido');
    }
}

function comparadorStep3 (event) {
    event.preventDefault();

    msgErro1.classList.add('escondido');
    msgErro2.classList.add('escondido');
    msgErro3.classList.add('escondido');

    if (!selectAlimentoA.checkValidity()) {
        msgErro1.classList.remove('escondido')
    }

    if (!pesoAlimentoA.checkValidity()) {
        msgErro2.classList.remove('escondido');
    }

    if (!selectAlimentoB.checkValidity()) {
        msgErro3.classList.remove('escondido');
    }

    if (selectAlimentoA.checkValidity() && pesoAlimentoA.checkValidity() && selectAlimentoB.checkValidity()) {
        form.submit();
    }

}

function dynamicLabelALimento () {
    if(!selectAlimentoA.checkValidity()){
        labelAlimento.textContent = '...'
    } else {
        const nomeAlimento = tomSelectInstanceA.options[tomSelectInstanceA.getValue()];

        const nomeSemTags = nomeAlimento.text.split('(')[0];

        labelAlimento.textContent = nomeSemTags;

    }
}

filtroCategoriasA.addEventListener('change', () => {
    filtrar(tomSelectInstanceA, filtroCategoriasA);
});

filtroCategoriasB.addEventListener('change', () => {
    filtrar(tomSelectInstanceB, filtroCategoriasB);
});

selectAlimentoA.addEventListener('change', dynamicLabelALimento)

pesoAlimentoA.addEventListener('input', limitarPesoA);

bntProx1.addEventListener('click', comparadorStep1);

bntProx2.addEventListener('click', comparadorStep2);

form.addEventListener('submit', comparadorStep3);

