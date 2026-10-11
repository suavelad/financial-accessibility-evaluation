<!-- Prompt given to the screenshot-review agent, 2026-09-25T11:47:06.702Z, session 1bdedf1c. -->

You are helping with an accessibility research audit (blind/low-vision users, WCAG 2.2) of a banking app. Directory: "<scan folder>/scans/results_Fidelity_2026-09-25-12:46:10" — this is a Google Accessibility Scanner export for the **Fidelity Bank (Nigeria) mobile app**: screenN.png screenshots (with outlined flagged areas) and matching reportN.txt findings (40 screens). Note: every touch-target finding says the item "originates from web content", and the scanner reported zero "Item label" findings — so this appears to be a hybrid/WebView app; assess whether that zero looks genuine or whether icon-only controls exist that the scanner may not have been able to evaluate. Read-only task: do NOT modify files.

View EVERY screenshot (Read tool on the png) together with its report, then return a concise factual evidence report (max ~900 words). Only state what is visible; say "not observed" otherwise. Cover:
1. Screen inventory: one line per screen N — what the screen is (e.g. login, home, transfer form, confirm transfer, success, statement, settings).
2. Login/authentication: PIN pad, password, OTP, biometric option (fingerprint/face icon or text) visible?
3. Transaction forms: which fields; are labels persistent or placeholder-only? Saved beneficiaries / autofill (reduces redundant entry)?
4. Confirmation/review screen before sending money: exists? shows recipient, amount, currency, fee? Receipt/success screen?
5. Error/validation messages visible (quote text); any OTP/session countdown timer.
6. Show/hide balance eye icon, colour-only state indicators, toggles.
7. Screen titles/headings — descriptive?
8. Gestures: swipe-to-confirm, sliders, carousels.
9. Support/help channels (call, email, chat, WhatsApp), fraud/dispute links, language selector, statement/receipt download.
10. Icon-only controls visible (bell, back arrow, QR, etc.) that would need labels. For "Text contrast" findings: which UI (esp. the worst ratios ~1.01 and the recurring #2DCE5A on #F8F7F7, #BBC1C7 on #FFFFFF, #92949C on #E8E8E8 pairs) and for small touch targets (<24dp): which controls.
11. Currency (NGN/₦) and amount formatting.
12. Anything else notably good or bad for a screen-reader user.
Cite screen numbers for every claim.
