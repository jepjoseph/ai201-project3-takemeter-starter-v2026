# TakeMeter
> **### 👋 Start here**

>

> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the

> notebook, the baseline, and what to do when something breaks.

>

> Once `python test.py` passes:

>

> ```bash

> head -5 data/practice_labels.csv     # the shape your labels.csv needs

> ```

>

> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with

> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this

> project. Run section 1, which reports the hardware you'll be training on.

> Everything else waits until you have data.

>

> Nothing to upload, nothing to connect, no accounts and no keys. The notebook

> runs on your machine and writes next to your code.

>

> ****The rest of this file is your submission.**** Fill it in as you go.

---
<!-- ─────────────────────────────────────────────────────────────────────────

     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown

     table, ready to copy. A screenshot of a matrix earns nothing. Paste the

     table.

     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

TakeMeter is a text-classification project using public programming questions collected from Stack Overflow through the Stack Exchange API. The classifier is designed to categorize questions by the richness of relevant supporting context provided in their titles and bodies.

The initial community exploration examines 30 questions and identifies four candidate distinctions: problem specificity, technical evidence, troubleshooting history, and environment or constraints. The proposed classification categories are `low_context`, `some_context`, and `detailed_context`. Model training and evaluation will be documented after the labeled dataset is completed.

---
## Label Taxonomy

The classifier evaluates the amount of relevant supporting context in each post's title and body. Every post receives exactly one of the following three labels. The examples below are the selected candidate posts documented in `research/milestone2_taxonomy.md`; their descriptions should be checked against the original Reddit posts before final submission.

### `low_context`

**Definition:** A post that states a question, opinion, or experience but gives no meaningful explanation or supporting background.

