"""Build Team-20-text.pdf: the report without tables and figures.

Run from the A2/Report folder:   python make_text_pdf.py

Unlike Assignment 1, the Assignment 2 brief only says tables and figures are excluded from
the 7-page limit -- it does NOT mention excluding references (or a technology statement,
there isn't one required here). So this script, unlike A1's version, does NOT cut the
References section. Confirm this reading with the course before relying on it; if references
turn out to be excluded too, add back a cut at "# References" like A1's script does.

Everything between <!-- FIGURE:start --> ... <!-- FIGURE:end --> and
<!-- TABLE:start --> ... <!-- TABLE:end --> is removed, table of contents / list of figures
are switched off, and the result is rendered with Quarto.
"""
import re
import subprocess
from pathlib import Path

SRC = Path("Team-20.qmd")
OUT = Path("Team-20-text.qmd")

text = SRC.read_text(encoding="utf-8")

# 1. Remove marked figure and table blocks
text, n_fig = re.subn(r"<!-- FIGURE:start -->.*?<!-- FIGURE:end -->", "", text, flags=re.S)
text, n_tab = re.subn(r"<!-- TABLE:start -->.*?<!-- TABLE:end -->", "", text, flags=re.S)

# Cross-references to removed figures/tables would print as "?@fig-...": replace with a plain word
text = re.sub(r"@fig-[\w-]+", "Figure", text)
text = re.sub(r"@tbl-[\w-]+", "Table", text)

# 2. No table of contents / list of figures (references stay, see module docstring)
text = text.replace("    toc: true\n", "    toc: false\n").replace("    lof: true\n", "    lof: false\n")

leftover = [m for m in ("FIGURE:", "TABLE:") if m in text]
if leftover:
    raise SystemExit(f"Unbalanced markers left in the text: {leftover}. Check the start/end pairs.")

OUT.write_text(re.sub(r"\n{3,}", "\n\n", text), encoding="utf-8")
print(f"Removed {n_fig} figures and {n_tab} tables -> {OUT}")

subprocess.run(["quarto", "render", str(OUT), "--to", "pdf"], check=True)
OUT.unlink()   # keep only the PDF
print("Done: Team-20-text.pdf")
