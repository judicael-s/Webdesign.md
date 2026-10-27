---
{
  "version": "alpha",
  "name": "Mira — Object Catalog",
  "description": "Proposed visual system r1; planning artifact, not approved identity.",
  "colors": {"primary": "#7D3F2F", "background": "#F5F1E8", "surface": "#E8E1D5", "text": "#25241F", "muted": "#5F5D55", "inverse": "#FFFDF8", "line": "#C9C2B5", "actionHover": "#5E2E22", "actionActive": "#452219"},
  "typography": {"display": {"fontFamily": "Georgia, 'Times New Roman', serif", "fontSize": "64px", "fontWeight": 400, "lineHeight": 1.05, "letterSpacing": "-0.035em"}, "displayMobile": {"fontFamily": "Georgia, 'Times New Roman', serif", "fontSize": "44px", "fontWeight": 400, "lineHeight": 1.08, "letterSpacing": "-0.025em"}, "section": {"fontFamily": "Georgia, 'Times New Roman', serif", "fontSize": "32px", "fontWeight": 400, "lineHeight": 1.15, "letterSpacing": "-0.02em"}, "body": {"fontFamily": "Arial, Helvetica, sans-serif", "fontSize": "16px", "fontWeight": 400, "lineHeight": 1.5, "letterSpacing": "0em"}, "caption": {"fontFamily": "Arial, Helvetica, sans-serif", "fontSize": "14px", "fontWeight": 400, "lineHeight": 1.45, "letterSpacing": "0em"}, "label": {"fontFamily": "Arial, Helvetica, sans-serif", "fontSize": "12px", "fontWeight": 400, "lineHeight": 1.4, "letterSpacing": "0.08em"}},
  "rounded": {"square": "0px"},
  "spacing": {"xs": "8px", "sm": "16px", "md": "24px", "lg": "48px", "xl": "96px"},
  "components": {"button": {"background": "{colors.primary}", "color": "{colors.inverse}", "typography": "{typography.body}", "borderRadius": "{rounded.square}", "minHeight": "44px", "paddingInline": "{spacing.md}"}, "buttonHover": {"background": "{colors.actionHover}", "color": "{colors.inverse}"}, "buttonActive": {"background": "{colors.actionActive}", "color": "{colors.inverse}"}, "buttonPending": {"background": "{colors.surface}", "color": "{colors.muted}", "minHeight": "44px"}, "textLink": {"color": "{colors.primary}", "typography": "{typography.body}"}, "focusRing": {"color": "{colors.primary}", "width": "3px", "offset": "4px"}, "captionRail": {"color": "{colors.muted}", "borderColor": "{colors.line}", "borderWidth": "1px", "typography": "{typography.caption}", "paddingTop": "{spacing.sm}"}, "photoPlaceholder": {"background": "{colors.surface}", "color": "{colors.muted}", "typography": "{typography.caption}"}, "navigation": {"color": "{colors.text}", "typography": "{typography.body}", "minHeight": "44px", "gap": "{spacing.md}"}}
}
---

## Overview

