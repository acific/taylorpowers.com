#!/usr/bin/env python3
"""Generate the case-study pages in work/<slug>/index.html from PROJECTS.

Run from the repo root:  python3 scripts/build_work.py
Edit the data here, not the generated HTML. Facts come from Taylor's resume (v9) and
public coverage; don't add claims that aren't in either.
"""
import html, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
V = "21"  # bump with ?v= in index.html when CSS/JS change

PROJECTS = [
    dict(slug="superfile-trackhouse-nascar", client="SuperFile × Trackhouse Racing", title="Daytona 500",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Sponsorship", "Livery", "Race-weekend activation", "VIP hospitality"],
         hero_img="/assets/img/daytona-race.jpg",
         lead="SuperFile arrived on NASCAR’s biggest stage: the black-and-volt #97 Chevrolet for Shane van Gisbergen at the Daytona 500.",
         body=["The Daytona 500 opened a multi-year partnership with Trackhouse Racing. Taylor oversaw the sponsorship rights, partner assets and brand integration, and built the event operation behind race-weekend hospitality for investors, clients and customers, from logistics and vendors to on-site execution.",
               "The program carried on through the season, including a Mr. Brainwash art car in Las Vegas, and extended into MotoGP with Trackhouse’s grand-prix team."],
         figures=[], link=("Race coverage", "https://speedcafe.com/nascar-news-2026-cup-series-shane-van-gisbergen-daytona-500-livery-svg-trackhouse-superfile/"),
         gallery=["/assets/img/daytona-race.jpg", "/assets/img/art-car.jpg"]),
    dict(slug="flex-lafc", client="FLEX × LAFC", title="Front of the jersey",
         year="2021 — 2023", role="Account Director → Senior Account Director, Realm Agency", disciplines=["Jersey sponsorship", "Campaign development", "Partner relations", "Experiential"],
         hero_clip="/assets/clips/flex-falcon.mp4", hero_img="/assets/clips/flex-falcon.jpg", hero_vimeo="781610331",
         lead="FLEX Power Tools on the front of Los Angeles FC’s jersey, and a campaign big enough to match.",
         body=["Taylor worked across FLEX’s LAFC front-of-jersey sponsorship, from campaign development and partner relations to experiential activations.",
               "The program reached more than 60 billion impressions."],
         figures=[("60B+", "Impressions")], film=dict(vimeo="781610331", title="FLEX × LAFC"),
         gallery=["/assets/img/flex-lafc-welcome.jpg", "/assets/clips/flex-soccer.jpg"]),
    dict(slug="superfile-ufc-wwe", client="SuperFile × UFC & WWE", title="Fight night, worldwide",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Global partnership", "Live events", "Brand integration"],
         hero_img="/assets/img/ufc-wwe.jpg",
         lead="A global partnership with TKO that made SuperFile the first Official Secure File Sharing Partner of both UFC and WWE.",
         body=["Taylor developed and managed the partnership across sponsorship rights, partner assets, brand integration and activation, taking SuperFile into the Octagon and the WWE ring for fight nights and live events."],
         figures=[], link=("Partnership announcement", "https://www.ufc.com/news/tko-and-superfile-announce-global-partnership-across-ufc-and-wwe"),
         gallery=[]),
    dict(slug="ego", client="EGO Power+", title="Out of the plane",
         year="2024 — 2025", role="Managing Director / Partner, Realm Agency", disciplines=["Product launches", "Live action", "VFX", "Post-production"],
         hero_clip="/assets/clips/ego.mp4", hero_img="/assets/clips/ego.jpg",
         lead="Launch creative for EGO’s outdoor power equipment, shot in the air and on the ground.",
         body=["At Realm Agency, Taylor oversaw the delivery of more than 20,000 creative and campaign assets for EGO, SKIL and FLEX, supporting over 200 product launches and integrated marketing initiatives, and executive produced campaigns across live action, VFX, animation and post-production."],
         figures=[("20,000+", "Assets delivered for EGO, SKIL & FLEX"), ("200+", "Product launches supported")],
         film=dict(video="/assets/video/reel.mp4#t=4.4", title="EGO"), gallery=[]),
    dict(slug="superfile-trackhouse-motogp", client="SuperFile Trackhouse MotoGP Team", title="Name on the grid",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Title partnership", "Content", "Hospitality"],
         hero_img="/assets/img/motogp-superfile.jpg",
         lead="From logos on the fairing to the name on the team: SuperFile’s title partnership with Trackhouse in MotoGP.",
         body=["Building on the NASCAR program, SuperFile became title partner of the Trackhouse MotoGP team. Taylor ran the partnership across rights, assets, paddock content and hospitality at each round."],
         figures=[], film=dict(yt="JF26n2-jgBI", title="SuperFile Trackhouse MotoGP Team"), gallery=[]),
    dict(slug="skil", client="SKIL", title="Don’t be a gas zombie",
         year="Realm Agency", role="Realm Agency", disciplines=["Campaign", "Talent", "Production", "VFX"],
         hero_clip="/assets/clips/skil.mp4", hero_img="/assets/clips/skil.jpg",
         lead="A cordless-power campaign for SKIL, played for laughs, with talent, production and visual effects.",
         body=["Part of Realm Agency’s work across Chervon’s brands, where Taylor led integrated campaigns from concept through delivery, coordinating creative teams, production, post-production and external partners."],
         figures=[], film=dict(yt="8U5-WrfmTlE", title="SKIL — Don’t Be a Gas Zombie"), gallery=[]),
    dict(slug="superfile-art-car", client="SuperFile × Mr. Brainwash", title="The art car",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Art car", "Culture", "NASCAR"],
         hero_img="/assets/img/art-car.jpg", hero_light=True,
         lead="The #97 handed to the street artist Mr. Brainwash for Las Vegas, turning a race weekend into a culture moment.",
         body=["A one-off livery inside SuperFile’s Trackhouse Racing program, bringing art into a sport built on speed."],
         figures=[], link=("Livery coverage", "https://www.jayski.com/2026/03/10/shane-van-gisbergen-running-unique-superfile-livery-at-las-vegas-sponsoring-connor-zilisch-at-new-hampshire/"),
         gallery=[]),
    dict(slug="superfile-brand-launch", client="SuperFile", title="Brand launch",
         year="2025 — 2026", role="VP of Brand, SuperFile", disciplines=["Brand development", "Integrated marketing", "Content", "Social"],
         hero_img="/assets/img/vm-1014838410.jpg", hero_vimeo="1014838410",
         lead="Taking a new brand to market across brand, creative, content, production and partnerships.",
         body=["Taylor launched SuperFile’s brand, building and leading a 25+ person department across brand, strategy, creative, partnerships and production, and aligning marketing, product and sales on go-to-market.",
               "On social, Taylor launched and scaled SuperFile’s Instagram to more than 150,000 followers in eight months, averaging 18,000+ new followers a month."],
         figures=[("$20M+", "Production budgets managed"), ("150K+", "Instagram followers in 8 months"), ("25+", "Person department built")],
         film=dict(vimeo="1014838410", title="SuperFile"), gallery=[]),
]

