# TakeMeter

**Author:** Jean Pierre Joseph  
**Course:** CodePath AI201  
**Project:** TakeMeter — Stack Overflow Question Context Classifier

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this project. Run section 1, which reports the hardware you'll be training on.
>
> Continue through the notebook in order, checking its outputs before training.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE
     Unit 5 asks for the first five sections. Unit 6 adds the sections below them.
     Everything is pasted as TEXT. No screenshots, no images.
     The confusion matrix especially: paste the Markdown table, not a screenshot.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

TakeMeter is a text-classification project using public programming questions collected from Stack Overflow through the Stack Exchange API. It categorizes questions by the richness of relevant supporting context in their titles and bodies.

An initial exploration of 30 questions identified four useful distinctions: problem specificity, technical evidence, troubleshooting history, and environment or constraints. The three labels are `low_context`, `some_context`, and `detailed_context`. A reviewed dataset of 200 Stack Overflow questions was used to fine-tune a DistilBERT classifier. The model was trained and evaluated on a held-out test set of 30 questions, achieving 70.0% accuracy and a macro F1 score of 0.275. The evaluation also revealed that the model predicted `detailed_context` for every test question, highlighting a limitation caused by its preference for the majority class.

---

## Label Taxonomy

The classifier evaluates the amount of relevant supporting context in each Stack Overflow question's title and body. Every question receives exactly one of the following three labels.

### `low_context`

**Definition:** A post that states a question or problem but gives little meaningful explanation or supporting background.

