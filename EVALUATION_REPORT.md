# Evaluation report: how the workbook values were produced

This report explains where every value in `data/Mobile App Accessibility Evaluation.xlsx` comes from, for the five apps in the paper. It also records where the workbook, the code and the paper differ, so that a reader can judge each result.

In short:

- **Scores** are Excel formulas over a Status and a fixed weight per criterion. `tools/reproduce_scores.py` recomputes all of them.
- **Instance counts** come from the scanner parser, with 8 of 43 values adjusted during rating.
- **Statuses, Notes and Recommendations** were written by Claude Opus 5.5 using the same process for all five apps. The session records, prompts and reports are kept for Equity, Fidelity, GTWorld and AccessMore; BK Mobile was evaluated first, in an earlier session whose records were not kept.
- **No human check** of the AI-written ratings has been recorded.

## 1. Pipeline

```
Scanner exports (screenN.png + reportN.txt)
   |                         |
   v                         v
Lane A: parser           Lane B: one Claude review agent per app
(counts, sizes,  ------>  (opens every screenshot with its report;
 contrast)       tally    the prompt includes the main parser findings)
   |                         |
   +-----------+-------------+
               v
   Rating: Status, Notes, Instances, Recommendation per criterion
   (written by the main Claude Code agent into workbook_build/ratings.py)
               v
   build_workbook.py writes the ratings into the app tabs
               v
   Excel formulas compute every score  ->  Comparison Dashboard
```

## 2. Apps and capture

All five apps were recorded with Google Accessibility Scanner 2.5 on a Google Pixel 8 (Android 17), using the author's own accounts. Each session exports one screenshot and one text report per screen.

| App | Country | Captured | Sessions | Screens | Unique reports | Repeated |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| BK Mobile | Rwanda | 17 Sep 2026 | 2 | 50 | 33 | 17 |
| Equity Mobile | Rwanda | 25 Sep 2026 | 1 | 24 | 20 | 4 |
| Fidelity | Nigeria | 25 Sep 2026 | 1 | 40 | 29 | 11 |
| GTWorld | Nigeria | 25 Sep 2026 | 3 | 33 | 22 | 11 |
| AccessMore | Nigeria | 25 Sep 2026 | 2 | 21 | 14 | 7 |
| **Total** | | | **9** | **168** | | |

## 3. Lane A: scanner tally

`tools/parse_scanner_reports.py` splits each report at blank lines. It skips the first block, which is a preamble, and treats each remaining block as one finding: category (line 1), element id or screen coordinates (line 2) and message (the rest). It prints:

- the number of findings per category, and the WCAG 2.2 criteria each one feeds (`SC_MAP` in the script);
- touch-target sizes, using the smaller side, in three bands: under 24 dp, 24–43 dp, and 44 dp or larger;
- for text and image contrast, the lowest ratio, how many findings fall below 3:1 and below 2:1, and the most frequent colour pairs;
- the 10 most frequent elements for each label-type category (this is how `btnNavigation` was found);
- a note when reports repeat, which means duplicate screens;
- a warning when every touch-target finding comes from web content, which signals a WebView interface (this flagged Fidelity).

The ratings for Equity, Fidelity, GTWorld and AccessMore were made with an earlier version, `workbook_build/parse_v1.py` with `summarize_app.py`, on 25 Sep 2026. It splits reports the same way and gives the same counts per category.

## 4. Lane B: AI-assisted screenshot review

On 25 Sep 2026 (about 11:46–11:50 UTC), one Claude Opus 5.5 (`claude-opus-5-5`) agent per app ran in Claude Code. Each agent opened every screenshot as an image together with its report and answered a 12-point checklist. The exact prompts are in `screenshot_reviews/prompts/`, and the reports the agents returned are in `screenshot_reviews/`.

| App | Screenshots opened | Report |
| --- | ---: | --- |
| Equity Mobile | 24 of 24 | `Equity_Mobile_RW.md` |
| Fidelity | 40 of 40 | `Fidelity_NG.md` |
| GTWorld | 33 of 33 | `GTWorld_NG.md` |
| AccessMore | 21 of 21 | `AccessMore_NG.md` |
| BK Mobile | All 50, by the same process in an earlier session | not kept |

Each prompt included that app's main parser findings, for example `btnNavigation (23x)`. The review was therefore informed by the tally, not independent of it. `tools/screenshot_review_checklist.md` is a generic version of the prompt, written on 28 Sep.

## 5. Ratings: Status, Notes, Recommendation (columns F, H, M)

For Equity, Fidelity, GTWorld and AccessMore, the main Claude Code agent combined the Lane A counts and the Lane B reports and wrote one Status, Note, Instances count and Recommendation per criterion into `workbook_build/ratings.py`. It also wrote each transaction check and a coverage note for the dashboard. `workbook_build/build_workbook.py` then copied the BK Mobile tabs as a template, wrote the ratings in, and added the dashboard rows. `verify_scores.py` recomputed every score as a check.

Rows not listed in `ratings.py` keep the template's Not Tested text. The build script stops with an error if a row that BK had scored would otherwise be copied to another app. Three transaction checks are always set by rule:

- **T6** (non-touchscreen channel) is always Not Tested.
- **T4** (accessible receipts) is Not Tested unless a receipt was captured.
- **T2, T3 and T10** keep the template's Not Tested text.

The ratings follow these rules:

| Situation | Status |
| --- | --- |
| A scanner failure recurs across screens | Fail |
| 2.5.8: more than 25% of flagged targets under 24 dp | Fail |
| 2.5.8: fewer than about 15% under 24 dp (the paper restates this as at least one but no more than 25%) | Partial |
| Any text-scaling finding, until clipping is confirmed | Partial (1.4.4) |
| The feature exists but only partly meets the criterion | Partial |
| A screenshot shows the criterion met and no scanner finding contradicts it | Pass |
| The flow was not captured | Not Tested, never Fail |
| The criterion needs interaction to test (focus order, announcements, timing, keyboard or switch access) | Not Tested |
| 3.2.4, excluded for non-web software | N/A |

