"""Build Team-20-text.pdf: the report without figures, tables, references and technology statement.

Run from the Report folder:   python make_text_pdf.py
Everything between <!-- FIGURE:start --> ... <!-- FIGURE:end --> and
<!-- TABLE:start --> ... <!-- TABLE:end --> is removed, the report is cut at "# References",
and the table of contents / list of figures are switched off. The result is rendered with Quarto.
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

# 2. Drop references and technology statement (everything from "# References" on)
text = text[: text.index("\n# References")]

# 3. No table of contents / list of figures, and no automatic bibliography
text = text.replace("    toc: true\n", "    toc: false\n").replace("    lof: true\n", "    lof: false\n")
text = text.replace("bibliography: references.bib\n", "bibliography: references.bib\nsuppress-bibliography: true\n")

leftover = [m for m in ("FIGURE:", "TABLE:") if m in text]
if leftover:
    raise SystemExit(f"Unbalanced markers left in the text: {leftover}. Check the start/end pairs.")

OUT.write_text(re.sub(r"\n{3,}", "\n\n", text), encoding="utf-8")
print(f"Removed {n_fig} figures and {n_tab} tables -> {OUT}")

subprocess.run(["quarto", "render", str(OUT), "--to", "pdf"], check=True)
OUT.unlink()   # keep only the PDF
print("Done: Team-20-text.pdf")
