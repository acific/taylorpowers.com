# Changelog

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

There are no version numbers; each entry is a date and the commits it covers. The `?v=` cache stamp is noted where it changed. There's no migration: it's a static site with no stored data or clients.

## 2026-11-20

- **About:** removed the full-width portrait (it stays as the home page's first card). Stamp 32.
- **All fourteen case studies expanded** from a second research pass (sources in docs/CONTENT.md): story sections with their own photos, Taylor's role, results and figures. New official images for UFC, MotoGP, FLEX, EGO, Wylie Co. and Digital Domain. **Every card graded** to one cinematic look by `scripts/grade_cards.sh` from originals in `sources/cards/`. Stamp 31.
- **About at desktop size matched to the template** (64 px statement, photo placement, light experience section, sideways-scrolling services row). **Cards in black and white** until centred (carousel) or hovered (Work, More to explore). Location now "Chicago / Los Angeles / Las Vegas". Stamp 30.
- **Carousel opens on Taylor:** the green portrait is the first card and opens About. **SuperFile × LAFC:** the owner's training-kit photo, four kit photos and LAFC's announcement film (Brightcove, added to the lightbox and the CSP). Stamp 29.
- **Carousel steps on the mouse wheel and trackpad** (one project per gesture). **About:** the owner's green portrait added full width between the opening photos and the experience band. Stamp 27.
- **Home scales with the window like the template:** the card grows from 299 px (tablet) to `13.1vw + 197px` (desktop), every arc position is in card units, the text sits in a centred 1520 px column; checked against the template at 1024, 1280, 1440 and 2000 px. Fixed sideways scrolling on phones. Stamp 26.
- **Home matched to the template at the pixel level** (type sizes, card frame and shadow, arc geometry, arrows, menu; "Works" in the menu). **About rebuilt like the template:** word-by-word statement, photo pair, black experience band, stacked full-screen service panels linking their projects, numbers, logos, closing pair; nine AI-generated images in `assets/about/`. New `assets/about.js`. Stamp 25.
- **SKIL case study** expanded from iSpot (2022 national TV spot for PWRCORE 40). The owner's Vimeo copy is blocked from embedding, so the film stays on SKIL's YouTube upload.
- **EGO Labs 2.0 case study** rewritten from egopowerplus.com/ridingmowers, the page the owner gave for it (next-generation Z6 riders); the unrelated mower video was dropped.
- **Whole site after the reference template:** a home-page carousel of all fourteen projects (`assets/carousel.js`), a Work grid, an About page (bio, portrait, experience, logos, services, numbers), and a case study for every project. Six new case studies (Wylie Co., Lefty Out There, SuperFile × LAFC, FLEX launch, Digital Domain, EGO Labs 2.0), and all fourteen expanded from public sources listed in docs/CONTENT.md. One generator builds every page; `assets/case.css` became `assets/main.css`; the old home's `home.css` and `home.js` are gone. Stamp 23.
- **Case pages matched to the reference template:** grey page, Baskervville serif headings and navigation (Google Fonts), square-cornered images, centred Home/Work navigation, the hero easing in, facts (Client, Year, Type), a "Taylor's role." row, the film as a full-width 3:2 still, square photo pairs, 4:3 More to explore cards, and a black footer with a rotating "Let's work together. / connect. / create." headline. The 404 page follows. Stamp 22.
- **Case pages redesigned** after a Framer portfolio template the owner liked: full-screen hero with title, summary and a client/year/role table; a black overview band; the film as a large still that opens the player; photos in pairs; Results./Coverage.; More to explore (next two projects); a black "Let's work together." footer. Switzer throughout. Stamp 21.
- **Polish:** a `404.html` page-not-found in the site's style (replaces GitHub's generic page); a schema.org `Person` search profile and canonical URL on the home page; a **SuperFile Brand Launch** card (second, linking to its case page), with the columns rebalanced for fourteen cards. Stamp 20.
- **Refinements:** one shared easing, page fade-in, crossfade between pages, photos that fade in once loaded and a gentler 2% hover zoom; the logo strip trimmed and evened out (one tone, matched visual weight, slower, pauses on hover); larger name, the bio's first sentence in ink, more space between sections, experience years in an aligned column; a new share card and tab icon in the light design, plus a home-screen icon. Stamp 19.
- **Case pages restyled** to match the home page: white, Switzer, a sticky bar with Taylor's name and **← All work**, the hero in a rounded frame with the title below it, black pill buttons, a round-arrow **Next project**, and the contact address `taylorraepowers@icloud.com` (as on the home page). New `assets/case.css`; `assets/site.css` and the Archivo font are gone. Stamp 18.
- **Premium pass:** card titles appear on hover (mouse only); 2× photos for large and high-density screens; silent clips on FLEX × LAFC, SKIL and EGO Z6; seven cards open their case pages. Case-page menu: About now goes to the top of the home page and Contact to its Reach out section. Fixed a bug from the two-column change where cards collapsed to zero height on phones. Stamp 17.
- **Two-column project cards:** the right side shows the thirteen cards in two height-balanced columns; both columns are pinned so the shorter one stops at its end. Phones keep one column in the original order. Stamp 16.
- **Home page redesign:** `index.html` now matches the owner's Framer design (willing-iris-827866.framer.app): two columns, Switzer, a logo strip, services, experience, contact and thirteen project cards linking to outside coverage. Its styles and script are `assets/home.css` and `assets/home.js`; its images and self-hosted fonts are in `assets/home/`. Contact is taylorraepowers@icloud.com, as in the design. Fixed from the Framer version: the mailto (it pointed at a template address), the Trackhouse NASCAR link and "Brand Lanches".
- **Security:** the CSP's `font-src` adds `'self'` for the self-hosted Switzer, in `index.html` and the case-page template. Case pages rebuilt. Stamp 15.
- **Hosting:** the repo moved from ShaneRealm/taylorpowers.com to acific/taylorpowers.com (the owner couldn't sign in to ShaneRealm). The domain was re-verified for acific and `www` now points to acific.github.io.

## 2026-10-22

- **Security:** every page has a Content-Security-Policy and a referrer policy as `<meta>` tags (GitHub Pages can't send headers): scripts and styles only from the site, Google Fonts, frames only from Vimeo and youtube-nocookie, `object-src 'none'`, `upgrade-insecure-requests`. The case pages get them from `scripts/build_work.py`. SECURITY.md updated.

- **Docs:** the full documentation set, the docs harness and the "where we left off" status page ([docs/STATUS.md](docs/STATUS.md)).

## 2026-10-21

- **605a391:** HD Vimeo background heroes on the FLEX × LAFC and SuperFile launch pages; FLEX "Welcome to the Club" key art in the gallery. Stamp 14.
- **2066bc7:** eight generated case-study pages (`scripts/build_work.py`); every work tile links to its page. Also a logo wall (13 logos), the portrait in About, a once-per-visit intro, a 1200×630 share card and an SVG favicon. Stamp 13.
- **790662b:** the accent changed from volt yellow to neon blue `#00a6ff`, with a glow on the headline. Stamp 12.
- **019dd20:** Head of Production, Head of Post-Production and Visual Effects Producer added at SuperFile and Realm. Stamp 11.
- **2ba1710:** content updated from resume v9:
  - figures of 60B+, 20,000+, 200+, 150K+, $20M+ and 25+
  - four capability pillars
  - studios and credits (*Dune: Part One*, *Terminator: Dark Fate*)
  - full titles in experience

  Stamp 10.
- **ff6ab7a:** the **cinematic, reel-first redesign**, now the current look. A full-screen reel with a sound toggle and progress line, work tiles with hover-to-play clips cut from the reel, condensed Archivo type, and no scroll effects.
- **7d19490:** replaced the masked-letter zoom with a GPU-only growing frame and dropped smooth scrolling (it stuttered).
- **0d022ae:** the reel inside the name with a scroll zoom, smooth scroll, parallax and a project index (reverted for stutter).
- **bc1d30a:** the showreel as the hero background; real race photography; the Mr. Brainwash art car.
- **344e3a5:** a cinematic hero slideshow and an asymmetric case layout.
- **5a1127e:** a restrained white editorial portfolio.
- **7fb275b:** a bright white theme.
- **349556a:** rebuilt as a full marketing site; contact changed to taylor@taylorpowers.com.
- **34d5320, 32958cf:** the CNAME re-saved to issue the HTTPS certificate.
- **DNS and email (outside the repo):**
  - DNS moved from GoDaddy parking to GitHub Pages, then to Cloudflare.
  - Cloudflare Email Routing set up for taylor@taylorpowers.com.

## Before 2026-10-21

- **d01179e:** the original one-page site.
