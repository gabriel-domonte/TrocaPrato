export function limitarPesoA(pesoAlimentoA) {
    /* Impede que o usuário digite mais que 3 algarismos no campo 'peso do alimento'. */
    if (pesoAlimentoA.value.length > 3){
        pesoAlimentoA.value = pesoAlimentoA.value.slice(0,3);
    }
}

export function formStep1(selectAlimentoA, msgErro1, divPeso, bntProx1, bntProx2) {
    /* Caso o usuário tenha preenchido a primeira parte do formulário corretamente, exibe a segunda parte. Caso contrário, exibe uma mensagem de erro. */
    if (!selectAlimentoA.checkValidity()) {
        msgErro1.classList.remove('escondido');
    } else {
        msgErro1.classList.add('escondido')
        divPeso.classList.remove('escondido');
        bntProx2.classList.remove('escondido');
        bntProx1.classList.add('escondido');
    }
}

export function formStep2(msgErro1, msgErro2, selectAlimentoA, pesoAlimentoA, divAlimentoB, btnSubmit, bntProx2) {
    /* Caso o usuário tenha preenchido a primeira e segunda parte do formulário corretamente, exibe a terceira parte. Caso contrário, exibe uma mensagem de erro. */
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

export function formStep3 (event, msgErro1, msgErro2, msgErro3, selectAlimentoA, pesoAlimentoA, selectAlimentoB, form) {
    /* Caso o usuário tenha preenchido o formulário corretamente, envia o formulário. Caso contrário, exibe mensagem de erro. */
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