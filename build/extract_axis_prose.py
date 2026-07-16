#!/usr/bin/env python3
"""Extract the actual §4 (Knowledge Source) and §5 (Operational Objective) prose from
main2.tex into data/axis_prose.json, so the axis overview / cell pages show the survey's
real content (substrate intros, sub-subsections, and the named resources) rather than a
coarse summary.

Structure:
  { "K": { "intro": str,
           "substrates": [ {code, name, intro, subsubs:[{title,text}]} ] },
    "O": { "intro": str,
           "tasks": [ {name, rung, text} ] } }

Re-run whenever §4/§5 change:
    python3 build/extract_axis_prose.py
"""
import re
import json
from pathlib import Path

TEX = Path(__file__).resolve().parents[1].parent / 'ACM' / 'csur_submission' / 'main2.tex'
BIB = Path(__file__).resolve().parents[1].parent / 'ACM' / 'csur_submission' / 'references.bib'
META = Path(__file__).resolve().parent / 'resource_meta.json'
OUT = Path(__file__).resolve().parents[1] / 'data' / 'axis_prose.json'

# curated homepage + one-line description per resource (see resource_meta.json)
RES_META = {k: v for k, v in json.loads(META.read_text()).items() if not k.startswith('_')} if META.exists() else {}

# Resource names whose §4 mention doesn't parse cleanly from the words before \cite
# (trailing lowercase words, missing ~). Keyed by the first cite key of the mention.
NAME_OVERRIDE = {
    'lee2023climate': 'IPCC assessment reports',
    'DBLP:conf/mss/KoblerBCH95': 'NASA EOSDIS',
    'clark2013cancer': 'TCGA',
}
CONNECTORS = {'of', 'and', 'the', 'for', 'de', '&', 'via'}

SUB_K = {'Textual': 'K1', 'Relational': 'K2', 'Structured-entity': 'K3', 'Perceptual': 'K4'}
TASK_RUNG = {
    'Question Answering': 'O1', 'Claim Verification': 'O2', 'Literature Synthesis': 'O2',
    'Property Prediction': 'O3', 'Molecular Design': 'O3', 'Materials Discovery': 'O3',
    'Hypothesis Generation': 'O3',
}


def strip_comments(s):
    out = []
    for line in s.splitlines():
        # drop a % that is not escaped as \%
        m = re.search(r'(?<!\\)%', line)
        if m:
            line = line[:m.start()]
        out.append(line)
    return '\n'.join(out)


LABEL_TEXT = {
    'sec:knowledge_source': 'the Knowledge Source axis',
    'sec:benchmark': 'the Operational Objective axis',
    'sec:method': 'the pipeline',
    'sec:m_construct': 'construction', 'sec:m_retrieve': 'retrieval',
    'sec:m_integrate': 'integration', 'sec:m_couple': 'verification',
    'sec:k1_textual': 'the textual substrate', 'sec:k2_relational': 'the relational substrate',
    'sec:k3_structured': 'the structured-entity substrate', 'sec:k4_perceptual': 'the perceptual substrate',
    'sec:overview': 'the overview', 'sec:evaluation': 'the evaluation axis',
    'sec:frontiers': 'the open challenges',
    'eq:guide': 'the pipeline equation', 'eq:method': 'the pipeline equation',
    'fig:overview': 'the overview figure', 'tab:method_systems': 'the systems table',
}


