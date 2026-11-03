# AML Assignment 2 - Parkinson's Disease Classification

Team 20, Advanced Machine Learning 2026. Deadline is **Sunday December 6, 20:00**, submitted through Canvas.

Same deal as last time: a previous group did basically this assignment last year with Alzheimer's instead of Parkinson's, same SVM/MLP/FIS setup, same thresholding idea. The pipeline shape is familiar, the numbers aren't, don't copy those.

## Task split and dates

- **Gilbert** - 1) Problem framing & EDA, 2) Preprocessing & feature engineering, now through Friday Nov 6
- **Habir** - 3) Models, 4) Validation & HPO, Nov 7-11
- **Kira** - 5) Model selection & thresholding, Nov 12-15
- **Ewa** - 6) Decision support & practical value, from Nov 16

**Nobody's on 7) Reflection right now.** Flag this in standup, someone needs to own it, and ideally also own stitching the final qmd together and running the render before the 6th. There's slack between Ewa's start date and the deadline, don't let that turn into "whoever's free at the end."

## What's in here

```
Assignment2_Parkinsons.ipynb     -> the main notebook, all 7 tasks, run top to bottom
parkinsons_disease_data.csv      -> the dataset
Parkinsons_Dataset_Attribute_Description.txt
Report/
  Team-20.qmd                    -> the report itself
  make_text_pdf.py               -> generates Team-20-text.pdf from the qmd
  images/, tables/               -> what the notebook saves, pulled into the report
  references.bib                 -> shared with A1, add your new citations here
```

## The one thing that matters more than last time: the test set

This assignment is built around not touching the test set until the very end. The notebook splits it off in the second cell, before any EDA, before any preprocessing is fit, before any tuning. Every task from 1 through 4 only ever sees `X_trainval` / `y_trainval`. If you're adding your own exploration and you catch yourself typing `X_test` anywhere before Task 5's final evaluation cell, stop, that's the mistake the whole assignment is designed to catch.

A few other things worth knowing before you start on your section:

- **Hyperparameter search is capped.** Linear + RBF SVM combined can't exceed 20 configurations total, MLP gets its own 20. Plan the grid before you run it, don't run something big and then explain away why it's technically fine.
- **Threshold rule is fixed for everyone**: maximize F2 on validation, freeze it, evaluate on test after. The number differs per model, the rule doesn't. Don't touch a threshold once you've seen test results, that defeats the entire point of reserving a test set in the first place.
- **FIS needs its own preprocessing, separate from the SVM/MLP pipeline.** Any scaling or ranges used for its membership functions come from training data only, same leakage rule, just done manually since it's not going through sklearn's Pipeline.
- **The FIS grading isn't about being clinically right.** It's about traceability, can you point at the attribute description or a paper and show how that became an input, a membership function, a rule. Keep that paper trail as you build it, it's much easier than reconstructing it afterward.

## The report

Same marker convention as Assignment 1: wrap anything that's a figure or table in

```
<!-- FIGURE:start -->
...
<!-- FIGURE:end -->
```

or `<!-- TABLE:start -->` / `<!-- TABLE:end -->`. `Report/make_text_pdf.py` strips those automatically to build `Team-20-text.pdf`.

One actual difference from Assignment 1 worth noting: the A1 brief excluded figures, tables, references *and* the technology statement from the page count. This year's brief only mentions tables and figures. So `make_text_pdf.py` here does **not** cut the References section the way the A1 version did. If that's wrong, easy fix, but worth confirming with the course rather than assuming it carries over.

## Submission checklist

- [ ] Team-20.pdf (full report)
- [ ] Team-20-text.pdf (text only, 7-page check)
- [ ] Code, zipped as Team-20-code.zip if more than one file
- [ ] All zipped into Team-20-A2.zip for Canvas

No pickle file this time, that was an A1-specific deliverable. Don't carry that habit over and waste time building one nobody asked for.

Questions go through Canvas or Thursday mornings.
