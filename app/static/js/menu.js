// guardando os elementos do html
const menu = document.getElementById('nav-menu');
const button = document.querySelector('.botao-burguer');


// toggle - alterna classe a cada clique
button.addEventListener('click', () => {
    // exibição do navegador
    menu.classList.toggle('aberto');
    // mudança de animação do botão
    button.classList.toggle('ativo');
});