def clean(s):
    s = strip_comments(s)
    # cross-references: turn Eq./Figure/section pointers into readable text, drop the rest.
    s = re.sub(r'(?:Eq\.|Equation)\s*~?\s*\(?\\ref\{[^}]*\}\)?', 'the pipeline equation', s)
    s = re.sub(r'(?:Figure|Fig\.)\s*~?\s*\\ref\{[^}]*\}', 'the overview figure', s)
    s = re.sub(r'\(\s*(?:\\S)?\s*~?\s*\\ref\{[^}]*\}\s*\)', '', s)          # parenthetical ref → drop
    s = re.sub(r'(?:\\S)?\s*~?\s*\\ref\{([^}]*)\}', lambda m: LABEL_TEXT.get(m.group(1), ''), s)
    s = re.sub(r'\\eqref\{[^}]*\}', 'the pipeline equation', s)
    s = re.sub(r'\\cite[a-z]*\{[^}]*\}', '', s)
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = s.replace('\\S', '§')
    # drop the colour-name argument of \textcolor{Kaxis}{...}, keeping the wrapped text
    s = re.sub(r'\\textcolor\{[^}]*\}', '', s)
    s = re.sub(r'\\hl[A-Za-z]*\{', '{', s)
    # unwrap single-arg text commands innermost-first, repeatedly
    for _ in range(6):
        new = re.sub(r'\\(?:textsc|emph|textbf|textit|text|texttt|mathcal)\{([^{}]*)\}', r'\1', s)
        if new == s:
            break
        s = new
    s = s.replace('{', '').replace('}', '')
    s = re.sub(r'\$[^$]*\$', '', s)          # inline math (Eq. symbols)
    s = s.replace('\\%', '%').replace('~', ' ')
    s = s.replace('--', '–')
    s = re.sub(r'\\[a-zA-Z]+', '', s)         # any leftover bare macros
    s = s.replace('\\', '')
    s = re.sub(r'\(\s*[,;]?\s*\)', '', s)     # empty () left by removed refs
    s = re.sub(r'\s+([,.;:])', r'\1', s)      # space before punctuation
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n\s*\n+', '\n\n', s)
    # collapse each paragraph's internal newlines into spaces
    paras = [re.sub(r'\s+', ' ', p).strip() for p in s.split('\n\n')]
    return '\n\n'.join(p for p in paras if p).strip()


def section_span(tex, start_label, end_label):
    a = tex.index(start_label)
    b = tex.index(end_label, a)
    return tex[a:b]


