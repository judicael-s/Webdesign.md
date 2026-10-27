# DESIGN.md contract

## Published format and compatibility

Verified 2026-10-27 against Google's [format specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md) and [tooling guidance](https://github.com/google-labs-code/design.md). The format is alpha and may change; verify current primary documentation if a consumer rejects it. Do not label a home-grown YAML schema as Google's format.

Use YAML front matter for exact tokens and Markdown for rationale. Interleaved YAML is also supported; define each top-level schema key only once across the document. Prefer front matter for this workflow because it keeps canonical values together. Quote color literals and token references.

Recognized groups are `colors`, `typography`, `rounded`, `spacing` and `components`, alongside metadata such as `version`, `name`, `description`, and `omitted`. Typography entries use `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`, with optional font features/variations. References use `{path.to.token}`. Component variants can use related named entries.

Use level-two headings (`##`) in the canonical prose order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts. An optional level-one heading (`#`) is for the document title only; section names at level one are not parsed as canonical sections. Put project-specific detail in subsections. Unknown extensions are not guaranteed to export to CSS or other formats; identify them and their implementation mapping.

The short format description above follows the published schema. The rest of this contract defines this workflow's own implementation-readiness requirements; it does not claim these extra requirements are Google's standard.

## Authoring recipe

Create a real project-specific `DESIGN.md`, not a filled-in universal palette. Use exact values derived from the chosen direction. This shape sketch intentionally contains no design values and must be completed before handoff:

```yaml
---
version: alpha
name: PROJECT_DESIGN_SYSTEM_NAME
colors: {}
typography: {}
rounded: {}
spacing: {}
components: {}
---
```

Populate relevant groups; use `omitted` with a reason for genuinely inapplicable groups. Empty groups, unresolved placeholders and prose-only visual adjectives do not make an implementation-ready system.

- Define a primary color and semantic text/surface/action/state roles as needed. Do not copy a sample palette from this guide or a reference brand.
- Choose a restrained set of typography roles sufficient for this site, with exact family, size, weight, line height, letter spacing and any needed features. Do not expand a small site to an arbitrary number of levels.
- Give spacing and radius values explicit units. Typography dimensions use px, em or rem; unitless line-height is useful. Spacing may use numeric counts/ratios where their meaning is documented.
- Reference canonical colors, type, spacing and radii from components rather than duplicating their values. A component typography reference can point to a whole typography role; other references should resolve to the appropriate value.
- Define only real components and variants. Explicitly describe relevant focus, hover, active, disabled, loading, error and success treatment.
- For layout, breakpoints, images, depth and motion beyond built-in groups, keep exact implementation rules in prose and optionally express string-valued tokens in named `components` entries. Explain custom property meanings and map them to CSS; unknown properties can produce consumer warnings. Do not claim extension fields are standard exports.
- Avoid unsupported top-level inventions such as nesting all tokens under `tokens` or inventing `schema_version: 1.0`.

## Required prose content for this workflow

### Overview

State the visual thesis, audience connection, emotional tone, signature device, usage limits and references to the brief and board. Identify proposed versus approved direction and the canonical approval record. Brand facts belong in the brief; link rather than repeat.

### Colors

Assign roles to tokens, approved foreground/background pairs and measured contrast guidance. Specify gradients, opacity and image-overlay conditions if used. Distinguish measured pairs from pairs awaiting verification; exact hex values alone are not proof of accessible contrast.

### Typography

Map roles to page functions and hierarchy. State font source, availability/license status, fallbacks and loading policy. Specify responsive size changes or exact fluid CSS formulas in prose when the token consumer accepts only simple dimensions. Define long-heading behavior, body measure and multilingual needs when relevant.

### Layout

Give grid and container limits, gutters, spacing usage and page patterns. Define exact breakpoints or observable layout-switch conditions, with mobile order, navigation transformation and image behavior. Distinguish mobile token variants from global overrides. Include the constrained reading width separately from the full visual canvas if needed.

### Elevation & Depth

Specify shadow, border, tonal-layer and texture rules. If the direction is flat, explain how contrast, scale or position establishes hierarchy. Give exact values for effects actually used; avoid arbitrary effects invented by the builder.

### Shapes

Explain corners, crops, recurring geometry, icon style and signature-device rules. State exclusions and limits. Link source assets rather than describing a substitute for an existing logo or artwork.

### Components

Map component and state tokens to roles. Specify navigation, CTAs, contact controls, case-study/content elements and any relevant imagery/illustration treatment. Keep page-specific behavior in its page brief. Under a motion subsection specify purpose, trigger, duration, easing, travel, interruption, input alternatives and reduced-motion behavior. If motion is absent, say so explicitly.

### Do's and Don'ts

Name a few high-value rules tied to the thesis, anti-references and generic patterns that would undermine it. Avoid blanket aesthetic bans unrelated to the project.

## Verification and handoff

Check canonical section heading levels and order, front matter parses, exact token references resolve without cycles, units/types match the consumer, component variants are unambiguous, prose agrees with values, and the board displays the same system. Check actual foreground/background combinations and important responsive/state rules.

If Google's CLI is already available, use its documented lint command, such as `npx --no-install @google/design.md lint DESIGN.md`. Do not trigger package downloads merely to claim validation. Capture command, consumer version, findings and limitations. Custom component properties may need documented handling. If tooling is unavailable, do a scoped manual/token check and label it as such; never report an official linter pass that did not run.

The final file is machine-readable tokens plus implementation guidance. It does not replace visitor journeys, content evidence, page behavior, human approval or browser inspection of the actual website.