e = html.escape

def film_attrs(f):
    if "yt" in f: return f'data-yt="{e(f["yt"])}"'
    if "vimeo" in f: return f'data-vimeo="{e(f["vimeo"])}"'
    return f'data-video="{e(f["video"])}"'

def page(p, more):
    """One case page. `more` is the next two projects, shown under "More to explore"."""
    light = p.get("hero_light")
    hero = (f'<video class="case-hero-media" autoplay muted loop playsinline poster="{p["hero_img"]}" aria-hidden="true"><source src="{p["hero_clip"]}" type="video/mp4"></video>'
            if p.get("hero_clip") else
            f'<img class="case-hero-media" src="{p["hero_img"]}" alt="{e(p["client"])}">')
    if p.get("hero_vimeo"):
        hero += (f'<iframe class="case-hero-vimeo" data-hd src="https://player.vimeo.com/video/{p["hero_vimeo"]}?background=1&autoplay=1&loop=1&muted=1&dnt=1" '
                 f'allow="autoplay; fullscreen; picture-in-picture" title="{e(p["client"])}" aria-hidden="true" tabindex="-1"></iframe>')
    body = "".join(f"<p>{e(t)}</p>" for t in p["body"])
    disciplines = "".join(f"<li>{e(d)}</li>" for d in p["disciplines"])

    film = ""
    if p.get("film"):
        film = (f'<section class="film wrap"><button type="button" class="film-poster" {film_attrs(p["film"])} data-title="{e(p["film"]["title"])}">'
                f'<img src="{p["hero_img"]}" alt="" loading="lazy"><span class="play"><span class="play-dot" aria-hidden="true"></span>Watch the film</span></button></section>')

    # Photos: skip any that repeat the hero; two or more show as pairs, a single one full width
    photos = [g for g in p["gallery"] if g != p["hero_img"]]
    gallery = ""
    if photos:
        figs = "".join(f'<figure class="{"light" if "art-car" in g else ""}"><img src="{g}" alt="" loading="lazy"></figure>' for g in photos)
        gallery = f'<section class="pair{" single" if len(photos) == 1 else ""} wrap">{figs}</section>'

    results = ""
    if p["figures"] or p.get("link"):
        figs = "".join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in p["figures"])
        link = (f'<a class="btn" href="{e(p["link"][1])}" target="_blank" rel="noopener">{e(p["link"][0])} ↗</a>' if p.get("link") else "")
        results = (f'<section class="split wrap"><h2>{"Results." if p["figures"] else "Coverage."}</h2><div>'
                   f'{f"<dl class=figures>{figs}</dl>" if figs else ""}{link}</div></section>')

    cards = "".join(
        f'<a class="more-card" href="/work/{m["slug"]}/"><span class="more-img"><img src="{m["hero_img"]}" alt="" loading="lazy"></span>'
        f'<span class="more-name">{e(m["client"])}</span><span class="more-sub">{e(m["title"])} · {e(m["year"])}</span></a>' for m in more)

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; media-src 'self'; frame-src https://player.vimeo.com https://www.youtube-nocookie.com; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(p["client"])} — {e(p["title"])} · Taylor Powers</title>
<meta name="description" content="{e(p["lead"])}">
<meta property="og:title" content="{e(p["client"])} — {e(p["title"])}">
<meta property="og:description" content="{e(p["lead"])}">
<meta property="og:image" content="https://taylorpowers.com{p["hero_img"]}">
<meta property="og:url" content="https://taylorpowers.com/work/{p["slug"]}/">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a0a0a">
<link rel="icon" href="/assets/favicon.svg">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" as="font" type="font/woff2" href="/assets/home/fonts/switzer-400.woff2" crossorigin>
<link rel="stylesheet" href="/assets/case.css?v={V}">
</head>
<body class="case">
<header class="hero-bar{" on-light" if light else ""}">
  <a class="who" href="/"><img src="/assets/home/avatar.jpg" alt=""><b>Taylor Powers</b></a>
  <nav><a href="/#work">Work</a><a href="mailto:taylorraepowers@icloud.com">Contact ↗</a></nav>
