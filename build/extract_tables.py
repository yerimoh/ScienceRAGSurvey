#!/usr/bin/env python3
"""Extract the paper's axis reference tables from main2.tex:

  Table 1 (tab:knowledge_source)  -> data/knowledge_sources.json  (the K axis: data)
  Table 2 (tab:benchmarks)        -> data/benchmarks.json         (the O axis: tasks)

Each axis page shows the table that matches its own semantics: K pages list the
knowledge sources (data resources), O pages list the benchmarks (tasks). The method
pipeline table (Table 3) stays on the K×O cell pages via extract_method_systems.py.

Re-run whenever those tables change:
    python3 build/extract_tables.py
"""
import re
import json
from pathlib import Path

TEX = Path(__file__).resolve().parents[1].parent / 'ACM' / 'csur_submission' / 'main2.tex'
BIB = Path(__file__).resolve().parents[1].parent / 'ACM' / 'csur_submission' / 'references.bib'
DATA = Path(__file__).resolve().parents[1] / 'data'
META = Path(__file__).resolve().parent / 'benchmark_meta.json'
BM_META = {k: v for k, v in json.loads(META.read_text()).items() if not k.startswith('_')} if META.exists() else {}

SUB_K = {'Textual': 'K1', 'Relational': 'K2', 'Structured-entity': 'K3', 'Perceptual': 'K4'}
SHORT_K = {'Txt': 'K1', 'Rel': 'K2', 'Str': 'K3', 'Prc': 'K4'}
TASK_RUNG = {
    'Question Answering': 'O1', 'Claim Verification': 'O2', 'Literature Synthesis': 'O2',
    'Property Prediction': 'O3', 'Molecular Design': 'O3', 'Materials Discovery': 'O3',
    'Hypothesis Generation': 'O3',
}

AMP = '\x00'  # sentinel standing in for an escaped literal ampersand during column split


def clean(s):
    s = re.sub(r'\s*\(\s*\\S?\s*\\ref\{[^}]*\}\s*\)', '', s)   # drop "(§ref)" pointers
    s = re.sub(r'\\S?\s*\\ref\{[^}]*\}', '', s)
    s = re.sub(r'\\textcolor\{\w+\}\{', '', s)
    s = re.sub(r'\\text\{([^}]*)\}', r'\1', s)                 # \text{hull} -> hull
    s = re.sub(r'\\text[a-z]+\{', '', s)
    s = s.replace('\\&', '&').replace(AMP, '&')
    s = s.replace('\\%', '%')
    s = s.replace('\\textasciitilde', '~').replace('textasciitilde', '~')
    s = s.replace('\\textperiodcentered', '·').replace('textperiodcentered', '·')
    s = s.replace('\\sim', '~').replace('\\approx', '≈')
    s = s.replace('\\', '').replace('$', '').replace('{', '').replace('}', '')
    s = s.replace('--', '–')
    return re.sub(r'\s+', ' ', s).strip()


def split_cols(line):
    """Split a LaTeX table row on unescaped & (escaped \\& is a literal ampersand)."""
    return [c.strip() for c in line.replace('\\&', AMP).split('&')]


def load_bib_links():
    """bib key -> best link (url > doi > arXiv eprint)."""
    if not BIB.exists():
        return {}
    text = BIB.read_text(errors='ignore')
    out = {}
    for m in re.finditer(r'@\w+\{([^,]+),(.*?)\n\}', text, flags=re.S):
        key = m.group(1).strip()
        fields = m.group(2)
        def field(name):
            fm = re.search(name + r'\s*=\s*[{"](.+?)[}"]\s*,?\s*\n', fields, flags=re.S | re.I)
            return fm.group(1).strip() if fm else None
        url, doi, eprint = field('url'), field('doi'), field('eprint')
        link = None
        if url:
            link = url.replace('\\_', '_').replace('\\&', '&')
        elif doi:
            link = 'https://doi.org/' + doi.replace('\\_', '_')
        elif eprint and re.match(r'^\d{4}\.\d+', eprint):
            link = 'https://arxiv.org/abs/' + eprint
        out[key] = link
    return out


