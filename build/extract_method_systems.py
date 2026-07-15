#!/usr/bin/env python3
"""Extract the paper's Table 3 (tab:method_systems) from main2.tex into
data/method_systems.json, the source for the at-a-glance systems tables on the
cell / axis pages. Each row decomposes a system into the pipeline stages of
Eq. (method): Construction (phi), Matching (s), Integration (G), Verifier (V),
plus its Knowledge Source substrate (K) and reached Operational Objective (O),
grouped by depth of verifier coupling (Open -> Closed-loop).

Re-run whenever main2.tex's systems table changes:
    python3 build/extract_method_systems.py
"""
import re
import json
from pathlib import Path

TEX = Path(__file__).resolve().parents[1].parent / 'ACM' / 'csur_submission' / 'main2.tex'
OUT = Path(__file__).resolve().parents[1] / 'data' / 'method_systems.json'

K_MAP = {'Txt': 'K1', 'Rel': 'K2', 'Str': 'K3', 'Prc': 'K4'}
O_MAP = {
    'QA': 'Question Answering', 'LS': 'Literature Synthesis', 'CV': 'Claim Verification',
    'HG': 'Hypothesis Generation', 'MD': 'Molecular Design', 'MtD': 'Materials Discovery',
    'PP': 'Property Prediction', 'CmG': 'Cross-modal Grounding',
}
# Rung each task belongs to (mirrors the survey's O1/O2/O3 grouping).
O_RUNG = {
    'Question Answering': 'O1', 'Cross-modal Grounding': 'O1',
    'Claim Verification': 'O2', 'Literature Synthesis': 'O2',
    'Property Prediction': 'O3', 'Molecular Design': 'O3',
    'Materials Discovery': 'O3', 'Hypothesis Generation': 'O3',
}


def clean(s):
    s = re.sub(r'\\textcolor\{\w+\}\{', '', s)
    s = s.replace('\\textsc{', '').replace('\\emph{', '').replace('\\textbf{', '')
    s = s.replace('}', '').replace('$', '').replace('\\', '').replace('~', ' ')
    return s.strip()


def main():
    tex = TEX.read_text()
    start = tex.index('\\label{tab:method_systems}')
    end = tex.index('\\end{table*}', start)
    body = tex[start:end]

    rows, coupling = [], None
    for line in body.splitlines():
        m = re.search(r'\\textbf\{(Open|Self-check|External-verify|Closed-loop)\}', line)
        if m and '\\multicolumn' in line:
            coupling = m.group(1)
            continue
        if '\\cite{' not in line:
            continue
        name = re.match(r'\s*([^&]*?)~?\\cite', line).group(1)
        name = re.sub(r'\\text[a-z]+\{|\}|\$|\\', '', name).replace('~', ' ').strip()
        bib = re.search(r'\\cite\{([^}]*)\}', line).group(1)
        cells = [c.strip() for c in line.split('&')]
        K = K_MAP.get(clean(cells[1]), clean(cells[1]))
        O = O_MAP.get(clean(cells[6]), clean(cells[6]))
        rows.append({
            'name': name,
            'bib_key': bib,
            'coupling': coupling,
            'K': K,
            'construction': clean(cells[2]),
            'matching': clean(cells[3]),
            'integration': clean(cells[4]),
            'verifier': clean(cells[5]),
            'O': O,
            'O_rung': O_RUNG.get(O, ''),
        })

    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    print(f'Wrote {len(rows)} systems to {OUT}')


if __name__ == '__main__':
    main()
