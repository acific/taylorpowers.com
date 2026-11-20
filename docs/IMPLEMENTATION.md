# Implementation

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

How each part is built, file by file.

## `index.html` (home)

The owner's Framer design (willing-iris-827866.framer.app), rebuilt as static HTML on 2026-11-20. Styles are in `assets/home.css`, behavior in `assets/home.js`; neither is shared with the case pages.

Two columns (`.layout`), stacked into one below 810 px:

1. **Left column** (`aside.info`, sticky). `home.js` sets its `top` (and the card grid's) to `min(0, viewport height − its height)`, so whichever column is shorter stops at its end while the longer one keeps scrolling.
   - Header: avatar (`assets/home/avatar.jpg`), name, "Brand & Marketing Executive", bio and the **Let's connect** button (LinkedIn).
   - Logo strip (`.marquee`): eleven logos from `assets/home/logos/` (named by brand), each trimmed to its artwork with a transparent background. CSS shows them all in one soft dark tone (`filter: brightness(0)` at 42% opacity, darker on hover) and sizes each by hand (`.h16`–`.h27`) so they carry the same visual weight. Duplicated once and scrolled with a CSS animation (45 s, paused on hover, stopped under reduced motion). The owner's design includes it, as an exception to the no-marquee rule (see DECISIONS).
   - **Services.** Five numbered areas with their sub-services.
   - **Experience.** Five roles (title, company, years, one line).
   - **Reach out.** The mailto link, the copyright and a back-to-top button.
2. **Project cards** (`section.work`, sticky like the left column). Two columns (`.col`) of thirteen cards, split in page order so the two columns end at about the same height (by image aspect ratio). Each card has an order class `.o1`–`.o13`; below 810 px the columns dissolve (`display: contents`) and the order classes put the cards back in their original sequence. The cards (`.card`) with an image from `assets/home/work/`, a title and a role. Seven open their case page under `work/` (NASCAR, FLEX × LAFC, UFC & WWE, MotoGP, EGO Z6 → `work/ego/`, SKIL, Mr. Brainwash → `work/superfile-art-car/`); the rest link to outside coverage, and Lefty Out There has no link.
   - **Titles on hover:** with a mouse or trackpad (`hover: hover` and `pointer: fine`), each card's title and its dark gradient fade in on hover or keyboard focus. On touch screens they're always shown.
   - **Sharper photos:** each image has a `srcset` with the 1024 px file and an `@2x.jpg` (up to 2048 px, re-saved as JPEG quality 80 from the Framer originals), so only large or high-density screens download the bigger one.
   - **Clips:** FLEX × LAFC (`flex-falcon`), SKIL (`skil`) and EGO Z6 (`ego`) carry `data-clip` and a `<video class="clip">`. `home.js` sets the source on first use; with a mouse it plays on hover and pauses on leave, on touch it plays while the card is in the middle 30% of the screen and pauses otherwise. Skipped under reduced motion.

Motion shares one easing (`--ease`). The page fades in on load, and pages crossfade when moving between the home page and a case page (`@view-transition`, in browsers that support it). Card photos fade in once loaded (`.js .card img:not(.loaded)`; `home.js` adds `js` and `loaded`), and zoom 2% on hover. The bio's first sentence is in ink (`.bio b`); experience years sit in their own right-aligned column with tabular figures. Every `.reveal` element fades up once as it enters the screen (an IntersectionObserver in `home.js`; `opacity` and `transform` only).

## `scripts/build_work.py` (case pages)

`PROJECTS` is a list of dicts with these keys:

- `slug`, `client`, `title`, `year`, `role`, `disciplines`
- `hero_img`, and optionally `hero_clip` (a local loop), `hero_vimeo` (an HD Vimeo background) and `hero_light` (a white render, which gets a dark title band)
- `lead`, `body` (paragraphs) and `figures` (number, label)
- optionally `film` (`yt`, `vimeo` or `video`, plus `title`), `link` (label, URL) and `gallery` (shown only with two or more images)

`page()` renders the template. Each page has a hero, a meta list (client, year, role, disciplines), text, actions (**Watch the film**, a coverage link), figures, a gallery, and a **Next project** link that wraps from the last to the first. It also sets per-page `<title>`, description and Open Graph tags. Pages use root-absolute paths (`/assets/...`), so they work only from the site root, which is how Pages and the local preview serve them.

`V` sets the `?v=` cache stamp on the case pages' CSS and JS; keep it equal to the stamp in `index.html`.

## `assets/site.js`

Used by the case pages (it was also the old home page's script; the Intro, Reel, Clips and Clock parts now find no elements and do nothing). The script is one IIFE, and every part guards for missing elements.

| Part | Details |
|---|---|
| Intro | Removes `#intro` after 1.3 s, or at once if seen this session or under reduced motion |
| Visibility | One IntersectionObserver pauses any video off screen. Videos marked `data-auto` (the reel, case heroes) resume when visible |
| Reel | Sound toggle, progress line, and the header's `.solid` state |
| HD heroes | Listens for Vimeo `play`, `playProgress` and `timeupdate` messages from `.case-hero-vimeo`. On the first one it fades the iframe in (`.on`) and pauses the local clip. Under reduced motion the iframe is removed |
| Clips | `startClip` and `stopClip` set `src` from `data-src` on first use and toggle `.playing`. Hover drives them on desktop; a centered-on-screen observer (`rootMargin -35%`) drives them on touch |
| Fade-ins | `.tile` elements fade up once (`html.js`, `.in`) |
| Clock | `Intl.DateTimeFormat` for America/Chicago, refreshed every 15 s |
| Lightbox | Builds a `<video>` or `<iframe>` and pauses every other video. On close it clears the frame and resumes visible `data-auto` videos |

## `assets/case.css` (case pages)

The case pages' look, matching the home page: white, Switzer (`@font-face` from `/assets/home/fonts/`), `--ink #0a0a0a`, `--muted #757575`, `--line #e3e3e3`, `--soft #f4f4f4`, content in a 1180 px `.wrap`.

- **Top bar** (`.case-bar`, sticky, frosted white): avatar and name linking home (`.who`), **← All work** (`.back`).
- **Hero** (`.case-hero`): a rounded 16:9 frame (at most 78vh) holding the image, the local clip or the Vimeo background (`.case-hero-vimeo`, full-width 16:9, fades in with `.on`). `hero_light` renders (`.case-hero-media.light`) are contained on light grey.
- **Head** (`.case-head`): client in grey, then the title.
- **Body** (`.case-body`): the meta list beside the lead and text; **Watch the film** (`.btn.solid`) and the coverage link (`.btn`); figures (`.case-figures`) and gallery (`.case-gallery`) span both columns. One column below 860 px.
- **Next project** (`.next`) with a round arrow, then the footer (`.case-foot`) with the contact address.
- **Lightbox** (`.player`): the dialog `site.js` opens for films.
- **Reduced motion:** transitions off.

`assets/site.css` (the old dark Archivo styles) was removed on 2026-11-20.

## Media

| Folder | Contents | How it was made |
|---|---|---|
| `assets/video/` | `reel.mp4` (1080p H.264, 45 s, about 5.6 MB) and `reel-poster.jpg` | The owner's showreel, re-saved with the index at the front (fast start) |
| `assets/clips/` | `ego`, `flex-falcon`, `flex-soccer`, `skil` (`.mp4` and `.jpg`) | Cut silent from the reel (EGO 4.4–7.9 s, falcon 19.4–22.6 s, soccer 30.0–34.6 s, SKIL 26.9–30.2 s), 1280×720 H.264 at about 2.2 Mbps, about 1 MB each |
| `assets/img/` | `daytona-race`, `ufc-wwe`, `motogp-superfile`, `art-car`, `vm-1014838410`, `flex-lafc-welcome`, `taylor-portrait` | See [CONTENT.md](CONTENT.md) for the source of each |
| `assets/logos/` | 13 SVGs | Wikimedia Commons, Simple Icons and the brands' own sites |

## Gaps

- No HD footage yet for EGO, SKIL, MotoGP, UFC & WWE or Daytona.
- The portrait is 800×800.
- GitHub Pages can't set response headers: the CSP and referrer policy are `<meta>` tags in every page (the case pages get them from the template in `scripts/build_work.py`); HSTS and anti-framing headers aren't possible there, and the domain has no DMARC or CAA records yet. See [OPERATIONS.md](OPERATIONS.md).