def table_body(tex, label):
    start = tex.index(label)
    end = tex.index('\\end{table', start)
    return tex[start:end]


def extract_knowledge_sources(tex):
    body = table_body(tex, '\\label{tab:knowledge_source}')
    out, cur = [], None
    for line in body.splitlines():
        m = re.search(r'\\textsc\{(Textual|Relational|Structured-entity|Perceptual)\}', line)
        if m and '\\multicolumn' in line:
            cur = m.group(1)
            continue
        if '\\cite{' not in line or '&' not in line:
            continue
        cells = split_cols(line)
        refs = re.search(r'\\cite\{([^}]*)\}', line)
        n_refs = len(refs.group(1).split(',')) if refs else 0
        out.append({
            'substrate': SUB_K.get(cur, cur),
            'substrate_name': cur,
            'resource_group': clean(cells[0]),
            'scale': clean(cells[1]),
            'access': clean(cells[2]),
            'notes': clean(cells[3]),
            'n_refs': n_refs,
        })
    return out


def extract_benchmarks(tex, bib_links):
    body = table_body(tex, '\\label{tab:benchmarks}')
    out, cur = [], None
    for line in body.splitlines():
        m = re.search(r'\\textbf\{\\textcolor\{Oaxis\}\{([^}]+)\}\}', line)
        if m and '\\multicolumn' in line:
            cur = clean(m.group(1))
            continue
        if '\\cite{' not in line or '&' not in line:
            continue
        name = clean(re.match(r'\s*([^&]*?)~?\\cite', line).group(1))
        bib = re.search(r'\\cite\{([^}]*)\}', line).group(1)
        cells = split_cols(line)
        sub = clean(cells[2])
        # link: curated benchmark homepage if any, else the paper (from references.bib)
        link = BM_META.get(name, {}).get('url') or bib_links.get(bib)
        out.append({
            'task': cur,
            'O_rung': TASK_RUNG.get(cur, ''),
            'benchmark': name,
            'bib_key': bib,
            'domain': clean(cells[1]),
            'K': SHORT_K.get(sub, sub),
            'scale': clean(cells[3]),
            'description': clean(cells[4]),
            'link': link,
        })
    return out


def extract_evaluation(tex):
    """Paper Table 4 (tab:evaluation): the four scoring dimensions of §7."""
    body = table_body(tex, '\\label{tab:evaluation}')
    codes = ['E1', 'E2', 'E3', 'E4']
    out = []
    for line in body.splitlines():
        if '&' not in line or '\\midrule' in line or 'textbf' in line or '\\toprule' in line:
            continue
        cells = split_cols(line.rstrip('\\ \n'))
        if len(cells) < 4:
            continue
        dim = clean(cells[0])
        if not dim:
            continue
        metrics = [m.strip() for m in re.split(r',\s*', clean(cells[2])) if m.strip()]
        out.append({
            'code': codes[len(out)] if len(out) < len(codes) else '',
            'dimension': dim,
            'measures': clean(cells[1]),
            'metrics': metrics,
            'ceiling': clean(cells[3]),
        })
    return out


def main():
    tex = TEX.read_text()
    bib_links = load_bib_links()
    ks = extract_knowledge_sources(tex)
    bm = extract_benchmarks(tex, bib_links)
    ev = extract_evaluation(tex)
    (DATA / 'knowledge_sources.json').write_text(json.dumps(ks, ensure_ascii=False, indent=2))
    (DATA / 'benchmarks.json').write_text(json.dumps(bm, ensure_ascii=False, indent=2))
    (DATA / 'evaluation_table.json').write_text(json.dumps(ev, ensure_ascii=False, indent=2))
    print(f'Wrote {len(ks)} knowledge-source rows, {len(bm)} benchmark rows, {len(ev)} evaluation dimensions.')


if __name__ == '__main__':
    main()
