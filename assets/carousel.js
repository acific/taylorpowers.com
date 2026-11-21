// Home page carousel: the projects on an arc. The centre card opens its case study; the others
// (and the arrows, arrow keys and swipes) bring a project to the centre. Transform/opacity only.
(() => {
  const ring = document.querySelector('.ring');
  if (!ring) return;
  const slides = [...ring.querySelectorAll('.slide')];
  const infos = [...document.querySelectorAll('.info')];
  const n = slides.length;
  let current = 0;

  // Position by distance from the centre, measured on the reference at several window sizes. Everything
  // scales with the card: x offset and drop in card widths, then scale and tilt in degrees.
  const ARC = [[0, 0, 1, 0], [.914, .207, .669, 6], [1.552, .396, .495, 12], [2.104, .526, .495, 16]];

  const layout = () => {
    const card = slides[0].clientWidth || 299;
    const kx = card * (innerWidth < 810 ? .62 : 1);  // phones: pull the side cards in so they peek
    const ky = card;
    slides.forEach((s, i) => {
      let d = i - current;
      if (d > n / 2) d -= n;
      if (d < -n / 2) d += n;
      const a = Math.abs(d), sign = Math.sign(d);
      const [x, y, sc, r] = ARC[Math.min(a, 3)];
      const far = a > 3;
      s.style.transform = `translate(${sign * (far ? x + .4 : x) * kx}px, ${y * ky}px) rotate(${sign * r}deg) scale(${far ? .4 : sc})`;
      s.style.opacity = far ? '0' : '1';
      s.style.zIndex = String(10 - a);
      s.style.pointerEvents = far ? 'none' : '';
      s.tabIndex = a === 0 ? 0 : -1;
      s.classList.toggle('is-center', a === 0);
      s.setAttribute('aria-hidden', a === 0 ? 'false' : 'true');
    });
    infos.forEach((el, i) => { el.hidden = i !== current; });
    films();
  };

  // Cards with a film play it the whole time while they're on screen (muted, looping): every visible
  // card loads and plays its film; cards pushed off the arc pause. Side cards stay black and white like
  // the stills. Skipped when the visitor prefers reduced motion.
  const still = matchMedia('(prefers-reduced-motion: reduce)');
  const films = () => slides.forEach((s, i) => {
    const v = s.querySelector('.slide-video');
    if (!v) return;
    let d = Math.abs(i - current); d = Math.min(d, n - d);
    if (d <= 3 && !still.matches && !document.hidden) {
      if (!v.src) { v.src = v.dataset.src; v.addEventListener('playing', () => v.classList.add('is-playing')); }
      v.play().catch(() => {});
    } else {
      v.pause();
    }
  });
  document.addEventListener('visibilitychange', films);

  const go = (i) => { current = (i + n) % n; layout(); };

  slides.forEach((s, i) => s.addEventListener('click', (ev) => {
    if (i !== current) { ev.preventDefault(); go(i); }
  }));
  document.querySelector('.arrow.prev')?.addEventListener('click', () => go(current - 1));
  document.querySelector('.arrow.next')?.addEventListener('click', () => go(current + 1));
  addEventListener('keydown', (ev) => {
    if (ev.key === 'ArrowLeft') go(current - 1);
    if (ev.key === 'ArrowRight') go(current + 1);
  });

  // Swipe
  let x0 = null;
  ring.addEventListener('pointerdown', (ev) => { x0 = ev.clientX; });
  ring.addEventListener('pointerup', (ev) => {
    if (x0 === null) return;
    const dx = ev.clientX - x0; x0 = null;
    if (Math.abs(dx) > 40) { ev.preventDefault(); go(current + (dx < 0 ? 1 : -1)); }
  });
  // Block the click that ends a swipe from opening the centre card
  let dragged = false;
  ring.addEventListener('pointermove', (ev) => { if (x0 !== null && Math.abs(ev.clientX - x0) > 8) dragged = true; });
  ring.addEventListener('click', (ev) => { if (dragged) { ev.preventDefault(); ev.stopPropagation(); dragged = false; } }, true);

  // Mouse wheel and trackpad: one project per gesture. Deltas add up until they pass a threshold,
  // then further scrolling is ignored until the gesture pauses, so a trackpad flick moves one step.
  let acc = 0, locked = false, idle;
  addEventListener('wheel', (ev) => {
    ev.preventDefault();
    const d = Math.abs(ev.deltaX) > Math.abs(ev.deltaY) ? ev.deltaX : ev.deltaY;
    clearTimeout(idle);
    idle = setTimeout(() => { acc = 0; locked = false; }, 180);
    if (locked) return;
    acc += d;
    if (Math.abs(acc) > 30) { go(current + (acc > 0 ? 1 : -1)); acc = 0; locked = true; }
  }, { passive: false });

  addEventListener('resize', layout);
  // Cards start stacked at the centre (CSS) and fan out on the next frame (timer as a fallback)
  requestAnimationFrame(() => requestAnimationFrame(layout));
  setTimeout(layout, 120);
})();
