// Плавный скролл
function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
}

// Модальное окно хронологии
document.querySelectorAll('.timeline-card').forEach(card => {
    card.addEventListener('click', () => {
        document.getElementById('modalYear').textContent = card.dataset.year;
        document.getElementById('modalTitle').textContent = card.dataset.title;
        document.getElementById('modalText').textContent = card.dataset.text;
        document.getElementById('modal').classList.remove('hidden');
    });
});

function closeModal() {
    document.getElementById('modal').classList.add('hidden');
}

// Нейро-краска
function paintReact(e, el) {
    const rect = el.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    el.querySelector('.neuro-paint').style.background = `radial-gradient(circle at ${x}px ${y}px, #a78bfa, #22d3ee, #f472b6, #fcd34d 80%)`;
}

function paintReset(el) {
    el.querySelector('.neuro-paint').style.background = '';
}

// Цитаты карусель
const quotes = [
    "Я не рисую то, что вижу. Я рисую то, что другие боятся увидеть.",
    "Каждая картина — это дверь. Вопрос только, хватит ли у тебя смелости войти.",
    "Цвет — это эмоция, которую ещё не придумали назвать.",
    "Когда краска начинает жить своей жизнью — значит, я сделал всё правильно.",
    "Где-то между снами и явью есть место, где я до сих пор работаю."
];
let current = 0;
let interval;
const carousel = document.querySelector('.quote-carousel .quotes p');

function showQuote() {
    carousel.parentElement.style.opacity = 0;
    setTimeout(() => {
        carousel.textContent = '"' + quotes[current] + '"';
        carousel.parentElement.style.opacity = 1;
        current = (current + 1) % quotes.length;
    }, 1000);
}

function startQuotes() {
    showQuote();
    interval = setInterval(showQuote, 7000);
}

function pauseQuotes() {
    clearInterval(interval);
    document.getElementById('pauseBtn').textContent = 'Продолжить';
    document.getElementById('pauseBtn').onclick = () => {
        startQuotes();
        document.getElementById('pauseBtn').textContent = 'Пауза';
        document.getElementById('pauseBtn').onclick = pauseQuotes;
    };
}

startQuotes();

// Анимация появления
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('opacity-100', 'translate-y-0');
        }
    });
}, { threshold: 0.2 });

document.querySelectorAll('.timeline-card, .neuro-canvas, section').forEach(el => {
    el.classList.add('opacity-0', 'translate-y-10');
    el.style.transition = 'all 1s cubic-bezier(0.22, 1, 0.36, 1)';
    observer.observe(el);
});