</header>
<main>
  <section class="case-hero{" light-hero" if light else ""}">
    {hero}
    <div class="case-hero-shade" aria-hidden="true"></div>
    <div class="case-hero-copy">
      <a class="all-work" href="/#work">← All work</a>
      <div class="case-hero-info">
        <h1>{e(p["title"])}</h1>
        <p>{e(p["lead"])}</p>
        <dl class="facts">
          <div><dt>Client</dt><dd>{e(p["client"])}</dd></div>
          <div><dt>Year</dt><dd>{e(p["year"])}</dd></div>
          <div><dt>Role</dt><dd>{e(p["role"])}</dd></div>
        </dl>
      </div>
    </div>
  </section>
  <section class="intro">
    <div class="wrap intro-grid">
      <div class="intro-side"><h2>Overview</h2><ul>{disciplines}</ul></div>
      <div class="intro-text">{body}</div>
    </div>
  </section>
  {film}
  {gallery}
  {results}
  <section class="more wrap">
    <h2>More to explore.</h2>
    <p>Two more projects from Taylor’s work.</p>
    <div class="more-grid">{cards}</div>
  </section>
</main>
<footer class="contact-foot">
  <div class="wrap">
    <h2>Let’s work together.</h2>
    <p>Taylor Powers · Brand &amp; Marketing Executive</p>
    <div class="contact-actions">
      <a class="pill" href="mailto:taylorraepowers@icloud.com">taylorraepowers@icloud.com</a>
      <a class="pill" href="https://www.linkedin.com/in/taylorpowers2026" target="_blank" rel="noopener">LinkedIn ↗</a>
    </div>
    <div class="contact-base"><span>© 2026 Taylor Powers</span><a href="/">taylorpowers.com</a></div>
  </div>
</footer>
<dialog class="player" id="player" aria-label="Video">
  <div class="frame" id="playerFrame"></div>
  <div class="player-bar"><span id="playerTitle"></span><button type="button" id="playerClose">Close ✕</button></div>
</dialog>
<script src="/assets/site.js?v={V}" defer></script>
</body>
</html>
'''

n = len(PROJECTS)
for i, p in enumerate(PROJECTS):
    out = ROOT / "work" / p["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(p, [PROJECTS[(i + 1) % n], PROJECTS[(i + 2) % n]]))
    print("wrote", out.relative_to(ROOT))
