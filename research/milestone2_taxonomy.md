# TakeMeter — Milestone 2: Label Taxonomy

## 1. Selected Community

**Community:** r/learnprogramming  
**Source:** https://www.reddit.com/r/learnprogramming/  
**Classification goal:** Classify programming-related posts by the level of relevant supporting context provided by the author.  
**Research source:** [Milestone 1 Observations](./milestone1_observations.md)

## 2. Label Taxonomy

Evaluate the original post's title and body. Assign exactly one label.

### Label 1: `low_context`

**Definition:** A post asks a question or expresses an opinion or experience without meaningful supporting background that explains the author's specific circumstances.

**Example 1 — Post 11: Python versus JavaScript**  
https://www.reddit.com/r/learnprogramming/comments/1t3f1fi/  
The author asks why Python is recommended for beginners when React appears in job listings, but gives little information about their own goals or circumstances.

**Example 2 — Choosing a first programming language**  
https://www.reddit.com/r/learnprogramming/comments/vli5zb/  
The author asks which language makes later languages easier to learn, without explaining previous experience or intended applications. **Note:** This post was added after the original 30-post reading log; it must be read and included in the research log to meet the 'from your reading' requirement.

### Label 2: `some_context`

**Definition:** A post provides at least one relevant supporting detail, such as prior experience, a specific difficulty, or a goal, but does not explain the situation with multiple connected concrete details.

**Example 1 — Post 24: Learning Git from scratch**  
https://www.reddit.com/r/learnprogramming/comments/1wlmea9/  
The author describes beginner status and asks for Git learning resources, without a specific task or failed attempt.

**Example 2 — Post 26: Understanding C++ pointers**  
https://www.reddit.com/r/learnprogramming/comments/1hla3ri/  
The author identifies pointers as confusing and mentions previous attempts to understand them, but supplies no specific code example or use case.

### Label 3: `detailed_context`

**Definition:** A post provides multiple concrete, relevant details that connect to one another and substantially explain its central problem, experience, or argument.

**Example 1 — Post 6: Python versus JavaScript**  
https://www.reddit.com/r/learnprogramming/comments/1qc5q4r/  
The author describes work responsibilities, previous HTML/CSS and JavaScript learning, interests, and competing reasons for choosing a language.

**Example 2 — Post 17: Learning software design**  
https://www.reddit.com/r/learnprogramming/comments/1s4cvsb/  
The author describes Python and C++ knowledge, success with small scripts, difficulty structuring larger projects, and gaps in computer science knowledge.

## 3. Classification Decision Rules

1. Read the full title and body, not only the title.
2. Ignore irrelevant details, repetition, post length, emotional intensity, and writing style when deciding how much supporting context exists.
3. Assign `detailed_context` if multiple concrete, relevant details connect to explain the central issue, experience, or argument.
4. Otherwise assign `some_context` if at least one meaningful supporting detail is present.
5. Otherwise assign `low_context`.

Apply the rules in this order so that each post receives exactly one label. Mentioning several technologies without explaining how they relate does not automatically make a post `detailed_context`.

## 4. Hardest Boundary — Real Borderline Post

**Competing labels:** `some_context` and `detailed_context`.

**Candidate borderline post — Post 22: Difficulty learning independently**  
https://www.reddit.com/r/learnprogramming/comments/1pmzjoe/

**Case for `some_context`:** Describing a recurring copy/paste/debug cycle identifies a difficulty, but might not provide enough concrete information about what the author tried or where learning broke down.

**Case for `detailed_context`:** If the author connects prior learning habits, attempts to solve problems, and specific consequences, those details may jointly explain the learning difficulty.

**Decision rule:** Assign `detailed_context` only if the post supplies multiple concrete details that *work together* to explain its central situation. If it merely identifies a struggle and general background, assign `some_context`, even when the post is long.

**Borderline adjudication:** Pending direct review of Post 22's full text. The arguments above are based on the Milestone 1 reading-log description, not a verified quotation of the post. Record the final chosen label and the decisive textual evidence after reading it.

## 5. AI-Generated Eight-Case Boundary Stress Test

These eight posts are **hypothetical AI-generated examples**, not Reddit posts. They intentionally sit near label boundaries. The assignments below are proposed applications of the rules, not results of an independent human or group test.

| # | Hypothetical post | Proposed label | Reason / boundary being tested |
|---|---|---|---|
| 1 | I'm new to programming and want to make games. Where should I start? | `some_context` | Game development is a relevant goal, but there are no concrete project details. |
| 2 | Is Python better than JavaScript for someone trying to find a job? | `some_context` | A job-related goal is given, but the situation is otherwise unspecified. |
| 3 | I keep getting errors in Python and don't know what to do. | `some_context` | Names a language and difficulty, but no error or attempt. |
| 4 | I've used Python for three months and finished two courses, but I still can't build a project without a tutorial. | `detailed_context` | Duration, completed learning, and the precise independent-work difficulty connect. |
| 5 | I'm learning React and Python, and I feel stuck and overwhelmed. | `some_context` | Multiple technologies and emotion do not explain a concrete problem. |
| 6 | I made a React form and the submit button does nothing. I added an `onSubmit` handler, checked the console, and saw no errors. | `detailed_context` | Describes an observable failure and connected troubleshooting steps. |
| 7 | I studied Git from videos, but branches still confuse me when I work with classmates. | `detailed_context` | Learning method, specific concept, and collaboration situation jointly explain the issue. |
| 8 | I'm a beginner, I use Windows, and I want to learn C++. Any suggestions? | `some_context` | Several facts are present, but only the learning goal is meaningfully developed. |

### Stress-Test Review

**Proposed distribution:** `low_context`: 0; `some_context`: 5; `detailed_context`: 3. This is intentionally not a balanced sample: the purpose is to challenge the `some_context` / `detailed_context` boundary rather than test obvious examples.

**Likely disagreements:** Cases 4 and 7 may be classified as `some_context` by someone who requires code, error messages, or attempted fixes for a `detailed_context` label. The rule intentionally permits detailed *learning experiences* as well as technical troubleshooting posts, provided the details are connected and explanatory.

**Independent review:** Not yet recorded. Apply the definitions without consulting the proposed labels, record any disagreements, and refine the decision rule if necessary.

## 6. Final Review and Remaining Verification

**Are the labels mutually exclusive?** The ordered decision rules are designed to produce exactly one label per post; real-world consistency remains to be tested during labeling.

**What was clarified?** The distinction between `some_context` and `detailed_context` depends on whether concrete details are connected and explanatory, not on word count or the number of technologies mentioned.

**Solo/group boundary discussion:** The strongest cases for each side of Post 22 are recorded in Section 4. An independent group choice or personal adjudication has not been recorded.

**Taxonomy decision:** Retain `low_context`, `some_context`, and `detailed_context` as the proposed taxonomy. Before declaring Milestone 2 complete, verify the six real examples against their full posts, add the extra low-context post to the reading log, adjudicate Post 22, and independently review the eight boundary cases.
