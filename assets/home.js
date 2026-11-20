// Home page: fade-in on scroll and the left column pinning. Guards for missing elements.
// Fade-in on scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Left column: stick to the bottom of the viewport once its end is reached
const info = document.getElementById('info');
if (info) {
const pin = () => { info.style.top = Math.min(0, innerHeight - info.offsetHeight) + 'px'; };
addEventListener('resize', pin); addEventListener('load', pin); pin();
}
