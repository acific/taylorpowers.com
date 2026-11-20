# Architecture

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

A static site. There's no server code: GitHub Pages serves the files in the repository as they are.

```
Visitor ──► Cloudflare DNS (taylorpowers.com, DNS only)
              │  A @ → 185.199.108–111.153     CNAME www → acific.github.io
              ▼
        GitHub Pages (repo acific/taylorpowers.com, branch main, folder /)
              │  index.html, work/, about/, 404.html, assets/*
              ├──► Google Fonts (Baskervville, case pages); Switzer self-hosted in assets/home/fonts
              ├──► Vimeo player (HD background heroes, films in the lightbox)
              └──► YouTube (nocookie) player (films in the lightbox)

Mail ──► MX route1-3.mx.cloudflare.net ──► Cloudflare Email Routing
              taylor@taylorpowers.com ──► taylorrpowers5@gmail.com
```

## Components

| Component | Where | What it does |
|---|---|---|
| Home | `index.html` | The project carousel (generated) |
| Wins | `wins/index.html` | Three wins from `WINS`, each a lead photo, the story and a photo pair (generated); `work/index.html` is a generated redirect to it |
| About | `about/index.html` | Statement, portrait, experience, logos, services, numbers (generated) |
| Case studies | `work/<slug>/index.html` | One per project (generated) |
| Generator | `scripts/build_work.py` | `PROJECTS`, `ABOUT` and every template; writes all the pages above |
| Styles | `assets/main.css` | Every page, including `404.html` |
| Behavior | `assets/carousel.js`, `assets/about.js`, `assets/site.js` | The home carousel; the About statement; case-page video, Vimeo heroes and the lightbox. Each part checks that its elements exist |
| Media | `assets/video/`, `assets/clips/`, `assets/img/`, `assets/logos/`, `assets/home/` | Showreel, clips, stills and logos used by the case pages; the home page's avatar, logo strip, card images and Switzer fonts |
| Share card and icons | `assets/og.jpg`, `assets/favicon.svg`, `assets/apple-touch-icon.png` | Link previews (1200×630: Taylor's photo, name and role beside three project photos, in the light design), the tab icon (black rounded tile, white "TP") and the phone home-screen icon (Taylor's photo, 180 px) |
| Domain | `CNAME` | Tells GitHub Pages to serve taylorpowers.com |

## Hosting and domain

- **GitHub Pages:** legacy build from `main` /, custom domain taylorpowers.com, HTTPS enforced. The certificate covers taylorpowers.com and www. Pushing to `main` deploys.
- **DNS:** Cloudflare zone `dc61b51522b6984b10dfe63b4a5b6dbd` in the shared Cloudflare account. The registrar is GoDaddy (Wild West Domains), with nameservers braelyn and kip.ns.cloudflare.com. Every web record is **DNS only** (gray cloud) so GitHub can issue and renew the certificate.
- **Email:** Cloudflare Email Routing. One rule forwards taylor@taylorpowers.com to taylorrpowers5@gmail.com, with MX, SPF and DKIM records added by Email Routing. Receive only; there's no mailbox to send from.

## External services the pages load

| Service | Used for |
|---|---|
| fonts.googleapis.com / fonts.gstatic.com | Baskervville (serif headings on the case pages and `404.html`). Switzer (400/500/600, from Fontshare) is self-hosted in `assets/home/fonts/`, so the CSP also allows `font-src 'self'` |
| player.vimeo.com | HD background heroes (`hero_vimeo`) and lightbox films |
| youtube-nocookie.com | Lightbox films |

Links in case pages also point to coverage on speedcafe.com, ufc.com and jayski.com.
