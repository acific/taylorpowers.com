# Architecture

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

A static site. There's no server code: GitHub Pages serves the files in the repository as they are.

```
Visitor ──► Cloudflare DNS (taylorpowers.com, DNS only)
              │  A @ → 185.199.108–111.153     CNAME www → shanerealm.github.io
              ▼
        GitHub Pages (repo ShaneRealm/taylorpowers.com, branch main, folder /)
              │  index.html, work/*/index.html, assets/*
              ├──► Google Fonts (Archivo, case pages; the home page self-hosts Switzer)
              ├──► Vimeo player (HD background heroes, films in the lightbox)
              └──► YouTube (nocookie) player (films in the lightbox)

Mail ──► MX route1-3.mx.cloudflare.net ──► Cloudflare Email Routing
              taylor@taylorpowers.com ──► taylorrpowers5@gmail.com
```

## Components

| Component | Where | What it does |
|---|---|---|
| Home page | `index.html` | The owner's Framer design: intro, logo strip, services, experience and contact on the left; project cards linking to outside coverage on the right |
| Case-study pages | `work/<slug>/index.html` | One per project. **Generated** by `scripts/build_work.py`; never edit by hand |
| Generator | `scripts/build_work.py` | Holds the `PROJECTS` data and the page template; writes the eight case pages |
| Styles | `assets/site.css`, `assets/home.css` | `site.css` styles the case pages; `home.css` styles the home page only |
| Behavior | `assets/site.js`, `assets/home.js` | `site.js` runs on the case pages; `home.js` (fade-ins, left-column pinning) on the home page; each part checks that its elements exist |
| Media | `assets/video/`, `assets/clips/`, `assets/img/`, `assets/logos/`, `assets/home/` | Showreel, clips, stills and logos used by the case pages; the home page's avatar, logo strip, card images and Switzer fonts |
| Share card and icon | `assets/og.jpg`, `assets/favicon.svg` | Link previews (1200×630) and the browser-tab icon |
| Domain | `CNAME` | Tells GitHub Pages to serve taylorpowers.com |

## Hosting and domain

- **GitHub Pages:** legacy build from `main` /, custom domain taylorpowers.com, HTTPS enforced. The certificate covers taylorpowers.com and www. Pushing to `main` deploys.
- **DNS:** Cloudflare zone `dc61b51522b6984b10dfe63b4a5b6dbd` in the shared Cloudflare account. The registrar is GoDaddy (Wild West Domains), with nameservers braelyn and kip.ns.cloudflare.com. Every web record is **DNS only** (gray cloud) so GitHub can issue and renew the certificate.
- **Email:** Cloudflare Email Routing. One rule forwards taylor@taylorpowers.com to taylorrpowers5@gmail.com, with MX, SPF and DKIM records added by Email Routing. Receive only; there's no mailbox to send from.

## External services the pages load

| Service | Used for |
|---|---|
| fonts.googleapis.com / fonts.gstatic.com | Archivo variable font (weights 100–900, widths 62–125) on the case pages. The home page's Switzer (400/500/600, from Fontshare) is self-hosted in `assets/home/fonts/`, so the CSP allows `font-src 'self'` |
| player.vimeo.com | HD background heroes (`hero_vimeo`) and lightbox films |
| youtube-nocookie.com | Lightbox films |

Links in case pages also point to coverage on speedcafe.com, ufc.com and jayski.com.
