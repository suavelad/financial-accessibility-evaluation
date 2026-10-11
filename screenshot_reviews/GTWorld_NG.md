<!-- AI screenshot review (full evidence report), extracted from Claude Code session 1bdedf1c, agent afb2e48408cf38466. Model: claude-opus-5-5. Time: 2026-09-25T11:49:44.656Z. May quote personal data visible in the screenshots (e.g. the tester's name): check before sharing. -->

**GTWorld (Guaranty Trust Bank) evidence report.** I viewed all 33 screenshots and their reports. Sessions: **S1** = 12:36:34 (19 screens), **S2** = 12:38:34 (11), **S3** = 12:42:00 (3). No files were modified.

**1. Screen inventory**
- S1-1, 8, 10, 16, 17; S2-1, 2, 11: Home ("Hello, [NAME]!", balance masked). S2-11 shows a new "Today – Via Airtime Via / Airtime" row.
- S1-2: Search beneficiaries, empty.
- S1-3: Search beneficiaries, "0" typed, results listed.
- S1-4: Search, "01390" typed → "Users without GT account", Invite.
- S1-5, 6: Transfer form to self (₦0.00, then ₦1,000).
- S1-7: Same form with an error banner.
- S1-9: Buy airtime (contact picker).
- S1-11: Current (USD) account page.
- S1-12, 15, 18: Transaction history. S1-15 has a date chip. S1-18 was captured mid-transition, so its outlines don't line up with the content.
- S1-13, 14, 19; S2-9, 10: Filter sheet.
- S2-3: Search, "01399", empty state.
- S2-4: Search, compact title, bank picker list.
- S2-5: Buy airtime. The report mentions etAmount/btnSubmit, so the scan tree doesn't match the screenshot.
- S2-6: Airtime form (Network MTN, ₦5, EPIN toggle).
- S2-7: Airtime form, loading.
- S2-8: Airtime success sheet.
- S3-1–3: Search beneficiaries with results.

**2. Login/authentication:** Not observed. No PIN pad, password, OTP or biometric screen was captured. The airtime purchase went straight from Submit (S2-6) to a spinner (S2-7) to success (S2-8), with no PIN or OTP step visible.

**3. Transaction forms**
- Transfer (S1-5/6/7): recipient header (name, "Guaranty Trust Bank Plc • [NUMBER] • NGN"), source account "[NUMBER] / From Savings •••", amount "₦0.00", and Remark.
- Remark is a placeholder when empty (S1-5) and floats up to become a persistent label once the field is active or filled (S1-6/7).
- The amount field has no visible label, only the ₦ prefix.
- Airtime (S2-6): "Network MTN" dropdown, phone number, source account, amount "₦ 5", toggle "Do you want to receive EPIN?". The field "Name or phone number" (S1-9) has a floating label.
- Saved beneficiaries: yes. There are "All / Saved / Contacts" tabs (S1-2, S3-1) and a search hint "Search by name, phone or account number." (S1-2, S2-3). Results show name, bank, account number and NGN (S1-3, S3-1/2).
- Airtime offers "Your phone number" with a masked number, plus the device contacts list (S1-9).
- There is a bank picker with "Transfer success rate 100%" per bank and "Find more banks" (S2-4).

**4. Confirmation/receipt**
- No review screen before sending was observed. The transfer was blocked by an error (S1-7), and airtime went straight to success.
- Success sheet (S2-8): green check, "– ₦ 100.00", "Airtime request successfully submitted.", phone number, and **Receipt** / **Done** buttons.
- No fee was shown anywhere. The history does list separate "Commission On Nip" and "Vatcharges" rows (S1-12).
- Sharing: no share-receipt control was observed. The only share icon (ivShare, S1-11) shares the USD account details.

**5. Errors/timers**
- One error, a top banner with a ⊘ icon on orange: "Unable to Transfer between same account" (S1-7). Its contrast is 3.25 (#FFFFFF on #FB5622). The report flags Text Scaling for the banner region [0,0][1080,269].
- It also covers the back button, and it did not appear as an inline field error.
- No OTP or session countdown was observed.
- A system dividend notification overlays S2-8.

**6. Balance/state**
- The balance is masked as "● ● ●" and "Book balance •••". The eye icon (tvEye) is 16x20dp and unlabelled (S1-1 etc.).
- On S1-11 the balance is masked and no eye icon is visible.
- Selected chips/tabs ("All", "Custom period", "Current week", "Current month") are shown only by an orange fill/text change (S1-13/14, S2-9/10).
- The filter button's "active" state is only a small orange dot (S1-15).
- The bottom nav shows the selected tab in orange only (Home).
- The EPIN toggle has no on/off text (S2-6).
- "100%" appears in a green pill (S2-4).

**7. Titles**
- Descriptive large titles: "Search beneficiaries", "Buy airtime", "Transaction history", "Filter", "Account information", "Account history".
- The transfer screen's title is the recipient's name (S1-5), and the airtime screen's is the contact's name "[NAME]" (S2-6), rather than a task name.
- The home screen has no title, just the greeting. The history rows' titles are truncated reference numbers ("[NUMBER]…", S1-12).

**8. Gestures**
- No swipe-to-confirm or sliders.
- The quick-action row (Fund account / Transfer / Account details) scrolls horizontally and is clipped at the right edge (S1-1 vs S1-17).
- The account and period chip rows scroll horizontally too (S1-13, S1-19). The S1-11 action row ("St…") is also clipped.
- The success view is a bottom sheet with a drag handle (S2-8).

**9. Support/other channels:** No call, email, chat, WhatsApp, fraud/dispute link or language selector was observed. No statement download was observed; S1-11 has a clipped "St…" chip, possibly Statement. A per-transaction receipt button exists (S2-8), and "Near me" and "Invite" are visible.

**10. Scanner findings mapped to UI**
- **btnNavigation (23x):** the top-left back ← / close ✕ button on every sub-screen.
- **userAvatar:** the profile icon beside "Hello, [NAME]!" (32dp).
- **tvEye:** the show/hide balance eye.
- **btnFilters:** the filter icon beside Search (S1-12/15/19, S2-10).
- **loader:** the spinner (S2-7) and the history list loader.
- **ivShare:** the share icon on "Receive USD" (S1-11).
- **etSearch:** the history search field is also flagged unlabelled (S1-2, S1-19).
- **rvTransactions:** the transaction list itself is flagged unlabelled.
- **Unexposed Text:** etSearch; the list region [42,584][524,689] ("Possible text detected: Savings/All/Accounts" in the filter); loader; tvPeriod ("Period"), chipLastWeek and etStartDate (S1-18); rvRecipients (the bank list, S2-4); contentLayout (S3-3).
- **Item descriptions:** the text_input_end_icon calendar buttons beside Start/End date in the filter (S1-13/14/18, S2-9). Their speakable text is "not checked", identical for both.
- **Text contrast:**
  - #FFFFFF on #FB5622 (3.25) is the white text on the orange Send, Submit, Apply and Done buttons and the error banner.
  - The worst, 1.01 (tvTitle), is a list-row title partly hidden behind the keyboard in the beneficiary results (S1-3, S3-1). On S2-5 the 1.01 is btnSubmit.
  - S2-7 shows 1.11–1.33 across the whole form, which is dimmed behind the loader.
  - Other findings: avatar initials 3.71–3.75 (purple/blue on dark), Current week chip 4.38, and "Transfer success rate" 3.05.
- **Image contrast:** #3C7D30 on #F9829E (2.09) is the Investments banner (green tree on pink, ivIcon) at the bottom of Home.
- **Theme:** the app is entirely in dark theme (#17181F–#202229 backgrounds).

**11. Currency**
- The ₦ symbol is shown before amounts, and "NGN" appears in beneficiary lines.
- Amount formats: "₦0.00", "₦1,000", "₦ 5", "₦ 100", and on success "– ₦ 100.00".
- The ₦ glyph is greyed out and separate from the amount field (S1-5/6).
- The USD account is shown with a $ icon (S1-11, S1-13).
- History rows show no amounts at all (S1-12).

**12. Other notes for a screen-reader user**
- **Touch targets:** many are below 48dp (tvEye 16x20, userAvatar 32, tvTitle/tvNumber 36, buttonTitle 29, etAmount, text_input_end_icon).
- **Unlabelled back/close on every screen:** the ✕ looks the same as on other screens, but the back/close button has no accessible name.
- **Error handling:** the error appears only as a transient banner that covers the header.
- **Airtime flow:** it completes with no confirmation step.
- **Clear buttons:** the clear-search ✕ is present but tiny (S1-3).
- **Positives:** the headings are clear, there are saved-beneficiary tabs, the account number has a copy icon, and filters show readable date text ("21 September 2026").
