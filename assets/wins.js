// Wins page: chapters and photos fade up once as they come into view, and each chapter's photo
// settles from a slight zoom. Triggered on entry, not tied to scroll position.
(() => {
  const items = [...document.querySelectorAll('.reveal, .win-hero')];
  if (!items.length || !('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('js');
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { threshold: 0.15, rootMargin: '0px 0px -6% 0px' });
  items.forEach((el) => io.observe(el));
})();
