# Status: where we left off

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

## State as of 2026-11-20

**Live and working:**

- https://taylorpowers.com: the home page now follows the owner's Framer design (v18 stamp, 2026-11-20; project cards in two columns, titles on hover, clips on three cards; case pages restyled to match; v19 adds the motion, logo-strip, type, share-card and icon refinements; v20 adds the 404 page, search profile and brand-launch card; v21 redesigns the case pages in an editorial layout; v22 matches them closely to the reference template). The eight case pages (with HD Vimeo heroes on FLEX × LAFC and the SuperFile launch) are still served under `work/`; seven home-page cards open them.
- The home page's contact link is taylorraepowers@icloud.com, as in the Framer design, not taylor@taylorpowers.com.
- taylor@taylorpowers.com forwards to Taylor's Gmail. DNS has fully propagated, including Google's resolvers.
- DNS is on Cloudflare, and HTTPS is on through GitHub Pages.

**The last thing the owner asked for** was "document everything and where we left off" (this doc set). Just before that, they approved the premium upgrades (case pages, logo wall, intro, share card) and said "do it" to swapping in better footage. Everything possible without new files was done.

## Waiting on the owner

| Item | Why it matters | What to do with it |
|---|---|---|
| **Vimeo links for EGO, SKIL, MotoGP, UFC/WWE and Daytona films** (the owner's Vimeo account, Shane Valdez / Realm Films) | Those five pages still use reel clips or press photos; HD footage is the biggest remaining upgrade | Add `hero_vimeo` (and `film`) to each in `PROJECTS`, rebuild, push |
| **A larger portrait** (over 800 px; from the photographer or Taylor's phone) | The current one is the largest online and is soft on big screens | Replace `assets/img/taylor-portrait.jpg` |
| **Rights for the shot about 10 s into the reel** (looks like *Dazed and Confused*) | It may be film footage the owner doesn't own | Re-cut the reel if needed |
| **Confirm "Visual Effects Producer"** | The resume says Coordinator; the owner asked for Producer (and said she held it at SuperFile and Realm) | Already on the site as the owner asked |

## Open improvements (not started)

- **Security hygiene:** add DMARC (`_dmarc` TXT `v=DMARC1; p=quarantine`), CAA (letsencrypt.org, for GitHub's certificates) and DNSSEC on the Cloudflare zone. The CSP and referrer policy are `<meta>` tags (2026-10-22); HSTS, `X-Frame-Options` and `nosniff` need response headers, which GitHub Pages can't set: proxy the site through Cloudflare with a response-header rule, or move it to Cloudflare Pages or Workers. See [../SECURITY.md](../SECURITY.md).
- Remove the unused `_domainconnect` CNAME imported from GoDaddy.
- A sending mailbox for taylor@ if Taylor wants to reply from that address.
- Optional: replace the press stills with the owner's own photography.

## Accounts and access

- **GitHub:** the repo is acific/taylorpowers.com (moved from ShaneRealm on 2026-11-20). Push as acific (OPERATIONS).
- **Cloudflare:** the shared account (acificlabs@gmail.com).
- **GoDaddy:** the owner's account (registrar only).
