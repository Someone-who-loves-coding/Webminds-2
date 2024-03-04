const divo = document.querySelectorAll('.ele');

divo.forEach(function (elem) {
    elem.addEventListener('mousedown', () => {
        elem.classList.toggle('active')
    });
});

document.querySelector('.input.submit').addEventListener('click', () => {
    document.querySelector('.input.submit').toggle('active')
});
