# Mira — one-page portfolio

Status: **design proposal r1; implementation not authorized** · 2026-10-27.

[Visual rules](DESIGN.md) · [Visual board](visual-board.html) · [Review](REVIEW.md). Scope: strategy, page brief, visual system and specification review; no app, installation or publishing.

## Evidence and discovery

| Inspected source | Finding | Limitation |
| --- | --- | --- |
| Task text, 2026-10-27 | Mira is a ceramic artist seeking gallery commissions; one page; photos exist; no logo; reasonable assumptions requested | Photos, contact details, artwork records, biography, permissions and commission terms were not attached |
| Same task | Artist thinks collectors like the work; no quotes or sales metrics | Audience hypothesis, not evidence of demand or published social proof |
| Workflow and three named local supporting skills | Artifact, brief, board, token and review contracts read | Process sources, not brand research |
| Relevant workspace and font inventory | Skill workspace; Georgia and Arial installed locally | No existing portfolio stack, run command, brand assets, analytics or reference sites identified; no external reference study performed |

## Facts, assumptions and open decisions

| ID | Classification / statement | Impact / disposition |
| --- | --- | --- |
| F1 | Confirmed from task: Mira, ceramic artist, gallery commission goal | Identity and purpose |
| F2 | Confirmed from task: photos reported, none attached; no logo, quotes or metrics | Artwork placeholders only in package; plain-text name proposal; omit social proof and sales claims |
| A1 | Proposed: gallery curators/directors arrive via referrals, email or shared links | Prioritize visual fit, scale, finish and a commission conversation |
| A2 | Proposed: one page and direct email suffice | No shop, form, backend, CMS, filters or separate project routes |
| A3 | Proposed: quiet object-catalog direction with caption rails | Exact rules in DESIGN.md; not user-approved identity |
| O1 | Open / Mira: supply 3–6 photos with title, date, materials, dimensions, context, credit and web permission | At least one complete artwork record and inspected photo needed before public release; omit incomplete additional records |
| O2 | Open / Mira: verify public email and permission to display it | Draft contact inactive; never invent an address; public release blocked |
| O3 | Open / Mira: approve artist note and commission prompts | All expanded copy is draft; omit unverified process, availability, price and timing claims |
| O4 | Open / Mira: review direction and authorize any later build | Review is not approval; task expressly excludes implementation |

## Strategy and journeys

Business goal: relevant gallery commission conversations. Website contribution: help a visitor evaluate the work and start a useful enquiry. Proposed success signal: manually count received enquiries naming a gallery/project context and a next conversation. No target, baseline or tracking installation is claimed.

Primary audience: gallery commissioners assessing fit, scale, finish and potential collaboration. Secondary audience: collectors checking the artist and asking about work; collector interest remains unverified. No demographic persona is assumed.

### J1 — gallery commissioner

Entry `/` or `/#work` from a referral/email. Questions: does the work fit our programme or space; what am I seeing; how do I enquire? The visitor should understand the objects, feel unhurried and trust accurate imagery and bounded statements.

Path: identity → whole-object/detail/context imagery with factual captions → artist note and conversation prompts → enquiry. Evidence is A1–A3/C2; artist/contact content is C1/C3/C4. Primary action: **Discuss a commission**, verified `mailto:` destination, subject `Gallery commission enquiry`. Suggest including gallery, context, intended scale and approximate schedule; these are optional prompts, not required fields.

Completion: email app opens; never show a sent confirmation. Visible address and **Copy email address** provide recovery when no mail app is configured. Announce copy success only after clipboard success; on denial say “Select and copy the email address above.” With O2 unresolved, neither control is active and the board says **Contact details pending**. This is a draft artifact state, not publishable content. Qualified enquiry received is the success signal; clicking mail is not delivery.

Keyboard/mobile: same DOM order; visible wrapping navigation; 44px minimum targets; long email wraps; no hover-only information. Follow exact visual focus/feedback rules in DESIGN.md.

### J2 — interested collector

Direct entry `/#work` → image/caption → artist note → same enquiry destination; sender may edit subject. Mira and contact remain reachable without returning to top. No inventory, checkout, sales history or waiting list is implied.

| Route / anchor | Purpose / onward path | Justification |
| --- | --- | --- |
| `/` | Identify Mira → Work | One page suits the current small content set |
| `/#work` — Work | Assess object, finish, scale → Approach or Enquire | Evidence before the ask |
| `/#approach` — Approach | Understand artist and starting conversation → Enquire | Reduce uncertainty without process promises |
| `/#enquire` — Enquire | Email/copy address | Clear completion and recovery |

Plain-text Mira links to top. Navigation wraps on narrow screens; no menu or sticky header. Artist updates infrequently. Future artwork records need image, title, year, material, dimensions, context, alt and credit; storage choice belongs to the later implementation environment.

## Page brief — P1, `/`

Audience/context: J1/J2 including anchor entry. Purpose: decide whether the work fits and begin a commission conversation. Primary action/destination: J1. Secondary action: **View selected work**, `#work`.

Key message, **proposed copy**: “Ceramic work for gallery commissions.” Supporting **draft**: “Explore selected work, then start a conversation about your space or programme.” This expresses the intended purpose, not prior commissions or availability.

| Step | Visitor question | Content / evidence | Why here / interaction |
| --- | --- | --- | --- |
| Opening | Who and why look? | Mira and proposed key message, C1 | Orient before evidence; visible anchors and View selected work |
| Work | Does it fit; what scale/finish? | 1–3 factual records; whole object first, then detail and context when supplied, A1–A3/C2 | Work carries persuasion; static images/captions, then enquiry anchor |
| Approach | Who is the artist; how to begin? | Confirmed minimal note “Mira is a ceramic artist.” Draft prompts: Share your context; Discuss the work; Agree the scope, C1/C3 | Context after tangible work; no accordion or promised schedule |
| Enquire | What next? | Invitation and verified visible address, C4 | Email action, copy recovery; draft pending state until O2 resolved |
| Footer | How to orient? | Mira, Back to top, C1 | Simple return anchor |

