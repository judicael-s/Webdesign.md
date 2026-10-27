---
name: website-design-workflow
description: "Use when planning, building, or substantially redesigning a website or web experience from an incomplete request, including marketing sites, artist portfolios, landing pages, editorial sites, and case-study sites. Coordinates discovery, visitor journeys, page briefs, visual direction, design approval, handoff, and rendered review. Also use when a site feels generic or its build needs a clear design package. For an isolated brief, visual-system task, or review, use the focused supporting skill. Do not restart discovery for a small fix to an approved site or use this for backend-only work."
---

# Website design workflow

Make important strategic and creative choices explicit enough that another agent can build without the conversation. Specificity is the goal; document count is not.

## Start or resume

1. Read applicable project instructions and the existing brief, design system, code, assets, and approval record. Inspect only relevant material. Inventory available brand files, content, research, analytics, stack, constraints, and browser/design tools. Record unavailable sources without pretending to inspect them.
2. Identify the current stage, requested scope, and what the user has already approved. Reuse adequate artifacts. A targeted change starts at its affected stage; it does not restart the whole process.
3. Choose the smallest package using [artifact contracts](references/artifact-contracts.md). Use existing project paths; otherwise use `docs/website/WEBSITE.md`, root `DESIGN.md`, and `docs/website/visual-board.html` or a supported visual equivalent. Add `REVIEW.md` when review begins and evidence captures when rendered pages exist.
4. Separate confirmed facts, assumptions, and open decisions. Give facts source pointers. Ask grouped questions only when answers could materially change audience, conversion path, content, creative direction, feasibility, or scope. With a fast-moving user, proceed with labeled proposals and reversible assumptions. Speed alone is not autonomous implementation authorization.

## Route the stages

Resolve supporting skills by their exact frontmatter names through the host's skill catalog. In a portable distribution they are sibling skill folders; installed folder names may change. Load only the relevant supporting skill. If a required support is unavailable, report the missing skill and continue independent discovery; do not silently invent its completed output.

| Stage | Owner | Exit evidence |
| --- | --- | --- |
| Discovery | This skill | Sources inspected, constraints, assumptions, material unknowns |
| Strategy and journeys | `website-brief-and-journeys` | Objectives, visitor needs and entry paths, justified sitemap, proof needs |
| Page briefs | `website-brief-and-journeys` | Purpose, message, sequence rationale, states, mobile behavior, acceptance |
| Visual direction | `web-visual-direction` | Rendered visual-system board plus exact, compatible `DESIGN.md` |
| Specification review | `website-design-review` | Fresh-context findings and disposition before coding |
| Approval and handoff | This skill | Scoped user approval or explicit autonomy; first build slice |
| Rendered review | `website-design-review` | Actual desktop/mobile/state inspection, findings, fixes and captures |

Stages may overlap while drafting. Review the combined package before implementation. A board is a design artifact: producing its HTML or static composition is allowed before approval. It does not authorize scaffolding or implementing the website.

## Review and approval

Use a fresh review agent when available and allowed. Supply the source material and draft package, not brainstorming, author conclusions, or suggested findings. Use the review skill's packet. Without a fresh context, do a separate pass and explicitly label it self-review.

Resolve missing detail within the draft. Surface consequential changes to approved direction for human decision. Keep findings with severity, evidence, proposed resolution, and disposition; do not silently rewrite approved choices to satisfy a reviewer.

Present the concrete board and linked package with the few decisions that need approval. Record approval with source, scope, document revisions or hashes, conditions, and outstanding decisions. A review pass is not approval. Never infer approval from silence, a timeout, or approval of a different revision.

Begin website implementation only after the user approves the relevant direction, or explicitly requests autonomous execution. Autonomy permits decisions within the requested scope; record agent choices as such rather than as user approval. Existing valid approval remains valid for unaffected work.

## Handoff and execution

Put the compact handoff in the package's existing handoff section. Link exact approved artifacts; identify the first implementation slice, relevant stack and run command, assets, acceptance criteria, and open limitations. Do not paste the whole specification or require reading unrelated project material.

A useful first slice exercises the main visitor decision and signature visual rule at desktop and mobile sizes. It might be a project image and enquiry path, an editorial opening and reading path, or a campaign narrative. Do not automatically choose a SaaS hero or component gallery.

Use the host's implementation tools and existing stack. This workflow does not require Sites, a particular framework, an image generator, or paid tooling, and does not authorize deployment. Make only the requested changes.

After implementation, inspect rendered pages using the review skill. Fix material mismatches within the approved direction, rerender affected views, and capture the final state. If browser access or content is unavailable, record exactly what remains unverified and give reproducible checks. Build success alone never establishes visual quality.

## Finish and maintain

Report deliverables, inspected scope, unresolved blockers, and the next authorized action. Keep each requirement at one canonical location. Update affected documents and approval scope when requirements change; do not manufacture new pages, brand assets, claims, testimonials, or case-study results to fill a template.
