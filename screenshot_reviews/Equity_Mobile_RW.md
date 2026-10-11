<!-- AI screenshot review (full evidence report), extracted from Claude Code session 1bdedf1c, agent a2fc6fc7a7e6e49a5. Model: claude-opus-5-5. Time: 2026-09-25T11:49:02.812Z. May quote personal data visible in the screenshots (e.g. the tester's name): check before sharing. -->

I viewed all 24 screenshots and read all 24 reports for Equity Mobile (Rwanda). The whole app uses a dark theme: charcoal backgrounds (#221F1F to #454344) with coral/salmon accents (#FF8583-ish) and dark-red account cards (#8F201F).

**Privacy caution for your paper:** the screenshots show the tester's full name and full account numbers (screens 5, 6, 9, 11, 12, 16). Screen 4 also shows a WhatsApp notification with personal group names. Redact these before publishing.

**1. Screen inventory**
- 1: Password login screen with an "Uh oh!" modal saying location permission wasn't granted.
- 2: Password login screen.
- 3: Login loading (spinner).
- 4: Home loading skeleton, covered by a WhatsApp notification.
- 5: Home, scrolled (My balance, Transact/Borrow/Save, My accounts carousel, Forex calculator).
- 6: "Accounts" tab (balance, accounts carousel, "Add existing", "My cards").
- 7: "Transact" hub with the Send money filter selected.
- 8, 10, 12: "Send to your own Equity account" payment form.
- 9: "Pay from" account picker sheet.
- 11: "Send to" account picker sheet.
- 13, 22, 24: "Transact" hub with the All filter selected.
- 14: "Send to another bank" sheet (recipient search, Favourites).
- 15: "Send to a bank account", bank picker (country + bank list).
- 16: Recipient details form (Full name, Account number).
- 17: Payment details form for "Send to a bank account". Its report lists Transact-hub IDs (startIcon, qrCodeIcon, itemParent), so the capture was probably taken mid-transition.
- 18: "Buy airtime" recipient sheet.
- 19: "Buy airtime" payment form.
- 20: "e-Kash limit" dialog over Transact.
- 21: "Send money via e-Kash" recipient sheet.
- 23: "Home" with the "Send money" bottom sheet open.

**2. Login**
- Password field with a persistent "Password" label, placeholder "Enter password", a show/hide eye icon and "Forgot your password?" (2, 3).
- Biometric option "Sign in with Touch ID" with a fingerprint icon (1, 2).
- The "Let me in" button appears disabled (grey) (2).
- PIN pad and OTP: not observed.

**3. Transaction forms**
- Own-account form (8, 10, 12): Send from, Send to, Currency (RWF dropdown), amount, Payment reason. Labels are persistent above the fields.
- The amount field has no label of its own, only the placeholder "Enter an amount", sitting beside the Currency label (8, 12, 17, 19).
- Payment reason uses the placeholder "Optional" under a persistent label.
- Bank recipient form (16): "Full name" and "Account number" show only as placeholder text on underlines.
- e-Kash (21): a single placeholder-only field, "Enter recipient account or phone numb", truncated.
- Airtime (18): "+250" country code dropdown, "Mobile number" field, Submit button.
- Features that reduce re-entry: contact-book icon (18, 21), "Search for a recipient/contact" (14, 18, 21), Favourites (14, 18, 21), Recents (18), Phonebook (21), and the bank search/list (15). All of these were empty in this account ("0 Favourites found", "No contacts found").

**4. Confirmation and receipt**
- Not observed. No review, confirmation, success or receipt screen was captured, so fee display cannot be assessed.
- The source account shows masked digits plus "Available balance 0.00 RWF" (8, 17, 19).

**5. Errors, validation and timers**
- 1: "Uh oh! Location permission has not been granted. This will affect the smooth working of the application" [Dismiss].
- 20: "e-Kash limit — You can only send up to 10M RWF with e-Kash. For higher amounts, use 'Another bank' instead. Would you like to continue?" [No, use Another bank] [Yes, continue].
- Inline field validation: not observed.
- OTP or session countdown timer: not observed.

**6. Balance visibility, colour-only states and toggles**
- "Show balance" plus an eye icon (5, 6, 23). The showBalanceText target is only 18dp tall (5, 6).
- Account balances on the cards are visible anyway ("0.00 RWF", "0.00 USD") (5, 6).
- Colour/shape-only indicators:
  - Forex rates: "To Buy" in green with an up arrow, "To Sell" in red with a down arrow (5).
  - Filter chips: the selected chip differs only by a coral outline and text colour (7, 13).
  - Carousel page dots (5, 6).
  - Radio buttons: all are announced as "not checked", identical for 6 items (15, report 15).
- Toggles: not observed.

**7. Titles and headings**
- Generally descriptive: "Transact", "What would you like to do?", "Send to your own Equity account", "Please enter the payment details", "Please select the recipient's bank", "e-Kash limit", "Home", "Accounts".
- Page titles are duplicated on sheets, e.g. the "Send to a bank account" header is repeated behind the sheet (15, 16).

**8. Gestures**
- Horizontal account-card carousel with page dots (5, 6).
- Horizontally scrolling filter chips; "Pay to merchant code" is cut off at the edge (7, 13).
- Swipe-to-confirm and sliders: not observed.

**9. Support and other channels**
- A chat-bubble icon, top right on login (1–3), apparently for chat or support. It was not flagged.
- Call, email, WhatsApp, fraud/dispute links, language selector, statement download: not observed.
- "Schedule Payments / Manage here" (13).
- "Add existing: bank account, card, mobile wallet or PayPal" (6).

**10. Scanner findings mapped to UI**

Item label (no screen-reader label):
- Popup close X (crossBackground): 1, 20.
- Back arrow at [0,142][147,289]: 8, 10, 12, 19.
- Sheet close X / back at [0,250][147,397]: 9, 11, 14, 15, 16, 18, 21.
- Currency dropdown (currencyClick): 8, 10, 12, 19.
- Card list: 11.
- Profile avatar "AS" (startIcon), QR scanner icon (qrCodeIcon) and notification bell (imgNotifications): 5, 6, 7, 13, 17, 22, 24.
- Carousel expand button (layoutExpandButton) and account "…" menu (accountActions): 5, 6.
- Scroll bar: 4.
- Send-money sheet close X (close / crossForeground, 24dp): 23.

Unexposed Text:
- Account number and "Savings Account" text on the account card (linkAccount), and "RWE", which is likely an OCR misread of "RWF" (cardsDescription): 5.
- "View" (shortCutView): 6.
- "Currency" (sendTitle): 17.

Item descriptions (duplicate labels):
- "Home" on the EQUITY centre button (equityHomeFab): 6.
- "Buy airtime" used twice: 19.
- Radio buttons all "not checked": 15.

Worst text-contrast ratios (the 1.0x ratios are mostly on overlapping cards in the carousel, which the scanner itself flags for manual checking):
- 1.04 iconText (#912422 on #8F201F): 6.
- 1.12 iconText: 6.
- 1.13 itemText / showBalanceText (#821A1A on #8F201F): 5, 6.
- 1.15 myBalance: 6.
- 1.24 accountNumber (#413F3F on #333131): 6.
- 1.41 "View all": 6.
- 1.67 cardName: 6.
- Near misses: 4.44 on login grey text (#938F99 on #2D2B2B), 2; 4.45 accountName (#FF8583 on #413F3F), 5.

Worst image contrast:
- 1.01 QR icon: 6.
- 1.02 accountActions: 5.
- 1.08–1.23 shortcut icons: 6.
- 1.45 item icons: 17.
- 1.47 red loading spinner (#8E2C1F on #373535): 3.

Text Scaling (fixed-height containers):
- "Let me in": 2.
- Bottom nav: 4, 5, 6.
- Balance/account cards: 5, 6.
- Shortcut labels: 6.
- Transact tiles (itemParent): 7, 13, 17, 22, 24.
- sendAction button: 8, 10, 12, 19.
- Bottom sheets: 9, 11, 14, 15, 16, 18, 21.
- Search fields, addBeneficiary, chooseCountryCode: 14, 15, 18, 21.

Touch targets:
- 24–32dp for icons and close buttons.
- 41–43dp for dropdowns and bottom-nav items.
- 32dp for Payment reason.

**11. Currency and amounts**
- RWF is the primary currency; the second account is USD.
- Format is "0.00 RWF" / "0.00 USD", with the code after the number and two decimals (5, 6, 8, 9).
- Forex: "USD 1 ⇄ RWF 1471.0", "To Buy 1USD 1471.0", "To Sell 1USD 1481.0" (5).
- Airtime uses the "+250" prefix (18).

**12. Other points for screen-reader users**

Good:
- Persistent labels on most dropdowns.
- Selected radio shows a checkmark shape, not colour alone (9).
- Plain-language limit dialog with clear choices (20).
- Account numbers masked on forms.

Bad:
- Unlabelled back/close buttons on nearly every screen.
- Unlabelled QR, notification and avatar icons in the persistent header.
- Disabled buttons (Continue, Let me in, Submit) are low-contrast grey (2, 8, 16, 18).
- The dimmed location modal appears at launch, before login (1).
- The truncated placeholder is the only label on the e-Kash field (21).
- Redundant duplicate entry points: Send money appears as both a Home sheet and a Transact tile (13, 23).
