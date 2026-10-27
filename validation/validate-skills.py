"""Validate this portable skill distribution using only the Python standard library.

This deliberately checks the subset used here: unquoted name and JSON-quoted
single-line description, plus generated quoted OpenAI interface strings.
It is not a general YAML parser or a substitute for the host's validator.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
NAMES = {
    'website-design-workflow', 'website-brief-and-journeys',
    'web-visual-direction', 'website-design-review',
}
errors, checks = [], []


def check(condition, message):
    (checks if condition else errors).append(message)


def frontmatter(path):
    text = path.read_text(encoding='utf-8-sig')
    match = re.match(r'\A---\n(.*?)\n---\n(.*)\Z', text, re.S)
    check(match is not None, f'{path.parent.name}: frontmatter delimiters')
    if not match:
        return {}, text
    fields = {}
    for line in match[1].splitlines():
        key, sep, value = line.partition(': ')
        check(bool(sep) and key not in fields, f'{path.parent.name}: unique field {key}')
        try:
            fields[key] = json.loads(value) if value.startswith('"') else value
        except json.JSONDecodeError:
            check(False, f'{path.parent.name}: valid quoted field {key}')
    return fields, match[2]


for name in sorted(NAMES):
    folder = SKILLS / name
    path = folder / 'SKILL.md'
    check(path.is_file(), f'{name}: SKILL.md exists')
    if not path.is_file():
        continue
    meta, body = frontmatter(path)
    check(set(meta) == {'name', 'description'}, f'{name}: required metadata only')
    check(meta.get('name') == name, f'{name}: directory and name agree')
    check(bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name)) and len(name) <= 64,
          f'{name}: valid Agent Skills name')
    desc = meta.get('description', '')
    check(isinstance(desc, str) and 0 < len(desc) <= 1024, f'{name}: description length/type')
    check(desc.startswith('Use when ') and 'Do not' in desc,
          f'{name}: trigger context and boundary present')
    check('<' not in desc and '>' not in desc, f'{name}: description characters')
    check(len(path.read_text(encoding='utf-8-sig').splitlines()) < 500,
          f'{name}: entry file under 500 lines')
    check('[TODO:' not in body, f'{name}: no initializer placeholders')
    ui = folder / 'agents' / 'openai.yaml'
    check(ui.is_file(), f'{name}: UI metadata exists')
    if ui.is_file():
        raw = ui.read_text(encoding='utf-8-sig')
        vals = {}
        for key, value in re.findall(r'^  ([a-z_]+): (.*)$', raw, re.M):
            try:
                vals[key] = json.loads(value)
            except json.JSONDecodeError:
                check(False, f'{name}: quoted UI string {key}')
        check(set(vals) == {'display_name', 'short_description', 'default_prompt'},
              f'{name}: expected interface metadata')
        check(25 <= len(vals.get('short_description', '')) <= 64,
              f'{name}: UI description length')
        check('$' + name in vals.get('default_prompt', ''), f'{name}: invocation in prompt')
    for doc in folder.rglob('*.md'):
        raw = doc.read_text(encoding='utf-8-sig')
        # Ignore illustrative project links inside template code fences.
        prose = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', raw, flags=re.M | re.S)
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', prose):
            if re.match(r'^[a-z]+://', target) or target.startswith('#'):
                continue
            check((doc.parent / target.split('#')[0]).is_file(),
                  f'{name}: reference exists: {target}')
        check(raw.count('```') % 2 == 0, f'{name}: balanced code fences: {doc.name}')
    check(not (folder / 'README.md').exists(), f'{name}: no redundant skill README')

cases = json.loads((ROOT / 'validation' / 'trigger-cases.json').read_text(encoding='utf-8-sig'))
check(len(cases) == 20, '20 semantic trigger cases')
check(len({x['id'] for x in cases}) == len(cases), 'unique trigger case IDs')
check(all(x['expected'] in NAMES | {'none'} for x in cases), 'trigger case routes resolve')
for name in NAMES | {'none'}:
    check(sum(x['expected'] == name for x in cases) == 4, f'4 trigger cases for {name}')

report = {
    'validation': 'dependency-free structural checks for the exact subset used by this package',
    'passed': len(checks), 'failed': len(errors), 'errors': errors,
    'official_yaml_validator': 'not run by this script',
    'semantic_trigger_evaluation': 'separate fresh-context review; not measured host auto-trigger behavior',
}
(ROOT / 'validation' / 'structure-results.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report, indent=2))
sys.exit(bool(errors))
