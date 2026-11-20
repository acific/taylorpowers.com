# User guide

> Last verified against the code: 2026-11-20 (commit 68010d3 + the Framer home page)

For Taylor and Shane: what the site does and how to change it.

## What visitors see

**Home (taylorpowers.com)**

A carousel of all fourteen projects. Arrows (or swiping, or the arrow keys) bring the next one to the middle; clicking the middle one opens its case study. The menu at the bottom goes to About and Work.

**About** and **Work**: the bio, experience, services and numbers; and all fourteen projects in a grid.

**Project pages (work/…)**

Each project page has:

- a full-screen header image or film (HD where there is one) with the title, a one-line summary and client, year and type
- a black band with the story, then Taylor's role
- client, year, role and disciplines
- the story and results
- **Watch the film** and/or a link to press coverage
- **More to explore** (two other projects) and a contact footer at the bottom

More photos and story make these pages richer: send them per project and they go into `PROJECTS` (`gallery` and `body`).

## Email

Mail to **taylor@taylorpowers.com** arrives in Taylor's Gmail (taylorrpowers5@gmail.com). It can receive but not send as taylor@. To send as taylor@, add a mailbox (Google Workspace, iCloud+ custom domain and so on).

When testing, send from a different account. Gmail hides a message that forwards back to the address that sent it.

## Changing things

Ask Claude in the `~/Strange/taylorpowers.com` folder, or edit by hand:

| To change | Edit |
|---|---|
| Any project, the About text, services, experience | `scripts/build_work.py` (`PROJECTS`, `ABOUT`), then run `python3 scripts/build_work.py`; images in `assets/home/` |
| A project page | `PROJECTS` in `scripts/build_work.py`, then run `python3 scripts/build_work.py` |
| Colors and type | `assets/main.css` |
| The showreel | Replace `assets/video/reel.mp4` (re-save with "fast start" so it streams) and `assets/video/reel-poster.jpg` |
| The portrait | Replace `assets/img/taylor-portrait.jpg` |
| Add HD footage to a project | Add `hero_vimeo="<Vimeo ID>"` to it in `PROJECTS` and rebuild |

Then deploy as in [OPERATIONS.md](OPERATIONS.md#deploying).

## FAQ

**I don't see my change.** Hard refresh (Cmd+Shift+R). If it's still old, the `?v=` stamp wasn't bumped (see OPERATIONS).

**A project's HD header doesn't play.** The Vimeo video's privacy must allow embedding on taylorpowers.com. The short clip or photo shows until it does.

**Can the phone number go on the site?** Yes, but it was left off on purpose because the page is public.