Proposed r1, not user-approved. [Brief and approval record](WEBSITE.md#decisions-and-approval) · [Board](visual-board.html). Thesis: let a gallery commissioner assess physical work through generous object space and precise catalog captions, then reach a direct enquiry. The tone is quiet and factual. No brand reference sites or artwork were inspected. This is a project-grounded proposal, not a reference study.

Signature device: a numbered caption rail, separated from each image by a single rule. Index occupies 44px; metadata occupies the remainder. Use on artwork only, never as decoration under every heading. Plain text “Mira” is a temporary name treatment, not a designed logo or invented brand identity.

Front matter uses JSON syntax, a valid YAML 1.2 subset, for deterministic standard-library parsing. Recognized schema groups follow the local contract for Google's alpha DESIGN.md format. Component property names beyond standard tokens are workflow CSS mappings, not guaranteed official exports. No official CLI is installed; no official linter pass is claimed.

## Colors

Background is warm paper; surface is only a placeholder/contact-pending layer; text is near-black; primary is restrained oxide for actions and focus, not a background wash. Muted supports captions. Line is decorative only: never the sole boundary of an input or state. No gradients, transparency, image text overlays or color-only status.

Calculated sRGB contrast of exact token pairs (not an audit of a finished page):

| Foreground / background | Ratio |
| --- | --- |
| text / background | 13.79:1 |
| muted / background | 5.85:1 |
| muted / surface | 5.08:1 |
| primary / background | 7.10:1 |
| inverse / primary | 7.87:1 |
| inverse / actionHover | 10.93:1 |
| inverse / actionActive | 13.81:1 |

These pairs exceed 4.5:1. Do not use muted on primary or line as readable text. Primary focus outline is drawn on background with a 4px gap; button labels use inverse. Hover/active retain inverse. Pending labels use muted on surface without opacity reduction.

## Typography

Display maps to the opening h1; section maps to section titles; body to prose/navigation/actions; caption to artwork metadata; label to sparse index/draft annotations. Use displayMobile below 640px, display otherwise. Body measure is at most 62ch; opening h1 at most 16ch. Headings wrap naturally, no forced line breaks, ellipsis or fixed heights. Long titles wrap and grow their caption.

Georgia and Arial are installed Windows system fonts used for this board. Do not redistribute font files. The complete fallback stacks are in tokens; no font downloads or licensing assumptions. Other systems may render Times New Roman/Helvetica or generic families. Verify wrapping with fallbacks in the later site. English only for this scope. Display uses font weight 400; no synthetic bold, condensed or outlined display treatment.

## Layout

At ≥1024px: maximum outer content width 1280px, centered, 48px side gutters, 12 equal columns with 24px gaps. From 640–1023px: 24px gutters and the same 12-column/gap logic. Below 640px: 20px gutters, single column, 24px between artwork records and 48px between sections. Desktop section gap is 96px. Gutters are included within the 1280px outer width (box-sizing border-box).

Opening title uses 8 columns; intro uses 4, aligned to the title's bottom. Work uses a 7/5 split with the second item 96px lower. Third/context item, if supplied, begins a new row spanning 8 columns from column 3. Below 640px title, intro, images, captions and contact stack in DOM order; remove stagger. At 640–1023px display remains 64px and may wrap; do not squeeze text. Inspect both sides of 640px.

Navigation: plain-text Mira at left, three text anchors at right; no sticky positioning. Below 640px put anchors in a second wrapping row with 24px gaps and 44px target height. Intro and approach can use 8/4 split at ≥640px; contact invitation and address use 7/5. Footer is a flat rule and back-to-top link.

Whole-object slot is 4:3, object-fit contain on background; no silhouette crop. Detail slot is 3:2 and may use cover only after focal-point inspection. Context slot uses its original ratio, max width 100%, no forced crop. Images have no rounded corners or decorative frame. Alt text describes supplied work, never invented characteristics. No photos are supplied; board placeholders are labeled and are not publishable artwork. Keep width/height reserved during image loading; no shimmer.

## Elevation & Depth

Flat composition: no shadow, blur, glass, gradients or fabricated clay texture. Hierarchy comes from image scale, asymmetric placement and serif/sans contrast. Caption and footer rules are 1px solid line. Do not add borders around all content. Pending contact uses surface as a functional status layer.

## Shapes

Square corners throughout. No logo mark exists. No decorative vessel drawings, floating shapes, bento cards or fake studio photography. Numbered rails use two digits with tabular numerals and a 44px index column; labels always carry words or actual metadata, not only color.

## Components

Token mappings: background/color map to CSS background-color/color; typography references copy the full role; borderRadius, minHeight, paddingInline, borderColor, borderWidth, paddingTop and gap map to their kebab-case CSS counterparts. focusRing width/offset map to outline-width/outline-offset and use solid outline. Custom variant names are separate token entries, not an implied standard variant engine.

- Navigation and text links: default text/primary respectively; text links are underlined with 1px stroke and 3px offset. Navigation gets the same underline on hover and active press; focus uses focusRing. Anchors have scroll-margin-top 24px. No scroll-spy state. Targets at least 44×44px; full link area participates.
- Primary email action: button tokens; hover and active use named variants; focus uses focusRing with gap. Square corners, no icon required. Label “Discuss a commission”. Do not make the entire contact region clickable.
- Draft contact pending: buttonPending appearance, “Contact details pending” label, plain status or disabled native button (not a dead link). No pointer cursor. This state belongs only to preview; missing email blocks public release. Pending status must remain readable.
- Copy control: textLink with 44px minimum height, visible address adjacent. Ready label “Copy email address”; success “Email address copied” via polite status only after successful clipboard write; failure “Select and copy the email address above.” with no color-only error. During an async attempt, label “Copying…” and disable repeat activation until resolved; keep dimensions at least their ready size. The control returns to ready on the next activation or address change. No form error or server success component is applicable.
- Artwork: image followed immediately by caption rail with index, verified title/date and materials/dimensions. Reserve 16px between image and rail; border then 16px top padding. Missing-image message stays in the reserved slot and retains caption; no fictional replacement. Loading uses photoPlaceholder, with no animation; loaded image removes placeholder text.
- Skip link: visually hidden until keyboard focus; render above content on background with primary outline, at least 44px high. No hidden menu, carousel, form, modal or download components.

## Motion

Only color and underline transitions, 120ms ease-out, triggered by pointer/focus state; no travel. Reversal interrupts and starts from the current color. Navigation uses immediate native anchor jumps (no smooth scrolling). No reveal animation, parallax, shimmer or autoplay. Under prefers-reduced-motion: reduce, transitions are 0ms. Keyboard/touch have the same information and controls without hover.

## Do's and Don'ts

- Let real, inspected object photography and accurate scale captions do the persuasive work.
- Preserve the caption rail and generous object space when color is removed; the system must remain recognizable through composition.
- Keep plain name treatment until an identity is actually commissioned/approved.
- Do not manufacture quotes, sales metrics, awards, gallery clients, stock ceramics or commission experience.
- Do not add fashionable decorative grids, full-bleed oxide backgrounds or animated hero graphics that compete with the work.

## Verification status

Exact token references, contrast and front-matter parsing checked with a local Python standard-library check; see REVIEW.md. All visual values are resolved proposals. Photo selection, factual copy and contact are content dependencies in WEBSITE.md, not unresolved visual tokens. Board styling is generated from this front matter and records its SHA-256. No official consumer/CLI validation or rendered-website review was performed.
