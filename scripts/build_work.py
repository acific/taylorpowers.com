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
V = "43"  # cache stamp for /assets/main.css, /assets/site.js and /assets/carousel.js; 404.html uses it too

EMAIL = "taylorraepowers@icloud.com"
LINKEDIN = "https://www.linkedin.com/in/taylorpowers2026"

# Each project: slug, name (as on the cards), type (the card's role label), year, client, title,
# role, disciplines, lead (one line), body (paragraphs), card (the card/carousel image),
# hero_img (case-page hero; defaults to the card's 2x image), optional hero_clip / hero_vimeo /
# hero_light, figures [(number, label)], film {yt|vimeo|video, title}, link (label, url), gallery [img].
W = "/assets/home/work/"
I = "/assets/img/"
PROJECTS = [
    dict(slug="superfile-trackhouse-nascar", name="SuperFile × Trackhouse Racing NASCAR", type="Brand Management",
         client="SuperFile × Trackhouse Racing", title="Daytona 500",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Sponsorship", "Livery", "Race-weekend activation", "VIP hospitality"],
         card=W + "trackhouse-nascar.jpg", hero_clip="/assets/clips/nascar-daytona.mp4", hero_img=I + "nascar-daytona-speed.jpg",
         lead="SuperFile’s first NASCAR partnership arrived on the sport’s biggest stage: Shane van Gisbergen’s black-and-neon #97 Chevrolet at the 2026 Daytona 500.",
         body=["On February 6, 2026, Trackhouse Racing announced SuperFile as the sponsor of Shane van Gisbergen’s No. 97 Chevrolet for the 68th Daytona 500. It was the Chicago company’s first step into NASCAR, introducing a brand built on what it calls sovereign file control: content that stays “trackable, unhackable, takebackable.”",
               "“There is no better place than Daytona to introduce SuperFile to NASCAR for the first time,” van Gisbergen said. Trackhouse owner Justin Marks added that SuperFile “has a very unique position in the tech space.”"],
         role_text=["Taylor oversaw the sponsorship rights, partner assets and brand integration, and built the event operation behind race-weekend hospitality for investors, clients and customers, from logistics and vendors to on-site execution."],
         sections=[
             dict(h="Daytona.", p=["The black and neon-yellow No. 97 started 13th in the Daytona 500 and led laps 101 to 103 before it was caught in the late Stage 2 crash. After repairs it finished 30th, one lap down.",
                                   "The race set the look for SuperFile’s season: a dark car with the SuperFile mark across the hood."],
                  img=[I + "nascar-daytona-pit-road.jpg", I + "nascar-daytona-grandstand.jpg"]),
             dict(h="A season of liveries.", p=["The deal grew into a multi-year, multi-race partnership, and the No. 97 changed its look through the year: a Mr. Brainwash art car for Las Vegas in March, a “SuperFile Salutes” digital-camo military tribute for the Coca-Cola 600 on Memorial Day weekend, and a Chicago-inspired livery by the artist Lefty Out There at Chicagoland in July.",
                                                "SuperFile was also announced as primary sponsor of Connor Zilisch’s No. 88 for New Hampshire in August, and several of the cars became official Lionel die-casts."],
                  img=[I + "nascar-martinsville.jpg", I + "nascar-texas-pit.jpg", I + "nascar-svg-daytona.jpg", I + "nascar-svg-texas.jpg"],
                  film=dict(video="/assets/video/nascar-new-hampshire.mp4", poster="/assets/video/nascar-new-hampshire.jpg", title="SuperFile at New Hampshire", label="Watch New Hampshire")),
             dict(h="Watkins Glen.", p=["On May 10, van Gisbergen won at Watkins Glen from pole, leading 74 of 100 laps and finishing more than seven seconds clear for his seventh Cup Series victory.",
                                        "“Yeah, this SuperFile Chevy was great,” he said afterwards."],
                  img=[I + "nascar-wg-burnout.jpg", I + "nascar-wg-smoke.jpg", I + "nascar-wg-victory-lane.jpg", I + "nascar-wg-champagne.jpg", I + "nascar-wg-trophy-group.jpg", I + "nascar-wg-trophy.jpg"]),
         ],
         figures=[("74 / 100", "Laps led from pole, Watkins Glen"), ("7th", "Cup Series win for van Gisbergen")],
         film=dict(video="/assets/video/nascar-daytona-500.mp4", poster="/assets/video/nascar-daytona-500.jpg", title="SuperFile × Trackhouse Racing at the Daytona 500"),
         link=("Watkins Glen win", "https://www.motorsport.com/nascar-cup/news/Shane-van-gisbergen-wins-nascar-watkins-glen/10819836/"),
         gallery=[]),
    dict(slug="superfile-brand-launch", name="SuperFile Brand Launch", type="Brand Management",
         client="SuperFile", title="Brand launch",
         year="2025 — 2026", role="VP of Brand, SuperFile", disciplines=["Brand development", "Integrated marketing", "Content", "Social"],
         card=W + "superfile-brand-launch.jpg", hero_clip="/assets/clips/superfile-anthem.mp4", hero_img="/assets/video/superfile-anthem.jpg",
         lead="Taking a new kind of security company to market, from its first brand system to some of the biggest stages in sport.",
         body=["SuperFile is a Chicago technology company building what it calls sovereign file control: letting enterprises, governments and creators secure, authenticate, track and revoke access to their content even after it has been shared or downloaded. Its line is “Trust. Control. Simplicity.”",
               "Led by founder and CEO Shane Valdez, the company opened an early-access waitlist where people reserve their own @name while the product is in development, and took the brand straight into sport."],
         role_text=["Taylor launched SuperFile’s brand, building and leading a 25+ person department across brand, strategy, creative, partnerships and production, and aligning marketing, product and sales on go-to-market.",
                    "On social, Taylor launched and scaled SuperFile’s Instagram to more than 150,000 followers in eight months, averaging 18,000+ new followers a month."],
         sections=[
             dict(h="From zero to the world stage.", p=["In 2026 the brand debuted at the Daytona 500, became title sponsor of a MotoGP team, went inside the Octagon at UFC FREEDOM 250 at the White House, signed on for WWE’s Premium Live Events and went onto the front of LAFC’s training kit.",
                                                        "Each partnership carried the same black and neon-yellow identity, from a race car’s hood to a fighter’s glove."]),
             dict(h="The anthem.", p=["The 30-second anthem film put the launch identity on screen in the brand’s black and neon yellow.",
                                    "It built on the brand film Valdez released in October 2024, which set out the idea before the product: “SuperFile isn’t just a tool — it’s a vision. It’s for creators.”"]),
         ],
         figures=[("$20M+", "Production budgets managed"), ("150K+", "Instagram followers in 8 months"), ("25+", "Person department built")],
         film=dict(video="/assets/video/superfile-anthem.mp4", poster="/assets/video/superfile-anthem.jpg", title="SuperFile anthem"),
         link=("SuperFile", "https://superfile.com"), gallery=[]),
    dict(slug="wylie-co", name="Wylie Co.", type="VFX Coordinator",
         client="Wylie Co.", title="Visual effects for film and television",
         year="2017 — 2020", role="VFX Coordinator, Wylie Co.", disciplines=["VFX production", "Feature film", "Television"],
         card=W + "wylie-dune.jpg", hero_img=I + "dune-eyes-of-ibad.jpg",
         lead="Visual effects production at Wylie Co., the studio behind postvis and final effects on Dune, including the Fremen’s blue eyes.",
         body=["Wylie Co. is a boutique visual effects studio in Culver City and Montreal, founded in 2015 as Rebellion VFX. Its credits run from Everest and Terminator: Dark Fate to Beastie Boys Story, The Stand and Dune.",
               "The studio works across the whole pipeline: previsualization, postvis that lets editors cut with temporary effects, and final shots."],
         role_text=["As VFX Coordinator, Taylor managed production workflows across the studio’s film and television slate, including Dune: Part One, Terminator: Dark Fate and Marvel productions."],
         sections=[
             dict(h="Dune.", p=["On Dune (2021), Wylie completed around 450 postvis shots and 950 visual effects shots. DNEG led the film’s effects, with Wylie Co. and Rodeo FX contributing.",
                                "To help Denis Villeneuve plan the scale of Arrakis, Wylie built a Vislab and an iOS app, Wylie Cam, that let him frame wide shots from an iPad."],
                  img=[I + "dune-mocha.jpg"]),
             dict(h="The Eyes of Ibad.", p=["Wylie delivered the Fremen’s blue “Eyes of Ibad”: nearly 450 eye shots, each tracked and composited so the glow sat naturally in every frame."]),
             dict(h="The Oscar.", p=["Dune won Best Visual Effects at the 94th Academy Awards, and the BAFTA and VES awards for its effects."]),
         ],
         figures=[("950", "VFX shots by Wylie on Dune"), ("~450", "Eyes of Ibad shots"), ("Oscar", "Best Visual Effects, Dune")],
         link=("How Wylie made Dune’s blue eyes", "https://borisfx.com/news/wylie-co--tracks-dunes-eyes-of-ibad-with-mocha-pro/"), gallery=[]),
    dict(slug="flex-lafc", name="FLEX Power Tools × LAFC", type="Account Management",
         client="FLEX × LAFC", title="Front of the jersey",
         year="2021 — 2023", role="Account Director → Senior Account Director, Realm Agency", disciplines=["Jersey sponsorship", "Campaign development", "Partner relations", "Experiential"],
         card=W + "flex-lafc.jpg", hero_clip="/assets/clips/flex-falcon.mp4", hero_img="/assets/clips/flex-falcon.jpg", hero_vimeo="781610331",
         lead="FLEX Power Tools on the front of Los Angeles FC’s jersey: a multi-year deal that launched a new tool brand with one of MLS’s loudest clubs.",
         body=["On March 26, 2021, LAFC named FLEX its Official Jersey Sponsor, replacing YouTube TV and putting FLEX on every Club, Community and specialty jersey. It was the first sports partnership for FLEX’s parent company, Chervon North America.",
               "The deal made FLEX the club’s Official Power Tool Partner and a member of its top Golden Boot Club tier, with exclusive content, media, signage and a co-branded retail promotion, timed to FLEX’s launch at Lowe’s that spring."],
         role_text=["At Realm Agency, Taylor worked across the sponsorship from campaign development and partner relations to experiential activations. The program reached more than 60 billion impressions."],
         sections=[
             dict(h="Welcome to the Club.", p=["LAFC announced the partnership with “Welcome to the Club FLEX Power Tools.” Two days later the club unveiled its Heart of Gold Community Kit with FLEX across the middle, gifting jerseys to essential workers at the launch."],
                  img=[I + "flex-welcome-club.jpg", I + "flex-heart-of-gold.jpg"]),
             dict(h="Three seasons on the front.", p=["FLEX stayed across the chest through the 2022 “5 Years Strong” primary kit and the 2023 “Smokescreen” away kit, both revealed at kit launches presented by FLEX Power Tools."],
                  img=[I + "flex-5-years-strong.jpg", I + "flex-smokescreen.jpg"]),
         ],
         figures=[("60B+", "Impressions"), ("3", "Seasons of kits with FLEX on the front")], film=dict(vimeo="781610331", title="FLEX × LAFC"),
         link=("The 2022 kit on LAFC.com", "https://www.lafc.com/culture/kit/2022"),
         gallery=[]),
    dict(slug="superfile-ufc-wwe", name="SuperFile × UFC", type="Brand Management",
         client="SuperFile × UFC & WWE", title="Fight night, worldwide",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Global partnership", "Live events", "Broadcast integration"],
         card=W + "superfile-ufc-wwe.jpg", hero_clip="/assets/clips/ufc-freedom-250.mp4", hero_img="/assets/clips/ufc-freedom-250.jpg",
         lead="A global partnership with TKO that made SuperFile the first Official Secure File Sharing Partner of both UFC and WWE.",
         body=["TKO and SuperFile announced the partnership on June 9, 2026, creating a new sponsorship category across both properties.",
               "“SuperFile is redefining how organizations protect, control, and share their digital content,” said Robby Miller of TKO. “When you build a company, there are certain moments you never forget,” said Shane Valdez. “This will be one of them.”"],
         role_text=["Taylor developed and managed the partnership across sponsorship rights, partner assets, brand integration and activation."],
         sections=[
             dict(h="The White House.", p=["Five days later SuperFile was an Official Partner of UFC FREEDOM 250 on the White House grounds, with its branding inside the Octagon and broadcast integrations reaching an estimated one billion households in 210 countries and territories.",
                                           "SuperFile presented the night’s Super Replay of its most memorable moments, a “Keys to Victory” feature on each fighter’s strategy, and the one-hour UFC FREEDOM 250 SuperFile Post-Show. Its mark also stood in front of the scale at the weigh-ins."],
                  film=dict(video="/assets/video/ufc-freedom-250.mp4", poster="/assets/video/ufc-freedom-250.jpg", title="SuperFile at UFC FREEDOM 250", label="Watch FREEDOM 250")),
             dict(h="UFC 329.", p=["SuperFile was then presenting partner of UFC 329, McGregor vs. Holloway 2, at T-Mobile Arena in Las Vegas on July 11, the headline event of International Fight Week, with activation across UFC’s numbered events and Fight Nights.",
                                  "Its mark ran across the fight poster and the weigh-in stage, and sat on the scale itself the day before, when Conor McGregor made weight for his first fight since 2021."],
                  img=[I + "ufc329-poster.jpg", I + "ufc329-weigh-in.jpg"],
                  film=dict(video="/assets/video/ufc-329.mp4", poster="/assets/video/ufc-329.jpg", title="SuperFile at UFC 329", label="Watch UFC 329")),
             dict(h="Round one.", p=["The round cards carried SuperFile too. For the co-main event, Paddy Pimblett against Benoît Saint Denis, Indiana Fever guard Sophie Cunningham walked the Octagon as a surprise ring-card holder with the SuperFile “1”. Dana White said he booked her about eight minutes before she went out, and the moment ran across Fox, Sports Illustrated and Bleacher Report."],
                  img=[I + "ufc329-round-card-cage.jpg", I + "ufc329-round-card.jpg"]),
             dict(h="WWE.", p=["In WWE, the deal brings side-ring-mat placements, presenting-partner designations and custom social and digital content across Premium Live Events including WrestleMania, Money in the Bank, Survivor Series and the Royal Rumble."]),
         ],
         figures=[("1B", "Households, UFC FREEDOM 250"), ("210", "Countries and territories")],
         link=("Partnership announcement", "https://www.ufc.com/news/tko-and-superfile-announce-global-partnership-across-ufc-and-wwe"),
         gallery=[]),
    dict(slug="superfile-lefty-out-there", name="SuperFile × Lefty Out There Artist Collaborations", type="Brand Management",
         client="SuperFile × Lefty Out There", title="Artist collaborations",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Artist collaboration", "Livery", "Merchandise"],
         card=W + "lefty-out-there.jpg", hero_clip="/assets/clips/lefty-chicagoland.mp4", hero_img=W + "lefty-out-there@2x.jpg",
         lead="SuperFile handed Shane van Gisbergen’s #97 to Chicago artist Lefty Out There for NASCAR’s return to Chicagoland.",
         body=["Trackhouse revealed the one-of-a-kind scheme on July 2, 2026: a Chicago-inspired SuperFile livery designed in part by Francesco Campanella, the Chicago-based visual artist who works as Lefty Out There.",
               "Black and white abstract shapes with neon-yellow accents wrapped the car, with SuperFile on the door and Lefty Out There behind the number."],
         role_text=["Part of SuperFile’s run of artist cars inside its Trackhouse Racing partnership, which Taylor led as VP of Brand."],
         sections=[
             dict(h="Chicagoland.", p=["The car ran in the eero 400 at Chicagoland Speedway, NASCAR’s first Cup race there since 2019, on an oval van Gisbergen had never raced. “It looks really challenging, really bumpy,” he said beforehand. He started 30th and finished 25th."],
                  img=[I + "lefty-race.jpg", I + "lefty-pit.jpg"]),
             dict(h="The artist.", p=["It was Lefty Out There’s second major motorsport project, after a virtual F1 livery with Max Verstappen. The car was also released as Lionel 1:24 and 1:64 die-casts and a T-shirt."],
                  img=[I + "lefty-artist.jpg", I + "lefty-door.jpg"]),
         ],
         figures=[], film=dict(video="/assets/video/nascar-chicagoland.mp4", poster="/assets/video/nascar-chicagoland.jpg", title="SuperFile × Lefty Out There at Chicagoland"),
         link=("The Chicagoland livery", "https://speedcafe.com/nascar-news-2026-cup-series-chicagoland-shane-van-gisbergen-livery-lefty-out-there-details/"), gallery=[]),
    dict(slug="superfile-lafc", name="SuperFile × LAFC", type="Brand Management",
         client="SuperFile × LAFC", title="The SuperFile training kit",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Sports partnership", "Training kit", "Brand integration", "Content"],
         card=W + "superfile-lafc.jpg",
         lead="SuperFile on the front of LAFC’s training kit, launched with the club’s own announcement film.",
         body=["Early in 2026 SuperFile became a Golden Boot Club partner of Los Angeles FC, the club’s top partnership tier, and the front-of-training-kit sponsor, putting the brand on the LAFC Training Kit the squad wears every day.",
               "LAFC gave fans a first look on April 4: “Final touches before kickoff. First look in the SuperFile training tops.”"],
         role_text=["Taylor developed and managed the partnership as part of SuperFile’s sports program."],
         sections=[
             dict(h="The kit.", p=["LAFC describes the kit as designed for the modern athlete and built for the daily grind, bridging high-performance technology and the club’s Black & Gold look. The club introduced it with a SuperFile announcement film shot with the players."],
                  img=[I + "lafc-superfile-l2.jpg", I + "lafc-superfile-l3.jpg"]),
             dict(h="Matchday.", p=["The tops went straight into pre-match warm-ups at BMO Stadium, in white for the squad and green for the goalkeepers."],
                  img=[I + "lafc-superfile-warmup.jpg", I + "lafc-superfile-keepers.jpg"]),
             dict(h="A force for good.", p=["To mark the start of the partnership, SuperFile donated $50,000 to the LAFC Foundation to support youth soccer and grow the game across Los Angeles."],
                  img=[I + "lafc-superfile-pitch.jpg"]),
         ],
         figures=[("$50K", "Donated to the LAFC Foundation")],
         film=dict(bc="5534894108001/6394924761112", title="LAFC × SuperFile — Training kit announcement"),
         link=("The kit on LAFC.com", "https://www.lafc.com/culture/kit/superfile"),
         gallery=[I + "lafc-superfile-p1.jpg", I + "lafc-superfile-p3.jpg"]),
    dict(slug="superfile-trackhouse-motogp", name="SuperFile Trackhouse MotoGP", type="Brand Management",
         client="SuperFile Trackhouse MotoGP Team", title="Name on the grid",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Title partnership", "Content", "Hospitality"],
         card=W + "trackhouse-motogp.jpg", hero_img=I + "motogp-assen-1-2.jpg",
         lead="From logos on the fairing to the name on the team: SuperFile became the first title sponsor of Trackhouse’s MotoGP team, and the bikes started winning.",
         body=["SuperFile first appeared on the Trackhouse Aprilias at the Spanish Grand Prix at Jerez in April 2026, the team’s first crossover between its NASCAR and MotoGP programs.",
               "On June 5 it became the team’s title sponsor, the first since Trackhouse entered MotoGP in 2024, with the black-and-yellow livery running from the Hungarian Grand Prix at Balaton Park. “What excites me most isn’t seeing the SuperFile name on the bike,” said Shane Valdez. “It’s who we’re building with.”"],
         role_text=["Building on the NASCAR program, Taylor ran the partnership across rights, assets, paddock content and hospitality at each round."],
         sections=[
             dict(h="Assen.", p=["At the Dutch TT in June the SuperFile bikes finished first and second twice. Raúl Fernández won the Sprint from fourth on the grid with Ai Ogura second; the next day Ogura took his first MotoGP win with Fernández second.",
                                 "Ogura became the first Japanese premier-class winner since 2004, and motogp.com noted that a double one-two in Sprint and Grand Prix had only been done before by the Ducati Lenovo Team."],
                  img=[I + "motogp-medal.jpg", I + "motogp-parc-ferme.jpg"]),
             dict(h="A summer on the podium.", p=["Ogura took pole at Brno and finished second. At the Sachsenring the team scored a second double podium in a row, Ogura second and Fernández third. At Silverstone in August, Fernández led from lights to flag for his second MotoGP win."],
                  img=[I + "motogp-silverstone.jpg", I + "motogp-garage.jpg"]),
         ],
         figures=[("1–2", "Sprint and Grand Prix, Dutch TT"), ("2", "Grand Prix wins in SuperFile colours")],
         film=dict(yt="JF26n2-jgBI", title="SuperFile Trackhouse MotoGP Team"),
         link=("Title sponsor announcement", "https://www.crash.net/motogp/news/1096813/1/motogps-newest-team-finally-gains-title-sponsor-third-year"), gallery=[]),
    dict(slug="ego", name="EGO Z6 Launch", type="Production",
         client="EGO Power+", title="EGO Z6 launch",
         year="2021", role="Realm Agency", disciplines=["Product launch", "Live action", "VFX", "Post-production"],
         card=W + "ego-z6.jpg", hero_clip="/assets/clips/ego.mp4", hero_img="/assets/clips/ego.jpg",
         lead="Launch creative for the EGO Z6, the world’s first platform-compatible zero-turn rider.",
         body=["EGO introduced the 42-inch Z6 as the world’s first platform-compatible zero-turn rider: it runs on the same 56V batteries as the rest of the POWER+ line. It reached Lowe’s, Ace Hardware and EGO dealers from February 2021, after what EGO says was more than six years of research and development.",
               "Its launch film, “Power without limits,” published in March 2021, carried the line “Power Like No Other.”"],
         role_text=["At Realm Agency, Taylor oversaw the delivery of more than 20,000 creative and campaign assets for EGO, SKIL and FLEX, supporting over 200 product launches, and executive produced campaigns across live action, VFX, animation and post-production."],
         sections=[
             dict(h="The machine.", p=["EGO rates the Z6 at the power of a 22 HP gas engine, with a top speed of 8 mph and up to two acres on a charge from four 10Ah batteries, with room for six. Four brushless motors, three drive modes, 32 LEDs and Bluetooth, with a five-year warranty on the machine and batteries."],
                  img=[I + "ego-z6-2021.jpg"]),
         ],
         figures=[("20,000+", "Assets delivered for EGO, SKIL & FLEX"), ("200+", "Product launches supported"), ("22 HP", "Gas-equivalent power, per EGO")],
         film=dict(yt="d1Lis7rNkAg", title="EGO Z6 — Power without limits"),
         link=("The EGO Z6", "https://egopowerplus.com/zero-turn-riding-mower-zt4204l/"), gallery=[]),
    dict(slug="skil", name="SKIL Gas Zombies Campaign", type="Account Management",
         client="SKIL", title="Don’t be a gas zombie",
         year="2022", role="Realm Agency", disciplines=["National TV", "Campaign", "Product launch"],
         card=W + "skil-gas-zombies.jpg", hero_clip="/assets/clips/skil-gas-zombie.mp4", hero_img="/assets/clips/skil-gas-zombie.jpg",
         lead="“Don’t Be a Gas Zombie”: SKIL’s national TV spot for its PWRCORE 40 cordless outdoor range.",
         body=["SKIL’s spot for PWRCORE 40, first published in March 2022, pitched its brushless 40V string trimmer, leaf blower, self-propelled mower and chainsaw as the way out of a world controlled by gas.",
               "SKIL carried the same idea across its pages: “Ditch the gas, keep the power.”"],
         role_text=["Part of Realm Agency’s work across Chervon’s brands, where Taylor led integrated campaigns from concept through delivery, coordinating creative teams, production, post-production and external partners."],
         sections=[
             dict(h="The spot.", p=["It plays for laughs: a couple shares their SKIL tools with their zombie neighbors, while one stubborn holdout tears his arm off trying to start his gas equipment. It closes on SKIL’s tagline, “What Powers You?”, with the range available at Lowe’s."],
                  img=[I + "skil-frame-blower.jpg", I + "skil-frame-handoff.jpg"]),
             dict(h="The reach.", p=["SKIL’s own 30-second upload had passed 18.9 million views on YouTube by November 2026, pointing viewers to a single call to action: ditch the gas."]),
         ],
         figures=[("18.9M", "YouTube views of the spot")], film=dict(yt="8U5-WrfmTlE", title="SKIL — Don’t Be a Gas Zombie"),
         link=("The TV spot on iSpot", "https://www.ispot.tv/ad/bIBQ/skil-pwrcore-40-dont-be-a-gas-zombie"), gallery=[]),
    dict(slug="superfile-art-car", name="SuperFile × Mr. Brainwash Artist Collaboration", type="Brand Management",
         client="SuperFile × Mr. Brainwash", title="The art car",
         year="2026", role="VP of Brand, SuperFile", disciplines=["Art car", "Culture", "NASCAR"],
         card=W + "mr-brainwash.jpg", hero_img=I + "artcar-render.jpg", hero_light=True,
         lead="The #97 handed to the street artist Mr. Brainwash for Las Vegas, turning a race weekend into a culture moment.",
         body=["Trackhouse unveiled the livery on March 10, 2026: Mr. Brainwash, the LA-based street artist Thierry Guetta, known for album covers for Madonna, Rick Ross and Kygo, painted Shane van Gisbergen’s No. 97 Chevrolet to celebrate SuperFile’s multi-year, multi-race partnership with the team.",
               "The artwork also marked the launch of SuperFile’s digital ownership platform."],
         role_text=["A one-off inside the Trackhouse program Taylor ran as VP of Brand, bringing art into a sport built on speed."],
         sections=[
             dict(h="SuperBrainHouse.", p=["SuperFile called it the “SuperBrainHouse” car. “This is our celebration car,” said Shane Valdez, “launching a multi-year partnership built on speed, art, and innovation.” Launching in Las Vegas was personal: “I wanted it to begin where my story started.”"],
                  img=[I + "art-car.jpg"]),
             dict(h="Las Vegas.", p=["Sprayed neon colours, repeated No. 97 decals and an engine graphic ahead of the rear wheels made it one of the most talked-about schemes of the spring. It debuted at Las Vegas Motor Speedway on March 15. “The car looks epic,” van Gisbergen said, “kind of like the lights on the Vegas Strip.”",
                                       "Lionel released it as an official die-cast the next day."]),
         ],
         figures=[], link=("The art car", "https://speedcafe.com/nascar-news-2026-cup-series-shane-van-gisbergen-superfile-livery-mr-brainwash-photos-render/"),
         gallery=[]),
    dict(slug="flex-launch", name="FLEX Power Tools Launch", type="Account Management",
         client="FLEX Power Tools", title="Stacked Lithium launch",
         year="Realm Agency", role="Realm Agency", disciplines=["Product launch", "Campaign", "Retail"],
         card=W + "flex-launch.jpg", hero_img=I + "flex-family.jpg",
         lead="The launch of FLEX’s 24V Stacked Lithium battery: a new kind of pack built to give the whole FLEX lineup more power.",
         body=["FLEX launched as a brand exclusively with Lowe’s, announced on March 18, 2021, with its first tools on sale that April alongside a “FLEX Face Off” launch event.",
               "Its next step was Stacked Lithium, first shown in November 2021: a pouch-style pack of layered flat cells instead of cylinders, with Power IQ and Therma-Tech+ heat management."],
         role_text=["At Realm Agency, Taylor managed the FLEX account through launches like this one, part of the more than 200 product launches Realm supported for EGO, SKIL and FLEX."],
         sections=[
             dict(h="Stacked Lithium.", p=["FLEX claims up to 200% more power, 300% longer battery life and 100% faster charging, in as little as 20 minutes, with every pack cross-compatible with all FLEX 24V tools and chargers. The launch led with a hammer drill, an impact driver and a circular saw, each with a five-year limited warranty."],
                  img=[I + "flex-stacked-lithium.jpg", I + "flex-worker.jpg"]),
             dict(h="Power that changes everything.", p=["The campaign spoke straight to the trade: “This is you 200% more,” “Power that changes everything” and #ITSWHATSNEXT, carried through to retail at Lowe’s."]),
         ],
         figures=[("200%", "More power, per FLEX"), ("300%", "Longer battery life, per FLEX")],
         link=("FLEX Stacked Lithium", "https://www.flexpowertools.com/stackedlithium"), gallery=[]),
    dict(slug="digital-domain", name="Digital Domain", type="VFX Coordinator",
         client="Digital Domain", title="Digital Human Group",
         year="2020 — 2021", role="VFX Coordinator, Digital Domain", disciplines=["VFX production", "Digital humans", "Machine learning"],
         card=W + "digital-domain.jpg", hero_clip="/assets/clips/digital-domain.mp4", hero_img="/assets/clips/digital-domain.jpg",
         lead="Visual effects coordination for Digital Domain’s Digital Human Group, the team behind some of the most convincing digital people on screen.",
         body=["Digital Domain’s Digital Human Group pioneers digital and virtual humans for every medium, building on the studio’s work on Thanos in Avengers: Infinity War and The Curious Case of Benjamin Button.",
               "Its tools include Masquerade facial capture, the Charlatan face-replacement system, machine-learning clothing and real-time digital-human rendering, used across film, live events, games and mobile."],
         role_text=["Taylor coordinated visual effects production for the group, managing international workflows, artist schedules and deliverables."],
         sections=[
             dict(h="DigiDoug.", p=["At TED in 2019, Doug Roble, Digital Domain’s head of software R&D, gave a talk alongside DigiDoug, a real-time digital double driven live from a single camera."],
                  img=[I + "dd-ted.jpg", I + "dd-masquerade.jpg"]),
             dict(h="Masquerade and Charlatan.", p=["In September 2020 the group released Masquerade 2.0, rebuilt facial-capture technology from the Thanos work that uses machine learning to run ten times faster and cut artist time by 95%.",
                                                    "Charlatan, its machine-learning face-replacement system, aged David Beckham by about 30 years for Malaria No More’s “Malaria Must Die” campaign."],
                  img=[I + "dd-beckham.jpg", I + "dd-lombardi.jpg"]),
             dict(h="Vince Lombardi.", p=["In February 2021 the group worked with the NFL and 72andSunny on a digital Vince Lombardi for Super Bowl LV, made with his estate’s blessing. Masquerade 2.0 won a Lumière Award, and the NFL spot won a Silver Telly and a Silver Clio."]),
         ],
         figures=[("95%", "Less artist time with Masquerade 2.0"), ("10×", "Faster facial capture")],
         link=("Digital Domain’s digital humans", "https://digitaldomain.com/digital-humans-lab/"), gallery=[]),
    dict(slug="ego-labs", name="EGO Labs 2.0", type="Account Management / Production",
         client="EGO Power+", title="The next generation of Z6 riders",
         year="Realm Agency", role="Realm Agency", disciplines=["Product launch", "Campaign", "Production"],
         card=W + "ego-labs.jpg", hero_img=I + "ego-z6-2026-hero.jpg",
         lead="EGO’s next generation of Z6 zero-turn riders: all the power of gas, with no exhaust and no oil changes.",
         body=["EGO announced its next-generation Z6 riders on March 17, 2026, under the line “All power. Zero compromise.” They are rated up to 27 HP gas-equivalent and up to three acres on a single charge, with an 80 mm wider track, 30% more peak torque than the first Z6 and IPX5 weather resistance.",
               "“All power, zero compromise,” said Tim Baker, EGO’s vice president of product."],
         role_text=["At Realm Agency, Taylor led account management and production for EGO across product launches and campaign content."],
         sections=[
             dict(h="Three riders.", p=["The range spans the 42-inch lap-bar ZT4214L, the 42-inch ZT4215S with E-Steer, which drives like a car, and the 52-inch ZT5216L. Peak Power combines up to six of EGO’s 56V batteries, the same packs that run more than 100 EGO tools, and a color display connects to the EGO Connect app."],
                  img=[I + "ego-z6-esteer.jpg", I + "ego-z6-overhead.jpg"]),
             dict(h="The brand behind it.", p=["EGO calls itself the number-one rated brand in cordless outdoor power, with more than 250,000 five-star reviews."]),
         ],
         figures=[("27 HP", "Gas-equivalent power, per EGO"), ("3 acres", "On a single charge, per EGO"), ("100+", "EGO tools on the same batteries")],
         link=("EGO’s Z6 riding mowers", "https://egopowerplus.com/ridingmowers"), gallery=[]),
]

