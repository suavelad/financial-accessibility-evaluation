<!-- AI screenshot review (full evidence report), extracted from Claude Code session 1bdedf1c, agent ac3b551aab7056a7a. Model: claude-opus-5-5. Time: 2026-09-25T11:50:10.474Z. May quote personal data visible in the screenshots (e.g. the tester's name): check before sharing. -->

**Fidelity Bank (Nigeria) scan: evidence from all 40 screenshots and reports**

I opened all 40 screenshots and read every report. Totals: 196 Text contrast, 167 Touch target, 1 Image contrast and 0 Item label findings.

**1. Screen inventory**
- 1: Login, blank password. 2: Login while typing, keyboard open, LOGIN button now active. 3: "Logging in" loading dialog.
- 4: Home, balance hidden. 5: Home, balance shown. 7: Home with an Android WhatsApp notification over it (not the app).
- 6, 8, 10, 13, 24, 28: "Transfers" list of transfer types.
- 9: Intrabank Transfer form, empty. 25: "Select Source Account" sheet, rendered blank. 26–27: Intrabank form showing limits.
- 11 and 22: "Select Source Account" sheet on Interbank, blank. 12, 14, 15: Interbank form, empty. 16: "retrieving banks" loading dialog.
- 17: Bank selected. 18: Typing the account number. 19: Form filled, scrolled. 20–21: Form filled. 29: Interbank form, flagged boxes misaligned.
- 30: Airtime form. 31: Bottom sheet containing only "Cancel". 32–33: MTN selected. 34: Product type "Data" with "Plans". 35: Data plan picker. 36: "No saved beneficiary" sheet. 37: New-beneficiary fields.
- 23 and 40: Home. 38: Account tab, Analytics view. 39: Same as 38, flagged boxes misaligned.

**2. Login**
- Username (pre-filled "suave.systems") and password fields (1–3).
- A fingerprint icon sits inside the password field (1–3).
- "Show Password" checkbox, "Forgot Username?", "Forgot Password?", "Sign Up Here" (1).
- LOGIN looks disabled only through dimmed colour (1 vs 2).
- PIN pad, OTP and face ID: not observed.

**3. Transaction forms**
- Intrabank (9, 26): Select source account, Beneficiary Account, Enter Amount, Narration, Additional Information, Save Beneficiary toggle, "Confirm Transfer".
- Interbank (12–21): adds "Select Beneficiary's Bank" and "Enter transaction narration"; button is "PROCEED".
- Labels are grey placeholders while a field is empty (9, 12). Once a field is focused or filled, the label floats above it and stays (17–21, 32–37).
- The source-account dropdown never gets a persistent label. It still reads "Select source account" in 20–21 even with the rest of the form filled.
- The beneficiary name fills itself in from the account number ("[NAME] [NAME] [NAME]", 19). Good.
- Redundant entry is reduced by "Choose saved beneficiaries >>" (9, 12), a "Beneficiaries" dropdown (30), "No saved beneficiary" (36) and "Select from contacts" (37).
- The source-account sheet shows a title but no visible items, although the scanner flagged invisible elements inside it (11, 22, 25).

**4. Confirmation and receipt**
- Not observed. The flow stopped at the filled form (20–21), and no transfer was submitted.
- No review screen with recipient, amount and fee; no success or receipt screen.
- Note: the intrabank button is labelled "Confirm Transfer" (9) but only a form is visible, so it is unclear whether a review step follows.

**5. Errors and timers**
- No validation or error messages were observed.
- Only informational text: "Daily limit on transfer(s) applies over a 24-hour cycle." (6, 9, 12) and the loading messages "Logging in" (3) and "retrieving banks" (16).
- OTP or session countdown: not observed.

**6. Balance toggle, colour-only states, toggles**
- The eye icon sits next to a separate text element, "Show Balance" / "Hide Balance"; the scanner flagged them as two targets (4, 5, 40).
- Instant Payments toggle: good, it has a text status, "Status: Enabled" (6).
- Save Beneficiary (9, 12) and New Beneficiary? (30, 37) toggles show their state visually only.
- The selected network logo is shown only by a green border and a tiny tick (32).
- The active Analytics tab is shown only by green fill (38).
- The active bottom-nav item is dark while the others are light grey (4, 38).
- Expense and Income use red and green, but also have icons and text labels (38).

**7. Titles and headings**
- Header titles are descriptive: "Transfers", "Intrabank Transfer", "Interbank Transfer", "Airtime" (6, 9, 12, 30).
- Sub-headings: "Transfer type", "Transfer to Other Banks", "Favorites", "Features".
- The title stays "Airtime" when Data is selected (34).

**8. Gestures**
- The "Features" promo banner changes on its own (Dangote in 4, Enugu Air in 5), so it appears to be an auto-rotating carousel.
- The account card has a page-dot indicator (4).
- The data plan list scrolls (35).
- Swipe-to-confirm and sliders: not observed.

**9. Support and other channels**
- "Contact" tab on the login screen (1) and "Support" tab in the bottom nav (4); neither was opened.
- Call, email, chat, WhatsApp, fraud or dispute links, a language selector and statement or receipt download: not observed.
- "Transaction History" tile and tab exist (4, 38) but were not opened.

**10. Icon-only controls and the zero "Item label" result**
Icon-only controls visible:
- Bell (4, 6 and every header)
- Profile avatar (4)
- Eye icon (4, 5)
- Back chevron (6, 9, 30)
- Fingerprint icon (1)
- Dropdown chevrons (9, 12)
- Network logos MTN, glo, airtel, 9mobile, vitel, shown as images only (30)
- Card page dot (4)

The zero looks unlikely to be genuine:
- Every touch-target finding carries the "originates from web content" note, so the app appears to be a WebView.
- The scanner flagged the bell, eye, avatar, back arrow and fingerprint for size but never for a missing label. It seems unable to evaluate labels on web content.
- The bell's report entry names its element "cart-btn" (4) instead of giving coordinates. This is an id reused from a template, not a meaningful name.
- The back arrow and bell on screens 6, 8 and 10 were not flagged at all, which suggests they may not be exposed as clickable.

Contrast findings:
- Worst ratio, 1.01 (#1A4EDA on #1A4FDA): the greeting and card-label area on 39–40. Those screens were captured mid-animation (boxes misaligned), so these are probably artifacts.
- Other artifacts: 1.05 and 1.07 (39) and 1.19 (35).
- 1.15 (#F8F7F7 on #E8E8E8, screens 9 and 29) and 1.09 (29): these are blank flagged boxes that do not line up with any visible text. They may be off-screen or mis-positioned elements rather than real text.
- #2DCE5A on #F8F7F7, 1.95:1: green text such as the "Daily limit…" note, "Choose saved beneficiaries >>", "Change Limit >>" and the "Beneficiary's bank" floating label (6, 9, 14, 17).
- White or #F8F7F7 on #2DCE5A, 1.95–2.08:1: the LOGIN, PROCEED, Confirm Transfer and CONFIRM RECHARGE buttons (2, 14, 26, 30).
- #BBC1C7 on #FFFFFF, 1.82:1: inactive bottom-nav labels Account, Services, Support and Profile (4, 23, 38).
- #92949C on #E8E8E8, 2.47:1: placeholder text such as "Select source account" and "Select the account" (9, 14, 30).
- #92949C on #F8F7F7, 2.83:1: "Daily: ₦250,000,000 | Rem: …" (14).
- Account card text: 1.90–2.94:1, including the account number #BFE7CE on #2AB95A at 1.90 (4).

Touch targets under 24dp:
- Login (1): "Forgot Username?" 15dp tall, "Forgot Password?" and "Sign Up Here" 16dp tall, Show Password checkbox 18–20dp.
- Home (4, 5, 40): "Show Balance" text 14–15dp tall, eye icon 18dp.
- Forms (9, 12–20): "Choose saved beneficiaries" 20–21dp tall, "Change Limit" 16–17dp tall.
- Screen 18: a 4dp-tall element.
- Between 24 and 48dp: fingerprint 37dp (1), bell 36×33dp (4), back arrow 43×34dp (9), Save Beneficiary toggle 33–34dp (12), "Select from contacts" 31dp (37), tabs 40dp (38).

**11. Currency and amounts**
- Balance "₦[BALANCE]" (5). The ₦ symbol is a separate element from the number (4, 5).
- Analytics uses "NGN 0" instead (38), so the notation is inconsistent.
- The amount field shows "60,000.00" with no currency symbol (19); airtime shows "0.00" (32).
- Limits: "Daily: ₦250,000,000 | Rem: ₦250,000,000.00" (12) and "₦25,000,000" (26), with inconsistent decimals.

**12. Other points for screen-reader users**
Bad:
- Blank selection sheets with invisible flagged items (11, 22, 25), and a sheet containing only "Cancel" (31).
- The balance is split into separate elements: ₦ symbol, masked digits and label (4).
- Promo banners are image-only text (1, 4).
- Loading dialogs may not be announced (3, 16).
- On screen 12, faint text reading "Select Source Account" is visible behind the form after the sheet closed.

Good:
- Descriptive header titles.
- Beneficiary name confirmed automatically (19).
- Text status for the Instant Payments toggle (6).
