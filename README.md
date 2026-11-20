# taylorpowers.com

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

The professional site for **Taylor Powers**, brand and creative production executive (Chicago). Laid out like a Framer portfolio template the owner chose (2026-11-20): a home-page carousel of fourteen projects, a Work grid, an About page, and a case study for every project. Every page is generated from one list in `scripts/build_work.py`.

**Live:** https://taylorpowers.com · **Contact:** taylor@taylorpowers.com, which forwards to Taylor's Gmail · **Where we left off:** [docs/STATUS.md](docs/STATUS.md)

## Run and deploy

It's a static site on GitHub Pages; pushing to `main` deploys it.

```bash
cd ~/Strange/taylorpowers.com
python3 -m http.server 5277          # preview at http://localhost:5277 (or the "taylorpowers" preview config)
python3 scripts/build_work.py        # regenerate the case pages after editing PROJECTS
node scripts/docs-check.mjs          # check the docs against the code
git push origin main   # as acific
```

After changing `assets/main.css`, `assets/site.js` or `assets/carousel.js`, bump `V` in `scripts/build_work.py` (and `?v=` in `404.html`), then rebuild. See [docs/OPERATIONS.md](docs/OPERATIONS.md).

## Map

| Path | What |
|---|---|
| `scripts/build_work.py` | The generator and all the content: `PROJECTS` (fourteen projects) and `ABOUT` |
| `index.html`, `wins/index.html`, `about/index.html`, `work/<slug>/index.html`, `work/index.html` | **Generated**: home carousel, Wins, About, case studies, and a redirect from the old Work page. Edit the generator, not the HTML |
| `404.html` | Page not found (hand-edited) |
| `assets/main.css`, `assets/carousel.js`, `assets/about.js`, `assets/site.js` | All styles; the home carousel; the About statement; case-page video and lightbox |
| `assets/about/` | The About page's images (AI-generated, see docs/CONTENT.md) |
| `assets/home/` | Card images (1024 px and `@2x`, graded), logos, Switzer fonts, avatar |
| `sources/cards/`, `scripts/grade_cards.sh` | Ungraded card originals, and the script that grades them into `assets/home/work/` (needs ffmpeg) |
| `assets/video/`, `assets/clips/` | The showreel, and silent loops cut from it |
| `assets/img/`, `assets/logos/` | Stills, the portrait, partner logos |
| `assets/og.jpg`, `assets/favicon.svg`, `assets/apple-touch-icon.png` | The share card, the tab icon and the home-screen icon |
| `CNAME` | Custom domain for GitHub Pages |

## Docs

| Doc | |
|---|---|
| [docs/STATUS.md](docs/STATUS.md) | Where we left off and what's waiting on the owner |
| [docs/GOALS.md](docs/GOALS.md) | Purpose, audience, goals |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Hosting, DNS, email |
| [docs/IMPLEMENTATION.md](docs/IMPLEMENTATION.md) | Every file and feature |
| [docs/USER-GUIDE.md](docs/USER-GUIDE.md) | What visitors see; how to change things |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Deploying, DNS records, troubleshooting |
| [docs/CONTENT.md](docs/CONTENT.md) | Where every fact and asset comes from |
| [docs/DECISIONS.md](docs/DECISIONS.md) | The design history and its rules |
| [AGENTS.md](AGENTS.md) | Rules for coding agents |
| [CHANGELOG.md](CHANGELOG.md) · [SECURITY.md](SECURITY.md) | History · security notes |
