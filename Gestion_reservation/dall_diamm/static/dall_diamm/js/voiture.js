window.addEventListener('scroll', function() {
    var scrollArrow = document.querySelector('.scroll-arrow');
    if (window.scrollY > 200) {
        scrollArrow.classList.add('active');
    } else {
        scrollArrow.classList.remove('active');
    }
});

document.querySelector('.scroll-arrow').addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
