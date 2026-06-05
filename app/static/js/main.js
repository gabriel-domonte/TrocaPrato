import { carregarAlimentos, initTomSelect, filtrar } from "./seletor.js";
import { limitarPesoA, formStep1, formStep2, formStep3, dynamicLabelALimento} from "./form.js";

/* Cria objetos para refenciar os elementos do HTML */
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

/* Cria variáveis vazias que irão receber uma instância do Tom Select */
let tomSelectInstanceA;
let tomSelectInstanceB;


async function iniciarlizar() {
    /* Aguarda a função carregarAlimentos() preencher o array OptionsOriginal para então criar as duas instâncias do Tom Select e habilitar o filtro por categorias */
    const optionsOriginal = await carregarAlimentos();

    tomSelectInstanceA = initTomSelect(selectAlimentoA, optionsOriginal);
    tomSelectInstanceB = initTomSelect(selectAlimentoB, optionsOriginal);

    filtroCategoriasA.addEventListener('change', () => {
        filtrar(tomSelectInstanceA, optionsOriginal, filtroCategoriasA);
    });

    filtroCategoriasB.addEventListener('change', () => {
        filtrar(tomSelectInstanceB, optionsOriginal, filtroCategoriasB);
    });
}

iniciarlizar();

/* Chama a função dynamicLabelAlimento() quando o valor do selectAlimentoA muda */
selectAlimentoA.addEventListener('change', () => {
    dynamicLabelALimento(tomSelectInstanceA, selectAlimentoA, labelAlimento)
})

/* Chama a função limitarPesoA() para o pesoAlimentoA */
pesoAlimentoA.addEventListener('input', () => {
    limitarPesoA(pesoAlimentoA)
});

/* Chama a função formStep1() quando o btnProx1 é clicado */
bntProx1.addEventListener('click', () => {
    formStep1(selectAlimentoA, msgErro1, divPeso, bntProx1, bntProx2)
});

/* Chama a função formStep2() quando o btnProx2 é clicado */
bntProx2.addEventListener('click', () => {
    formStep2(msgErro1, msgErro2, selectAlimentoA, pesoAlimentoA, divAlimentoB, btnSubmit, bntProx2)
});

/* Chama a função formStep3() quando o btnSubmit é clicado */
form.addEventListener('submit', (event) => {
    formStep3(event, msgErro1, msgErro2, msgErro3, selectAlimentoA, pesoAlimentoA, selectAlimentoB, form)
});