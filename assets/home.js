// Home page: fade-in on scroll and pinning of both columns. Guards for missing elements.
// Fade-in on scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Both columns: once a column is taller than the viewport, it scrolls to its end and then
// stays pinned there while the longer column keeps going.
const cols = [document.getElementById('info'), document.getElementById('work')].filter(Boolean);
const pin = () => cols.forEach(c => { c.style.top = Math.min(0, innerHeight - c.offsetHeight) + 'px'; });
addEventListener('resize', pin); addEventListener('load', pin); pin();
