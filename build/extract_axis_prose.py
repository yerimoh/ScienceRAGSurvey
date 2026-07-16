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
OUT = Path(__file__).resolve().parents[1] / 'data' / 'axis_prose.json'

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


def clean(s):
    s = strip_comments(s)
    # cross-references and citations carry no reader-facing text
    s = re.sub(r'~?\\S?~?\\ref\{[^}]*\}', '', s)
    s = re.sub(r'\\eqref\{[^}]*\}', '', s)
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
    return clean(intro), [(clean(t), clean(b)) for t, b in subs]


def extract_K(tex):
    block = section_span(tex, '\\section{Knowledge Source}', '\\section{Operational Objective}')
    block = strip_comments(block)  # drop commented-out \subsection duplicates first
    # drop the Table 1 float so its LaTeX doesn't bleed into the prose
    block = re.sub(r'\\begin\{table\*\}.*?\\end\{table\*\}', '', block, flags=re.S)
    head, subs = parse_subsections(block)
    head = re.sub(r'^.*?\\label\{sec:knowledge_source\}', '', head, flags=re.S)
    substrates = []
    for title_raw, body in subs:
        name = clean(title_raw)
        intro, subsubs = parse_subsubs(body)
        substrates.append({
            'code': SUB_K.get(name, name),
            'name': name,
            'intro': intro,
            'subsubs': [{'title': t, 'text': x} for t, x in subsubs],
        })
    return {'intro': clean(head), 'substrates': substrates}


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
        tasks.append({'name': name, 'rung': TASK_RUNG.get(name, ''), 'text': clean(body)})
    return {'intro': clean(head), 'tasks': tasks}


def main():
    tex = TEX.read_text()
    data = {'K': extract_K(tex), 'O': extract_O(tex)}
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    ks = data['K']['substrates']
    print(f'K: {len(ks)} substrates, subsubs = ' + ', '.join(f"{s['code']}:{len(s['subsubs'])}" for s in ks))
    print(f'O: {len(data["O"]["tasks"])} tasks')


if __name__ == '__main__':
    main()
