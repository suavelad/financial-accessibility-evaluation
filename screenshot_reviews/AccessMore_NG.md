<!-- AI screenshot review (full evidence report), extracted from Claude Code session 1bdedf1c, agent ae9c4ea8e91f1d02d. Model: claude-opus-5-5. Time: 2026-09-25T11:49:37.325Z. May quote personal data visible in the screenshots (e.g. the tester's name): check before sharing. -->

AccessMore (Access Bank Nigeria) evidence report. I viewed all 21 screenshots and read every report. S1 is session 12:40:46 and S2 is session 12:42:56. Coordinates are in original pixels (1080x2400).

**1. Screen inventory**
- S1-1: A "Dangote Refinery IPO is open" promo modal over Access Transfers. Buttons: "SHOW ME LATER", "CLICK HERE", "Don't show me again".
- S1-2: Access Transfers form, "Access Account" tab (the other tab is "Convert FX").
- S1-3: Other Banks Transfers form, with the account-number field being typed in and the keyboard open.
- S2-1, S2-4, S2-7: Splash/logo screen with no text. Scanner: no suggestions.
- S2-2, S2-6, S2-8: Home/dashboard. Balance goes ₦2,041.02, then ₦1,530.27, then ₦1,430.27.
- S2-3: Other Banks Transfers with the account field empty. Limit shows "₦1,000.00 used".
- S2-5: Success screen.
- S2-9: Transaction History.
- S2-10: Support.
- S2-11: Livechat loading, a blank white page with only a blue progress bar.
- S2-12: Tamada chat (web view), showing "Connecting…".
- S2-13: Side/hamburger menu (Account, Transfers, Payment Methods, Bill Payments, Lifestyle, Cards, Loans & Investments, Logout).
- S2-14, S2-15, S2-16: Debit Cards. All three are identical and stuck on a grey skeleton loader with no loading text.
- S2-17: Profile/settings.
- S2-18: Profile with a "Show details" bottom sheet showing BVN, Username and Phone in full.

**2. Login/authentication**
- No login, PIN pad, password or OTP screen was observed. Each time, the splash screen (S2-1/4/7) goes straight to Home.
- S2-17 has toggles for "Biometric Login" (ON), "Auto Login on app start" (ON) and "Biometric Transactions" (OFF, fingerprint icon). S2-18 lists "Change/Reset PIN" and "Change Password".

**3. Transaction forms**
- S1-2 fields: Beneficiary Account Number, a "Mobile Number" alternative button, "₦ Amount", "Narration", and PROCEED.
  - All three text inputs show placeholder text only. The scanner flags each as "Item label" (not readable by screen readers) at [111,1427], [147,1644] and [111,1888], and as 15dp and 23dp touch targets.
- S1-3 / S2-3: A "Bank" dropdown with a persistent label (GTBank Plc), and a floating "Beneficiary Account Number" label that stays visible while typing.
- Saved recipients: yes. There is a "Frequent Beneficiaries" chip (S1-2 "RHEMAWO…", S1-3/S2-3 "[NAME] .") and a "Find Beneficiary" link. S2-5 offers "Save Beneficiary", "Schedule" and "Add 1-Tap Payment".

**4. Confirmation and receipt**
- No review screen before sending was observed. S2-3 goes straight to the S2-5 success screen.
- S2-5 shows "Success" and "Transfer Request Successful". It does **not** show the recipient, amount or fee. It offers "Share Receipt".
- Fees appear only afterwards in S2-9: "COMMISSION … -₦10.00" and "VAT … -₦0.75".

**5. Errors and timers**
- S1-3: The account field has a red border and the red helper text "10 digits required", which is partly hidden behind the keyboard.
- No OTP or session countdown timer was observed.

**6. Balance, colour and toggles**
- Balance eye (show/hide) icons appear on S1-2, S1-3, S2-2 and S2-9, plus a greeting-row eye on S2-2. A share icon sits next to each.
- "Hide Account Balance" is ON in S2-17.
- Toggle state is shown by knob position and teal colour only, with no ON/OFF text visible.
  - S2-17 "Item descriptions": speakable text "ON" is identical for 3 items, which suggests the toggles announce only "ON" with no name.
  - Four toggles are flagged at 46x27dp ([906,898], [906,1085], [906,1273], [906,1460]).
  - The outlines are drawn about two rows off from the visible toggles.
- S2-17 "Unexposed Text": "Biometric Transactions", "Hide Account Balance" and "Transaction Limits" rows have visible text missing from their labels.
- S2-9: Debits are red with a "-" sign and credits are green with no "+". So the sign distinguishes them, not colour alone.
- S1-2 / S2-3: The limit bar uses blue and grey legend squares, and the text says "used" / "remaining".

**7. Titles/headings**
- Descriptive titles: "Access Transfers", "Other Banks Transfers", "Transaction History", "Support", "Debit Cards", "Profile", "Success".
- No title: Home (S2-2, greeting only), the menu (S2-13) and Livechat (S2-11).
- S2-2: The "Recent Transactions" heading is a clickable 19dp target, and no transactions are listed under it.

**8. Gestures**
- S2-2/6/8: A carousel page indicator under the account card (unlabelled, 20x8dp, [514,858]) and a rotating "Featured" banner.
- No swipe-to-confirm or sliders were observed.

**9. Support, fraud, language, limits**
- S2-10: Account Officer, "Chat with Tamada", Access Inflow Details, FAQ, "Report an Issue", Send Feedback, and "Call us" numbers [NUMBER]-7 and [NUMBER]. There is also a "What is new… Click here" link.
- S2-2: Fraud banner "secure the gates! Do not give fraudsters…".
- Not observed: WhatsApp, email, a dispute link, a language selector, statement download.
- Limits are disclosed:
  - S1-2 / S2-3: "Daily Transaction Limit: ₦5,000,000", used/remaining, and "Maximum Transaction Amount: ₦5,000,000.00".
  - S2-17 has a "Transaction Limits" row.

**10. What the findings correspond to**
- **Item type label**
  - "CLICK HERE" is the IPO promo's call-to-action button (S1-1).
  - ", Add 1-Tap Payment" is the S2-5 tile. Its label starts with a stray comma.
- **Item descriptions, empty "" [100,682][173,756]:** the eye (show/hide balance) icon on the home account card. It is duplicated with the share icon at [195,682]. Both are 28dp.
- **Item label (unlabelled)**
  - The S1-2 inputs (see section 3).
  - The S2-2/6/8 carousel dot.
  - S2-12: the whole chat web view [0,132][1080,2208].
  - S2-13: the whole menu drawer.
  - S2-18: the whole details sheet.
- **Unexposed Text**
  - S2-12: "message" (the "Type your message" field).
  - S2-18: "Privacy and Security".
  - S2-17: see section 6.
- **Text contrast**
  - #4887EC / #4886EA on #3F3F3F (2.95–2.98) is the blue icons on grey circles: the balance eye/share buttons (S1-2, S1-3, S2-3, S2-9), the bank dropdown chevron (S1-3), the Loyalty+ "Register" chevron (S2-2), the menu chevrons (S2-13) and the settings row icons (S2-17).
  - #FFFFFF on #FF8200 (2.49) is white text on orange buttons: CLICK HERE (S1-1), PROCEED (S1-2) and CLOSE (S2-5).
  - Others:
    - #FFFFFF on #87B319 (2.47): the success checkmark (S2-5).
    - #F58634 on #FCFCFC (2.45, image contrast): the Featured banner (S2-2).
    - #355487 on #222222 (2.10): the filter icon (S2-9).
    - #E24412 (4.16): Logout (S2-13).
    - Several items at 1.16–1.51: S2-17.
- **Touch targets under 24dp**
  - S1-1: "Don't show me again" (18dp).
  - S1-2/3, S2-3: "Upgrade Now" (15dp), "Find Beneficiary" (18dp), the form inputs (15dp and 23dp).
  - S2-2/6/8:
    - Carousel dot (20x8dp) and Featured "More" (36x19dp).
    - "Recent Transactions" (19dp).
    - 7 Days / 30 Days (24dp).
    - S2-6 only: a 3dp sliver at [542,1095].
  - S2-12: the chat message field (21dp).
  - Borderline, just above 24dp: header icons of 25–33dp (S2-2), filter 26x27dp (S2-9), the Debit Cards account dropdown (26dp, S2-14 to S2-16), and the settings toggles 46x27dp (S2-17).
- **"Web content"** appears only in S2-12, the Tamada chat. Refresh is 31x30dp and cancel is 25x26dp.

**11. Currency formatting**
- The ₦ symbol is used throughout, but spacing varies: "₦2,051.77" (S1-2), "₦ 2,041.02" (S2-2), "-₦ 500.00" (S2-9).
- Decimals also vary: "₦5,000,000" vs "₦5,000,000.00" (S1-2).
- No "NGN" text was observed.

**12. Other points for screen-reader users**
- The S2-9 transaction list uses dense all-caps descriptions ("MOBILE TRF TO GTB…") and a long reference number.
- The S2-14 to S2-16 Debit Cards page never finishes loading and shows no status text.
- The S2-11 Livechat page is blank.
- The S1-1 promo interrupts the transfer flow.
- The S2-18 sheet shows the full BVN and phone number.
- Back buttons have oversized empty tap areas ([53,179][318,255]) that are only 29dp tall.
- S2-10 (Support) had no findings.
