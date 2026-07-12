#!/usr/bin/env python3
"""Generate llms.txt, llms-full.txt, topics/*.md, cell/*.md, domain/*.md.

Mimics the huggingscience.co layout: a top-level llms.txt with category overview,
an llms-full.txt with every entry, and per-topic markdown files.
"""
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path('/gallery_millet/yerim.oh/ScienceRAGServey/site')

# Reuse the canonical taxonomy and the already-remapped catalog from the HTML generator, so
# llms.txt / llms-full.txt describe the same substrate × objective taxonomy as the site.
# Importing render_html runs its central remap once (its __main__ block is guarded, so no
# pages are written here).
from render_html import papers, K_LABELS, O_LABELS  # noqa: E402

DOMAIN_LABELS = {
    'bio': 'Biology',
    'chem': 'Chemistry',
    'medical': 'Medicine',
    'material': 'Materials Science',
    'physics': 'Physics',
    'earth': 'Earth Science',
    'astronomy': 'Astronomy',
    'Quantum': 'Quantum',
    'general': 'General Science',
}

TYPE_LABELS = {
    'Method': 'Methods',
    'benchmark': 'Benchmarks',
    'dataset': 'Datasets',
    'summary': 'Surveys',
}

# --- Helpers ---

def short_desc(p):
    """Build a one-line description, ≤ 200 chars."""
    parts = []
    if p.get('method') and p.get('method') != p.get('title', ''):
        parts.append(p['method'])
    if p.get('venue'):
        parts.append(p.get('venue', ''))
    if p.get('year'):
        parts.append(str(p['year']))
    head = ' · '.join([x for x in parts if x])
    note = p.get('note') or p.get('ko_note') or ''
    if note:
        note = note.strip().rstrip('.').strip()
        if len(note) > 180:
            note = note[:177] + '…'
    return f'{head} — {note}' if head and note else (head or note)


def entry_md(p, show_tags=True):
    """Render a paper as one markdown bullet (huggingscience.co style)."""
    title = p.get('title') or p.get('bib_key', '?')
    url = p.get('paper_link') or ''
    desc = short_desc(p)
    if url:
        line = f'- **[{title}]({url})**'
    else:
        line = f'- **{title}**'
    if desc:
        line += f' — {desc}'
    if show_tags:
        tags = []
        for c in p.get('ko_cells', []):
            tags.append(c)
        for d in p.get('domain', []):
            tags.append(DOMAIN_LABELS.get(d, d))
        if p.get('type') and p['type'] != 'unknown':
            tags.append(TYPE_LABELS.get(p['type'], p['type']))
        if tags:
            line += f'  `[{", ".join(tags)}]`'
    return line


# --- Group papers ---
by_cell = defaultdict(list)
by_dom = defaultdict(list)
by_type = defaultdict(list)
unassigned = []

for p in papers:
    cells = p.get('ko_cells') or []
    if cells:
        for c in cells:
            by_cell[c].append(p)
    else:
        unassigned.append(p)
    for d in p.get('domain', []):
        by_dom[d].append(p)
    t = p.get('type', 'unknown')
    by_type[t].append(p)

# --- llms.txt: compact overview ---

def cell_intro(cell):
    K, O = cell.split('.')
    return f'**[{cell}]** {K_LABELS[K][0]} × {O_LABELS[O][0]}'


llms_lines = [
    '# Scientific RAG Hub — AI for Science Retrieval-Augmented Generation Index',
    '',
    'A curated catalog of Retrieval-Augmented Generation (RAG) systems, benchmarks, and datasets',
    'across the sciences, organized by the survey\'s two axes: the retrieval SUBSTRATE a system draws',
    'on (the native form of what it indexes) and the OPERATIONAL OBJECTIVE it serves (the rung, ordered',
    f'by how far the ground truth sits from the corpus). {len(papers)} entries across a 12-cell landscape.',
    '',
    'Companion to the upcoming survey "Scientific Retrieval-Augmented Generation: A Survey through',
    'Knowledge Source and Scientific Mission" (Oh et al., Vision and Learning Lab, Seoul National University).',
    '',
    'Axes:',
    '  K1 Textual · K2 Relational · K3 Structured-entity · K4 Perceptual   (substrate, §4)',
    '  O1 Grounding · O2 Synthesis · O3 Discovery                          (objective rung, §5)',
    '',
    '## Browse by substrate × objective cell (12 cells)',
    '',
]
for K in ['K1', 'K2', 'K3', 'K4']:
    for O in ['O1', 'O2', 'O3']:
        cell = f'{K}.{O}'
        count = len(by_cell.get(cell, []))
        kn, kd = K_LABELS[K]
        on, od = O_LABELS[O]
        llms_lines.append(f'- [/cell/{cell}.md]({cell}.md) — {kn} × {on} ({count} entries)')
