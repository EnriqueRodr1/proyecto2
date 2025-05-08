// MENU RESPONSIVE
document.querySelector(".menu-btn").addEventListener("click", function () {
    document.querySelector(".mobile-menu").classList.toggle("show");
});

// SLIDER PRINCIPAL - AUTOMÁTICO Y MANUAL
const slides = document.querySelectorAll(".slide");
const prevBtn = document.querySelector(".prev");
const nextBtn = document.querySelector(".next");
let currentIndex = 0;

// Función para actualizar el slider
function updateSlider() {
    slides.forEach((slide, i) => {
        slide.style.opacity = i === currentIndex ? "1" : "0";
    });
}

// Función para cambiar de slide
function changeSlide(direction) {
    slides[currentIndex].classList.remove("active");

    if (direction === "next") {
        currentIndex = (currentIndex + 1) % slides.length;
    } else if (direction === "prev") {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    }

    slides[currentIndex].classList.add("active");
    updateSlider();
}

// Eventos para los botones del slider principal
prevBtn.addEventListener("click", () => changeSlide("prev"));
nextBtn.addEventListener("click", () => changeSlide("next"));

// Cambio automático cada 5 segundos
let sliderInterval = setInterval(() => changeSlide("next"), 5000);

// Pausar el slider automático cuando el usuario interactúe
prevBtn.addEventListener("mouseenter", () => clearInterval(sliderInterval));
nextBtn.addEventListener("mouseenter", () => clearInterval(sliderInterval));
prevBtn.addEventListener("mouseleave", () => sliderInterval = setInterval(() => changeSlide("next"), 5000));
nextBtn.addEventListener("mouseleave", () => sliderInterval = setInterval(() => changeSlide("next"), 5000));

// Inicializar el slider
updateSlider();

// SLIDER DE SERVICIOS - AUTOMÁTICO Y MANUAL
const serviceSlides = document.querySelectorAll(".service-banner");
let serviceIndex = 0;

// Función para cambiar los servicios
function changeServiceSlide() {
    serviceSlides.forEach((slide, i) => {
        slide.style.opacity = i === serviceIndex ? "1" : "0";
        slide.style.transform = i === serviceIndex ? "scale(1)" : "scale(0.9)";
    });

    serviceIndex = (serviceIndex + 1) % serviceSlides.length;
}

// Cambio automático cada 5 segundos
setInterval(changeServiceSlide, 2000);

// HEADER CAMBIA DE COLOR AL HACER SCROLL
window.addEventListener("scroll", function () {
    const header = document.querySelector("header");
    if (window.scrollY > 50) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
});

// ANIMACIÓN EN FAVORITOS Y RESERVA
document.querySelectorAll(".fav-btn").forEach(btn => {
    btn.addEventListener("click", function () {
        this.classList.toggle("active");
        this.style.background = this.classList.contains("active") ? "darkred" : "red";
    });
});

document.querySelectorAll(".reserve-btn").forEach(btn => {
    btn.addEventListener("click", function () {
        alert("Reserva realizada con éxito!");
    });
});






document.addEventListener('DOMContentLoaded', async () => {
    const tipoPista = new URLSearchParams(window.location.search).get('tipo');
    const pistaId = 1; // deberías obtenerlo dinámicamente según la pista seleccionada
    const fechaInput = document.getElementById('fecha');
    const horaSelect = document.getElementById('hora');

    async function actualizarHoras() {
        const fecha = fechaInput.value;
        if (!fecha) return;

        const res = await fetch(`http://localhost:8000/api/horas-disponibles/pistas?fecha=${fecha}&pista_id=${pistaId}`);
        const data = await res.json();

        horaSelect.innerHTML = '';
        const todas = [...data.disponibles, ...data.ocupadas].sort();

        todas.forEach(hora => {
            const option = document.createElement('option');
            option.value = hora;
            option.textContent = hora;
            if (data.ocupadas.includes(hora)) {
                option.style.color = 'red';
                option.disabled = true;
            }
            horaSelect.appendChild(option);
        });
    }

    fechaInput.addEventListener('change', actualizarHoras);
});