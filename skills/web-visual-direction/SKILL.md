---
name: web-visual-direction
description: "Use when defining or refining a website's visual identity, art direction, brand-system board, design tokens, typography, imagery, motion, or implementation-ready DESIGN.md. Applies to marketing sites, portfolios, landing pages, publications, and case-study sites, especially when a design feels generic or only has vague style adjectives. Preserve existing approved direction. For audience and page purpose use website-brief-and-journeys; for inspecting a finished render use website-design-review. Do not use for unrelated print branding or an isolated implementation fix with already clear visual rules."
---

# Web visual direction

Turn the brand and visitor purpose into a recognizable visual language. Deliver a visual synthesis and reusable implementation rules; neither substitutes for journeys or page briefs.

## Ground the direction

Read the brief, verified brand material, actual assets, page purposes, constraints and approval record. If the brief is absent, establish the audience, main visitor decision and content constraints before styling. Use `website-brief-and-journeys` when those gaps require strategy work. Do not turn a visual task into a full restart of an approved site.

State a visual thesis connecting brand evidence and audience needs to visible choices. For example, a material archive may use calibrated object scale, precise captions and macro texture to make craft assessable. `Modern, bold, premium` alone cannot guide implementation.

Extract useful principles from references: composition, rhythm, type contrast, image treatment, density, navigation, and motion. Record source and what was inspected. Translate principles rather than copying layouts, assets or identity. If no references are available, label the direction as a proposal grounded in project evidence; do not invent a reference study.

Use two or three concise directions only when a real creative fork remains. Recommend one with reasons and make the alternatives easy to compare. When direction is already approved, refine it within that scope.

## Make the system specific

Define emotional tone, signature visual device or brand move, usage limits, anti-references, and practical rules. A signature device may be a distinctive crop grammar, typographic rhythm, editorial annotation, or purposeful interaction; it need not be decorative animation.

Use [board contract](references/visual-board.md) to compose a concise visual-system board. Show actual website applications and the relevant identity, colors, type, imagery, layout, components, states, icons, micro-details and motion. Mark absent inputs `not applicable` or `not yet decided`. Do not invent a logo, tagline, brand values, packaging mockups or business claims to fill the board.

Use [DESIGN.md contract](references/design-md.md) to write exact machine-readable tokens and human-readable usage rules in Google's published format where compatible. Keep strategy and page behavior in the brief. Document typography sourcing and fallbacks, approved color pairs and contrast, responsive composition, component states, media treatment, motion and reduced-motion behavior. Every value that controls the chosen direction must be exact or explicitly unresolved; an unresolved draft is not implementation-ready.

## Produce and inspect both deliverables

Create the board as a visual artifact using available tools: self-contained HTML, SVG, a design canvas, or a composed static image. Board HTML is a review artifact, not permission to implement the site. Use exact approved or proposed tokens from `DESIGN.md`; derive generated board styling from those values and update it when the source changes. Do not maintain a second hand-edited token source.

Show at least a representative desktop composition and mobile adaptation using real page messages and available project assets. Include enough of a secondary/content/case-study view to demonstrate the system beyond a hero when that page exists. Clearly label missing imagery or draft copy. Image generation can explore atmosphere when appropriate; generated images do not establish exact typography, colors, UI states, factual artwork, client work or tokens.

Open and inspect the produced board with the available visual/browser tools. Correct clipping, fallback-font problems, illegibility and inconsistencies. If no viewer is available, deliver the artifact as uninspected and state the limitation; do not claim it was visually checked. A palette table or a written plan for a board alone is incomplete.

## Handoff

Link the board to the brief/journeys, page briefs and `DESIGN.md`, and link back from the index. Explain the visual thesis in a few sentences, name open decisions, and submit the combined package for specification review and approval. Preserve approved creative choices. The agent may propose improvements; it cannot silently replace user approval with its own aesthetic preference.
