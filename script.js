// Smooth scroll navigation
function scrollToSection(e){document.getElementById(e).scrollIntoView({behavior:"smooth"})}

// Modal functionality
const modal=document.getElementById("modal"),modalYear=document.getElementById("modalYear"),modalTitle=document.getElementById("modalTitle"),modalText=document.getElementById("modalText");
document.querySelectorAll(".timeline-card").forEach(e=>{e.addEventListener("click",()=>{modalYear.textContent=e.dataset.year,modalTitle.textContent=e.dataset.title,modalText.textContent=e.dataset.text,modal.classList.remove("hidden")})});
function closeModal(){modal.classList.add("hidden")}

// Neuro-paint with debouncing
let paintTimeout;
function paintReact(e,t){clearTimeout(paintTimeout);const n=t.getBoundingClientRect(),o=e.clientX-n.left,a=e.clientY-n.top;t.querySelector(".neuro-paint").style.background=`radial-gradient(circle at ${o}px ${a}px,#a78bfa,#22d3ee,#f472b6,#fcd34d 80%)`}
function paintReset(e){paintTimeout=setTimeout(()=>{e.querySelector(".neuro-paint").style.background=""},50)}

// Quote carousel
const quotes=["Я не рисую то, что вижу. Я рисую то, что другие боятся увидеть.","Каждая картина — это дверь. Вопрос только, хватит ли у тебя смелости войти.","Цвет — это эмоция, которую ещё не придумали назвать.","Когда краска начинает жить своей жизнью — значит, я сделал всё правильно.","Где-то между снами и явью есть место, где я до сих пор работаю."];
let currentQuote=0,quoteInterval;
const carousel=document.querySelector(".quote-carousel .quotes p"),pauseBtn=document.getElementById("pauseBtn");
function showQuote(){const e=carousel.parentElement;e.style.opacity="0",setTimeout(()=>{carousel.textContent='"'+quotes[currentQuote]+'"',e.style.opacity="1",currentQuote=(currentQuote+1)%quotes.length},1e3)}
function startQuotes(){showQuote(),quoteInterval=setInterval(showQuote,7e3)}
function pauseQuotes(){clearInterval(quoteInterval),pauseBtn.textContent="Продолжить",pauseBtn.onclick=()=>{startQuotes(),pauseBtn.textContent="Пауза",pauseBtn.onclick=pauseQuotes}}
startQuotes();

// Intersection Observer for animations
const observer=new IntersectionObserver(e=>{e.forEach(e=>{e.isIntersecting&&(e.target.classList.add("opacity-100","translate-y-0"),observer.unobserve(e.target))})},{threshold:.2,rootMargin:"0px 0px -50px 0px"});
document.querySelectorAll(".timeline-card,.neuro-canvas,section").forEach(e=>{e.classList.add("opacity-0","translate-y-10"),e.style.transition="all 1s cubic-bezier(0.22,1,0.36,1)",observer.observe(e)});

// Lazy load background images
if("loading"in HTMLImageElement.prototype){document.querySelectorAll(".back,.mid").forEach(e=>{e.style.backgroundImage&&(e.dataset.bg=e.style.backgroundImage,e.style.backgroundImage="none");const t=new IntersectionObserver(t=>{t.forEach(t=>{t.isIntersecting&&(e.style.backgroundImage=e.dataset.bg,observer.unobserve(e))})});t.observe(e)})}
