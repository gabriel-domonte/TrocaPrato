export function limitarPesoA(pesoAlimentoA) {
    /* Impede que o usuário digite mais que 3 algarismos no campo 'peso do alimento'. */
        pesoAlimentoA.value = pesoAlimentoA.value.slice(0,3);
}


function validar(campo, msgErro){
    /* Verifica se o campo foi preenchido corretamente, caso contrário exibe mensagem de erro */
    msgErro.classList.toggle('escondido', campo.checkValidity())
    return campo.checkValidity();
}

export function formStep1(selectAlimentoA, msgErro1, divPeso, bntProx1, bntProx2) {
    /* Caso o usuário tenha preenchido o formulário corretamente, exibe a próxima etapa do formulário*/
    if(!validar(selectAlimentoA, msgErro1)){
        return;
    }

    divPeso.classList.remove('escondido');
    bntProx2.classList.remove('escondido');
    bntProx1.classList.add('escondido');
}

export function formStep2(msgErro1, msgErro2, selectAlimentoA, pesoAlimentoA, divAlimentoB, btnSubmit, bntProx2) {
    /* Caso o usuário tenha preenchido o formulário corretamente, exibe a próxima etapa do formulário*/
    const campo1 = validar(selectAlimentoA, msgErro1);
    const campo2 = validar(pesoAlimentoA, msgErro2);

    if(!campo1 || !campo2){
        return;
    }

    divAlimentoB.classList.remove('escondido');
    btnSubmit.classList.remove('escondido');
    bntProx2.classList.add('escondido');
}

export function formStep3 (event, msgErro1, msgErro2, msgErro3, selectAlimentoA, pesoAlimentoA, selectAlimentoB, form) {
    /* Caso o usuário tenha preenchido o formulário corretamente, envia o formulário*/
    event.preventDefault();

    const campo1 = validar(selectAlimentoA, msgErro1);
    const campo2 = validar(pesoAlimentoA, msgErro2);
    const campo3 = validar(selectAlimentoB, msgErro3);

    if(campo1 && campo2 && campo3){
        form.submit();
    }
}

export function dynamicLabelALimento (tomSelectInstanceA, selectAlimentoA, labelAlimento) {
    /* Exibe um label dinâmico no formulário com base no alimento escolhido pelo usuário */
    if(!selectAlimentoA.checkValidity()){
        labelAlimento.textContent = '...'
    } else {
        const nomeAlimento = tomSelectInstanceA.options[tomSelectInstanceA.getValue()];

        const nomeSemTags = nomeAlimento.text.split('(')[0];

        labelAlimento.textContent = nomeSemTags;

    }
}