**Example 1 — Python versus JavaScript:** [Reddit post](https://www.reddit.com/r/learnprogramming/comments/1t3f1fi/). The author questions why Python is recommended for beginners when React appears in job listings, without providing meaningful details about their own career goals or circumstances.

**Example 2 — Choosing a first programming language:** [Reddit post](https://www.reddit.com/r/learnprogramming/comments/vli5zb/). The author asks which language would make it easier to learn other languages, without describing their experience or intended applications.

### `some_context`

**Definition:** A post that provides relevant background, a specific topic, or a previous difficulty but does not sufficiently develop the central situation.

**Example 1 — Learning Git from scratch:** [Reddit post](https://www.reddit.com/r/learnprogramming/comments/1wlmea9/). The author identifies themselves as a beginner and requests Git learning resources, but does not describe a specific Git task or attempt.

**Example 2 — Understanding C++ pointers:** [Reddit post](https://www.reddit.com/r/learnprogramming/comments/1hla3ri/). The author identifies pointers as confusing and mentions previous attempts to understand them, but provides no code example or concrete use case.

### `detailed_context`

**Definition:** A post that includes multiple concrete, relevant details that work together to explain the author's problem, experience, or argument.

**Example 1 — Python versus JavaScript:** [Reddit post](https://www.reddit.com/r/learnprogramming/comments/1qc5q4r/). The author describes office and data-related work, prior web-development learning, interests, and reasons for considering Python.

**Example 2 — Learning software design:** [Reddit post](https://www.reddit.com/r/learnprogramming/comments/1s4cvsb/). The author explains their Python and C++ knowledge, experience with small scripts, and difficulties structuring larger projects.

### The hardest boundary
**Which two labels:**
**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even

     if the tone is heated." -->

---
## The Dataset
<!-- Where you collected from, how you labelled, your counts, and three hard

     cases. -->

**Where the posts came from:** Public posts in [r/learnprogramming](https://www.reddit.com/r/learnprogramming/). The initial research log records 30 post URLs in `research/milestone1_observations.md`; this is not yet the labeled training dataset.
**How I labelled them:** Not started. The label taxonomy will be defined first; the initial 20 training examples must be labeled independently before any optional AI-assisted pre-labeling. <!-- Cold first? Pre-labelled with AI and corrected?

Say so plainly — the disclosure is required, not penalised. -->

**Counts per label:** Pending dataset collection and labeling; no per-label counts are available yet.
| Label | Count | Share |

|---|---|---|

|  |  |  |

|  |  |  |

|  |  |  |

| **Total** |  | 100% |

**Three hard cases**
<!-- Any post that made you pause: what it was, which two labels it could have

     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> **The post:**

>

> **Could have been:**

>

> **I chose, because:**

**2.**
> **The post:**

>

> **Could have been:**

>

> **I chose, because:**

**3.**
> **The post:**

>

> **Could have been:**

>

> **I chose, because:**

---
## The Training Run
<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:** Not recorded yet; confirm the model identifier in the notebook before training.
****Settings:** Training has not run. Record the actual epochs, learning rate, batch size, seed, and other settings after configuring the notebook.** <!-- epochs, learning rate, batch size, seed -->

**Anything I changed from the defaults, and why:** Not applicable yet; record any actual changes when training.
****Split sizes:** Not available until the dataset is created and split.** <!-- train / val / test, and per-label counts in the test

split. If a label had fewer than about 8 in test, say so — it explains a lot

of next unit's variance. -->

---
## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.
     Plus disclose any AI pre-labelling. -->

**Moment 1 — Community research and documentation**

- **What I asked for:** Help finding the top candidate posts from r/learnprogramming. 
- **What came back:** A research-log format, candidate distinctions, post URLs, and suggested summaries.
- **What I changed:** Compiled the research document with 30 entries, supporting examples, ambiguous cases, and conclusions. I must still independently verify the posts and observations before treating them as confirmed research.

**Moment 2 — README preparation**

- **What I asked for:** 
- **What came back:** 
- **What I changed:** 

**Pre-labelling disclosure:** No training dataset has been labeled or AI-pre-labeled yet. AI-generated research-log descriptions are not training labels. This disclosure will be updated if AI-assisted pre-labeling is used later.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.

     ═══════════════════════════════════════════════════════════════════ -->

---
## Baseline vs. Trained
<!-- Both models on the same posts. `python baseline.py --trained results.json`

     prints this table for you. -->

| Measure | Baseline | Trained | Difference |

|---|---|---|---|

| Overall accuracy |  |  |  |

| Macro F1 |  |  |  |

| F1 — `label_one` |  |  |  |

| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A

     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added

     nothing — and that is a real finding, not a failure. Say it plainly. -->

---
## Run Log — Before
<!-- Five criteria across three seeds. The notebook's section 6 prints the

     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |

|---|---|---|---|---|---|

| 1.  |  |  |  |  |  |

| 2.  |  |  |  |  |  |

| 3.  |  |  |  |  |  |

| 4.  |  |  |  |  |  |

| 5.  |  |  |  |  |  |

### Confusion matrix
<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.

     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |

|---|---|---|---|

| ****** |  |  |  |

| ****** |  |  |  |

| ****** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which

     direction. "7 real analysis posts were called hot_take and only 3 went the

     other way" is a direction, not just an error rate. -->

---
## Verdicts and Diagnoses
<!-- MET or MISSED against LAST UNIT's target. The target has to hold across

     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |

|---|---|---|---|---|

| 1 |  |  |  |  |

| 2 |  |  |  |  |

| 3 |  |  |  |  |

| 4 |  |  |  |  |

| 5 |  |  |  |  |

**Diagnoses**
<!-- For each miss: the cause, and how you know. The four common causes are:

     too few examples for a label, a boundary you applied inconsistently, a

     genuinely hard label pair, and a task the model can't reach from this

     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you

     have that can tell a LABELLING problem from a MODEL problem, and this

     section is graded on whether you used it that way. -->

---
## Agreement Report
<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in

     data/staff_taxonomy.md, not your own — so every argument below is made

     from those definitions and those decision rules. -->

****Agreement rate:**** **___ / 30 = ___**%

<!-- Nobody grades this number. A 60% who argues every disagreement from the

     stated rules beats a 95% who wrote "staff was right" nine times. Several

     of the 30 were chosen because they're genuinely ambiguous — you should be

     winning some of these. -->

**Disagreements**
<!-- Three lines each: the post, both labels, and who you think is right and

     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:

       (a) the rule covered it and I applied it loosely → a consistency problem

       (b) the rule genuinely doesn't say               → a gap in the definitions

       (c) the rule is ambiguous here and my reading is defensible → argue it.

           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a

     written rule two different ways on 30 posts, that is direct evidence about

     what you did across your own 200. -->

**1.**
> **The post:**

>

> **Staff said / I said:**

>

> **My call, and why:**

>

> **Which pile:**

**2.**
> **The post:**

>

> **Staff said / I said:**

>

> **My call, and why:**

>

> **Which pile:**

**What the pattern in my disagreements tells me:**
---
## The Improvement
**What I changed:**
**Which diagnosis pointed at it:**
### Run Log — After
| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |

|---|---|---|---|---|---|

| 1.  |  |  |  |  |  |

| 2.  |  |  |  |  |  |

| 3.  |  |  |  |  |  |

| 4.  |  |  |  |  |  |

| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**
<!-- If it didn't, say so. Relabelling that didn't help is a genuinely

     interesting result and earns full credit. -->

---
## What's Still Broken
<!-- For each criterion still missed: what you'd do, and why you stopped. -->

**The gap between what I meant my labels to capture and what the model

learned:**

<!-- Two sentences. Your confusion matrix is the evidence. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER

       [ ] Each has a reason underneath tied to your data or taxonomy

       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split

       [ ] No label above 70%

       [ ] All five unit 5 sections have real content

       [ ] Label Taxonomy includes the decision rule for your hardest boundary

       [ ] The Dataset includes three hard cases

       [ ] results.json and test_split.csv committed (the notebook does this)

       [ ] At least four new commits

       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand

       [ ] Run Log — Before, five criteria across three seeds

       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE

       [ ] A verdict on every criterion

       [ ] A diagnosis for every miss, using the agreement report as evidence

       [ ] Agreement Report with every disagreement adjudicated

       [ ] One improvement, with Run Log — After

       [ ] What's Still Broken

       [ ] results_three_seeds_before.json, results_three_seeds_after.json,

           baseline_results.json and

           agreement_results.json committed

       [ ] At least four new commits

       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.

     ═════════════════════════════════════════════════════════════════════ -->

---
📖 ****How to run this project: [RUNNING.md](**RUNNING.md**)****