for p in PROJECTS:  # the case-page hero defaults to the card image at 2x
    p.setdefault("hero_img", p["card"].rsplit(".", 1)[0] + "@2x.jpg")
    p.setdefault("figures", []); p.setdefault("gallery", [])

ABOUT = dict(
    statement="I’m Taylor Powers, a brand and marketing executive across film, global consumer brands, and sports and entertainment.",
    paras=["Over 8+ years I’ve worked across Hollywood productions, global consumer brands, and high-profile partnerships in sports and entertainment.",
           "My background includes leading brand development, strategic partnerships, multidisciplinary teams, and large-scale marketing and creative production initiatives."],
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
    numbers=[("8+", "Years of experience"), ("60B+", "Impressions, FLEX × LAFC")],
    summary="Hollywood visual effects, then agency leadership, then building a brand from the ground up.",
    # Projects behind each service (same order as services), linked from the service panels
    service_work=[["superfile-brand-launch", "superfile-lefty-out-there", "superfile-lafc"],
                  ["skil", "ego", "flex-launch"],
                  ["superfile-ufc-wwe", "flex-lafc", "superfile-trackhouse-motogp"],
                  ["wylie-co", "digital-domain", "ego-labs"],
                  ["superfile-trackhouse-nascar", "superfile-art-car"]],
    # Image slots: top pair, one backdrop per service, closing pair
    img_small="/assets/about/editing.jpg", img_big="/assets/about/portrait.jpg",
    img_services=["/assets/about/service-1.jpg", "/assets/about/service-2.jpg", "/assets/about/service-3.jpg", "/assets/about/service-4.jpg", "/assets/about/service-5.jpg"],
)
ABOUT_STATEMENT_SHORT = "A brand and marketing executive with 8+ years across Hollywood productions, global consumer brands, and high-profile partnerships in sports and entertainment."