These rules were written into the workbook's Methodology tab on 28 Sep, after the four apps had been rated on 25 Sep. For those apps, the rules describe the reasoning in `ratings.py`; they were not fixed in advance.

**BK Mobile** was evaluated first, by the same process: scanner tally, screenshot review and ratings. That session's prompt, review report and code were not kept, so its ratings can be traced only through the Notes in the workbook. Its tabs then served as the template for the other four apps.

## 6. Instances found (column I)

Instance counts start from the parser output. Each scanner category is added to the criteria it feeds:

| Criterion | Count |
| --- | --- |
| 1.1.1 | Item label + Unexposed Text |
| 2.4.4 | Item label |
| 2.5.3 | Unexposed Text |
| 4.1.2 | Item label + Clickable items + Item descriptions (+ Unsupported item type, Item type label) |
| 1.3.1 | Clickable items + Item descriptions |
| 1.4.3 | Text contrast |
| 1.4.11 | Image contrast |
| 1.4.4 | Text Scaling |
| 2.5.8 and 2.5.5 | Touch target (all of them, in both rows) |

Counts are raw, so a screen captured twice is counted twice. They support the ratings but do not enter any score. A dash means no scanner evidence; for Fidelity, the label criteria show a dash because its WebView hid every control from the label checks.

Of the 43 non-blank values for these criteria across the five apps, 35 match `parse_scanner_reports.py` exactly (its output on the original reports is in `expected_output/`). The 8 that don't:

| App | Criterion | Workbook | Parser | Reason |
| --- | --- | ---: | ---: | --- |
| AccessMore | 1.4.11 | 22 | 1 | About 21 findings reported as text contrast are blue icons on grey circles (2.95:1), so they were moved here (see Notes) |
| AccessMore | 2.5.3 | 7 | 5 | Two labels with action words ("CLICK HERE", "Tap") added from the screenshots (see Notes) |
| AccessMore | 4.1.2 | 13 | 15 | The 2 Item type label findings were not counted; the earlier parser did not map that category |
| AccessMore | 2.4.4 | 8 | 9 | Not explained in the Notes |
| AccessMore | 1.3.1 | 3 | 4 | Not explained in the Notes |
| Fidelity | 1.3.1 | 3 | 0 | Split balance and blank bottom sheets seen in the screenshots; no scanner finding |
| BK Mobile | 4.1.2 | 154 | 159 | Counts Item label + Clickable items only; the 5 Item descriptions findings are left out |
| BK Mobile | 1.3.1 | 8 | 13 | Same: Clickable items only |

## 7. Weights and scores

Weights (column E) are fixed in the template and identical for every app. Every score is an Excel formula:

```
Status score  G = 1 for Pass, 0.5 for Partial, 0 otherwise
Tested?       L = 1 if Pass, Partial or Fail, else 0
Weighted      J = E x G
WCAG score    E44 = 100 x SUM(J) / SUMPRODUCT(L x E)            all levels, including AAA
Level A %     E45 = same, Level A rows only
Level AA %    E46 = same, Level A and AA rows
Fail count    E47 = COUNTIF(F, "Fail")
Not Tested    E48 = COUNTIF(F, "Not Tested") + COUNTIF(F, "N/A")
Transaction   D21 = 100 x SUM(weight x status) / SUM(weight of rated checks), T1-T12
```

Not Tested and N/A rows count in neither the numerator nor the denominator. The Comparison Dashboard pulls each app's E44–E48 and D21 by cell reference.

**Criterion numbering.** Three workbook rows are numbered one place off: its 3.3.9 Redundant Entry is WCAG 2.2 **3.3.7**, its 3.3.7 Accessible Authentication (Minimum) is **3.3.8**, and its 3.3.8 Accessible Authentication (Enhanced) is **3.3.9**. The names and levels are correct. `reproduce_scores.py` and the paper use WCAG 2.2 numbers.

## 8. Corrections made to the paper

An earlier draft (11 Oct 2026) differed from the data in several places. The current `main.tex` was corrected as follows, and every number in its Results section now reproduces with `tools/reproduce_scores.py`:

| # | Earlier draft | Corrected to |
| ---: | --- | --- |
| 1 | Transaction table: BK T7, GTWorld T7, and T8 for Equity, Fidelity and GTWorld shown as Partial | Not Tested, as in the workbook; this matches the "checks scored" counts and transaction scores |
| 2 | Scanner-only scores leave out "3.3.7 and 3.3.8" | 3.3.8 and 3.3.9, the two Accessible Authentication criteria in WCAG 2.2 numbering |
| 3 | "A researcher checked the screens cited for every rating" | Human verification is stated as not carried out in this phase |
| 4 | "4 to 11 repeated reports" | 4 to 17 (17 in BK Mobile) |
| 5 | Parser warns "when every finding comes from web content" | When every touch-target finding comes from web content |
| 6 | Limitation: the 2.5.8 rule leaves 15–25% undefined | Removed; the rating rules now define that band as Partial |
| 7 | Lane B: "the same fixed prompt" | The same checklist prompt, filled in with each app's sessions and main Lane A findings |

Still open in the paper: the repository URL and licence, a systematic literature search, and citations for national policy.

## 9. Verification status

The ratings for Equity, Fidelity, GTWorld and AccessMore are AI output, as written on 25 Sep 2026. The session records show no human review between the agents' reports and the ratings being written. The paper's scanner-only scores (Section 4.6, reproduced by `reproduce_scores.py`) show how much the results depend on those ratings.
