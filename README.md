# Website design skills

Four portable Agent Skills for distinctive, evidence-based website planning and review.

| Skill | Responsibility |
| --- | --- |
| `website-design-workflow` | Coordinate discovery through approved handoff and rendered review |
| `website-brief-and-journeys` | Audience needs, visitor decisions, navigation, proof and page briefs |
| `web-visual-direction` | Project-specific visual board and exact `DESIGN.md` rules |
| `website-design-review` | Challenge the specification and inspect the actual rendered website |

Start with the workflow for a new site or substantial redesign. Use a supporting
skill directly for a focused brief, visual-system task, or review. Small fixes to
an approved site should not trigger a new design process.

## Use in this workspace

These are source skill folders, not a verified personal installation. Tell the
agent to read `skills/website-design-workflow/SKILL.md` and follow it. It resolves
the three supporting skills by frontmatter name; in this distribution their
folders are siblings. The skills are independent of a framework or paid tool.

For a normal install, add all four complete folders to your host's supported
skills location. Each folder contains standard `SKILL.md` frontmatter and
`agents/openai.yaml` UI metadata. Preserve referenced files. Use the environment's
supported personal-skill installation mechanism rather than editing a cached
plugin. Installation in this session was blocked by filesystem/network access.

## What a website project receives

By default, one compact `docs/website/WEBSITE.md` owns discovery, strategy,
journeys, page briefs, proof, technical acceptance, approval and handoff. Root
`DESIGN.md` owns exact visual rules. A rendered visual board demonstrates how the
rules apply. A review report is added at review time. Substantial page briefs may
be split; existing project conventions take precedence.

The templates contain no default palette, font pairing, brand claims or section
inventory. Unavailable inputs stay explicit. Planning may include a board
artifact; website implementation requires relevant approval or explicit autonomy.

## Validation

Run `python validation/validate-skills.py` for dependency-free structural checks
of the exact metadata subset used here. The script is not a general YAML parser.
`validation/trigger-cases.json` contains 20 semantic routing cases, including
near-misses. Fresh-context task runs and their limits are recorded under
`validation/`. Those checks do not measure real host auto-invocation rates or
prove that every resulting website will be visually distinctive.

Google format reference: <https://github.com/google-labs-code/design.md/blob/main/docs/spec.md>.
Agent Skills reference: <https://agentskills.io/specification>.
