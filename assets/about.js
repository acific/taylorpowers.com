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

// Desktop services: while the band scrolls past, slide the row of panels sideways so the last one
// ends at the right edge. The section is made tall enough to hold the sideways distance.
(() => {
  const wrap = document.querySelector('.svcs'), track = document.querySelector('.svcs-track');
  if (!wrap || !track) return;
  const wide = matchMedia('(min-width: 1200px)');
  let dist = 0;
  const size = () => {
    if (!wide.matches) { wrap.style.height = ''; track.style.transform = ''; return; }
    dist = Math.max(0, track.scrollWidth - innerWidth);
    wrap.style.height = `${innerHeight + dist}px`;
    move();
  };
  const move = () => {
    if (!wide.matches) return;
    const top = wrap.getBoundingClientRect().top;
    const p = Math.min(1, Math.max(0, -top / Math.max(1, dist)));
    track.style.transform = `translate3d(${-p * dist}px, 0, 0)`;
  };
  addEventListener('scroll', () => requestAnimationFrame(move), { passive: true });
  addEventListener('resize', size); wide.addEventListener('change', size);
  addEventListener('load', size); size();
})();
