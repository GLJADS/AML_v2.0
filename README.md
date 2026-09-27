# Report folder

`Team-XX.qmd` is the report skeleton, structured around the 9 sections required by the
2026 brief (not the same as the 8 task numbers, see the comment block at the top of the file).

Expected structure once you start filling it in:

```
Report/
  Team-XX.qmd
  images/     <- figures saved from the notebook (class_balance.png, top50_words.png, ...)
  tables/     <- csv tables saved from the notebook (top100_mutual_information.csv, ...)
```

The notebook (`Assignment1_CDs_Vinyl.ipynb`) already saves into `Report/images/` and
`Report/tables/` — create those two folders before running it, or adjust the paths.

## Producing the two required PDFs

The assignment requires **two** PDFs:
1. `Team-XX.pdf` — the full report, figures and tables included.
2. `Team-XX-text.pdf` — the same report with figures, tables, references and the
   Technology Statement removed, used only to check the 6-page limit on the actual text.

Every figure/table block in `Team-XX.qmd` is wrapped in HTML comments:

```
<!-- FIGURE:start -->
...
<!-- FIGURE:end -->
```

or `<!-- TABLE:start --> ... <!-- TABLE:end -->`.

Two ways to produce the text-only version:

**Option A — quick and manual (fine for a student assignment):**
Duplicate `Team-XX.qmd` as `Team-XX-text.qmd`, delete every block between a
`FIGURE:start`/`TABLE:start` marker and its matching `:end` marker, delete the
References and Technology Statement sections, then render:
```
quarto render Team-XX-text.qmd --to pdf
```

**Option B — scripted:** write a small Python script that reads `Team-XX.qmd`, strips
everything between matching `FIGURE:start/end` and `TABLE:start/end` markers plus the
`# References` and `# Technology Statement` sections, writes `Team-XX-text.qmd`, then
shells out to `quarto render`. Worth it only if you expect to regenerate this often.

Render the full version the normal way:
```
quarto render Team-XX.qmd --to pdf
```

If you don't have Quarto set up (the 2025 project's `pyproject.toml` / `uv sync` handles
this), Pandoc with a `.md` file works too — rename `.qmd` to `.md` and strip the YAML
`format:` block, or just write directly in Word/Google Docs from this skeleton's headings
and TODOs if that's simpler for your team.

