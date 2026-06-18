const menuToggle =  document.querySelector('.menu-toggle')
const navLinks = document.querySelector('.nav-links')


// isso é um ouvinte de evento, ao clicar vai fazer a função abaixo
menuToggle.addEventListener('click', () => {
    menuToggle.classList.toggle('active'); //alternar = toggle
    navLinks.classList.toggle('active');
})