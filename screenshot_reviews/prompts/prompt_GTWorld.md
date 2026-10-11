<!-- Prompt given to the screenshot-review agent, 2026-09-25T11:47:15.141Z, session 1bdedf1c. -->

You are helping with an accessibility research audit (blind/low-vision users, WCAG 2.2) of a banking app. Directory: "<scan folder>/scans/" — use the three subfolders results_GTWorld_2026-09-25-12:36:34, results_GTWorld_2026-09-25-12:38:34, results_GTWorld_2026-09-25-12:42:00. These are Google Accessibility Scanner exports for **GTWorld (Guaranty Trust Bank, Nigeria)**: screenN.png screenshots (with outlined flagged areas) and matching reportN.txt findings (33 screens total). Read-only task: do NOT modify files.

View EVERY screenshot (Read tool on the png) together with its report, then return a concise factual evidence report (max ~900 words). Only state what is visible; say "not observed" otherwise. Cover:
1. Screen inventory: one line per session/screen N — what the screen is (e.g. login, home, transfer form, confirm transfer, success, statement, settings).
2. Login/authentication: PIN pad, password, OTP, biometric option (fingerprint/face icon or text) visible?
3. Transaction forms: which fields; labels persistent or placeholder-only? Saved beneficiaries / autofill (reduces redundant entry)?
4. Confirmation/review screen before sending money: exists? shows recipient, amount, currency, fee? Receipt/success screen, share receipt?
5. Error/validation messages visible (quote text); any OTP/session countdown timer.
6. Show/hide balance eye icon (tvEye), colour-only state indicators, toggles.
7. Screen titles/headings — descriptive?
8. Gestures: swipe-to-confirm, sliders, carousels.
9. Support/help channels (call, email, chat, WhatsApp), fraud/dispute links, language selector, statement/receipt download.
10. For "Item label" (unlabelled) findings — btnNavigation (23x), userAvatar, tvEye, btnFilters, loader, ivShare: what visible controls these are. For "Unexposed Text", "Item descriptions" ("not checked" on text_input_end_icon), "Text contrast" (worst ~1.01, recurring #FFFFFF on #FB5622), "Image contrast" (#3C7D30 on #F9829E): what UI they correspond to. Dark theme?
11. Currency (NGN/₦) and amount formatting.
12. Anything else notably good or bad for a screen-reader user.
Cite session+screen numbers for every claim.
