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
