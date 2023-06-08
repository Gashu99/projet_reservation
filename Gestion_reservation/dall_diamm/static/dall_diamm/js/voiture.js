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
document.getElementById("myButton").addEventListener("click", function() {
    window.location.href = "{% url '../dall_diamm/template/reservationVoiture.html' %}";
});

function toggleDropdown(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    if (dropdown.style.display === "none") {
        dropdown.style.display = "block";
    } else {
        dropdown.style.display = "none";
    }
}