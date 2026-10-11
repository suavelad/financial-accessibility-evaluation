# Replication package: accessibility of mobile banking apps for blind and visually impaired users in Rwanda and Nigeria

This repository holds the data and code behind the paper *Digital Accessibility and Financial Inclusion: A Scanner-Based and AI-Assisted Evaluation of Mobile Banking Applications for Blind and Visually Impaired Users in Rwanda and Nigeria* (Ajayi and Umuhoza). It covers five Android banking apps: BK Mobile and Equity Mobile (Rwanda), and Fidelity, GTWorld and AccessMore (Nigeria).

With it you can:

- reproduce every number in the Results section from the ratings workbook;
- collect your own Google Accessibility Scanner reports and run the same Lane A parser on them;
- trace each rating back to the AI screenshot review (Lane B) and the code that wrote it into the workbook.

[EVALUATION_REPORT.md](EVALUATION_REPORT.md) explains how every value in the workbook was produced.

## Requirements

- **To reproduce the results:** Python 3.8 or later. All scripts in `tools/` use only the standard library, so nothing needs installing. Excel or LibreOffice is only needed to view the workbook.
- **To collect new scans:** an Android phone running Android 9 or later, the Google Accessibility Scanner app, and accounts with the banks whose apps you want to scan.

## 1. Reproduce the results

Run from the repository root:

```bash
python3 tools/reproduce_scores.py
```

This recomputes every score and table in the Results section from the Status and Weight cells of the workbook, independently of its Excel formulas. Compare your output with the reference copy:

```bash
python3 tools/reproduce_scores.py | diff - expected_output/scores.txt && echo "scores match"
```

| Paper | Reproduces exactly from this repository? |
| --- | --- |
| Table "Scores per app" (Section 4.1) | Yes |
| Table "Recurring barriers by criterion and app" (4.2) | Yes |
| Table "Transaction-level checks by app" (4.4) | Yes |
| The 15 criteria Not Tested in all five apps (4.5) | Yes |
| Table "Weighted and unweighted scores" (4.6) | Yes |
| BK Mobile at 25.8 with authentication treated as Not Tested (4.6) | Yes |
| Table "Score bounds" and its figure (4.6) | Yes |
| Table "Scanner-only scores" (4.6) | Yes |
| Lane A counts, size bands and contrast ratios (3.4, 4.2, 4.3) | Our parser output is in `expected_output/scanner_counts_<app>.txt`. The scanner reports themselves are not released (see below) |
| Status, Notes and Recommendation per criterion | Recorded, not re-run: see `screenshot_reviews/` and `workbook_build/` |

## 2. Collect your own scanner reports

The scanner reports behind the paper are not released, because they quote text from the screens of the author's own bank accounts. Section 5 explains why. You can collect equivalent reports for any Android app with Google Accessibility Scanner, then process them with the same parser.

Your counts will not match ours exactly. Banking apps change often, the screens you can reach depend on your own accounts, and results vary with the device, Android version and scanner version. The paper's scans used a Google Pixel 8 running Android 17, with Accessibility Scanner 2.5.

### 2.1 Install and turn on the scanner

1. Install **Accessibility Scanner** from Google Play. It needs Android 9.0 or later.
2. Open the phone's **Settings** app.
3. Tap **Accessibility**, then **Accessibility Scanner**.
4. Turn on **Use Accessibility Scanner**. A floating Accessibility Scanner button appears on the screen.

### 2.2 Record a session

1. Open the banking app and sign in.
2. Tap the floating Accessibility Scanner button, then tap **Record**.
3. Walk slowly through the six flows used in the paper, pausing on each screen so the scanner captures it:
    1. login (PIN, password or biometric screen);
    2. home dashboard;
    3. send money: to your own account, and to another bank, as far as the confirmation screen;
    4. airtime or bill payment;
    5. transaction history;
    6. customer support or help.
4. To stop, swipe down the notification shade, tap **Accessibility Scanner is recording**, then tap **Stop**.

You don't need to complete a payment. If the app blocks screenshots after login, the scanner still records the accessibility findings, but the screenshots will be black. If one session can't reach every flow, record more sessions and pass them all to the parser together.

### 2.3 Export the results

1. When the results open, tap **Share** and save or send the export to your computer. To export an older scan, tap the floating button, select the scan, then tap **Share**.
2. The export is a zip named like `results_<App>_<timestamp>.zip`. It holds one `screenN.png` (the screen, with flagged elements outlined) and one `reportN.txt` (the findings for that screen) per captured screen.
3. Put the zips in a folder called `scans/` in this repository. `.gitignore` keeps it, and every image and zip, out of version control.

The screenshots will show your name, account numbers and balances. Don't commit or share them.

### 2.4 Run the Lane A parser

Pass every session of one app at once, as zips or unzipped folders:

```bash
python3 tools/parse_scanner_reports.py scans/results_MyBank_*.zip
```

The output gives:

