# Screenshot review checklist (Methodology, Section 8, Step 3)

Use this prompt with a vision-capable AI model, such as Claude in Claude Code. Run one review per app. Replace the bracketed parts.

---

You are helping with an accessibility audit of a banking app, focused on blind and low-vision users and WCAG 2.2.

- **App:** [app name, bank, country].
- **Scan folder(s):** [path(s)]. Each folder is a Google Accessibility Scanner export. It contains screenN.png screenshots, with flagged areas outlined, and matching reportN.txt findings.
- **Known scanner totals:** [paste the output of parse_scanner_reports.py].
- **Read-only:** do not modify any files.

Open every screenshot together with its report. Then write a factual evidence report of about 900 words at most.

Rules:
- Only state what is visible. Write "not observed" rather than infer.
- Cite the screen number (and session, if there are several) for every claim.

Cover these 12 points:

1. **Screen inventory.** One line per screen saying what it is. Examples: login, home, transfer form, confirm transfer, success, history, settings.
2. **Login and authentication.** Is there a PIN pad, password, OTP, or a biometric option (fingerprint or face icon, or text)?
3. **Transaction forms.**
   - Which fields are there?
   - Are the labels persistent, or placeholder-only?
   - Are saved beneficiaries, a contact picker, or autofill available? These reduce redundant entry.
4. **Confirmation and review.**
   - Is there a review screen before money is sent?
   - Does it show recipient, amount, currency and fee?
   - Is there a success or receipt screen?
5. **Errors and timers.** Quote any error or validation text. Note any OTP or session countdown.
6. **State shown by colour or icon only.** Look at the show/hide balance control, selected chips and tabs, and toggles.
7. **Screen titles and headings.** Are they descriptive?
8. **Gestures.** Look for swipe-to-confirm, sliders and carousels.
9. **Channels.**
   - Support: call, email, chat, WhatsApp.
   - Fraud or dispute links.
   - Language selector.
   - Statement or receipt download.
   - Limits disclosure.
10. **Scanner findings mapped to UI.** For each Item label, Unexposed Text, Item descriptions, worst Text/Image contrast, sub-24dp Touch target and Text Scaling finding, say which visible control it refers to. Flag results that look like artefacts, such as captures taken mid-animation or behind the keyboard.
11. **Currency and amounts.** Which symbol or code is used, and how are amounts formatted? Note any inconsistency.
12. **Other barriers.** Anything else notably good or bad for a screen-reader user. Also note any personal data visible in the screenshots, which must be redacted before publication.

---

## After the review

- Rate each criterion using the rules in Methodology Section 8, Step 4. Cite screen numbers in the Notes column.
- Before publication, spot-check the cited screens for every Fail or Partial that rests on screenshot evidence alone (Step 5).
