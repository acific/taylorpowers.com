#!/usr/bin/env python3
"""Generate every page of taylorpowers.com from PROJECTS (and the About data below):

  index.html               home: the project carousel
  work/index.html          all work, in a two-column grid
  about/index.html         bio, experience, services, numbers
  work/<slug>/index.html   one case study per project

Run from the repo root:  python3 scripts/build_work.py
Edit the data here, never the generated HTML. Facts come from Taylor's resume (v9), the owner's
own statements and the public sources listed in docs/CONTENT.md; don't add claims that aren't there.
The layout follows the Framer portfolio template the owner chose (see docs/DECISIONS.md).
"""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
V = "23"  # cache stamp for /assets/main.css, /assets/site.js and /assets/carousel.js; 404.html uses it too

EMAIL = "taylorraepowers@icloud.com"
LINKEDIN = "https://www.linkedin.com/in/taylorpowers2026"

# Each project: slug, name (as on the cards), type (the card's role label), year, client, title,
# role, disciplines, lead (one line), body (paragraphs), card (the card/carousel image),
# hero_img (case-page hero; defaults to the card's 2x image), optional hero_clip / hero_vimeo /
# hero_light, figures [(number, label)], film {yt|vimeo|video, title}, link (label, url), gallery [img].
W = "/assets/home/work/"
PROJECTS = [
    dict(slug="superfile-trackhouse-nascar", name="SuperFile × Trackhouse Racing NASCAR", type="Brand Management",
         client="SuperFile × Trackhouse Racing", title="Daytona 500",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Sponsorship", "Livery", "Race-weekend activation", "VIP hospitality"],
         card=W + "trackhouse-nascar.jpg", hero_img="/assets/img/daytona-race.jpg",
         lead="SuperFile’s first NASCAR partnership arrived on the sport’s biggest stage: the black-and-neon #97 Chevrolet Camaro for Shane van Gisbergen at the 2026 Daytona 500.",
         body=["Trackhouse Racing announced the partnership on February 6, 2026, nine days before the Daytona 500, putting the cybersecurity file-management platform on Shane van Gisbergen’s #97 Chevrolet in a black and neon livery.",
               "Taylor oversaw the sponsorship rights, partner assets and brand integration, and built the event operation behind race-weekend hospitality for investors, clients and customers, from logistics and vendors to on-site execution.",
               "The program grew into a multi-year, multi-race partnership: a Mr. Brainwash art car in Las Vegas, an artist livery by Lefty Out There at Chicagoland, and title sponsorship of Trackhouse’s MotoGP team."],
         figures=[], link=("Race coverage", "https://speedcafe.com/nascar-news-2026-cup-series-shane-van-gisbergen-daytona-500-livery-svg-trackhouse-superfile/"),
         gallery=[W + "trackhouse-nascar@2x.jpg", "/assets/img/art-car.jpg"]),
    dict(slug="superfile-brand-launch", name="SuperFile Brand Launch", type="Brand Management",
         client="SuperFile", title="Brand launch",
         year="2025 — 2026", role="VP of Brand, SuperFile", disciplines=["Brand development", "Integrated marketing", "Content", "Social"],
         card=W + "superfile-brand-launch.jpg", hero_img="/assets/img/vm-1014838410.jpg", hero_vimeo="1014838410",
         lead="Taking a new brand to market across brand, creative, content, production and partnerships.",
         body=["Taylor launched SuperFile’s brand, building and leading a 25+ person department across brand, strategy, creative, partnerships and production, and aligning marketing, product and sales on go-to-market.",
               "On social, Taylor launched and scaled SuperFile’s Instagram to more than 150,000 followers in eight months, averaging 18,000+ new followers a month."],
         figures=[("$20M+", "Production budgets managed"), ("150K+", "Instagram followers in 8 months"), ("25+", "Person department built")],
         film=dict(vimeo="1014838410", title="SuperFile"), gallery=[]),
    dict(slug="wylie-co", name="Wylie Co.", type="VFX Coordinator",
         client="Wylie Co.", title="Visual effects for film and television",
         year="2017 — 2020", role="VFX Coordinator, Wylie Co.", disciplines=["VFX production", "Feature film", "Television"],
         card=W + "wylie-dune.jpg",
         lead="Visual effects production at Wylie Co., the studio behind previs, postvis and final effects on Dune: Part One, as well as Terminator: Dark Fate and Marvel productions.",
         body=["On Dune (2021), Wylie Co. delivered previs, postvis and final visual effects: about 950 VFX shots, around 450 postvis shots and nearly 450 shots of the Fremen’s blue “Eyes of Ibad.”",
               "As VFX Coordinator, Taylor managed production workflows across the studio’s film and television slate, including Dune: Part One, Terminator: Dark Fate and Marvel productions."],
         figures=[("~950", "VFX shots by Wylie on Dune (2021)")], link=("How Wylie made Dune’s blue eyes", "https://blog.borisfx.com/wylie-co.-tracks-dunes-eyes-of-ibad-with-mocha-pro"), gallery=[]),
    dict(slug="flex-lafc", name="FLEX Power Tools × LAFC", type="Account Management",
         client="FLEX × LAFC", title="Front of the jersey",
         year="2021 — 2023", role="Account Director → Senior Account Director, Realm Agency", disciplines=["Jersey sponsorship", "Campaign development", "Partner relations", "Experiential"],
         card=W + "flex-lafc.webp", hero_clip="/assets/clips/flex-falcon.mp4", hero_img="/assets/clips/flex-falcon.jpg", hero_vimeo="781610331",
         lead="FLEX Power Tools on the front of Los Angeles FC’s jersey: a multi-year deal that made a new tool brand part of one of MLS’s loudest clubs.",
         body=["LAFC announced FLEX as its Official Jersey Sponsor on March 26, 2021, putting the brand on every Club, Community and specialty jersey. FLEX also became the club’s Official Power Tool Partner and a Golden Boot Club Partner, with exclusive content, media, signage and a co-branded retail promotion, timed to FLEX’s 24V line launching nationwide.",
               "At Realm Agency, Taylor worked across the sponsorship from campaign development and partner relations to experiential activations, including the club’s 2022 “5 Years Strong” kit with FLEX across the chest.",
               "The program reached more than 60 billion impressions."],
         figures=[("60B+", "Impressions")], film=dict(vimeo="781610331", title="FLEX × LAFC"),
         link=("FLEX named LAFC’s jersey sponsor", "https://www.lafc.com/news/lafc-announces-flex-power-tools-official-jersey-sponsor"),
         gallery=["/assets/img/flex-lafc-welcome.jpg", "/assets/clips/flex-soccer.jpg"]),
    dict(slug="superfile-ufc-wwe", name="SuperFile × UFC & WWE", type="Brand Management",
         client="SuperFile × UFC & WWE", title="Fight night, worldwide",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Global partnership", "Live events", "Brand integration"],
         card=W + "superfile-ufc-wwe.png", hero_img="/assets/img/ufc-wwe.jpg",
         lead="A global partnership with TKO that made SuperFile the first Official Secure File Sharing Partner of both UFC and WWE.",
         body=["TKO and SuperFile announced the partnership on June 9, 2026. Five days later, SuperFile was an Official Partner of UFC FREEDOM 250 at the White House, with Octagon branding and broadcast integrations reaching an estimated one billion households in 210 countries and territories, plus the SuperFile Super Replay, “Keys to Victory” and a one-hour SuperFile Post-Show.",
               "SuperFile went on to present UFC 329, McGregor vs. Holloway 2, at T-Mobile Arena in Las Vegas. In WWE, the deal covers Premium Live Events including WrestleMania, Money in the Bank, Survivor Series and the Royal Rumble, with ring-side placements and custom social content.",
               "Taylor developed and managed the partnership across sponsorship rights, partner assets, brand integration and activation."],
         figures=[("1B", "Households, UFC FREEDOM 250"), ("210", "Countries and territories")], link=("Partnership announcement", "https://www.ufc.com/news/tko-and-superfile-announce-global-partnership-across-ufc-and-wwe"),
         gallery=[]),
    dict(slug="superfile-lefty-out-there", name="SuperFile × Lefty Out There Artist Collaborations", type="Brand Management",
         client="SuperFile × Lefty Out There", title="Artist collaborations",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Artist collaboration", "Brand partnerships"],
         card=W + "lefty-out-there.jpg",
         lead="SuperFile handed Shane van Gisbergen’s #97 to the artist Lefty Out There for Chicagoland.",
         body=["Lefty Out There, the American artist Francesco Campanella, designed the livery for van Gisbergen’s SuperFile-backed #97 Trackhouse Camaro at the 2026 Chicagoland eero 400. It was his second major motorsport project, after a virtual F1 livery with Max Verstappen.",
               "The collaboration was part of SuperFile’s run of artist cars inside its Trackhouse Racing partnership, which Taylor led as VP of Brand."],
         link=("The Chicagoland livery", "https://speedcafe.com/nascar-news-2026-cup-series-chicagoland-shane-van-gisbergen-livery-lefty-out-there-details/"), figures=[], gallery=[]),
    dict(slug="superfile-lafc", name="SuperFile × LAFC", type="Brand Management",
         client="SuperFile × LAFC", title="SuperFile × LAFC",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Sports partnership", "Brand integration"],
         card=W + "superfile-lafc.webp",
         lead="SuperFile on the front of LAFC’s black-and-gold training kit.",
         body=["In 2026 SuperFile became a Golden Boot Club partner of Los Angeles FC and the front-of-training-kit sponsor, putting the brand on the club’s black-and-gold LAFC Training Kit.",
               "Alongside the partnership, SuperFile donated $50,000 to the LAFC Foundation to support youth soccer. Taylor developed and managed the partnership as part of SuperFile’s sports program."],
         figures=[("$50K", "Donated to the LAFC Foundation")], link=("The LAFC Training Kit", "https://www.lafc.com/culture/kit/superfile"), gallery=[]),
    dict(slug="superfile-trackhouse-motogp", name="SuperFile Trackhouse MotoGP", type="Brand Management",
         client="SuperFile Trackhouse MotoGP Team", title="Name on the grid",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Title partnership", "Content", "Hospitality"],
         card=W + "trackhouse-motogp.jpg", hero_img="/assets/img/motogp-superfile.jpg",
         lead="From logos on the fairing to the name on the team: SuperFile became the first title sponsor of Trackhouse’s MotoGP team.",
         body=["On June 5, 2026, SuperFile became title partner of Trackhouse’s MotoGP team, the last team on the grid without one, in what both sides called a long-term strategic commitment. The team races as the SuperFile Trackhouse MotoGP Team.",
               "The black-and-yellow SuperFile livery runs for the rest of the season, starting at the Hungarian Grand Prix at Balaton Park, with riders Raúl Fernández and Ai Ogura, after a first SuperFile livery at the Spanish Grand Prix.",
               "Building on the NASCAR program, Taylor ran the partnership across rights, assets, paddock content and hospitality at each round."],
         figures=[], film=dict(yt="JF26n2-jgBI", title="SuperFile Trackhouse MotoGP Team"),
         link=("Title sponsor announcement", "https://www.crash.net/motogp/news/1096813/1/motogps-newest-team-finally-gains-title-sponsor-third-year"), gallery=[]),
    dict(slug="ego", name="EGO Z6 Launch", type="Production",
         client="EGO Power+", title="EGO Z6 launch",
         year="2024 — 2025", role="Managing Director / Partner, Realm Agency", disciplines=["Product launch", "Live action", "VFX", "Post-production"],
         card=W + "ego-z6.png", hero_clip="/assets/clips/ego.mp4", hero_img="/assets/clips/ego.jpg",
         lead="Launch creative for EGO’s Z6, the world’s first platform-compatible zero-turn rider.",
         body=["The 42-inch Z6 zero-turn riding mower (ZT4204L) runs on four of EGO’s 56V batteries, the same packs that power the rest of the POWER+ line, and cuts up to two acres on a charge. The launch film, “Power without limits,” introduced it as the world’s first platform-compatible rider.",
               "At Realm Agency, Taylor oversaw the delivery of more than 20,000 creative and campaign assets for EGO, SKIL and FLEX, supporting over 200 product launches, and executive produced campaigns across live action, VFX, animation and post-production."],
         link=("The EGO Z6", "https://egopowerplus.com/zero-turn-riding-mower-zt4204l/"), figures=[("20,000+", "Assets delivered for EGO, SKIL & FLEX"), ("200+", "Product launches supported")],
         film=dict(yt="d1Lis7rNkAg", title="EGO Z6"), gallery=[W + "ego-z6@2x.jpg"]),
    dict(slug="skil", name="SKIL Gas Zombies Campaign", type="Account Management",
         client="SKIL", title="Don’t be a gas zombie",
         year="2022", role="Realm Agency", disciplines=["National TV", "Campaign", "Product launch"],
         card=W + "skil-gas-zombies.png", hero_clip="/assets/clips/skil.mp4", hero_img="/assets/clips/skil.jpg",
         lead="“Don’t Be a Gas Zombie”: SKIL’s national TV spot for its PWRCORE 40 cordless outdoor range.",
         body=["SKIL’s spot for PWRCORE 40, first published in March 2022, pitched its brushless 40V string trimmer, leaf blower, self-propelled mower and chainsaw as the way out of a world controlled by gas.",
               "It plays for laughs: a couple shares their SKIL tools with their zombie neighbors, while one stubborn holdout tears his arm off trying to start his gas equipment. The spot closes on SKIL’s tagline, “What Powers You?”, with the range available at Lowe’s.",
               "Part of Realm Agency’s work across Chervon’s brands, where Taylor led integrated campaigns from concept through delivery, coordinating creative teams, production, post-production and external partners."],
         figures=[], film=dict(yt="8U5-WrfmTlE", title="SKIL — Don’t Be a Gas Zombie"),
         link=("The TV spot on iSpot", "https://www.ispot.tv/ad/bIBQ/skil-pwrcore-40-dont-be-a-gas-zombie"), gallery=[]),
    dict(slug="superfile-art-car", name="SuperFile × Mr. Brainwash Artist Collaboration", type="Brand Management",
         client="SuperFile × Mr. Brainwash", title="The art car",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Art car", "Culture", "NASCAR"],
         card=W + "mr-brainwash.jpg", hero_img="/assets/img/art-car.jpg", hero_light=True,
         lead="The #97 handed to the street artist Mr. Brainwash for Las Vegas, turning a race weekend into a culture moment.",
         body=["Trackhouse unveiled the livery on March 10, 2026: Mr. Brainwash, the artist Thierry Guetta, painted Shane van Gisbergen’s #97 Chevrolet to mark SuperFile’s multi-year, multi-race partnership with the team. SuperFile called it the “SuperBrainHouse” car.",
               "It debuted at Las Vegas Motor Speedway on March 15. “The car looks epic,” van Gisbergen said.",
               "A one-off inside the Trackhouse program Taylor ran as VP of Brand, bringing art into a sport built on speed."],
         figures=[], link=("The art car", "https://speedcafe.com/nascar-news-2026-cup-series-shane-van-gisbergen-superfile-livery-mr-brainwash-photos-render/"),
         gallery=[W + "mr-brainwash@2x.jpg"]),
    dict(slug="flex-launch", name="FLEX Power Tools Launch", type="Account Management",
         client="FLEX Power Tools", title="Stacked Lithium launch",
         year="Realm Agency", role="Realm Agency", disciplines=["Product launch", "Campaign"],
         card=W + "flex-launch.jpg",
         lead="The launch of FLEX’s 24V Stacked Lithium battery, built to give the whole FLEX lineup more power and longer run time.",
         body=["FLEX’s Stacked Lithium battery, with Therma-Tech+ cooling, works with every FLEX 24V tool. FLEX launched it alongside a hammer drill, an impact driver and a circular saw, claiming up to 200% more power, 300% longer battery life and charging as fast as 20 minutes.",
               "At Realm Agency, Taylor managed the FLEX account through launches like this one, part of the more than 200 product launches Realm supported for EGO, SKIL and FLEX."],
         figures=[("200%", "More power, per FLEX"), ("300%", "Longer battery life, per FLEX")], link=("FLEX Stacked Lithium", "https://www.flexpowertools.com/stackedlithium"), gallery=[]),
    dict(slug="digital-domain", name="Digital Domain", type="VFX Coordinator",
         client="Digital Domain", title="Digital Human Group",
         year="2020 — 2021", role="VFX Coordinator, Digital Domain", disciplines=["VFX production", "Digital humans"],
         card=W + "digital-domain.jpg",
         lead="Visual effects coordination for Digital Domain’s Digital Human Group, the team building the studio’s digital humans.",
         body=["Digital Domain’s Digital Human Group brings together technicians, programmers and artists to build digital humans and the tools behind them, from the Masquerade and Charlatan capture systems to real-time rendering, for film, live events, gaming and mobile.",
               "Taylor coordinated visual effects production for the group, managing international workflows, artist schedules and deliverables."],
         figures=[], link=("Digital Domain’s digital humans", "https://digitaldomain.com/digital-humans-lab/"), gallery=[]),
    dict(slug="ego-labs", name="EGO Labs 2.0", type="Account Management / Production",
         client="EGO Power+", title="The next generation of Z6 riders",
         year="Realm Agency", role="Realm Agency", disciplines=["Product launch", "Campaign", "Production"],
         card=W + "ego-labs.png",
         lead="Launch work for EGO’s next generation of Z6 zero-turn riding mowers: all the power of gas, with no exhaust and no oil changes.",
         body=["EGO introduced its next generation of Z6 zero-turn riding mowers with the line “All power. Zero compromise.” The range runs from the 42-inch Z6 to the 52-inch ZT5216L, rated up to 27 HP gas-equivalent and up to three acres on a single charge, plus a 42-inch model with E-Steer that drives like a car and the T6 lawn tractor.",
               "Peak Power combines up to six of EGO’s 56V batteries, the same ones that run more than 100 EGO tools, and a color display connects to the EGO Connect app for blade speed, driving mode and mowing history. EGO calls itself the number one rated brand in cordless outdoor power, with more than 250,000 five-star reviews.",
               "At Realm Agency, Taylor led account management and production for EGO across product launches and campaign content."],
         figures=[("27 HP", "Gas-equivalent power, per EGO"), ("3 acres", "On a single charge, per EGO"), ("100+", "EGO tools on the same batteries")],
         link=("EGO’s Z6 riding mowers", "https://egopowerplus.com/ridingmowers"), gallery=[]),
]
for p in PROJECTS:  # the case-page hero defaults to the card image at 2x
    p.setdefault("hero_img", p["card"].rsplit(".", 1)[0] + "@2x.jpg")
    p.setdefault("figures", []); p.setdefault("gallery", [])

