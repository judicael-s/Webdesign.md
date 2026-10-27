# Website skill validation

## Source and structure

The workspace was initially empty. Applicable parent instructions and two
existing motion-design skill conventions were inspected. New source skills use
required Agent Skills `name` and `description` frontmatter, short instructions,
progressively loaded references, and generated `agents/openai.yaml` metadata.

The four skills were initialized with the environment's initializer. The
published Agent Skills specification and Google's DESIGN.md specification were
checked on 2026-10-27. The package includes no default visual identity.

Dependency-free structural validation: **90 checks passed, 0 failed**.
See `structure-results.json` and `validate-skills.py` for scope. The metadata
subset checked is simple names and JSON-quoted YAML strings; this is not a
general YAML parser. The bundled `quick_validate.py` could not run because
PyYAML is unavailable, and a local dependency installation attempt failed.
No official-validator pass is claimed.

## Trigger descriptions

A fresh context received only the four name/description pairs and 20 queries,
without expected routes. All **20 primary routes matched** the expected set.
There are four queries for each skill plus four nearby out-of-scope requests.
Cases include portfolios, culture/architecture/arts sites, single pages,
resuming approved work, visual-only tasks, source-only review limits, and small
fixes that should not restart planning.

This is one semantic routing exercise. It does not measure host auto-invocation,
repeatability, statistical accuracy, or whether every future agent will comply.
See `trigger-cases.json`, `trigger-actual.json`, and `trigger-results.json`.

## Forward use

A no-skill baseline planned a ceramic artist portfolio. It avoided fabricated
quotes and metrics, but invented an incompatible DESIGN.md schema and moved
from a board to implementation without requiring direction approval. Its YAML
used `schema_version`, `project`, and a nested `tokens` object. Those observed
gaps informed the explicit format and authorization contracts in the skills.

A fresh reviewer then used `website-design-review` on a supplied magazine
package with an approved vivid, dense editorial direction. It preserved that
direction, identified missing journeys, contradictory spacing, incomplete type
rules and board, hover-only navigation, mobile gaps, and an unsupported claim.
It correctly excluded form/motion requirements because those features were
out of scope, and did not claim to inspect rendered pages. This checks behavior
on one scenario, not general visual quality. The supplied color-pair assessment
was a token-level estimate, not browser accessibility certification.

A separate portfolio planning run produced a linked brief, exact-token DESIGN.md, static desktop/mobile visual board, and explicitly labeled self-review under `portfolio/outputs`. The final board was opened and visually inspected. Twenty-four token references resolve without cycles, and the board wrapper matches the current source hash. No website was implemented and no browser behavior was tested. Missing photos, permissions, factual captions and email remain explicit, and the design remains a proposal awaiting approval.

This run exposed a format gap: the initial output used H1 headings for canonical DESIGN.md sections. The skill guidance now explicitly requires H2 headings, and the corrected output passed a targeted heading-order check. Additional section headings are allowed by the published format. See `portfolio-results.json`. A static evaluation viewer is available in `evaluation.html`; no user feedback or statistical benchmark is claimed.

## Availability

These are portable source files in this workspace. Personal installation and
saving could not be completed: the normal personal location was unwritable and
the supported fallback could not connect. No global installation is claimed.
The skills can be read directly by path and later installed through a supported
host mechanism. No website app or production site was built or deployed.

