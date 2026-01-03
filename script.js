// Optimized JavaScript with performance improvements
(function() {
    'use strict';
    
    // Debounce function for performance
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // Throttle function for mousemove events
    function throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
    
    // Smooth scroll
    window.scrollToSection = function(id) {
        const el = document.getElementById(id);
        if (el) {
            el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    };
    
    // Modal functionality
    function initModal() {
        const modal = document.getElementById('modal');
        const cards = document.querySelectorAll('.timeline-card');
        
        cards.forEach(card => {
            card.addEventListener('click', () => {
                const year = card.dataset.year;
                const title = card.dataset.title;
                const text = card.dataset.text;
                
                document.getElementById('modalYear').textContent = year;
                document.getElementById('modalTitle').textContent = title;
                document.getElementById('modalText').textContent = text;
                modal.classList.remove('hidden');
            });
        });
    }
    
    window.closeModal = function() {
        document.getElementById('modal').classList.add('hidden');
    };
    
    // Optimized neuro-paint with throttling
    const paintReactThrottled = throttle(function(e, el) {
        const rect = el.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const paintEl = el.querySelector('.neuro-paint');
        if (paintEl) {
            paintEl.style.background = `radial-gradient(circle at ${x}px ${y}px, #a78bfa, #22d3ee, #f472b6, #fcd34d 80%)`;
        }
    }, 16); // ~60fps
    
    window.paintReact = function(e, el) {
        paintReactThrottled(e, el);
    };
    
    window.paintReset = function(el) {
        const paintEl = el.querySelector('.neuro-paint');
        if (paintEl) {
            paintEl.style.background = '';
        }
    };
    
    // Quotes carousel
    const quotes = [
        "Я не рисую то, что вижу. Я рисую то, что другие боятся увидеть.",
        "Каждая картина — это дверь. Вопрос только, хватит ли у тебя смелости войти.",
        "Цвет — это эмоция, которую ещё не придумали назвать.",
        "Когда краска начинает жить своей жизнью — значит, я сделал всё правильно.",
        "Где-то между снами и явью есть место, где я до сих пор работаю."
    ];
    
    let currentQuote = 0;
    let quoteInterval;
    const carousel = document.querySelector('.quote-carousel .quotes p');
    const carouselParent = carousel?.parentElement;
    
    function showQuote() {
        if (!carouselParent || !carousel) return;
        
        carouselParent.style.opacity = '0';
        setTimeout(() => {
            carousel.textContent = '"' + quotes[currentQuote] + '"';
            carouselParent.style.opacity = '1';
            currentQuote = (currentQuote + 1) % quotes.length;
        }, 1000);
    }
    
    function startQuotes() {
        if (!carousel) return;
        showQuote();
        quoteInterval = setInterval(showQuote, 7000);
    }
    
    window.pauseQuotes = function() {
        clearInterval(quoteInterval);
        const btn = document.getElementById('pauseBtn');
        if (btn) {
            btn.textContent = 'Продолжить';
            btn.onclick = function() {
                startQuotes();
                btn.textContent = 'Пауза';
                btn.onclick = pauseQuotes;
            };
        }
    };
    
    // Intersection Observer for animations
    function initAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('opacity-100', 'translate-y-0');
                    observer.unobserve(entry.target); // Stop observing once animated
                }
            });
        }, { threshold: 0.2 });
        
        const animatedElements = document.querySelectorAll('.timeline-card, .neuro-canvas, section');
        animatedElements.forEach(el => {
            el.classList.add('opacity-0', 'translate-y-10');
            el.style.transition = 'all 1s cubic-bezier(0.22, 1, 0.36, 1)';
            observer.observe(el);
        });
    }
    
    // Lazy load background images
    function lazyLoadBackgrounds() {
        const layers = document.querySelectorAll('.layer.back, .layer.mid');
        layers.forEach(layer => {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        // Background images are already in CSS, but we can optimize loading
                        observer.unobserve(entry.target);
                    }
                });
            }, { rootMargin: '50px' });
            observer.observe(layer);
        });
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    function init() {
        initModal();
        initAnimations();
        lazyLoadBackgrounds();
        startQuotes();
    }
})();