ABOUT = dict(
    statement="I’m Taylor Powers, a brand and marketing executive with 8+ years of experience spanning Hollywood productions, global consumer brands, and high-profile partnerships in sports and entertainment.",
    paras=["My background includes leading brand development, strategic partnerships, multidisciplinary teams, and large-scale marketing and creative production initiatives."],
    jobs=[("Vice President of Brand", "SuperFile", "2025-2026", "Built and launched the brand, leading strategy, integrated marketing, creative production, and high-profile partnerships. Managed a multidisciplinary team of professionals."),
          ("Managing Director", "Realm Agency", "2024-2025", "Led agency operations, client strategy, and creative production, overseeing multimillion-dollar budgets, cross-functional teams, and integrated campaigns for global brands."),
          ("Account Leadership", "Realm Agency", "2021-2024", "Advanced from Account Executive to Senior Account Director, managing major accounts, brand launches, marketing campaigns, and creative production for all agency clients."),
          ("VFX Coordinator", "Digital Domain", "2020-2021", "Coordinated visual effects production for the Digital Human Group, managing international workflows, artist schedules, and deliverables."),
          ("VFX Coordinator", "Wylie Co.", "2017-2020", "Managed VFX production workflows across major film and television projects, including Dune: Part One, Terminator: Dark Fate, and Marvel productions.")],
    services=[("Brand Strategy", ["Brand Development & Positioning", "Creative Strategy & Brand Direction", "Brand Launches & Go-To-Market Strategy", "Content & Social Media Strategy"]),
              ("Integrated Marketing", ["Marketing Strategy", "Integrated Campaign Development", "Marketing Operations", "Budget & Resource Management"]),
              ("Partnerships & Sponsorships", ["Partnership Strategy & Development", "Sponsorship Negotiations", "Brand Integrations & Activations", "Account Management"]),
              ("Creative Production", ["Creative Leadership & Direction", "End-to-End Production Management", "VFX, Animation & Finishing Supervision", "Production Operations & Resource Management"]),
              ("Experiential Marketing and Events", ["Experiential Strategy", "Event Production & Management", "Sponsorship Activations", "Executive & VIP Hospitality", "Branded Merchandise & Promotional Programs"])],
    numbers=[("8+", "Years of experience"), ("60B+", "Impressions, FLEX × LAFC"), ("$20M+", "Production budgets managed")],
)
LOGOS = [("ego", "EGO", 16), ("skil", "SKIL", 19), ("flex", "FLEX", 19), ("digital-domain", "Digital Domain", 19), ("wylie", "Wylie Co.", 23),
         ("netflix", "Netflix", 18), ("abc", "ABC", 27), ("fox", "FOX", 20), ("apple-tv", "Apple TV", 22), ("superfile", "SuperFile", 17), ("realm", "Realm", 20)]

