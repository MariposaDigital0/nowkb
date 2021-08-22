const nav_btn = document.getElementById('hm-btn')
const mob_menu = document.getElementById('mb-nav');

nav_btn.addEventListener('click', () => {
    mob_menu.classList.toggle('is-active');
});



