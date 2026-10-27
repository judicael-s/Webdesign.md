# Artifact contracts

Use this contract to size the documentation, track approval, and prepare handoff. Adapt paths to existing conventions. The files describe the actual project, not a generic example website.

## Smallest complete package

| Artifact | Owns | Does not own |
| --- | --- | --- |
| `WEBSITE.md` | Discovery sources, strategy, journeys, page briefs, technical acceptance, decision/approval record, compact handoff | Exact visual tokens |
| `DESIGN.md` | Visual thesis, tokens, layout and component rules, responsive/motion rules | Business facts or page content inventories |
| Visual-system board | Human-visible synthesis and representative website applications derived from `DESIGN.md` | Independent token definitions or page requirements |
| `REVIEW.md` | Specification findings; later actual rendered inspection and evidence | A replacement design system or approval record |

For one page, keep strategy and page brief as separate sections in `WEBSITE.md`. For a larger site, split only substantial page briefs into `pages/<slug>.md`, link them from the index, and keep shared strategy and rules in their canonical files. A repeated page template needs one shared brief plus explicit content differences. Do not create empty page folders or separate plans per section.

A portfolio may have one page and mail contact; a publication may need reading, archive and search journeys. Let real visitor decisions determine scope. Analytics, CMS, forms, ecommerce, localization and integrations are conditional requirements, not default additions.

## WEBSITE.md starting structure

Use the relevant slots below. Remove irrelevant scaffolding; use `not applicable` with a reason where its absence would otherwise be ambiguous.

```markdown
# Website brief

Status: draft | in review | approved | implementing | rendered review
Scope and current stage:
Canonical visual rules: [DESIGN.md](../../DESIGN.md)
Visual synthesis: [board](visual-board.html)
Review: add a link when the report exists

## Evidence and discovery
Source / path / inspected finding / limitation.
Existing stack, assets, constraints, permissions and content availability.

## Facts, assumptions and open decisions
ID / classification / statement / source or reason / impact / resolution.
Do not promote a hypothesis to a fact because it recurs in a document.

## Strategy and journeys
Business goal, website objective, audiences, needs, entry points, journey
steps and decision barriers, desired actions, success signals, sitemap and
navigation rationale. Cite proof and content records by ID.

## Page briefs
Use the brief-and-journeys skill's page contract. Link split briefs if needed.

## Proof and asset register
ID / claim or role / verified source or file / permission / status / usage.
Missing evidence: omit claim, label proposed content, or request source.

## Technical acceptance
Stack and browser constraints; applicable accessibility, responsive,
performance, search/discoverability, content delivery and functional checks.
Each criterion has an observable result and a check method. Keep visual
values in DESIGN.md and page behavior in page briefs; reference their IDs.

## Decisions and approval
Decision ID / source / status / scope / affected revision or hash /
conditions / unresolved owner. Record explicit autonomy separately.

## Implementation handoff
Fill only when implementation is authorized. Link the exact approved
package, first slice, run command, assets, acceptance IDs and open limits.
```

## Readiness checks

- A builder can identify the audience, main visitor decision, page purpose, proof, and conversion destination.
- A brand-specific thesis becomes visible through concrete typography, composition, assets, and a signature device, not adjectives alone.
- The board visibly applies the rules to this site's desktop and mobile experiences. A written plan for a board is not a delivered board.
- The token values are exact and supported by the documented format; no unresolved placeholder controls implementation.
- Important states, content sources, responsive changes and verification methods are specified.
- Material assumptions are resolved or explicitly accepted. Minor pending content has a safe omission or clearly marked draft treatment.
- Independent review findings are dispositioned. An important open finding is a blocker or a recorded human acceptance of the tradeoff.
- Approval covers the current relevant documents; changes invalidate only affected approval scope.

## Compact handoff contract

```markdown
Implementation authorization: source and scope, or explicit autonomy.
Approved snapshot: WEBSITE.md revision/hash, DESIGN.md revision/hash, board.
Read for this slice: exact page/section links, relevant assets, acceptance IDs.
Build first: one concrete visitor path plus its visual and responsive behavior.
Environment: existing stack, entry points, run/build commands, constraints.
Verify: functional checks, desktop/mobile/state review, required captures.
Open limits: known missing content, deferred decisions, and blocked actions.
```

Do not add another implementation instruction file if an existing task or plan already owns the handoff. Link it once from the index.