**Example 1 — Python command usage:** [Stack Overflow question 80010880](https://stackoverflow.com/questions/80010880). The author asks about the difference between `python` and `python3`, providing little additional background beyond the Python version and command.

**Example 2 — Running an executable from x86 assembly:** [Stack Overflow question 80010721](https://stackoverflow.com/questions/80010721). The author asks how to run an executable using the Win32 API in a 32-bit assembly program, without developing the environment, attempted approach, or observed result in much detail.

### `some_context`

**Definition:** A post that provides relevant background, a specific topic, or a previous difficulty but does not sufficiently develop the central situation.

**Example 1 — Ansys Fluent to Mechanical:** [Stack Overflow question 80010854](https://stackoverflow.com/questions/80010854). The author describes 100 data files, the intended time-step conversion, and attempted import approaches, but does not fully explain the results of those attempts.

**Example 2 — SwiftUI TabView:** [Stack Overflow question 80010879](https://stackoverflow.com/questions/80010879). The author describes disappearing tabs after applying `.tabViewStyle(.page)` and includes a code example, but gives limited additional diagnostic information.

### `detailed_context`

**Definition:** A post that includes multiple concrete, relevant details that work together to explain the author's problem, experience, or argument.

**Example 1 — vcpkg packaging failure:** [Stack Overflow question 80010870](https://stackoverflow.com/questions/80010870). The author provides the failing command, error output, project directory structure, and relevant configuration.

**Example 2 — SystemVerilog simulator discrepancy:** [Stack Overflow question 80010865](https://stackoverflow.com/questions/80010865). The author provides code examples, the exact error message, and differences between three simulators.

### The hardest boundary

**Which two labels:** `some_context` and `detailed_context`.

**The decision rule I used:** If multiple concrete, relevant details work together to explain the situation, choose `detailed_context`. If the post contains useful background but does not sufficiently develop the situation, choose `some_context`. Length alone does not determine the label; the relevance and explanatory value of the details matter.

---

## The Dataset

**Where the posts came from:** Public programming questions from [Stack Overflow](https://stackoverflow.com/questions), collected through the Stack Exchange API with question bodies included. The collection contains 200 records with 200 unique question IDs and nonempty text fields. The classifier uses each question's title and body. The initial community-research sample contained 30 questions.

**How I labeled them:** I first assigned labels to 20 questions independently, before using AI to propose labels for the remaining 180. I reviewed the AI suggestions and made the final labeling decisions using the taxonomy above. I also revisited eight borderline `detailed_context` cases and changed them to `some_context` after reviewing whether the supporting details actually developed the central problem. The final review file records 20 rows with `cold` notes and 180 with `ai_reviewed` notes. The training and review files were compared: all 200 labels and notes matched, and all question texts matched after whitespace normalization.

**Files:** `labels.csv` contains `text`, `label`, and `note` for training. `data/stackoverflow_labeling_review.csv` retains `question_id`, `url`, `text`, `label`, and `note` for traceability. The preparation script `prepare_stackoverflow_labels.py` converts the original Stack Overflow JSON into blank-label CSV files; it is not used to regenerate the completed labels.

**Counts per label:**

| Label              |   Count |    Share |
| ------------------ | ------: | -------: |
| `low_context`      |      10 |       5% |
| `some_context`     |      50 |      25% |
| `detailed_context` |     140 |      70% |
| **Total**          | **200** | **100%** |

The largest class, `detailed_context`, represents 70% of the dataset. This satisfies the Unit 5 requirement that no label exceed 70%, but it does not meet my stricter acceptance criterion of 60% maximum representation. This imbalance is an important limitation to investigate during Unit 6. This is a dataset statistic, not a trained-model evaluation result.

**Three borderline labeling cases:**

1. **[Ansys Fluent to Mechanical — question 80010854](https://stackoverflow.com/questions/80010854).** **Could have been:** `some_context` or `detailed_context`. **Label assigned:** `some_context`. The author describes 100 data files, the conversion objective, and attempted import approaches. Those details establish the task, but the results of the attempts are not developed enough to explain the failure fully. The number of details alone does not justify `detailed_context`.
2. **[SwiftUI TabView — question 80010879](https://stackoverflow.com/questions/80010879).** **Could have been:** `some_context` or `detailed_context`. **Label assigned:** `some_context`. The question includes a specific symptom and code, but provides limited diagnosis or evidence about what has already been tested. A code block by itself is not sufficient for `detailed_context`.
3. **[SystemVerilog simulator discrepancy — question 80010865](https://stackoverflow.com/questions/80010865).** **Could have been:** `some_context` or `detailed_context`. **Label assigned:** `detailed_context`. The code, exact error, and comparison of behavior across simulators reinforce one another and provide a concrete explanation of the problem. This satisfies the rule for multiple relevant supporting details.

These three recorded labels were checked against the reviewed dataset. They illustrate the difficult `some_context`/`detailed_context` boundary; the explanations above describe the rationale for the labels rather than claiming an unrecorded personal reaction to each post.

---

## The Training Run

**Base model:** `distilbert-base-uncased` (DistilBERT), fine-tuned to classify Stack Overflow questions into three context levels: `low_context`, `some_context`, and `detailed_context`.

**Training device:** CPU, using PyTorch `2.14.1+cpu`. The training completed in approximately 68 seconds.

**Settings:**

- Random seed: `42`
- Number of epochs: `3`
- Learning rate: `2e-5`
- Training batch size: `16`
- Evaluation batch size: `16`
- Maximum sequence length: `128` tokens

**Anything I changed from the defaults, and why:** I replaced the starter label configuration (`analysis`, `hot_take`, `reaction`) with `low_context`, `some_context`, and `detailed_context` to match the labels in my Stack Overflow dataset. I kept the default training hyperparameters: three epochs, learning rate `2e-5`, batch size `16`, and random seed `42`.

**Split sizes:** The 200 labeled Stack Overflow questions were divided into 139 training examples, 31 validation examples, and 30 test examples.

| Label              | Training | Validation |   Test |
| ------------------ | -------: | ---------: | -----: |
| `low_context`      |        7 |          1 |      2 |
| `some_context`     |       35 |          8 |      7 |
| `detailed_context` |       97 |         22 |     21 |
| **Total**          |  **139** |     **31** | **30** |

**Training results:** The model successfully completed all three epochs. Final validation accuracy was 70.97%, with a macro F1 score of 0.2767. Validation loss decreased from 0.794938 in epoch 1 to 0.697430 in epoch 3.

**Held-out test results:** The trained model achieved 70.0% accuracy and a macro F1 score of 0.275 on the 30 test questions.

| Label              | Test examples | F1 score |
| ------------------ | ------------: | -------: |
| `low_context`      |             2 |    0.000 |
| `some_context`     |             7 |    0.000 |
| `detailed_context` |            21 |    0.824 |

**Observations and limitations:** The model's results suggest that it strongly favors the majority class, `detailed_context`. The test split contains only two `low_context` examples and seven `some_context` examples, so their evaluation metrics are sensitive to individual predictions. These limitations will be investigated further in Unit 6.

**Saved results:** Section 5 of `takemeter.ipynb` successfully generated `results.json` and `test_split.csv`. These files preserve the training evaluation evidence and held-out test data for the next unit.

---

## How I Used AI

**Moment 1 — Community research and taxonomy**

- **What I asked for:** Help choosing a permitted public community after Reddit API access failed, and help revising the research and taxonomy for Stack Overflow.
- **What came back:** Guidance on the assignment, commands to inspect the Stack Overflow collection, and proposed research distinctions and taxonomy examples.
- **What I changed:** I collected and checked 200 Stack Overflow questions, used the Stack Overflow-specific taxonomy, and independently labeled the first 20 questions.

**Moment 2 — AI-assisted labeling and dataset verification**

- **What I asked for:** Proposed labels for the remaining 180 Stack Overflow questions and help examining borderline decisions and validating the CSV files.
- **What came back:** Suggested labels, explanations of the `some_context`/`detailed_context` boundary, and read-only Python checks for counts, fields, and agreement between the two CSV files.
- **What I changed:** I reviewed the 180 suggestions, made the final label decisions, and accepted eight reviewed changes from `detailed_context` to `some_context`. I verified 200 unique questions, 20 `cold` and 180 `ai_reviewed` records, no invalid or missing labels, and matching labels and notes across the review and training files. The texts matched after whitespace normalization.

**Pre-labeling disclosure:** The first 20 questions were labeled independently. AI proposed labels for the other 180 questions, but I reviewed the suggestions and retained responsibility for the final labels. AI also assisted with documentation and verification scripts. This process does not constitute independent human agreement testing.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════
     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure                 | Baseline | Trained | Difference |
| ----------------------- | -------- | ------- | ---------- |
| Overall accuracy        |          |         |            |
| Macro F1                |          |         |            |
| F1 — `low_context`      |          |         |            |
| F1 — `some_context`     |          |         |            |
| F1 — `detailed_context` |          |         |            |

**What I predicted before I looked:**

<!-- Write the prediction before seeing the trained numbers. -->

**What the gap actually means:**

<!-- Explain what the comparison shows after results are available. -->

---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion                        | Target                   | Seed 42 | Seed 7 | Seed 2024 | Verdict |
| -------------------------------- | ------------------------ | ------- | ------ | --------- | ------- |
| 1. Held-out accuracy             | ≥65%                     |         |        |           |         |
| 2. Per-class F1                  | ≥0.55 for each class     |         |        |           |         |
| 3. Largest predicted label share | ≤60%                     |         |        |           |         |
| 4. Independent human agreement   | ≥75% on 20 posts         |         |        |           |         |
| 5. High-confidence accuracy      | ≥75% at confidence ≥0.80 |         |        |           |         |

### Confusion matrix

<!-- Paste the notebook's actual confusion matrix as a Markdown table, not an image. -->

| true \ predicted   | `low_context` | `some_context` | `detailed_context` |
| ------------------ | ------------: | -------------: | -----------------: |
| `low_context`      |               |                |                    |
| `some_context`     |               |                |                    |
| `detailed_context` |               |                |                    |

**My biggest off-diagonal number, and what it means:**

<!-- Identify the most frequent confusion and its direction, using actual results. -->

---

## Verdicts and Diagnoses

<!-- MET or MISSED against the targets. All three seeds must satisfy the
     model-metric targets. -->

| #   | Criterion                     | Target                   | Verdict | How I decided |
| --- | ----------------------------- | ------------------------ | ------- | ------------- |
| 1   | Held-out accuracy             | ≥65%                     |         |               |
| 2   | Per-class F1                  | ≥0.55 for each class     |         |               |
| 3   | Largest predicted label share | ≤60%                     |         |               |
| 4   | Independent human agreement   | ≥75% on 20 posts         |         |               |
| 5   | High-confidence accuracy      | ≥75% at confidence ≥0.80 |         |               |

**Diagnoses**

<!-- For each miss: identify the cause and evidence. Use the agreement report
     to distinguish labeling inconsistency from model limitations. -->

---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.
     Label the 30 posts under the STAFF taxonomy in data/staff_taxonomy.md,
     not your own taxonomy. -->

**Agreement rate:** **_ / 30 = _**%

<!-- Every disagreement needs the post, both labels, your evidence-based call,
     and a classification into a consistency issue, rule gap, or defensible ambiguity. -->

**Disagreements**

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

| Criterion                        | Target                   | Seed 42 | Seed 7 | Seed 2024 | Verdict |
| -------------------------------- | ------------------------ | ------- | ------ | --------- | ------- |
| 1. Held-out accuracy             | ≥65%                     |         |        |           |         |
| 2. Per-class F1                  | ≥0.55 for each class     |         |        |           |         |
| 3. Largest predicted label share | ≤60%                     |         |        |           |         |
| 4. Independent human agreement   | ≥75% on 20 posts         |         |        |           |         |
| 5. High-confidence accuracy      | ≥75% at confidence ≥0.80 |         |        |           |         |

**Did it help, and how do I know:**

<!-- Explain the change in measured results, even if there was no improvement. -->

---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->

**The gap between what I meant my labels to capture and what the model learned:**

<!-- Use the confusion matrix and evaluation results as evidence. -->

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
           baseline_results.json and agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
