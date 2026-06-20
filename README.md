<div align="center">

  # Shellback Mono

  **A water-cooled monospace for security notes, terminals and Obsidian vaults. Every glyph is generated from a parametric Python engine: clean geometric letterforms, a slashed zero, unambiguous 0O / Il1 / 5S / 8B, and seven coding ligatures.**

  [![License: OFL-1.1](https://img.shields.io/badge/License-OFL--1.1-cba6f7.svg)](OFL.txt)
  [![Version](https://img.shields.io/badge/version-1.0.0-89b4fa)](https://github.com/Real-Fruit-Snacks/shellback-mono/releases)
  
  [Live Specimen](https://real-fruit-snacks.github.io/shellback-mono/) • [Report Issue](https://github.com/Real-Fruit-Snacks/shellback-mono/issues)

</div>

---

## Overview


## Highlights

| | |
|---|---|
| **Styles** | Regular · Medium · Bold + matching italics (6 total) |
| **Glyphs** | A–Z, a–z, 0–9, full ASCII, Latin-1 accents (à é ñ ü ç …), smart quotes, dashes, math (`× ÷ ± ≠ ≤ ≥`), arrows, symbols (`© ® ™ € £ µ § ¶ ✓`) |
| **Terminal** | Box-drawing (light/heavy/double/rounded), block elements, shades, Powerline separators — full-cell, seamless tiling |
| **Ligatures** | `-> <- => != == === !== <= >= := ::` via standard `calt` + `liga`; `ss01` for a dotted zero |
| **Metrics** | True monospace — every glyph exactly one cell (600/1000 UPM) |
| **Formats** | TTF (desktop) · WOFF2 (web, ~5 KB per style) |
| **License** | [SIL Open Font License 1.1](OFL.txt) — free to use, modify and embed |

Every release is built from source by CI and ships with **signed build provenance**
— see [Verify the download](#verify-the-download). Full history in [CHANGELOG.md](CHANGELOG.md).

## Download

Grab the [**latest release**](https://github.com/Real-Fruit-Snacks/shellback-mono/releases/latest):

| Asset | Contents |
|---|---|
| `ShellbackMono-TTF.zip` | Desktop fonts for Windows / macOS / Linux |
| `ShellbackMono-WOFF2.zip` | Web fonts + ready-made `shellback.css` |
| `ShellbackMono-Obsidian.zip` | Single-file CSS snippet for Obsidian (fonts embedded) |
| `SHA256SUMS.txt` | Checksums for everything — verify before you trust |

### Verify the download

Every release is built by GitHub Actions and carries signed build provenance.
Confirm a file came from this repo's pipeline (not a hand-upload):

```bash
gh attestation verify ShellbackMono-TTF.zip --repo Real-Fruit-Snacks/shellback-mono
sha256sum -c SHA256SUMS.txt        # or: shasum -a 256 -c
```

## Install

**Windows** — right-click each TTF → **Install**, or run the scripted per-user install:

```powershell
py tools/install_windows.py
```

**macOS** — open each TTF in Font Book → **Install Font**.

**Linux**

```bash
mkdir -p ~/.local/share/fonts/ShellbackMono
cp *.ttf ~/.local/share/fonts/ShellbackMono/
fc-cache -f
```

## Obsidian

1. Drop [`shellback-mono.css`](obsidian/shellback-mono.css) — one file, all six
   font styles are embedded in it — into `<vault>/.obsidian/snippets/`.
2. **Settings → Appearance → CSS snippets** → enable **shellback-mono**.

The snippet themes **all of Obsidian** — interface, note text, and code (with
ligatures) — in any vault, on any machine, no font install required. Each
numbered section in the file can be commented out independently, e.g. keep
your UI font but write notes in Shellback. Prefer the built-in way? Install
the TTFs and pick the font under **Settings → Appearance → Font** (restart
Obsidian after installing so it appears in the list).

> Why embedded? Obsidian resolves `url()` in snippet CSS against the app, not
> the snippets folder, so a snippet can't reference font files sitting next to
> it. Base64-embedding sidesteps that.

## Web

The [`docs/`](docs/) folder is the published specimen site. Reuse the stylesheet
anywhere:

```html
<link rel="stylesheet" href="shellback.css">
<style> code, pre { font-family: "Shellback Mono", monospace; } </style>
```

### Published notes sites (Quartz, MkDocs, Hugo…)

Hosting your vault as a static site? Copy `dist/webfonts/*.woff2` and
`docs/shellback.css` into the site's static assets and point code at the font:

```css
/* Quartz: custom.scss · MkDocs Material: docs/stylesheets/extra.css · etc. */
@import url("/shellback.css");          /* or copy the @font-face rules in */
:root { --font-monospace: "Shellback Mono", ui-monospace, monospace; }
code, pre, kbd, .cm-editor { font-family: "Shellback Mono", ui-monospace, monospace;
  font-feature-settings: "calt" 1, "liga" 1; }   /* keep coding ligatures on */
```

That keeps your published notes visually identical to your local vault.

## Build from source

The font is generated, not hand-drawn — every glyph is Python.

```
tools/
  glyphlab.py    parametric geometry engine (strokes, corners, box-rings)
  glyphs.py      core glyph definitions + base ligatures
  glyphs_more.py accented letters, symbols, extra ligatures, dotted zero
  box_glyphs.py  box-drawing, block elements, shades, Powerline
  build.py       compiles 6 styles to TTF + WOFF2 (fontTools): gasp/prep/STAT
  validate.py    monospace / naming / metrics / GSUB checks
  package.py     release archives + SHA256SUMS    make_obsidian_snippet.py
  proof.py · proof_ext.py · chart.py · zoom.py · closeup.py   QA renders
  og_image.py    specimen social card + favicon
  check_gsub.py  dumps ligature rules    check_strings.py  scans name tables
  install_windows.py  per-user Windows install
```

```bash
pip install -r requirements.txt
py tools/build.py        # -> dist/ttf + dist/webfonts (6 styles)
py tools/validate.py     # -> ALL PASS
fontbakery check-universal --error-code-on FAIL dist/ttf/*.ttf   # 0 FAIL
```

Want a heavier weight, wider cut or rounder corners? The whole family falls out
of three numbers per style — `w` (stroke weight), `cut` (corner radius), `segs`
(corner smoothing) — in `build.py`. Change them and rebuild.

## Design notes

- **Slashed zero, footed one, tailed ell, serifed cap-I** — hashes, IPs and
  base64 stay unambiguous at 2 a.m.
- **Large x-height, open counters** — holds up at 12 px in a packed terminal.
- The italics are obliques cut at 8° from the same skeletons, so weights and
  spacing match the uprights exactly.
- The `preview/` folder documents the design exploration — three candidate
  directions were rendered from the same skeletons before this one was chosen.

## License

[SIL Open Font License 1.1](OFL.txt). Use it, ship it, modify it — just don't
sell the font files by themselves, and use a different name for forks
("Shellback Mono" is reserved).

---

Designed & built 2026 by **Real-Fruit-Snacks**. Fork it, re-cut it, sail on.
