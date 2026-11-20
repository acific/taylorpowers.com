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

// Video loops: the clip loads on first use. Mouse: plays on hover. Touch: plays while the card
// is in the middle of the screen. Off screen it's paused. Skipped under reduced motion.
const clipCards = [...document.querySelectorAll('.card[data-clip]')];
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const start = (card) => {
  const v = card.querySelector('.clip'); if (!v) return;
  if (!v.src) v.src = card.dataset.clip;
  v.play().then(() => card.classList.add('playing')).catch(() => {});
};
const stop = (card) => {
  const v = card.querySelector('.clip'); if (!v) return;
  card.classList.remove('playing'); v.pause();
};
if (clipCards.length && !reduce) {
  if (matchMedia('(hover: hover) and (pointer: fine)').matches) {
    clipCards.forEach(c => {
      c.addEventListener('mouseenter', () => start(c));
      c.addEventListener('mouseleave', () => stop(c));
    });
  } else {
    const mid = new IntersectionObserver((entries) => {
      entries.forEach(e => (e.isIntersecting ? start : stop)(e.target));
    }, { rootMargin: '-35% 0px -35% 0px' });
    clipCards.forEach(c => mid.observe(c));
  }
}