LOGOS = [("ego", "EGO", 16), ("skil", "SKIL", 19), ("flex", "FLEX", 19), ("digital-domain", "Digital Domain", 19), ("wylie", "Wylie Co.", 23),
         ("netflix", "Netflix", 18), ("abc", "ABC", 27), ("fox", "FOX", 20), ("apple-tv", "Apple TV", 22), ("superfile", "SuperFile", 17), ("realm", "Realm", 20)]

e = html.escape
CSP = ("default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; "
       "img-src 'self' data:; media-src 'self'; frame-src https://player.vimeo.com https://www.youtube-nocookie.com https://players.brightcove.net; connect-src 'self'; "
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
    return (f'<header class="nav {cls}"><nav class="nav-mid">{a("/", "Home", "home")}{a("/about/", "About", "about")}{a("/wins/", "Wins", "wins")}</nav>'
            f'<a class="nav-end" href="mailto:{EMAIL}">Contact ↗</a></header>')

FOOT = f"""<footer class="foot">
  <div class="wrap">
    <div class="cols foot-top">
      <div>
        <h2 class="rotate" aria-label="Let’s work together.">Let’s <span class="words" aria-hidden="true"><span>work together.</span><span>connect.</span><span>create.</span><span>work together.</span></span></h2>
        <p class="foot-line">Let’s work together to bring your ideas to life.</p>
      </div>
      <div class="foot-right">
        <p class="place">Chicago / Los Angeles / Las Vegas</p>
        <ul class="foot-links">
          <li><a href="{LINKEDIN}" target="_blank" rel="noopener"><span>LinkedIn</span><span aria-hidden="true">↗</span></a></li>
          <li><a href="/wins/"><span>Wins</span><span aria-hidden="true">↗</span></a></li>
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
    if "bc" in f: return f'data-bc="{e(f["bc"])}"'
    if "yt" in f: return f'data-yt="{e(f["yt"])}"'
    if "vimeo" in f: return f'data-vimeo="{e(f["vimeo"])}"'
    return f'data-video="{e(f["video"])}"'

def img2x(src):
    """srcset for a card image that has an @2x.jpg next to it."""
    if src.startswith(W) and "@2x" not in src:
        return f' srcset="{src} 1024w, {src.rsplit(".", 1)[0]}@2x.jpg 2048w"'
    return ""

# ---------- Home: the carousel ----------
# The first carousel card is Taylor herself and opens About
ME = dict(slug=None, href="/about/", name="Taylor Powers", type="Brand & Marketing Executive",
          lead=ABOUT_STATEMENT_SHORT, year="Chicago / Los Angeles / Las Vegas", card=W + "taylor-powers.jpg")

def home():
    items = [ME] + PROJECTS
    slides = "".join(
        f'<a class="slide" href="{p.get("href") or "/work/" + p["slug"] + "/"}" data-i="{i}" aria-label="{e(p["name"])}">'
        f'<img src="{p["card"]}"{img2x(p["card"])} sizes="320px" alt="" {"loading=\"lazy\" " if i > 3 and i < len(items) - 3 else ""}draggable="false">'
        + (f'<video class="slide-video" muted loop playsinline preload="none" data-src="{p["hero_clip"]}" aria-hidden="true"></video>' if p.get("hero_clip") else "")
        + '</a>'
        for i, p in enumerate(items))
    info = "".join(
        f'<div class="info" data-i="{i}"{"" if i == 0 else " hidden"}><div class="info-left"><h1>{e(p["name"])}</h1><p>{e(p["lead"])}</p><span class="info-year">{e(p["year"])}</span></div>'
        f'<p class="info-type">{e(p["type"])}</p></div>' for i, p in enumerate(items))
    logo = lambda n, alt, h: f'<img class="h{h}" src="/assets/home/logos/{n}.{"svg" if n == "skil" else "png"}" alt="{alt}" draggable="false">'
    logo_set = "".join(logo(n, e(alt), h) for n, alt, h in LOGOS)
    strip = (f'<div class="home-logos" role="region" aria-label="Brands and studios"><div class="home-logos-track">'
             f'<div class="home-logos-set">{logo_set}</div><div class="home-logos-set" aria-hidden="true">{"".join(logo(n, "", h) for n, alt, h in LOGOS)}</div></div></div>')
    person = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Taylor Powers",'
              '"jobTitle":"Brand & Marketing Executive","url":"https://taylorpowers.com/","image":"https://taylorpowers.com/assets/home/avatar.jpg",'
              f'"email":"mailto:{EMAIL}","sameAs":["{LINKEDIN}"]}}</script>\n')
    return (head("Taylor Powers — Brand & Marketing Executive", ABOUT["statement"], "/", "/assets/og.jpg", person)
            + f"""<body class="home">
<main class="stage" aria-roledescription="carousel" aria-label="Selected work">
  <div class="infos" aria-live="polite">{info}</div>
  <div class="ring">{slides}</div>
  {strip}
  <div class="arrows"><button type="button" class="arrow prev" aria-label="Previous work"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M13.5 8L9.5 12L13.5 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button><button type="button" class="arrow next" aria-label="Next work"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M10.5 8L14.5 12L10.5 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>
</main>
<footer class="home-nav">{nav("inline", "home")}</footer>
<script src="/assets/carousel.js?v={V}" defer></script>
</body>
</html>
""")

# ---------- Work: all projects ----------
WINS = [
    dict(id="watkins-glen", slug="superfile-trackhouse-nascar", partner="SuperFile × Trackhouse Racing",
         series="NASCAR Cup Series", when="May 10, 2026", place="Watkins Glen", title="Victory lane at Watkins Glen.",
         stat=("74/100", "Laps led from pole"), stat2=("7th", "Cup Series win for van Gisbergen"),
         p=["Shane van Gisbergen put the SuperFile Chevrolet on pole for Go Bowling at The Glen, led 74 of the 100 laps and won by more than seven seconds.",
            "It came three months after the brand’s NASCAR debut at the Daytona 500. Taylor, who ran the partnership, was in victory lane with the team."],
         hero=I + "nascar-wg-burnout.jpg", gallery=[I + "nascar-wg-trophy-group.jpg", I + "nascar-wg-victory-lane.jpg"],
         caption="Taylor, beside the trophy, with van Gisbergen and the SuperFile team."),
    dict(id="assen-silverstone", slug="superfile-trackhouse-motogp", partner="SuperFile Trackhouse MotoGP Team",
         series="MotoGP", when="June & August 2026", place="Assen & Silverstone", title="One-two at Assen. Lights to flag at Silverstone.",
         stat=("1–2", "Sprint and Grand Prix, Dutch TT"), stat2=("2", "Grand Prix wins in SuperFile colours"),
         p=["At the Dutch TT the SuperFile Aprilias finished first and second twice in one weekend. Raúl Fernández won the Sprint; the next day Ai Ogura took his first MotoGP win, the first for a Japanese rider in the premier class since 2004.",
            "In August, Fernández led every lap at Silverstone for his second Grand Prix win."],
         hero=I + "motogp-assen-1-2.jpg", gallery=[I + "motogp-silverstone.jpg", I + "motogp-medal.jpg"], caption=""),
    dict(id="mls-cup", slug="flex-lafc", partner="FLEX Power Tools × LAFC",
         series="MLS Cup", when="November 5, 2022", place="Los Angeles", title="Champions, with FLEX on the front.",
         stat=("128′", "Bale’s equaliser, the latest goal in MLS history"), stat2=("3–0", "On penalties after a 3–3 draw"),
         p=["LAFC won its first MLS Cup in FLEX’s second season on the front of the shirt. Gareth Bale’s header in the 128th minute forced a shootout, and LAFC beat the Philadelphia Union 3–0 on penalties.",
            "With the Supporters’ Shield already won, it completed the club’s first double."],
         hero=I + "wins-lafc-mls-cup.jpg", gallery=[I + "wins-lafc-bale.jpg", I + "wins-lafc-vela.jpg"], caption="",
         feature=dict(img=I + "wins-lafc-ring.jpg", kicker="The ring", title="128 black diamonds.",
                      text="LAFC presented its championship rings, made with Baron, on March 4, 2023. The top carries 128 black diamonds for Bale’s 128th-minute goal, set in a black obsidian finish that was a first in major league sports.")),
]

def wins():
    by_slug = {p["slug"]: p for p in PROJECTS}
    index = "".join(f'<li><a href="#{w["id"]}"><span>{e(w["place"])}</span><span>{e(w["series"])} · {e(w["when"][-4:])}</span></a></li>' for w in WINS)
    def feature(f):
        if not f: return ""
        return (f'<div class="win-feature wrap"><figure class="reveal"><img src="{f["img"]}" alt="" loading="lazy"></figure>'
                f'<div class="win-feature-text reveal"><p class="win-meta">{e(f["kicker"])}</p><h3>{e(f["title"])}</h3><p>{e(f["text"])}</p></div></div>')
    chapters = ""
    for w in WINS:
        cap = f'<p class="win-cap">{e(w["caption"])}</p>' if w["caption"] else ""
        text = "".join(f"<p>{e(t)}</p>" for t in w["p"])
        gallery = "".join(f'<figure class="reveal"><img src="{g}" alt="" loading="lazy"></figure>' for g in w["gallery"])
        chapters += f"""
  <section class="win" id="{w["id"]}" aria-label="{e(w["title"])}">
    <div class="win-hero">
      <img src="{w["hero"]}" alt="" loading="lazy">
      <div class="win-shade" aria-hidden="true"></div>
      <div class="win-hero-copy wrap">
        <div class="reveal"><p class="win-meta">{e(w["series"])} <span aria-hidden="true">—</span> {e(w["when"])}</p><h2>{e(w["title"])}</h2></div>
        <p class="win-stat reveal"><b>{e(w["stat"][0])}</b><span>{e(w["stat"][1])}</span></p>
      </div>
    </div>
    <div class="win-body wrap">
      <div class="win-side reveal"><p class="win-partner">{e(w["partner"])}</p><dl class="win-stat2"><dt>{e(w["stat2"][0])}</dt><dd>{e(w["stat2"][1])}</dd></dl></div>
      <div class="win-text reveal">{text}<a class="win-link" href="/work/{w["slug"]}/">The full story: {e(by_slug[w["slug"]]["name"])} <span aria-hidden="true">→</span></a></div>
    </div>
    <div class="win-gallery wrap">{gallery}</div>
    {f'<div class="wrap">{cap}</div>' if cap else ""}{feature(w.get("feature"))}
  </section>"""
    return (head("Wins · Taylor Powers", "Championships and race wins from the partnerships Taylor Powers built and ran: NASCAR at Watkins Glen, MotoGP at Assen and Silverstone, and LAFC's 2022 MLS Cup.", "/wins/", I + "wins-wg-taylor-champagne.jpg")
            + f"""<body class="page wins">
{nav("", "wins")}
<main>
  <section class="wins-hero">
    <img src="{I}wins-wg-taylor-champagne.jpg" alt="Taylor Powers celebrating with the SuperFile team in victory lane at Watkins Glen">
    <div class="wins-shade" aria-hidden="true"></div>
    <div class="wins-hero-copy wrap">
      <div>
        <h1>Wins<span>.</span></h1>
        <p class="wins-lede">The partnerships Taylor built and ran, on the days they finished first.</p>
      </div>
      <div class="wins-index-wrap">
        <ol class="wins-index">{index}</ol>
        <p class="wins-credit">Taylor, far left, in victory lane at Watkins Glen.</p>
      </div>
    </div>
  </section>{chapters}
</main>
{FOOT}
<script src="/assets/wins.js?v={V}" defer></script>
</body>
</html>
""")

def work_redirect():
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Wins · Taylor Powers</title>
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="robots" content="noindex"><link rel="canonical" href="https://taylorpowers.com/wins/">
<meta http-equiv="refresh" content="0; url=/wins/"></head>
<body><p><a href="/wins/">Wins</a></p></body></html>
"""

# ---------- About ----------
def about():
    a = ABOUT
    by_slug = {p["slug"]: p for p in PROJECTS}
    words = " ".join(f"<span>{e(w)}</span>" for w in a["statement"].split())
    jobs = "".join(
        f'<li class="job"><span class="plus" aria-hidden="true">+</span><div class="job-main"><h3>{e(t)}</h3><p>{e(d)}</p></div>'
        f'<span class="job-co">{e(c)}</span><span class="job-yr">[{e(y)}]</span></li>' for t, c, y, d in a["jobs"])
    # The services as a presentation: cover, contents, one slide per service, closing
    k = len(a["services"])
    n = k + 3
    top = lambda label, i: f'<p class="deck-top"><span>{label}</span><span>{i:02d} / {n:02d}</span></p>'
    def slide(i, kind, label, img, inner):
        return (f'<article class="deck-slide deck-{kind}{" is-on" if i == 1 else ""}" data-i="{i - 1}" aria-roledescription="slide" aria-label="{i} of {n}: {e(label)}">'
                f'<img src="{img}" alt="" loading="{"eager" if i == 1 else "lazy"}"><div class="deck-shade"></div><div class="deck-copy">{top("Taylor Powers" if kind == "cover" else "Services", i)}{inner}</div></article>')
    cover = slide(1, "cover", "Cover", a["img_small"],
        '<div class="deck-cover-main"><p class="deck-kicker">Capabilities</p><h3 class="deck-title">Brand, partnerships<br>and production.</h3></div>'
        f'<div class="deck-foot"><p class="deck-lede">{e(ABOUT_STATEMENT_SHORT)}</p><p class="deck-meta">Chicago / Los Angeles / Las Vegas<br>{len(a["services"])} services · selected work</p></div>')
    contents = slide(2, "contents", "Contents", a["img_services"][0],
        '<h3 class="deck-title">Contents</h3><ol class="deck-toc">'
        + "".join(f'<li><button type="button" data-go="{i + 2}"><span class="num">{i:02d}</span>{e(name)}</button></li>' for i, (name, _) in enumerate(a["services"], 1))
        + '</ol>')
    panels = cover + contents + "".join(
        slide(i + 2, "svc", name, img,
              f'<h3><span class="num">{i:02d}.</span> {e(name)}</h3>'
              f'<div class="deck-foot"><ul class="deck-list">{"".join(f"<li>{e(x)}</li>" for x in items)}</ul>'
              f'<div class="deck-work"><p>Selected work</p><ul>{"".join(f"<li><a href='/work/{w}/'>{e(by_slug[w]['name'])}</a></li>" for w in work)}</ul></div></div>')
        for i, ((name, items), work, img) in enumerate(zip(a["services"], a["service_work"], a["img_services"]), 1))
    panels += slide(n, "close", "Contact", a["img_services"][-1],
        '<div class="deck-cover-main"><p class="deck-kicker">Thank you</p><h3 class="deck-title">Let’s build<br>what’s next.</h3></div>'
        f'<div class="deck-foot"><p class="deck-lede">Brand, marketing and partnership leadership across film, consumer brands and sport.</p>'
        f'<p class="deck-contact"><a href="mailto:{EMAIL}">Email ↗</a><a href="{LINKEDIN}" rel="noopener" target="_blank">LinkedIn ↗</a><a href="/wins/">Wins →</a></p></div>')
    bars = "".join(f'<button type="button" class="deck-seg{" is-on" if i == 0 else ""}" aria-label="Slide {i + 1}"></button>' for i in range(n))
    numbers = "".join(f'<div><dt>{e(n)}</dt><dd>{e(l)}</dd></div>' for n, l in a["numbers"])
    logos = "".join(f'<img class="h{h}" src="/assets/home/logos/{n}.{"svg" if n == "skil" else "png"}" alt="{e(alt)}">' for n, alt, h in LOGOS)
    return (head("About · Taylor Powers", a["statement"], "/about/", "/assets/og.jpg")
            + f"""<body class="page about">
{nav("ink", "about")}
<main>
  <section class="wrap ab-top">
    <p class="statement" aria-label="{e(a["statement"])}">{words}</p>
    <div class="ab-intro">
      <div class="ab-paras">{"".join(f"<p>{e(x)}</p>" for x in a["paras"])}<p>{e(a["summary"])}</p></div>
      <figure class="ab-small"><img src="{a["img_small"]}" alt=""></figure>
      <figure class="ab-big"><img src="{a["img_big"]}" alt="Taylor Powers"></figure>
    </div>
  </section>
  <section class="wrap ab-exp">
    <div class="ab-exp-head"><h2>Brands, studios, and my experience.</h2><p>{e(a["summary"])}</p></div>
    <ul class="jobs">{jobs}</ul>
  </section>
  <section class="wrap ab-numbers">
    <div><h2>In numbers.</h2><p>Highlights from campaigns, partnerships and productions across film, consumer brands and sport.</p></div>
    <dl class="big-figures">{numbers}</dl>
  </section>
  <section class="wrap logos" aria-label="Brands and studios">{logos}</section>
  <div class="dark">
    <section class="deck" aria-roledescription="carousel" aria-label="Services">
      <div class="deck-pin">
        <div class="deck-stage">{panels}</div>
        <div class="deck-bar"><div class="deck-segs">{bars}</div><span class="deck-count" aria-live="polite">01 / {n:02d}</span>
          <div class="deck-arrows"><button type="button" class="arrow deck-prev" aria-label="Previous slide"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M13.5 8L9.5 12L13.5 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button><button type="button" class="arrow deck-next" aria-label="Next slide"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M10.5 8L14.5 12L10.5 16" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div></div>
      </div>
    </section>
  </div>
</main>
{FOOT}
<script src="/assets/about.js?v={V}" defer></script>
</body>
</html>
""")

# ---------- Case study ----------
def page(p):
    light = p.get("hero_light")
    hero = (f'<video class="hero-media" autoplay muted loop playsinline poster="{p["hero_img"]}" aria-hidden="true"><source src="{p["hero_clip"]}" type="video/mp4"></video>'
            if p.get("hero_clip") else f'<img class="hero-media" src="{p["hero_img"]}" alt="{e(p["client"])}">')
    if p.get("hero_vimeo"):
        hero += (f'<iframe class="case-hero-vimeo" data-hd src="https://player.vimeo.com/video/{p["hero_vimeo"]}?background=1&autoplay=1&loop=1&muted=1&dnt=1" '
                 f'allow="autoplay; fullscreen; picture-in-picture" title="{e(p["client"])}" aria-hidden="true" tabindex="-1"></iframe>')
    body = "".join(f"<p>{e(t)}</p>" for t in p["body"])
    media = ""
    def film_btn(f, poster):
        return (f'<button type="button" class="full film" {film_attrs(f)} data-title="{e(f["title"])}">'
                f'<img src="{f.get("poster", poster)}" alt="" loading="lazy"><span class="play"><span class="play-dot" aria-hidden="true"></span>{e(f.get("label", "Watch the film"))}</span></button>')
    if p.get("film"):
        media += film_btn(p["film"], p["card"].rsplit(".", 1)[0] + "@2x.jpg" if p["card"].startswith(W) else p["hero_img"])
    photos = [g for g in p["gallery"] if g != p["hero_img"]]
    if len(photos) == 1:
        g = photos[0]
        media += f'<figure class="full{" light" if "art-car" in g else ""}"><img src="{g}" alt="" loading="lazy"></figure>'
    elif photos:
        media += '<div class="pair">' + "".join(f'<figure class="{"light" if "art-car" in g else ""}"><img src="{g}" alt="" loading="lazy"></figure>' for g in photos) + "</div>"
    media = f'<section class="media wrap">{media}</section>' if media else ""
    # Story sections: a serif heading beside the text, then the section's own photos (one full width, two or more in pairs)
    def pics(imgs):
        if not imgs: return ""
        if len(imgs) == 1:
            g = imgs[0]
            return f'<section class="media wrap"><figure class="full{" light" if "art-car" in g else ""}"><img src="{g}" alt="" loading="lazy"></figure></section>'
        return '<section class="media wrap"><div class="pair">' + "".join(f'<figure class="{"light" if "art-car" in g else ""}"><img src="{g}" alt="" loading="lazy"></figure>' for g in imgs) + "</div></section>"
    sections = "".join(
        f'<section class="row wrap"><h2>{e(sec["h"])}</h2><div class="row-text">{"".join(f"<p>{e(t)}</p>" for t in sec["p"])}</div></section>' + pics(sec.get("img", []))
        + (f'<section class="media wrap">{film_btn(sec["film"], p["hero_img"])}</section>' if sec.get("film") else "")
        for sec in p.get("sections", []))
    results = ""
    if p["figures"] or p.get("link"):
        figs = "".join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in p["figures"])
        link = f'<a class="text-link" href="{e(p["link"][1])}" target="_blank" rel="noopener">{e(p["link"][0])} ↗</a>' if p.get("link") else ""
        results = (f'<section class="row wrap"><h2>{"Results." if p["figures"] else "Coverage."}</h2><div class="row-text">'
                   f'{f"<dl class=figures>{figs}</dl>" if figs else ""}{link}</div></section>')
    return (head(f'{p["name"]} · Taylor Powers', p["lead"], f'/work/{p["slug"]}/', p["hero_img"])
            + f"""<body class="case">
{nav("on-light" if light else "", "work")}
<main>
  <section class="hero{" light-hero" if light else ""}">
    <div class="hero-frame">{hero}</div>
    <div class="hero-shade" aria-hidden="true"></div>
    <a class="all-works" href="/">← Home</a>
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
    <div class="row-text">{"".join(f"<p>{e(t)}</p>" for t in p.get("role_text", []))}<p>{e(p["role"])}.</p><p>{e(" · ".join(p["disciplines"]))}</p></div>
  </section>
  {media}
  {sections}
  {results}
  <div class="case-end"></div>
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
    write("wins/index.html", wins())
    write("work/index.html", work_redirect())
    write("about/index.html", about())
    for p in PROJECTS:
        write(f"work/{p['slug']}/index.html", page(p))
