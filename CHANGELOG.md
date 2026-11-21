# Changelog

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

There are no version numbers; each entry is a date and the commits it covers. The `?v=` cache stamp is noted where it changed. There's no migration: it's a static site with no stored data or clients.

## 2026-11-20

- **EGO Labs 2.0:** card, hero loop and film from EGO's 765 CFM Blower (LB7654) spot (YouTube pT_z7orpfJE), shot in the EGO Labs set.
- **SuperFile × Trackhouse NASCAR:** new card (the SuperFile Racing booth) and hero loop from the owner's Trackhouse Fan Day film (`26-0601_FanDay_Assembly_PH_v2.mp4`).
- **New link preview** (`assets/og-2026.jpg`, 2400×1260): the 2026 headshot on a dark olive ground with "Taylor Powers." in the site serif, the role, the brands and the URL; used by Home, About and the 404, with image size and alt tags for iMessage. **Phone pass:** finger-sized tap areas for the menu, carousel arrows, back link and deck links; safe-area spacing for the home menu; the Wins opener keeps Taylor in frame on tall screens; on phones only the centred home card plays its film. **Mr. Brainwash art car:** new card (the three-car poster) and hero (the artist with the car in Las Vegas). Stamp 46.
- **New cards and hero videos:** EGO POWER+ from the Z6 "Power without limits" film (also its YouTube film), FLEX × LAFC from FLEX's Stacked Lithium hero video, and Wylie Co. from the Dune official trailer (also its film). Stamp 45.
- **EGO POWER+:** new card, hero loop and film from EGO's 22" Select Cut mower spot (YouTube Mq8TwQIQwxw), replacing the Z6 clip and the deck reel.
- **Case studies rewritten from the owner's write-ups** (deck "26-1120_TaylorPowers_Portfolio_Case-Study_Writeups_TP", in third person): NASCAR, MotoGP, SuperFile × LAFC, SuperFile × TKO (renamed from SuperFile × UFC), EGO POWER+ (renamed from EGO Z6 Launch), FLEX × LAFC, FLEX launch and SKIL now open with the owner's overview, strategy, role and impact, use the deck's stats as Results, and add its photos and films (MotoGP season film and hero loop, LAFC training-top hero loop, EGO reel, FLEX × LAFC film and spot, FLEX Stacked Lithium spot and hero loop). **New headshot:** the owner's 2026 headshot is the About portrait and the home page's first card.
- **About:** the large portrait is now the owner's 2026 headshot.
- **Home:** card films now play the whole time they are on screen (black and white at the sides, colour in the centre), not only when centred. Stamp 43.
- **SuperFile Brand Launch:** removed the glove and medal photo pair (owner's request).
- **Wins:** the LAFC chapter adds the 2022 MLS Cup ring (128 black diamonds for Bale's 128th-minute goal; LAFC/Baron release, Mar 4, 2023); the opener photo is brightened. Stamp 42.
- **Wins redesigned to feel premium** (owner: "make it absolutely great"): black cinematic page, full-screen opener of Taylor in victory lane with an oversized "Wins." and an index, then a full-screen chapter per win with a headline number (74/100, 1–2, 128′), the story and two photos; content fades up once on entry (`assets/wins.js`). Stamp 41.
- **Works page replaced by Wins** (`/wins/`, owner's idea): Watkins Glen victory lane (with Taylor, identified by the owner), the MotoGP one-two at Assen and Silverstone win, and LAFC's 2022 MLS Cup with FLEX on the shirt. Menu, footer, deck, case-page back link and 404 now point to Wins or Home; `/work/` forwards to `/wins/`. Stamp 40.
- **NASCAR:** added the two Watkins Glen trophy photos (owner's request) to the Watkins Glen section.
- **SKIL:** the hero and home-card loop is now the full "Don't Be a #GasZombie" spot (YouTube 8U5-WrfmTlE, silent 720p), replacing a clip from an older SKIL spot.
- **Case pages:** removed "More to explore" (owner: distracting); pages end after Results. Stamp 39.
- **SuperFile media from the owner:** the anthem film is the brand-launch hero and film; NASCAR gets the Daytona 500 film and loop, Daytona/Martinsville/Texas photos, the New Hampshire highlight and the Watkins Glen win (burnouts, victory lane, champagne); Lefty Out There gets the Chicagoland highlight, race, pit, artist and door photos and a new card; UFC gets the FREEDOM 250 and UFC 329 films; the MotoGP card is the unveil graphic. Sections can now carry their own film. **About:** "In numbers" and the logos now sit above the deck. Stamp 38.
- **About deck is now a full presentation:** cover (editing-desk image, "Brand, partnerships and production."), a contents slide whose entries jump to each service, the five service slides and a closing slide with email, LinkedIn and Work links. Eight slides. Stamp 37.
- **About:** the small photo is now the owner's editing-desk image; the closing photo pair at the bottom is gone. Stamp 36.
- **About services as a deck** (owner's choice, "deck on a stage"): one framed 16:9 slide at a time on the black band with a segmented progress bar, a counter and arrows; from 810 px the band pins and the page scroll steps through the five slides (arrows and segments scroll to a slide). Phones show the slides stacked. Replaces the sideways row. Stamp 35.
- **Home cards play their film** when centred (FLEX × LAFC, EGO, SKIL, Digital Domain): the card's `hero_clip` loads only when the card reaches the centre, plays muted and pauses when it leaves; off for reduced motion. **Digital Domain:** the studio's own showreel banner from digitaldomain.com as the case-page hero and card film. Stamp 34.
- **Home:** an endless logo strip (the About logos) in the space between the arrows and the nav, hidden on desktop windows under 760 px tall and still for reduced motion. **Wylie Co.:** the card is now the Dune (2021) poster. **SuperFile × UFC** (renamed from UFC & WWE): UFC 329 weigh-in hero and card, the fight poster, and Sophie Cunningham's SuperFile round card. **FLEX × LAFC** links to LAFC's 2022 kit page. Stamp 33.
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
