# AGENTS.md

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

The contract for coding agents working on taylorpowers.com.

## Map

- Every page except `404.html` is **generated** by `scripts/build_work.py` from `PROJECTS` and `ABOUT`: `index.html` (carousel), `work/index.html` (grid), `about/index.html` and `work/<slug>/index.html` (one case study per project). Change the data or templates there, run `python3 scripts/build_work.py`, and never hand-edit the generated HTML.
- `assets/main.css` styles every page; `assets/carousel.js` runs the home carousel; `assets/about.js` the About statement; `assets/site.js` runs on case pages (hero video, Vimeo heroes, lightbox). Every part of the scripts must guard for missing elements.
- Docs: [README.md](README.md) and [docs/README.md](docs/README.md); start with [docs/STATUS.md](docs/STATUS.md).

## Commands

| Command | What |
|---|---|
| `python3 -m http.server 5277` | Preview (or the `taylorpowers` config in `~/Strange/.claude/launch.json`) |
| `python3 scripts/build_work.py` | Regenerate the case pages |
| `node scripts/docs-check.mjs` | Docs harness; it's in `enforce` mode, so fix the docs, never the checker copy |
| `git push origin main` (as acific) | Deploy (GitHub Pages) |

## Invariants

1. **Facts only from [docs/CONTENT.md](docs/CONTENT.md)** sources: Taylor's resume (v9), the owner's own statements and the public coverage listed there. Never invent numbers, credits or roles.
2. **No scroll-driven animation and no scroll-jacking libraries** (one owner-requested exception: the About page's sideways-scrolling services row on desktop, matched to the reference template). Animate `transform` and `opacity` only. Pause off-screen video. See [docs/DECISIONS.md](docs/DECISIONS.md).
3. **No "AI-made" decoration:** gradient text, glow blobs, grain, mono numbered eyebrows, italic-serif accent words, count-ups, pill chips, marquees. (Exception: the home page's logo strip, which is in the owner's own Framer design.)
4. **Ask the owner before any redesign.** They have rejected several guessed directions.
5. **Content-Security-Policy:** every page has a CSP `<meta>` (`CSP` in `scripts/build_work.py` for every generated page, and `404.html`; keep the two identical). Scripts and styles only from the site, no inline executable `<script>` or `style=` (the home page's `application/ld+json` search-profile block is data, not script, and is allowed); fonts from Google Fonts or self-hosted (`font-src 'self'`); frames only from player.vimeo.com, www.youtube-nocookie.com and players.brightcove.net (LAFC's films). A new outside origin has to be added to both, or the browser blocks it.
6. **Cache stamp:** after a CSS or JS change, bump `V` in `scripts/build_work.py` and `?v=` in `404.html` together, then rebuild.
7. **Keep the phone number off the site.**
8. **Pass the visual check before pushing:** preview at desktop and phone (375 px) widths, no horizontal overflow, no console errors.

## Conventions

- Commit with no AI or tool attribution lines.
- Push as acific. The repo moved from ShaneRealm/taylorpowers.com on 2026-11-20; that old repo is stale.
- Update the docs in the same commit as the change, and refresh each doc's `Last verified` line.
- Media: re-save video with the index at the front (fast start). Clips are silent 720p at about 2 Mbps. Don't upscale images.

## Sharing a checkout

Run `git status` first; commit only your own files. Don't switch the active `gh` account globally.
