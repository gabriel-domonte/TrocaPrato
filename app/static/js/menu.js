const menu = document.getElementById('nav-menu');
const button = document.querySelector('.botao-burguer');


/* toggle - alterna classe a cada clique*/
button.addEventListener('click', () => {
    menu.classList.toggle('aberto');
    button.classList.toggle('ativo');
});