---
name: website-design-review
description: "Use when independently challenging a website brief or design specification before coding, or reviewing actual rendered web pages against approved visual direction, DESIGN.md, page briefs, and acceptance criteria. Also use for generic-looking results, missing responsive or interaction states, and post-build visual QA on marketing sites, portfolios, landing pages, publications, or case-study sites. Supports fresh-context review and honest self-review fallback. Do not use source code or build success as evidence of rendered visual quality, and do not substitute this for a general security or backend code review."
---

# Website design review

Review the agreement and the experience as two distinct tasks. Keep evidence, inference, preference and unverified items separate. A reviewer challenges decisions; it does not become the owner of the creative direction.

Read [review contracts](references/review-contracts.md) for the independent input packet, severity rubric, report shape and inspection matrix. Load only the phase required by the task. Review an existing package without restarting discovery.

## Specification review

Use a fresh agent context when available and permitted. Give it relevant project material and the draft specification, board and assets. Do not give it brainstorming history, the author's defense, a diagnosis, or expected findings. Without this capability, perform a separate self-review and disclose the lack of independence.

Trace key journeys through page briefs, visual rules and acceptance criteria. Identify missing requirements, unsupported assumptions and claims, vague visual decisions, contradictions, inaccessible states, responsive gaps, content dependencies, performance risks, and ways the result could become an interchangeable AI-generated site.

Test specificity: can two builders understand the same intended composition, imagery, hierarchy and signature device without guessing? If all that distinguishes the direction is an accent color and adjectives, name the missing decisions. Do not demand uniqueness through novelty that harms usability or contradicts brand evidence.

Return bounded findings with severity, source evidence, consequence and suggested resolution. Classify an aesthetic preference as a preference, not a failure. Surface important changes to approved scope for human decision. Do not rewrite approved direction automatically or treat your verdict as user approval.

## Rendered review

1. Identify the exact running URL, build/revision, approved package snapshot and in-scope routes/journeys. Start the existing local environment if authorized and needed; use available browser/computer-use tools in accordance with their instructions.
2. Inspect actual pages at an agreed desktop and mobile viewport. Use project sizes; if none exist, propose representative sizes such as 1440 x 900 and 390 x 844 and label them test choices. Add a narrow or intermediate width where the design's transition is at risk.
3. Exercise important interactions and states: navigation open/closed/current, keyboard focus, hover when relevant, active controls, form validation/error/success/loading, or media as applicable. Do not trigger live purchases, outbound enquiries or destructive actions merely to inspect a state; use a local test environment or mark that state untested.
4. Compare the render to the approved board, `DESIGN.md`, page briefs and acceptance criteria. Inspect hierarchy, typography and font loading, assets/crops, spacing, signature device, content/proof, navigation, overflow, touch and keyboard use, and relevant motion/reduced motion. Do not infer dynamic behavior from screenshots alone.
5. Capture overview and focused evidence with route, viewport, state and revision. Capture final states after repairs; do not deliver only screenshots from before the fix. Record what you actually inspected, partial checks and unavailable tools/assets.

For a small site, inspect each distinct layout on desktop and mobile plus the priority journey. For a larger site, choose representative templates and explicitly list routes or states not sampled. Do not imply complete coverage from one homepage screenshot.

## Resolve and report

When the user requested fixes, correct material mismatches within the agreed direction, then rerender affected views and rerun the failed checks. A review-only request produces findings without unrequested edits. Changes to approved strategy or creative direction require human decision unless explicit autonomy covers them.

Stop when required checks pass and material findings are resolved or clearly reported. Deliver a factual verdict, scoped inspection matrix, remaining findings/limits, and final captures. Without browser inspection, report rendered review as unverified; static source checks and a successful build do not establish visual quality.