def take_braced(s, i):
    """s[i] == '{'; return (inner_text, index_after_matching_close) with nesting."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == '{':
            depth += 1
        elif s[j] == '}':
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
    return s[i + 1:], len(s)


def split_on_command(block, cmd):
    """Split a block on a sectioning command, honouring braces in its argument.
    Returns (intro_before_first, [(title_raw, body)])."""
    marker = '\\' + cmd + '{'
    positions = [m.start() for m in re.finditer(re.escape(marker), block)]
    if not positions:
        return block, []
    intro = block[:positions[0]]
    out = []
    for pi, pos in enumerate(positions):
        title, after = take_braced(block, pos + len(marker) - 1)
        end = positions[pi + 1] if pi + 1 < len(positions) else len(block)
        out.append((title, block[after:end]))
    return intro, out


def parse_subsections(block):
    return split_on_command(block, 'subsection')


def parse_subsubs(block):
    intro, subs = split_on_command(block, 'subsubsection')
    # keep raw body too, so resources can be pulled with their \cite keys intact
    return (clean(intro), intro), [(clean(t), clean(b), b) for t, b in subs]


def load_bib_links():
    """key -> {title, link}. link prefers an explicit url/doi field."""
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
        url = field('url')
        doi = field('doi')
        link = None
        if url:
            link = url.replace('\\_', '_').replace('\\&', '&')
        elif doi:
            link = 'https://doi.org/' + doi.replace('\\_', '_')
        elif key.startswith('DBLP:'):
            link = None
        out[key] = {'title': field('title'), 'link': link}
    return out


def _namey(tok):
    t = tok.strip('.,;:()')
    if not t:
        return False
    return bool(re.match(r'^[A-Z0-9]', t)) or '-' in t or '/' in t or any(c.isupper() for c in t[1:])


def resource_name_before(left):
    """The proper-noun phrase immediately preceding a \\cite, read right-to-left."""
    left = left.rstrip()
    left = left.rstrip('~')
    toks = left.split()
    kept = []
    for tok in reversed(toks):
        if '\\cite' in tok or '~' in tok or '{' in tok or '}' in tok:
            break
        if kept and re.search(r'[,;]$', tok):   # trailing comma = end of a prior list item
            break
        core = tok.strip('.,;:()')
        if _namey(tok):
            kept.append(core)
        elif core.lower() in CONNECTORS and kept:
            kept.append(core)
        else:
            break
    kept.reverse()
    # trim leading/trailing connectors
    while kept and kept[0].lower() in CONNECTORS:
        kept.pop(0)
    while kept and kept[-1].lower() in CONNECTORS:
        kept.pop()
    return ' '.join(kept).strip()


def extract_resources(raw_body, bib):
    """[{name, keys, link}] for each cited resource in a sub-subsection, de-duplicated."""
    out, seen = [], set()
    for m in re.finditer(r'\\cite[a-z]*\{([^}]+)\}', raw_body):
        keys = [k.strip() for k in m.group(1).split(',')]
        name = NAME_OVERRIDE.get(keys[0]) or resource_name_before(raw_body[:m.start()])
        if not name or len(name) < 2:
            continue
        norm = name.lower()
        if norm in seen:
            continue
        seen.add(norm)
        bib_link = None
        for k in keys:
            if bib.get(k, {}).get('link'):
                bib_link = bib[k]['link']
                break
        meta = RES_META.get(name, {})
        # prefer the curated dataset homepage; fall back to the paper link in references.bib
        link = meta.get('url') or bib_link
        out.append({'name': name, 'keys': keys, 'link': link, 'desc': meta.get('desc', '')})
    return out


def first_sentence(text):
    if not text:
        return ''
    m = re.match(r'(.+?[.!?])(\s|$)', text)
    return (m.group(1) if m else text).strip()


def extract_K(tex, bib):
    block = section_span(tex, '\\section{Knowledge Source}', '\\section{Operational Objective}')
    block = strip_comments(block)  # drop commented-out \subsection duplicates first
    # drop the Table 1 float so its LaTeX doesn't bleed into the prose
    block = re.sub(r'\\begin\{table\*\}.*?\\end\{table\*\}', '', block, flags=re.S)
    head, subs = parse_subsections(block)
    head = re.sub(r'^.*?\\label\{sec:knowledge_source\}', '', head, flags=re.S)
    substrates = []
    for title_raw, body in subs:
        name = clean(title_raw)
        (intro, _), subsubs = parse_subsubs(body)
        substrates.append({
            'code': SUB_K.get(name, name),
            'name': name,
            'intro': intro,
            'summary': first_sentence(intro),
            'subsubs': [{
                'title': t,
                'text': x,
                'summary': first_sentence(x),
                'resources': extract_resources(raw, bib),
            } for t, x, raw in subsubs],
        })
    return {'intro': clean(head), 'summary': first_sentence(clean(head)), 'substrates': substrates}


def extract_O(tex):
    # §5 runs until the Method section
    block = section_span(tex, '\\section{Operational Objective}', '\\section{The Scientific RAG Pipeline}')
    block = strip_comments(block)
    block = re.sub(r'\\begin\{table\*\}.*?\\end\{table\*\}', '', block, flags=re.S)
    head, subs = parse_subsections(block)
    head = re.sub(r'^.*?\\label\{sec:benchmark\}', '', head, flags=re.S)
    tasks = []
    for title_raw, body in subs:
        name = clean(title_raw)
        txt = clean(body)
        tasks.append({'name': name, 'rung': TASK_RUNG.get(name, ''),
                      'text': txt, 'summary': first_sentence(txt)})
    return {'intro': clean(head), 'summary': first_sentence(clean(head)), 'tasks': tasks}


STAGE_CODE = {
    'Knowledge Construction and Indexing': 'M1',
    'Retrieval': 'M2',
    'Integration and Generation': 'M3',
    'Verification': 'M4',
}


def extract_M(tex):
    # §6 The Scientific RAG Pipeline, runs until the Evaluation section
    block = section_span(tex, '\\section{The Scientific RAG Pipeline}', '\\section{\\texorpdfstring')
    block = strip_comments(block)
    block = re.sub(r'\\begin\{table\*\}.*?\\end\{table\*\}', '', block, flags=re.S)
    head, subs = parse_subsections(block)
    head = re.sub(r'^.*?\\label\{sec:method\}', '', head, flags=re.S)
    stages = []
    for title_raw, body in subs:
        name = clean(title_raw)
        (intro, _), subsubs = parse_subsubs(body)
        stages.append({
            'code': STAGE_CODE.get(name, name),
            'name': name,
            'intro': intro,
            'summary': first_sentence(intro),
            'subsubs': [{'title': t, 'text': x, 'summary': first_sentence(x)} for t, x, _ in subsubs],
        })
    return {'intro': clean(head), 'summary': first_sentence(clean(head)), 'stages': stages}


def extract_abstract(tex):
    m = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', tex, flags=re.S)
    return clean(m.group(1)) if m else ''


def main():
    tex = TEX.read_text()
    bib = load_bib_links()
    data = {'abstract': extract_abstract(tex),
            'K': extract_K(tex, bib), 'O': extract_O(tex), 'M': extract_M(tex)}
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    ks = data['K']['substrates']
    print(f'K: {len(ks)} substrates, subsubs = ' + ', '.join(f"{s['code']}:{len(s['subsubs'])}" for s in ks))
    print(f'O: {len(data["O"]["tasks"])} tasks')
    print(f'M: {len(data["M"]["stages"])} stages, subsubs = ' + ', '.join(f"{s['code']}:{len(s['subsubs'])}" for s in data['M']['stages']))


if __name__ == '__main__':
    main()