e = html.escape
CSP = ("default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; "
       "img-src 'self' data:; media-src 'self'; frame-src https://player.vimeo.com https://www.youtube-nocookie.com; connect-src 'self'; "
       "object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests")

def head(title, desc, url, image, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="https://taylorpowers.com{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://taylorpowers.com{url}">
<meta property="og:image" content="https://taylorpowers.com{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f4f4f4">
<link rel="icon" href="/assets/favicon.svg">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baskervville:wght@400..700&display=swap">
<link rel="preload" as="font" type="font/woff2" href="/assets/home/fonts/switzer-400.woff2" crossorigin>
<link rel="stylesheet" href="/assets/main.css?v={V}">
{extra}</head>
"""

def nav(cls="", current=""):
    def a(href, label, key):
        return f'<a href="{href}"{" aria-current=\"page\"" if key == current else ""}>{label}</a>'
    return (f'<header class="nav {cls}"><nav class="nav-mid">{a("/", "Home", "home")}{a("/about/", "About", "about")}{a("/work/", "Work", "work")}</nav>'
            f'<a class="nav-end" href="mailto:{EMAIL}">Contact ↗</a></header>')

FOOT = f"""<footer class="foot">
  <div class="wrap">
    <div class="cols foot-top">
      <div>
        <h2 class="rotate" aria-label="Let’s work together.">Let’s <span class="words" aria-hidden="true"><span>work together.</span><span>connect.</span><span>create.</span><span>work together.</span></span></h2>
        <p class="foot-line">Let’s work together to bring your ideas to life.</p>
      </div>
      <div class="foot-right">
        <p class="place">Based in Chicago</p>
        <ul class="foot-links">
          <li><a href="{LINKEDIN}" target="_blank" rel="noopener"><span>LinkedIn</span><span aria-hidden="true">↗</span></a></li>
          <li><a href="/work/"><span>All work</span><span aria-hidden="true">↗</span></a></li>
        </ul>
      </div>
    </div>
    <div class="foot-pills">
      <a class="pill" href="mailto:{EMAIL}"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M3 5.5h14v9H3z M3 6l7 5 7-5" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>{EMAIL}</a>
    </div>
    <p class="foot-base">TAYLOR POWERS © 2026 ALL RIGHTS RESERVED</p>
  </div>
</footer>"""

PLAYER = """<dialog class="player" id="player" aria-label="Video">
  <div class="frame" id="playerFrame"></div>
  <div class="player-bar"><span id="playerTitle"></span><button type="button" id="playerClose">Close ✕</button></div>
</dialog>"""

def film_attrs(f):
    if "yt" in f: return f'data-yt="{e(f["yt"])}"'
    if "vimeo" in f: return f'data-vimeo="{e(f["vimeo"])}"'
    return f'data-video="{e(f["video"])}"'

def img2x(src):
    """srcset for a card image that has an @2x.jpg next to it."""
    if src.startswith(W) and "@2x" not in src:
        return f' srcset="{src} 1024w, {src.rsplit(".", 1)[0]}@2x.jpg 2048w"'
    return ""

# ---------- Home: the carousel ----------
def home():
    slides = "".join(
        f'<a class="slide" href="/work/{p["slug"]}/" data-i="{i}" aria-label="{e(p["name"])}">'
        f'<img src="{p["card"]}"{img2x(p["card"])} sizes="320px" alt="" {"loading=\"lazy\" " if i > 3 and i < len(PROJECTS) - 3 else ""}draggable="false"></a>'
        for i, p in enumerate(PROJECTS))
    info = "".join(
        f'<div class="info" data-i="{i}"{"" if i == 0 else " hidden"}><div class="info-left"><h1>{e(p["name"])}</h1><p>{e(p["lead"])}</p><span class="info-year">{e(p["year"])}</span></div>'
        f'<p class="info-type">{e(p["type"])}</p></div>' for i, p in enumerate(PROJECTS))
    person = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Taylor Powers",'
              '"jobTitle":"Brand & Marketing Executive","url":"https://taylorpowers.com/","image":"https://taylorpowers.com/assets/home/avatar.jpg",'
              f'"email":"mailto:{EMAIL}","sameAs":["{LINKEDIN}"]}}</script>\n')
    return (head("Taylor Powers — Brand & Marketing Executive", ABOUT["statement"], "/", "/assets/og.jpg", person)
            + f"""<body class="home">
<main class="stage" aria-roledescription="carousel" aria-label="Selected work">
  <div class="infos" aria-live="polite">{info}</div>
  <div class="ring">{slides}</div>
  <div class="arrows"><button type="button" class="arrow prev" aria-label="Previous work">‹</button><button type="button" class="arrow next" aria-label="Next work">›</button></div>
</main>
<footer class="home-nav"><span class="me">Taylor Powers</span>{nav("inline", "home")}</footer>
<script src="/assets/carousel.js?v={V}" defer></script>
</body>
</html>
""")

# ---------- Work: all projects ----------
def work_index():
    cards = "".join(
        f'<a class="w-card{" tall" if i % 2 else ""}" href="/work/{p["slug"]}/"><span class="w-img"><img src="{p["card"]}"{img2x(p["card"])} sizes="(max-width: 809px) 100vw, 45vw" alt="" loading="lazy"></span>'
        f'<span class="w-name">{e(p["name"])}</span><span class="w-sub">{e(p["type"])} · {e(p["year"])}</span></a>' for i, p in enumerate(PROJECTS))
    return (head("Work · Taylor Powers", "Selected work by Taylor Powers: brand launches, sports partnerships, campaigns and visual effects.", "/work/", "/assets/og.jpg")
            + f"""<body class="page">
{nav("ink", "work")}
<main class="wrap">
  <h1 class="page-title">Selected <span>work</span></h1>
  <div class="w-grid">{cards}</div>
</main>
{FOOT}
</body>
</html>
""")

# ---------- About ----------
def about():
    a = ABOUT
    jobs = "".join(f'<li class="job"><div><h3>{e(t)}</h3><p>{e(d)}</p></div><span>{e(c)}</span><span class="yr">[{e(y)}]</span></li>' for t, c, y, d in a["jobs"])
    services = "".join(f'<li><span class="num">{i:02d}.</span><h3>{e(n)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></li>' for i, (n, items) in enumerate(a["services"], 1))
    numbers = "".join(f'<div><dt>{e(n)}</dt><dd>{e(l)}</dd></div>' for n, l in a["numbers"])
    logos = "".join(f'<img class="h{h}" src="/assets/home/logos/{n}.{"svg" if n == "skil" else "png"}" alt="{e(alt)}">' for n, alt, h in LOGOS)
    return (head("About · Taylor Powers", a["statement"], "/about/", "/assets/og.jpg")
            + f"""<body class="page">
{nav("ink", "about")}
<main>
  <section class="wrap about-top">
    <p class="statement">{e(a["statement"])}</p>
    <div class="cols about-more"><div></div><div>{"".join(f"<p>{e(x)}</p>" for x in a["paras"])}<a class="btn solid" href="{LINKEDIN}" target="_blank" rel="noopener">Let’s connect</a></div></div>
  </section>
  <section class="wrap about-photos">
    <figure class="ph-small"><img src="/assets/home/work/superfile-brand-launch.jpg" alt="" loading="lazy"></figure>
    <figure class="ph-big"><img src="/assets/img/taylor-portrait.jpg" alt="Taylor Powers"></figure>
  </section>
  <section class="wrap row">
    <h2>Brands and studios, and my experience.</h2>
    <div class="row-text"><p>Hollywood visual effects, then agency leadership, then building a brand from the ground up.</p></div>
  </section>
  <section class="wrap"><ul class="jobs">{jobs}</ul></section>
  <section class="wrap logos" aria-label="Brands and studios">{logos}</section>
  <section class="wrap"><ol class="services">{services}</ol></section>
  <section class="wrap row">
    <h2>In numbers.</h2>
    <div class="row-text"><dl class="figures">{numbers}</dl></div>
  </section>
  <div class="spacer"></div>
</main>
{FOOT}
</body>
</html>
""")

# ---------- Case study ----------
def page(p, more):
    light = p.get("hero_light")
    hero = (f'<video class="hero-media" autoplay muted loop playsinline poster="{p["hero_img"]}" aria-hidden="true"><source src="{p["hero_clip"]}" type="video/mp4"></video>'
            if p.get("hero_clip") else f'<img class="hero-media" src="{p["hero_img"]}" alt="{e(p["client"])}">')
    if p.get("hero_vimeo"):
        hero += (f'<iframe class="case-hero-vimeo" data-hd src="https://player.vimeo.com/video/{p["hero_vimeo"]}?background=1&autoplay=1&loop=1&muted=1&dnt=1" '
                 f'allow="autoplay; fullscreen; picture-in-picture" title="{e(p["client"])}" aria-hidden="true" tabindex="-1"></iframe>')
    body = "".join(f"<p>{e(t)}</p>" for t in p["body"])
    media = ""
    if p.get("film"):
        poster = p["card"].rsplit(".", 1)[0] + "@2x.jpg" if p["card"].startswith(W) else p["hero_img"]
        media += (f'<button type="button" class="full film" {film_attrs(p["film"])} data-title="{e(p["film"]["title"])}">'
                  f'<img src="{poster}" alt="" loading="lazy"><span class="play"><span class="play-dot" aria-hidden="true"></span>Watch the film</span></button>')
    photos = [g for g in p["gallery"] if g != p["hero_img"]]
    if len(photos) == 1:
        g = photos[0]
        media += f'<figure class="full{" light" if "art-car" in g else ""}"><img src="{g}" alt="" loading="lazy"></figure>'
    elif photos:
        media += '<div class="pair">' + "".join(f'<figure class="{"light" if "art-car" in g else ""}"><img src="{g}" alt="" loading="lazy"></figure>' for g in photos) + "</div>"
    media = f'<section class="media wrap">{media}</section>' if media else ""
    results = ""
    if p["figures"] or p.get("link"):
        figs = "".join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in p["figures"])
        link = f'<a class="text-link" href="{e(p["link"][1])}" target="_blank" rel="noopener">{e(p["link"][0])} ↗</a>' if p.get("link") else ""
        results = (f'<section class="row wrap"><h2>{"Results." if p["figures"] else "Coverage."}</h2><div class="row-text">'
                   f'{f"<dl class=figures>{figs}</dl>" if figs else ""}{link}</div></section>')
    cards = "".join(
        f'<a class="more-card" href="/work/{m["slug"]}/"><span class="more-img"><img src="{m["card"]}"{img2x(m["card"])} sizes="(max-width: 809px) 100vw, 45vw" alt="" loading="lazy"></span>'
        f'<span class="more-name">{e(m["name"])}</span><span class="more-sub">{e(m["type"])} · {e(m["year"])}</span></a>' for m in more)
    return (head(f'{p["name"]} · Taylor Powers', p["lead"], f'/work/{p["slug"]}/', p["hero_img"])
            + f"""<body class="case">
{nav("on-light" if light else "", "work")}
<main>
  <section class="hero{" light-hero" if light else ""}">
    <div class="hero-frame">{hero}</div>
    <div class="hero-shade" aria-hidden="true"></div>
    <a class="all-works" href="/work/">← All Works</a>
    <div class="hero-copy">
      <h1>{e(p["name"])}</h1>
      <p>{e(p["lead"])}</p>
      <dl class="facts">
        <div><dt>Year</dt><dd>{e(p["year"])}</dd></div>
        <div><dt>Type</dt><dd>{e(p["type"])}</dd></div>
      </dl>
    </div>
  </section>
  <section class="intro"><div class="wrap cols"><div></div><div class="intro-text">{body}</div></div></section>
  <section class="row wrap">
    <h2>Taylor’s role.</h2>
    <div class="row-text"><p>{e(p["role"])}.</p><p>{e(" · ".join(p["disciplines"]))}</p></div>
  </section>
  {media}
  {results}
  <section class="more wrap">
    <h2>More to explore.</h2>
    <p>Two more projects to look through.</p>
    <div class="more-grid">{cards}</div>
  </section>
</main>
{FOOT}
{PLAYER}
<script src="/assets/site.js?v={V}" defer></script>
</body>
</html>
""")

def write(rel, text):
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print("wrote", rel)

if __name__ == "__main__":
    write("index.html", home())
    write("work/index.html", work_index())
    write("about/index.html", about())
    n = len(PROJECTS)
    for i, p in enumerate(PROJECTS):
        write(f"work/{p['slug']}/index.html", page(p, [PROJECTS[(i + 1) % n], PROJECTS[(i + 2) % n]]))
