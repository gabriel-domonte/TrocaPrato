const menu = document.getElementById('nav-menu');
const button = document.querySelector('.botao-burguer');

button.addEventListener('click', () => {
    menu.classList.toggle('ativo');
    button.classList.toggle('aberto');
});