llms_lines += [
    '',
    '## Browse by scientific domain',
    '',
]
for d, label in DOMAIN_LABELS.items():
    if d in by_dom:
        llms_lines.append(f'- [/domain/{d}.md]({d}.md) — {label} ({len(by_dom[d])} entries)')

llms_lines += [
    '',
    '## Browse by resource type',
    '',
]
for t, label in TYPE_LABELS.items():
    if t in by_type:
        llms_lines.append(f'- [/topics/{t.lower()}.md]({t.lower()}.md) — {label} ({len(by_type[t])} entries)')

llms_lines += [
    '',
    '## Knowledge Source axis — retrieval substrate (K1-K4)',
    '',
]
for K, (n, d) in K_LABELS.items():
    llms_lines.append(f'- **{K} {n}** — {d}')
llms_lines += [
    '',
    '## Operational Objective axis — objective rung (O1-O3)',
    '',
]
for O, (n, d) in O_LABELS.items():
    llms_lines.append(f'- **{O} {n}** — {d}')
llms_lines += [
    '',
    'For the full catalog with descriptions, see /llms-full.txt',
    '',
]
(ROOT / 'llms.txt').write_text('\n'.join(llms_lines))
print(f'Wrote llms.txt ({len(llms_lines)} lines)')


# --- llms-full.txt: every entry ---
full = [
    '# Scientific RAG Hub — Full Catalog',
    '',
    f'{len(papers)} retrieval-augmented generation systems, benchmarks, and datasets for scientific discovery.',
    'Organized by the survey\'s two axes: retrieval substrate (Textual/Relational/Structured-entity/Perceptual) × objective rung (Grounding/Synthesis/Discovery).',
    '',
    'Each entry carries tags `[K.O cell(s), domain(s), type]`. Cross-source papers appear in multiple cells.',
    '',
]
for K in ['K1', 'K2', 'K3', 'K4']:
    kn, kd = K_LABELS[K]
    full.append(f'## K{K[1]} — {kn}')
    full.append('')
    full.append(f'_{kd}_')
    full.append('')
    for O in ['O1', 'O2', 'O3']:
        cell = f'{K}.{O}'
        on, od = O_LABELS[O]
        ps = by_cell.get(cell, [])
        full.append(f'### {cell}  ·  {kn} × {on}  ({len(ps)})')
        full.append(f'_{od}_')
        full.append('')
        for p in sorted(ps, key=lambda x: -int(x.get('year') or 0) if str(x.get('year', '')).isdigit() else 0):
            full.append(entry_md(p))
        full.append('')
    # Catalog entries on this substrate that carry no objective rung yet (benchmarks,
    # datasets, and databases without a resolved task).
    k_only = by_cell.get(K, [])
    if k_only:
        full.append(f'### {K}  ·  {kn} — no objective rung yet  ({len(k_only)})')
        full.append('')
        for p in sorted(k_only, key=lambda x: -int(x.get('year') or 0) if str(x.get('year', '')).isdigit() else 0):
            full.append(entry_md(p))
        full.append('')

if unassigned:
    full.append('## Unassigned (no objective rung yet)')
    full.append('')
    full.append(f'{len(unassigned)} catalog entries placed on a substrate but without a resolved objective rung yet.')
    full.append('')
    for p in unassigned:
        full.append(entry_md(p))
    full.append('')

(ROOT / 'llms-full.txt').write_text('\n'.join(full))
print(f'Wrote llms-full.txt ({len(full)} lines)')