- the number of screens and findings;
- a note if the same screen was captured more than once;
- findings per category, with the WCAG 2.2 criteria each feeds;
- touch-target sizes in three bands (under 24 dp, 24 to 43 dp, 44 dp or larger);
- the lowest contrast ratios and the most frequent colour pairs;
- the most frequent unlabelled elements;
- a warning if every touch-target finding comes from web content, which means a WebView interface where label checks can't be trusted.

`expected_output/scanner_counts_<app>.txt` shows what this output looked like for each app in the paper.

### 2.5 Rate and score

To rate an app the same way:

1. Review each screenshot beside its report using `tools/screenshot_review_checklist.md`.
2. Apply the rating rules in Section 3.6 of the paper.
3. Enter each Status in a copy of the **App Template** tabs of the workbook.

The workbook's formulas compute the scores, and `tools/reproduce_scores.py` can recompute them once you add the tab name to its `APPS` list.

### 2.6 Sharing your own reports (optional)

If you want to publish your reports, `tools/redact_reports.py` copies only the text reports, never the screenshots. It replaces names you give it with `[NAME]`, and replaces long numbers and account endings with `[NUMBER]`. The parser gives the same counts on the redacted copies.

```bash
python3 tools/redact_reports.py redacted/MyBank --name "Your Name" -- scans/results_MyBank_*.zip
```

Read the redacted files yourself before sharing them.

## 3. Repository layout

```
README.md                  This file
EVALUATION_REPORT.md       How every workbook value was produced
LICENSE                    MIT licence for the code
LICENSE-DATA               CC BY 4.0 licence for the data and documents
data/
  Mobile App Accessibility Evaluation.xlsx
                           Ratings workbook: one tab per app, a Transactions tab per app,
                           Comparison Dashboard, Methodology, SC Glossary, App Template
tools/
  reproduce_scores.py      Recomputes every Results table from the workbook
  parse_scanner_reports.py Lane A parser for Accessibility Scanner exports
  screenshot_review_checklist.md   Lane B 12-point checklist
  redact_reports.py        Makes shareable copies of scanner reports
screenshot_reviews/
  <app>.md                 Lane B evidence report returned by the AI reviewer, redacted
  prompts/prompt_<app>.md  Exact prompt each reviewer received
workbook_build/            Code that wrote the ratings into the workbook (record only)
  ratings.py               Status, Notes, Instances and Recommendation per criterion
                           for Equity, Fidelity, GTWorld and AccessMore
  build_workbook.py        Writes ratings.py into app tabs and the dashboard
  verify_scores.py         Python cross-check of the Excel scores
  parse_v1.py, summarize_app.py    First parser and per-app summary used before rating
expected_output/
  scores.txt               Output of reproduce_scores.py
  scanner_counts_<app>.txt Parser output on the paper's original scans
```

The scripts in `workbook_build/` are a record of how the workbook was built. They need `openpyxl` and the original scans to run again, and you don't need them to reproduce the results.

## 4. Known differences

- **Instance counts.** For the 10 criteria that take scanner counts, 35 of the 43 non-blank Instances values in the workbook match the parser output in `expected_output/` exactly. The other 8 were adjusted during rating, mostly where the screenshot review moved findings to another criterion. EVALUATION_REPORT.md, Section 6, lists them. Instance counts don't enter any score.
- **Criterion numbering in the workbook.** Three rows are numbered one place off. The workbook's 3.3.9 Redundant Entry is WCAG 2.2 **3.3.7**, its 3.3.7 Accessible Authentication (Minimum) is **3.3.8**, and its 3.3.8 Accessible Authentication (Enhanced) is **3.3.9**. Names and levels are correct. `reproduce_scores.py` converts to WCAG 2.2 numbers, as used in the paper.

## 5. What is not in this repository

- **Scanner reports and screenshots.** The screenshots show account holders' names, account numbers, balances and, in one case, a Bank Verification Number. The text reports quote on-screen text from the same accounts. Both are withheld; Section 2 explains how to collect your own. The parser's output on the original reports is in `expected_output/`.
- **The account balance in one review report** (Fidelity) was replaced with `[BALANCE]`.
- **NCBA NOW (Kenya).** It was evaluated with the same method but isn't part of the paper, so its tabs, reports and code were removed.
- **Full Claude Code session logs.** The prompts and returned reports are included instead, for four apps. BK Mobile was reviewed by the same process in an earlier session whose prompt and report were not kept.

## Citation

> S. I. Ajayi and E. Umuhoza, "Digital Accessibility and Financial Inclusion: A Scanner-Based and AI-Assisted Evaluation of Mobile Banking Applications for Blind and Visually Impaired Users in Rwanda and Nigeria," *[venue, year]*.

## Licence

- **Code** (`tools/*.py`, `workbook_build/`): [MIT](LICENSE).
- **Data and documents** (the workbook, `screenshot_reviews/`, `expected_output/`, the checklist and this documentation): [CC BY 4.0](LICENSE-DATA). You may reuse and adapt them for any purpose if you credit the paper above.
