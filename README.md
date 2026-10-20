# Qingdao Lumber English Site — GitHub Rebuild

Static rebuild of **en.qdlumber.com** (previously Strikingly) for GitHub Pages.
9 pages: Home, Solutions, Capabilities, About Us, Case Study (+RFQ form), and 4 industry pages.

## Structure

| Path | Page |
|---|---|
| `/` | Home |
| `/solutions/` | Solutions (incl. FAQ accordion + FAQPage JSON-LD) |
| `/capabilities/` | Capabilities (incl. 8-photo factory gallery) |
| `/about/` | About Us |
| `/case-studies/` | Case Study + RFQ form (`#rfq`) |
| `/industries/data-servers-precision-electronics/` | Data Server & Precision Electronics |
| `/industries/ev-battery-charging/` | EV Battery & Charging Station · UN38.3 |
| `/industries/industrial-machinery-infrastructure/` | Industrial Machinery & Infrastructure |
| `/industries/high-voltage-insulators-power-transmission/` | High Voltage Insulator & Power Transmission |

Also: `sitemap.xml`, `robots.txt`, `assets/css/style.css`, `assets/js/main.js`,
`assets/img/*.webp` (12 images), `gen_site.py` (generator — edit content there, re-run).

## Build

```bash
cd ~/workspace/qdlumber-en-rebuild
python3 gen_site.py
python3 -m http.server 8000   # local preview at http://localhost:8000/
```

All internal links are relative, so the site works under any subpath
(`hilaoboy-cloud.github.io/qdlumber-en/`) and later at the domain root.

## Deliberate changes vs the Strikingly site

- **Removed everywhere:** `wirebound` / `military` / `HHG` references (business exited).
  - Home product list: only Custom Wooden Crates, Knock-Down Crate Kits, Server Crates, Export Packaging Systems.
  - Case Study "High-voltage utility equipment": engineering focus rewritten without wirebound.
  - Case Study "High-volume relocation & HHG logistics" → "High-volume relocation logistics".
  - Industry page `industries-power-electrical`: title and body rewritten from "Wire Bound Crates" to reinforced wooden crate systems.
- **Case Study**: the two same-named "Welcome Section" blocks renamed to "Proven Across Industries" / "Engineering Standards".
- **Deleted template junk:** fake team names/testimonials, $99/mo pricing section, $4500 store products (+BUY NOW), `/portfolio/*` store pages (not rebuilt).
- **Fixed:** `lat-pack` → `flat-pack`; About Us keeps "20+ years".
- **Clean URLs:** `/solutions/`, `/capabilities/`, `/about/`, `/case-studies/` (no `/2`, `/3`).
- **All 12 images have descriptive alt text** (written fresh from visual inspection; the 20 alts rewritten in the 2026-10-16 Strikingly audit were saved only in the Strikingly backend and were not recoverable — fresh alts follow the same descriptive style).
- **Solutions FAQ answers** were reconstructed from site copy (the accordion answers were not extractable from the live page).
- **No back-to-top button** (deliberately hidden on the Strikingly site at user request; not carried over).
- Excluded image `wirebound-crate-line.webp` (wirebound line photo) — wirebound business exited.

## Still pending (needs parent/user)

1. **formsubmit activation** — the RFQ form posts to `https://formsubmit.co/ajax/Evan.chen@qdlumberco.com`; formsubmit sends a one-time activation email to that mailbox which the owner must confirm before submissions are delivered. Until then the form falls back to `mailto:`. **Do not claim the form is live.**
2. **About Us (7) and Case Study (3) images** — exist on the Strikingly site but were not extractable via page-text fetch; those pages are currently text-led. Pull the full image inventory from the Strikingly backend and slot them in.
3. **Home hero/section images** — only the logo was extractable; home is currently text-led with strong typography.
4. **UN C420506 dangerous-goods cert** — not found on the English pages (it lives on the Chinese site); not included here. Add if desired.
5. **GA4 / Search Console** — add the `G-` measurement ID to all pages and verify in Search Console after launch.
6. **DNS switch** — only after the user approves the github.io preview. Strikingly stays live until then.
