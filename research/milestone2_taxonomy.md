# TakeMeter — Milestone 2: Label Taxonomy (Stack Overflow)

## 1. Selected community and classification goal

**Community:** Stack Overflow (public programming questions)  
**Source:** https://stackoverflow.com/questions  
**Research:** [Milestone 1 observations](./milestone1_observations.md)  
**Unit of classification:** One question's complete title and body. Exclude answers, comments, votes, tags, and author reputation from the model input.

**Goal:** Classify how much *relevant supporting context* a question provides for understanding its specific request. Do not classify technical correctness, author expertise, politeness, or likelihood of receiving an answer.

## 2. Three labels and six real examples

The examples below are drawn from the collected 30-question Stack Overflow sample. They are **proposed adjudications** for the student to review against the full original questions before finalizing.

### `low_context`

**Definition:** The question states its request but gives no meaningful background, evidence, or constraints beyond what is necessary to identify the topic.

- **Example 1 — [80010880, Python general usage](https://stackoverflow.com/questions/80010880/python-general-usage):** Asks why one would invoke `python3` rather than `python`. The installed version and command form are provided, but may be intrinsic to the question rather than explanatory context. **Borderline with `some_context`; verify.**
- **Example 2 — [80010744, transition into blockchain development](https://stackoverflow.com/questions/80010744/how-to-quickly-transition-into-blockchain-development):** **Candidate only.** Read the complete body before using it as a `low_context` example; the title alone cannot establish the label.

### `some_context`

**Definition:** The question gives at least one meaningful, relevant supporting detail about the situation, attempted work, observed behavior, or constraint, but does not connect enough details to explain the situation substantially.

- **Example 1 — [80010854, Ansys Fluent to Mechanical](https://stackoverflow.com/questions/80010854/data-transfer-from-ansys-fluent-to-ansys-mechanical):** Describes 100 temperature data files, desired time steps, an import limitation, and attempted routes; however, the precise workflow and outcomes remain underdeveloped. **Borderline with `detailed_context`; verify.**
- **Example 2 — [80010879, SwiftUI TabView](https://stackoverflow.com/questions/80010879/how-to-keep-tabs-when-applying-tabviewstyle-page):** Describes disappearing tabs after `.tabViewStyle(.page)` and provides a compact code example, but limited further environment or diagnostic evidence.

### `detailed_context`

**Definition:** The question provides multiple concrete, relevant, connected details that substantially explain the request, its observed behavior, and the conditions or evidence needed to reason about it.

- **Example 1 — [80010870, vcpkg packaging failure](https://stackoverflow.com/questions/80010870/publish-package-for-distribution-via-vcpkg-fails-due-to-missing-debug-share):** Supplies the command, error output, directory structure, and port configuration, all tied to the packaging failure.
- **Example 2 — [80010865, SystemVerilog simulator discrepancy](https://stackoverflow.com/questions/80010865/why-does-xcelium-throw-a-hierarchical-name-error-on-a-module-parameter):** Supplies design and testbench snippets, the Xcelium error, and comparison with two other simulators; the details jointly explain the standards question.

**Before finalizing:** Replace any candidate whose full text does not support its proposed label. In particular, find and verify **two unambiguous `low_context` examples** from the 30-question reading log or extend that log with new questions read directly. Do not represent candidate labels as independently verified.

## 3. Decision rules

1. Read the **whole title and body**. Interpret code, error output, and formatting as part of the question; do not score raw HTML markup.
2. Identify the central request and which details actually help a reader understand it.
3. Assign `detailed_context` when **multiple concrete, relevant details work together** to explain the situation, evidence, behavior, and/or constraints. A code dump alone does not guarantee this label.
4. Otherwise, assign `some_context` if **at least one meaningful supporting detail** is present.
5. Otherwise, assign `low_context`.

**Special cases:** A short conceptual question may be self-contained without being detailed; do not reward or penalize length alone. A version number counts as context only when it helps explain the question, rather than merely naming the topic. A long post containing unrelated material is not automatically detailed. Do not require code for `detailed_context` when connected non-code evidence is sufficient.

## 4. Hardest boundary: `some_context` vs `detailed_context`

**Real borderline candidate:** [80010854 — Ansys Fluent to Mechanical](https://stackoverflow.com/questions/80010854/data-transfer-from-ansys-fluent-to-ansys-mechanical).

**Case for `some_context`:** The author names the data formats, desired 100-step result, and attempted import routes, but gives little detail about the specific settings and outcomes of each attempt.

**Case for `detailed_context`:** The quantity of files, mapping to time steps, tool limitation, and alternative approaches are concrete details that may together explain the practical task.

**Decision rule:** If the details collectively explain the concrete task and the obstacle well enough to reason about the request, choose `detailed_context`; if they merely list relevant facts and approaches without explaining their relationship or results, choose `some_context`.

**Final adjudication (student to complete after reading):** `__________`  
**Decisive evidence from the post:** `__________`

**Second boundary worth testing:** [80010804 — FAT12 bootloader](https://stackoverflow.com/questions/80010804/my-bootloader-fails-to-properly-read-the-fat12-root-directory). A large code listing must not automatically be classified `detailed_context`.

## 5. Eight hypothetical AI-generated boundary tests

These are **synthetic examples for testing the definitions**, not collected Stack Overflow questions and **not training data**. Suggested labels are provisional; classify them independently before checking the suggestions.

| # | Hypothetical question | Suggested label | Why it tests a boundary |
|---|---|---|---|
| 1 | Why use `python3` instead of `python`? | `low_context` | Conceptual request with no extra context |
| 2 | Why use `python3` instead of `python`? I'm on Windows 11. | `some_context` | Is the platform relevant enough to count? |
| 3 | My SwiftUI tabs disappear when I use `.tabViewStyle(.page)`. | `some_context` | Names a concrete symptom and trigger, but no other evidence |
| 4 | My SwiftUI tabs disappear with `.tabViewStyle(.page)`. Here is the view code, my expected behavior, and the exact result on iOS 18. | `detailed_context` | Connected code, expectation, observation, environment |
| 5 | I get a segmentation fault in NASM. Here's 300 lines of code. | `some_context` | Length alone does not explain the failure |
| 6 | My NASM program crashes after a `call`; here are the minimal instructions, the build command, and the debugger location. | `detailed_context` | Connected diagnostic evidence |
| 7 | How do I move data from Fluent to Mechanical? I have 100 files. | `some_context` | Relevant scale but limited workflow details |
| 8 | My package build fails: I ran `vcpkg install`, got the missing `debug/share` error, and included the portfile and directory tree. | `detailed_context` | Reproducible failure context |

**Independent stress-test review:** Pending. Record any cases you classify differently and refine rules before labeling the full dataset.

## 6. Verification checklist before committing

- [ ] Personally read the real example questions and confirm two clear examples for each label.
- [ ] Complete the borderline adjudication with a chosen label and supporting evidence.
- [ ] Independently classify the eight synthetic examples, then review disagreements.
- [ ] Copy the finalized definitions into `README.md` and `label_definitions.txt` exactly.
- [ ] Confirm the labels match the planned `LABELS` in `takemeter.ipynb` (do not run training yet).

**Source change:** This revision replaces Reddit examples in the original Milestone 2 taxonomy with Stack Overflow questions. Previous work remains in Git history.
