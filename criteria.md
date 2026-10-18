# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1. Overall classification accuracy

The classifier must achieve at least **65% overall accuracy** on the held-out test set for **each of the three training seeds**.

**Why this target:** I chose 65% because the classifier distinguishes three levels of supporting context, and posts near the `some_context` / `detailed_context` boundary can be difficult to separate. I consider 65% a useful target for a small, three-label dataset without expecting every borderline case to be classified correctly.

**How to check:** For each seed, divide correctly predicted held-out posts by the total number of held-out posts. Each seed must reach at least 0.65.

---

## 2. Minimum F1 for every label

Each label — `low_context`, `some_context`, and `detailed_context` — must achieve an **F1 score of at least 0.55** on the held-out test set for **each of the three training seeds**.

**Why this target:** I chose 0.55 because distinguishing `some_context` from `detailed_context` can be ambiguous, and the planned dataset of approximately 200 posts may leave relatively few test examples per label. I still want acceptable performance for every context level, rather than good overall accuracy driven by only one label.

**How to check:** Calculate F1 separately for each of the three labels for each seed. All nine label-by-seed scores must be at least 0.55.

---

## 3. Dataset label balance

No single label may account for **more than 60%** of the complete labeled dataset in `labels.csv`.

**Why this target:** I chose 60% so all three context levels are represented without one category dominating the examples used for training. This also sets a stricter balance limit than the assignment's 70% maximum.

**How to check:** For each label, divide its row count in `labels.csv` by the total number of labeled rows. The largest share must be at most 0.60.

---

## 4. Independent labeling consistency

Two people independently applying the TakeMeter taxonomy to the **same 20 Reddit posts** must agree on at least **75%** of their labels (**15 of 20 posts**).

**Why this target:** I chose 75% because the distinction between `some_context` and `detailed_context` involves judgment even with a written boundary rule. Agreement on at least three out of four posts would show that another person can apply the taxonomy reasonably consistently while leaving room for difficult cases.

**How to check:** Select and record the 20 post IDs before comparing labels. Each person labels the same title and body independently, using `low_context`, `some_context`, or `detailed_context` and the same decision rules. Count exact matches and divide by 20. The separate Unit 6 staff-taxonomy exercise does not measure this criterion.

---

## 5. Accuracy of high-confidence predictions

For **each of the three training seeds**, held-out test predictions whose **highest predicted class probability is at least 0.80 (80%)** must achieve **at least 75% accuracy** among those qualifying predictions.

**Why this target:** I chose 80% as the cutoff to focus on predictions the model considers relatively certain. I chose 75% accuracy because those predictions should be more reliable than the 65% overall accuracy target, even though borderline supporting-context posts can remain difficult.

**How to check:** For each seed, take the maximum predicted probability across the three labels for each held-out post. Filter predictions with maximum probability >= 0.80, then divide the number correctly classified by the number qualifying. Record both counts. If zero predictions qualify for a seed, mark this criterion **not met / not evaluable for that seed**, never as passed; the criterion is met only if all three seeds have qualifying predictions and each qualifying subset reaches 0.75 accuracy.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

        ## 2. Every label performs acceptably

        The model performs well on all labels.

        **Why this target:** ...

        > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
        > the held-out set.
        >
        > **Why revised:** "performs well" gave me nothing to check. I
        > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

        ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
          0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
