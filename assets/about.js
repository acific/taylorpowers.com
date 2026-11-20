// About page: the statement darkens word by word once, when it first comes into view.
// (Triggered on entry, not tied to scroll position.)
(() => {
  const st = document.querySelector('.statement');
  if (!st) return;
  [...st.querySelectorAll('span')].forEach((w, i) => { w.style.transitionDelay = `${i * 45}ms`; });
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) { st.classList.add('in'); io.disconnect(); } });
  }, { threshold: 0.4 });
  io.observe(st);
})();

// Services deck: one slide at a time. From 810px the band pins and the page scroll steps through the
// slides (the section is one screen tall per slide); the arrows and the progress segments scroll to a slide.
// Smaller screens show the slides stacked, with no pinning.
(() => {
  const deck = document.querySelector('.deck');
  if (!deck) return;
  const slides = [...deck.querySelectorAll('.deck-slide')];
  const segs = [...deck.querySelectorAll('.deck-seg')];
  const count = deck.querySelector('.deck-count');
  const prev = deck.querySelector('.deck-prev'), next = deck.querySelector('.deck-next');
  const n = slides.length;
  const wide = matchMedia('(min-width: 810px)');
  let current = -1;
  const step = () => innerHeight * 0.9;
  const show = (i) => {
    if (i === current) return;
    current = i;
    slides.forEach((s, k) => { s.classList.toggle('is-on', k === i); s.inert = wide.matches && k !== i; });
    segs.forEach((s, k) => s.classList.toggle('is-on', k <= i));
    if (count) count.textContent = `${String(i + 1).padStart(2, '0')} / ${String(n).padStart(2, '0')}`;
    if (prev) prev.disabled = i === 0;
    if (next) next.disabled = i === n - 1;
  };
  const size = () => {
    deck.style.height = wide.matches ? `${innerHeight + (n - 1) * step()}px` : '';
    if (!wide.matches) slides.forEach((s) => { s.inert = false; });
    current = -1; move();
  };
  const move = () => {
    if (!wide.matches) return;
    const p = -deck.getBoundingClientRect().top / step();
    show(Math.min(n - 1, Math.max(0, Math.round(p))));
  };
  const go = (i) => {
    i = Math.min(n - 1, Math.max(0, i));
    const top = deck.getBoundingClientRect().top + scrollY + i * step();
    scrollTo({ top, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  };
  prev?.addEventListener('click', () => go(current - 1));
  next?.addEventListener('click', () => go(current + 1));
  segs.forEach((s, k) => s.addEventListener('click', () => go(k)));
  deck.querySelectorAll('[data-go]').forEach((b) => b.addEventListener('click', () => wide.matches ? go(+b.dataset.go) : slides[+b.dataset.go]?.scrollIntoView({ behavior: 'smooth', block: 'center' })));
  addEventListener('scroll', () => requestAnimationFrame(move), { passive: true });
  addEventListener('resize', size); wide.addEventListener('change', size);
  size();
})();