# --- Per-cell markdown pages: substrate × objective cells ---
for K in ['K1', 'K2', 'K3', 'K4']:
    for O in ['O1', 'O2', 'O3']:
        cell = f'{K}.{O}'
        kn, kd = K_LABELS[K]
        on, od = O_LABELS[O]
        ps = by_cell.get(cell, [])
        lines = [
            f'# [{cell}]  {kn} × {on}',
            '',
            f'**K {K[1]}:** {kd}',
            '',
            f'**O {O[1]}:** {od}',
            '',
            f'_{len(ps)} entries_',
            '',
            '---',
            '',
        ]
        for p in sorted(ps, key=lambda x: -int(x.get('year') or 0) if str(x.get('year', '')).isdigit() else 0):
            lines.append(entry_md(p, show_tags=False))
        lines.append('')
        (ROOT / 'cell' / f'{cell}.md').write_text('\n'.join(lines))

# --- K-only axis pages (K1-K4): papers on knowledge-source axis without O ---
for K in ['K1', 'K2', 'K3', 'K4']:
    kn, kd = K_LABELS[K]
    ps = by_cell.get(K, [])
    lines = [
        f'# [{K}]  {kn}',
        '',
        f'**K {K[1]}:** {kd}',
        '',
        f'_{len(ps)} entries on the K-axis only (datasets / knowledge sources without a paired O assignment in main.tex)_',
        '',
        '---',
        '',
    ]
    for p in sorted(ps, key=lambda x: -int(x.get('year') or 0) if str(x.get('year', '')).isdigit() else 0):
        lines.append(entry_md(p, show_tags=False))
    lines.append('')
    (ROOT / 'cell' / f'{K}.md').write_text('\n'.join(lines))

# --- O-only axis pages (O1-O3): papers on objective axis without K ---
for O in ['O1', 'O2', 'O3']:
    on, od = O_LABELS[O]
    ps = by_cell.get(O, [])
    lines = [
        f'# [{O}]  {on}',
        '',
        f'**O {O[1]}:** {od}',
        '',
        f'_{len(ps)} entries on the O-axis only (benchmarks without a paired K assignment in main.tex)_',
        '',
        '---',
        '',
    ]
    for p in sorted(ps, key=lambda x: -int(x.get('year') or 0) if str(x.get('year', '')).isdigit() else 0):
        lines.append(entry_md(p, show_tags=False))
    lines.append('')
    (ROOT / 'cell' / f'{O}.md').write_text('\n'.join(lines))

# --- Per-domain markdown pages ---
for d, label in DOMAIN_LABELS.items():
    if d not in by_dom:
        continue
    ps = by_dom[d]
    lines = [
        f'# {label}',
        '',
        f'_{len(ps)} entries in the {label.lower()} domain._',
        '',
        '---',
        '',
    ]
    for p in sorted(ps, key=lambda x: -int(x.get('year') or 0) if str(x.get('year', '')).isdigit() else 0):
        lines.append(entry_md(p))
    lines.append('')
    (ROOT / 'domain' / f'{d}.md').write_text('\n'.join(lines))

# --- Per-type markdown pages ---
for t, label in TYPE_LABELS.items():
    if t not in by_type:
        continue
    ps = by_type[t]
    lines = [
        f'# {label}',
        '',
        f'_{len(ps)} entries of type "{t}"._',
        '',
        '---',
        '',
    ]
    for p in sorted(ps, key=lambda x: -int(x.get('year') or 0) if str(x.get('year', '')).isdigit() else 0):
        lines.append(entry_md(p))
    lines.append('')
    (ROOT / 'topics' / f'{t.lower()}.md').write_text('\n'.join(lines))

k_only_count = sum(1 for k in ['K1','K2','K3','K4'] if (ROOT/'cell'/f'{k}.md').exists())
o_only_count = sum(1 for o in ['O1','O2','O3'] if (ROOT/'cell'/f'{o}.md').exists())
print(f'Wrote {len(by_cell)} cell entries (12 substrate×objective + {k_only_count} K-only + {o_only_count} O-only), {len(by_dom)} domain/*.md, {len(by_type)} topics/*.md')
