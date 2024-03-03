const divo = document.querySelectorAll('.ele');

divo.forEach(function (elem) {
    elem.addEventListener('mousedown', () => {
        elem.classList.toggle('active')
    });
});
