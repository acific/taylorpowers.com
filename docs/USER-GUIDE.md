# User guide

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

For Taylor and Shane: what the site does and how to change it.

## What visitors see

**Home (taylorpowers.com)**

On a computer, two columns; on a phone, one.

1. Left: Taylor's photo, name and bio, **Let's connect** (LinkedIn), a moving strip of client logos, **Services** (five areas), **Experience** (five roles) and **Reach out** (email).
2. Right: thirteen project cards in two columns. On a computer the titles appear when you hover; FLEX × LAFC, SKIL and EGO also play a short clip. On a phone the titles are always shown and those clips play as the card reaches the middle of the screen. Seven cards open the project's own page; the others open press coverage or the film in a new tab.

**Project pages (work/…)**

Each project page has:

- the same light look as the home page, with a link back to all work
- a big rounded header image or film (HD where there is one)
- client, year, role and disciplines
- the story and results
- **Watch the film** and/or a link to press coverage
- **Next project** at the bottom

## Email

Mail to **taylor@taylorpowers.com** arrives in Taylor's Gmail (taylorrpowers5@gmail.com). It can receive but not send as taylor@. To send as taylor@, add a mailbox (Google Workspace, iCloud+ custom domain and so on).

When testing, send from a different account. Gmail hides a message that forwards back to the address that sent it.

## Changing things

Ask Claude in the `~/Strange/taylorpowers.com` folder, or edit by hand:

| To change | Edit |
|---|---|
| Home text, services, experience, project cards | `index.html` (images in `assets/home/`) |
| A project page | `PROJECTS` in `scripts/build_work.py`, then run `python3 scripts/build_work.py` |
| Colors and type | `assets/home.css` (home) and `assets/case.css` (project pages) |
| The showreel | Replace `assets/video/reel.mp4` (re-save with "fast start" so it streams) and `assets/video/reel-poster.jpg` |
| The portrait | Replace `assets/img/taylor-portrait.jpg` |
| Add HD footage to a project | Add `hero_vimeo="<Vimeo ID>"` to it in `PROJECTS` and rebuild |

Then deploy as in [OPERATIONS.md](OPERATIONS.md#deploying).

## FAQ

**I don't see my change.** Hard refresh (Cmd+Shift+R). If it's still old, the `?v=` stamp wasn't bumped (see OPERATIONS).

**A project's HD header doesn't play.** The Vimeo video's privacy must allow embedding on taylorpowers.com. The short clip or photo shows until it does.

**Can the phone number go on the site?** Yes, but it was left off on purpose because the page is public.