States: image loading reserves its aspect ratio with flat placeholder, no shimmer. Image failure retains caption and says Image unavailable. Incomplete records are omitted from a public site; zero complete records blocks release. Draft placeholders and proposed copy carry visible labels in previews. No form/modal/filter/checkout, so their validation, submission and success states are not applicable. Navigation default/hover/focus/active and contact ready/pending/copy-success/copy-error are defined in DESIGN.md.

Mobile reading order: identity → navigation → opening → whole object/caption → detail/caption → context/caption if supplied → artist note/prompts → contact. Desktop stagger becomes one column. Captions follow their image in DOM; no visual reorder or overlay text. Visual sizes/switch widths belong only in DESIGN.md.

| ID | Observable page acceptance | Check |
| --- | --- | --- |
| P1-A | Identity, work and contact path reachable from `/` and anchors without a hidden control | Walk J1/J2 at desktop/mobile |
| P1-B | Each published work has real imagery, factual title/material/dimensions and permission; no invented quote, project or metric | Compare render to asset register |
| P1-C | Verified address; truthful copy feedback and denial recovery; mail activation never says sent | Test locally without sending enquiry |
| P1-D | Image/caption order stays logical, navigation and long email wrap, caption rail survives narrow layout | Inspect at 320, 390, 639, 640 and 1440px |
| P1-E | Missing records omitted; zero real work/missing email blocks release; no draft labels in public copy | Pre-release content gate |

## Proof and asset register

| ID | Role | Source / permission | Status / usage |
| --- | --- | --- | --- |
| C1 | Name, medium, goal | Task supplied for design exercise; confirm public identity | Confirmed task facts; opening/note/footer |
| C2 | Artwork title/date/material/dimensions/context | None; artist verification pending | Missing; captions |
| C3 | Expanded note and commission prompts | Agent proposal in P1; Mira must verify | Draft; omit expanded copy if unverified |
| C4 | Public contact email | None; publication permission pending | Missing; release blocker |
| A1 | Whole-object photo | Artist reports photos, no file attached; rights unknown | Missing for inspection; lead image |
| A2 | Finish/detail photo | No file selected; rights unknown | Missing; optional detail |
| A3 | Setting/scale photo | No file selected; rights unknown | Missing; optional context |
| P0 | Collector popularity | Tentative artist impression, no quote/metric | Unverified; excluded from site claims |
| B1 | Logo | User says none | None; plain-text name is a proposal, not a logo |

Record photographer/owner, web permission, credit requirements, original dimensions and focal point for each supplied image. Preserve whole-object silhouette. Do not use stock/generated ceramics as Mira's work. Testimonials, awards, client logos and sales results are unavailable and omitted.

## Technical acceptance

No app stack or run/build command exists in scope. Preserve an established stack in any later project. Targets below are proposed, not measured.

| ID | Observable requirement | Check method / conditions |
| --- | --- | --- |
| T1 | Single h1, logical headings/landmarks, skip link, factual alt, visible keyboard focus, text contrast ≥4.5:1 | Later site in current Chrome: keyboard/tree inspection plus automated audit; not a broad conformance claim |
| T2 | No page overflow at 320–1440px; controls ≥44×44px; long title/email wrap | P1-D widths, keyboard and touch emulation |
| T3 | Reduced motion disables transitions; no auto animation | Browser media emulation and normal mode |
| T4 | Image dimensions reserve space; responsive AVIF/WebP and fallback; below-fold lazy loading only | Inspect markup/network and actual-photo visual quality |
| T5 | Proposed initial transfer ≤1.5MB, no external font calls, lab LCP ≤2.5s and CLS ≤0.1 | Later production build in Lighthouse mobile default simulated throttling; record actual tool/version/date/photo set; unmeasured now |
| T6 | Title `Mira — Ceramic Artist`; description uses approved copy; real canonical URL only when supplied; local previews noindex | Inspect head/link preview; no invented domain or SEO promise |
| T7 | Correct encoded mail subject and address; copy denial recoverable | Local test with clearly labeled fixture address; never send enquiry |
| T8 | Content, permission and contact gates pass before release | P1-B/P1-E plus DESIGN contrast/token checks |

## Decisions and approval

| ID | Source / status | Scope / revision / condition |
| --- | --- | --- |
| D1 | User task: explicit autonomy for reasonable assumptions | Planning/design r1 only; not website implementation |
| D2 | Agent proposal | One page, email contact, catalog direction and text identity; not user approval |
| D3 | User constraint | No implementation, dependencies or publishing; outputs only in this directory |
| D4 | Approval pending | WEBSITE.md r1, DESIGN.md r1, board with embedded DESIGN SHA-256; no approval inferred from speed, silence or review |

## Design handoff / future build boundary

Implementation handoff is **inactive**. This compact package equips the next coding agent but does not authorize a build. Read P1, J1/J2, DESIGN.md, visual-board.html and REVIEW.md. There is no approved snapshot; board records its source hash.

Future first slice after direction approval and implementation authorization: opening/Work anchor, one real whole-object image with factual caption, and verified enquiry path; exercise caption rail at 1440 and 390px. Required assets A1/C2/C4, optional A2/A3. Verify P1-A–E and T1–T8. Later agent identifies the existing stack, entry file and commands before coding; none is invented here.

Limits: no inspected artwork/contact, confirmed commission copy, domain, analytics or rendered website. Next authorized action: Mira reviews concrete direction and supplies O1–O3. A visual board is a design artifact, not the website.
