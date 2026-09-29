# AML Assignment 1 - CDs & Vinyl

Task Division for both coding and report! 

1-3: Kira; 01.10.2026 (Thursday)
4 & 5: Habir; 05.10.2026 (Monday)
6: Ewa; 08.10.2026 (Thursday)
7: Gilbet. 12.10.2026 (Monday0

Team 20, Advanced Machine Learning 2026. Deadline is **Sunday October 25, 20:00**, submitted through Canvas.

We're basically redoing what a previous group did last year (Movies & TV instead of CDs & Vinyl), so a lot of the pipeline is already sketched out. Don't just copy their numbers though, our dataset is different so every result needs to be regenerated.

## What's in here

```
Assignment1_CDs_Vinyl.ipynb   -> the main notebook, all 8 tasks, run top to bottom
cds_vinyl_50k.csv             -> the dataset (50k reviews)
Report/
  Team-XX.qmd                 -> the report itself
  images/                     -> figures the notebook saves, gets pulled into the report
  tables/                     -> csv tables the notebook saves, same deal
  README.md                   -> how to get two PDFs out of one qmd file
```

## Getting set up

Same as last time, `uv sync` in the project folder, then restart your IDE completely if it doesn't pick up the venv right away (VSCode is annoying about this).

## How the notebook is organized

It follows the assignment tasks 1 through 8 in order. Every spot where you actually need to write something is marked with `# TODO` in code cells or a markdown cell that says TODO. Some cells already run and produce output, that's just scaffolding so you're not starting from a blank cell, don't assume the numbers in there are final or correct until you've actually run it yourself.

A few things worth flagging before you start:

- **Task 2 has a new question this year**: "should all reviews be included in the analysis." Last year's version of this assignment didn't ask that. There's a cell that checks for empty/punctuation-only/very short reviews, but you still need to decide and write down what you did with them.
- **Naive Bayes on embeddings**: multinomial NB doesn't work on Word2Vec vectors because they go negative. We're using GaussianNB instead, just make sure that ends up explained in the report, not just in a code comment.
- **Don't mix up the CV score and your final score.** GridSearchCV's `best_score_` is what it used internally to pick hyperparameters. The number you report as "our model's performance" comes from evaluating on the held-out test set afterward, once. This trips people up every year apparently, there's now a whole warning about it in the assignment PDF.
- **FuzzyTM will eat your RAM if you don't prune the vocabulary first.** The notebook does this, but whatever threshold you land on, write it down, they specifically ask for it.
- **BERTopic downloads a model the first time you run it.** If you're on a flaky connection or a locked-down laptop, you can hand it your own embeddings instead so it skips the download, there's a note about this in the notebook.

## The report

`Report/Team-XX.qmd` has the 9 sections the assignment wants, which is not the same as the 8 tasks (task 2 splits into "preprocessing" and "analysis", task 6 splits into "training procedure" and "evaluation"). Fill in the TODOs, and whenever you add a figure or table, wrap it in

```
<!-- FIGURE:start -->
...
<!-- FIGURE:end -->
```

or `<!-- TABLE:start -->` / `<!-- TABLE:end -->`. Reason for that: we need to submit two PDFs, `Team-XX.pdf` (the real report) and `Team-XX-text.pdf` (same thing but with figures, tables, references and the technology statement stripped out, used to check we're under 6 pages of actual text). Having everything marked makes it a five minute job instead of a rewrite. Check `Report/README.md` for the actual render steps.

## Submission checklist

Don't wait until the night before for this, the zip has more parts than you'd think:

- [ ] Team-XX.pdf (full report)
- [ ] Team-XX-text.pdf (text only, for the page count check)
- [ ] Code, zipped as Team-XX-code.zip if it's more than one file, keep it readable, don't dump dead experiments in there
- [ ] Team-XX.pickle, our best Logistic Regression model as one fitted sklearn Pipeline (vectorizer + model together, not separate files)
- [ ] All of the above zipped into a single Team-XX-A1.zip, that's the file that actually goes on Canvas

If you only did part of a task but didn't write it up in the report, we don't get the points for it, so don't leave findings sitting in a notebook cell and assume that counts.

Questions go through Canvas or Thursday morning sessions, not to each other in a WhatsApp void at 1am the day before the deadline please.
