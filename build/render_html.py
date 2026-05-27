#!/usr/bin/env python3
"""Render the full HTML site from data/papers.json.

Outputs:
  index.html                — landing page with K×O grid + search
  about.html                — survey context + methodology
  browse.html               — full paper browser with client-side filter
  cell/<K>.<O>.html         — 12 K×O cell pages
  domain/<dom>.html         — 8 domain pages
  topics/<type>.html        — 4 type pages (method/benchmark/dataset/survey)
"""
import html
import json
import re
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path('/gallery_millet/yerim.oh/ScienceRAGServey/site')
papers = json.loads((ROOT / 'data/papers.json').read_text())

# ---------- Reference tables (mirror generate_content.py) ----------
K_LABELS = {
    'K1': ('Primary Literature', 'Peer-reviewed papers, preprints, scientific corpora (PubMed, arXiv, S2ORC, ChemRxiv, bioRxiv).'),
    'K2': ('Curated Knowledge Base', 'Community-maintained structured records (PubChem, RCSB PDB, AlphaFold DB, ChEMBL, UMLS, PrimeKG, Materials Project, OQMD, AFLOW).'),
    'K3': ('Observational & Experimental', 'Raw modality data: images, spectra, sequencing, time-series (cryo-EM, mass spec, telescope archives, EHR images).'),
    'K4': ('Tacit Knowledge', 'Institutional memory (RHIC, DUNE, CMS), lab protocols, private EHRs, governmental/industry process docs. ★ Novelty axis.'),
}
O_LABELS = {
    'O1': ('Ground', 'Single-source grounding: retrieve, cite, answer over one corpus.'),
    'O2': ('Synthesis', 'Multi-source integration, claim verification across documents.'),
    'O3': ('Hypothesis', 'Generate new scientific candidates — molecules, mechanisms, parameters.'),
}
DOMAIN_LABELS = {
    'bio': 'Biology', 'chem': 'Chemistry', 'medical': 'Medicine',
    'material': 'Materials Science', 'physics': 'Physics', 'earth': 'Earth Science',
    'astronomy': 'Astronomy', 'Quantum': 'Quantum', 'general': 'General Science',
}
DOMAIN_EMOJI = {
    'bio': '🧬', 'chem': '⚗️', 'medical': '🩺', 'material': '🪨',
    'physics': '⚛️', 'earth': '🌍', 'astronomy': '🔭', 'Quantum': '🌀', 'general': '📚',
}
TYPE_LABELS = {
    'Method': 'Methods', 'benchmark': 'Benchmarks',
    'dataset': 'Datasets', 'summary': 'Surveys',
}

O_SUBSECTIONS = {
    'O1': {'Text-only Closed-form QA', 'Text-only Long-form Citation', 'Cross-modal'},
    'O2': {'Aggregative Synthesis', 'Verificative Synthesis'},
    'O3': {'Docking-verified Hypothesis', 'Database-verified Prediction', 'Simulation-verified Materials Discovery', 'Weakly-verified Hypothesis Generation'},
}
K_SUBSECTIONS = {
    'K1': {'General-purpose literature', 'Domain-specific literature', 'Preprint literature'},
    'K2': {'Chemistry and drug discovery', 'Biology and genomics', 'Medicine and clinical knowledge', 'Materials science and physics'},
    'K3': {'Medical imaging and clinical EHR', 'Structural biology', 'Astronomy, earth, and climate', 'Particle and nuclear physics'},
    'K4': {'Embedded in software', 'Held by institutions', 'Held by individuals and communities'},
}
# Per-cell allow-list of O-side subsection chips. Overrides axis_subsections() when the
# cell key is present. Use it to suppress subsections that the cell's overview paragraph
# explicitly assigns to a different cell (e.g. Weakly-verified is a K3.O3/K4.O3 frontier
# concept, so it shouldn't appear as a chip on K2.O3 even when a paper carries that tag
# because of its substrate cell).
CELL_SUBSECTIONS = {
    'K2.O3': {'Docking-verified Hypothesis', 'Database-verified Prediction', 'Simulation-verified Materials Discovery'},
    'K3.O3': {'Weakly-verified Hypothesis Generation'},
    'K4.O3': {'Weakly-verified Hypothesis Generation'},
}
# Cell-tier labels (§4 K×O Cross-Tab Analysis).
# (tier, subsection_name, label_for_hero_chip)
CELL_TIERS = {
    'K1.O1': ('Active',   'Literature-grounded Answering'),
    'K1.O2': ('Active',   'Literature Synthesis'),
    'K2.O1': ('Active',   'Knowledge-base Lookup'),
    'K3.O1': ('Emerging', 'Cross-modal Grounding'),
    'K2.O2': ('Emerging', 'Knowledge-graph Synthesis'),
    'K1.O3': ('Emerging', 'Strong-verifier Hypothesis'),
    'K4.O1': ('Emerging', 'Private-document Retrieval'),
    'K2.O3': ('Frontier', 'Simulation-verified Materials Discovery'),
    'K3.O3': ('Frontier', 'Weakly-verified Hypothesis Generation'),
    'K4.O2': ('Frontier', 'Tacit Synthesis (open)'),
    'K4.O3': ('Frontier', 'Tacit Hypothesis (open)'),
    'K1.O3.weak': ('Frontier', 'Weak-verifier Hypothesis'),
}

def axis_subsections(axis_scope, cell_key=None):
    """Return the set of subsections to render as filter chips.
    If cell_key has a CELL_SUBSECTIONS entry, use that allow-list; otherwise fall
    back to the axis (O1/O2/O3 or K1-K4) default."""
    if cell_key and cell_key in CELL_SUBSECTIONS:
        return CELL_SUBSECTIONS[cell_key]
    if axis_scope in O_SUBSECTIONS:
        return O_SUBSECTIONS[axis_scope]
    if axis_scope in K_SUBSECTIONS:
        return K_SUBSECTIONS[axis_scope]
    return None  # no filtering


def subsec_filter_html(papers_list, prefix='', axis_scope=None, cell_key=None):
    """Return filter-chip bar + inline JS for subsection filtering.
    Only emitted when 2+ distinct subsections exist in papers_list.
    prefix: CSS class prefix to avoid ID collisions between pages.
    cell_key: full cell ID (e.g. 'K2.O3') for per-cell chip allow-list override.
    """
    from collections import Counter
    allowed = axis_subsections(axis_scope, cell_key=cell_key)
    counts = Counter()
    for p in papers_list:
        subs = p.get('subsection') or ''
        items = subs if isinstance(subs, list) else [subs]
        for s in items:
            if not s: continue
            if allowed is not None and s not in allowed: continue
            counts[s] += 1
    if len(counts) < 1:
        return ''
    total = len(papers_list)
    chips = f'<button class="subsec-btn active" data-sub="">All <span class="subsec-n">{total}</span></button>\n'
    for sub, n in sorted(counts.items(), key=lambda x: -x[1]):
        chips += f'<button class="subsec-btn" data-sub="{esc(sub)}">{esc(sub)} <span class="subsec-n">{n}</span></button>\n'
    return f'''<div class="subsec-filter" id="{prefix}subf">
{chips}</div>
<script>
(function(){{
  var bar = document.getElementById('{prefix}subf');
  if (!bar) return;
  bar.querySelectorAll('.subsec-btn').forEach(function(btn){{
    btn.addEventListener('click', function(){{
      bar.querySelectorAll('.subsec-btn').forEach(function(b){{b.classList.remove('active');}});
      btn.classList.add('active');
      var sub = btn.dataset.sub;
      document.querySelectorAll('.card').forEach(function(card){{
        var cardSub = card.dataset.sub || '';
        var cardSubs = cardSub.split(' | ');
        card.style.display = (sub === '' || cardSubs.indexOf(sub) >= 0) ? '' : 'none';
      }});
    }});
  }});
}})();
</script>
'''


def cell_label(code):
    """Convert K/O code to human-readable label, e.g. 'K1.O1' → 'Primary Literature × Ground'."""
    if '.' in code:
        k, o = code.split('.', 1)
        kn = K_LABELS.get(k, (k,))[0]
        on = O_LABELS.get(o, (o,))[0]
        return f'{kn} × {on}'
    if code in K_LABELS:
        return K_LABELS[code][0]
    if code in O_LABELS:
        return O_LABELS[code][0]
    return code

# ---------- Group ----------
by_cell = defaultdict(list)
by_dom = defaultdict(list)
by_type = defaultdict(list)
papers_by_key = {}
for p in papers:
    if p.get('bib_key'):
        papers_by_key[p['bib_key']] = p
    for c in p.get('ko_cells', []):
        by_cell[c].append(p)
    for d in p.get('domain', []):
        by_dom[d].append(p)
    by_type[p.get('type', 'unknown')].append(p)


def esc(s):
    if s is None:
        return ''
    return html.escape(str(s))


def year_sort(p):
    y = p.get('year')
    try:
        return -int(y)
    except (TypeError, ValueError):
        return 0


# ---------- Common HTML pieces ----------
def sidebar(base='', current=''):
    """Render the left sidebar with sticky nav. `current` matches page identifiers like
    'home', 'about', 'insights', 'browse', 'cell/K1.O1', 'domain/bio', 'topics/method'."""

    def cls(key):
        return ' active' if current == key else ''

    # K×O 12 cells
    cell_items = ''
    for K in ['K1', 'K2', 'K3', 'K4']:
        for O in ['O1', 'O2', 'O3']:
            c = f'{K}.{O}'
            n = len(by_cell.get(c, []))
            cell_items += f'<a href="{base}cell/{c}.html" class="sb-sub{cls(f"cell/{c}")}">{cell_label(c)} <span class="sb-count">{n}</span></a>\n'

    # K-only axis pages (K1-K4)
    k_axis_items = ''
    for K in ['K1', 'K2', 'K3', 'K4']:
        n = len(by_cell.get(K, []))
        k_axis_items += f'<a href="{base}cell/{K}.html" class="sb-sub{cls(f"cell/{K}")}">{K_LABELS[K][0]} <span class="sb-count">{n}</span></a>\n'

    # O-only axis pages (O1-O3)
    o_axis_items = ''
    for O in ['O1', 'O2', 'O3']:
        n = len(by_cell.get(O, []))
        o_axis_items += f'<a href="{base}cell/{O}.html" class="sb-sub{cls(f"cell/{O}")}">{O_LABELS[O][0]} <span class="sb-count">{n}</span></a>\n'

    # Domain items
    dom_items = ''
    for d in DOMAIN_LABELS:
        if d not in by_dom:
            continue
        dom_items += f'<a href="{base}domain/{d}.html" class="sb-sub{cls(f"domain/{d}")}">{DOMAIN_EMOJI.get(d,"")} {esc(DOMAIN_LABELS[d])} <span class="sb-count">{len(by_dom[d])}</span></a>\n'

    # Determine if K×O / Domains sections should auto-open
    cell_open = ' open' if current.startswith('cell/') else ''
    dom_open = ' open' if current.startswith('domain/') else ''

    return f'''
<aside class="sidebar" id="sidebar">
  <a href="{base}index.html" class="sb-logo">
    <span class="sb-logo-mark">🔬</span>
    <div class="sb-logo-text">
      <div class="sb-logo-title">Scientific RAG</div>
      <div class="sb-logo-sub">by Vision Lab · SNU</div>
    </div>
  </a>
  <nav class="sb-nav">
    <a href="{base}index.html" class="sb-item{cls("home")}"><span class="sb-icon">🏠</span> Home</a>
    <a href="{base}about.html" class="sb-item{cls("about")}"><span class="sb-icon">🚀</span> Getting Started</a>

    <details class="sb-group"{cell_open}>
      <summary class="sb-item"><span class="sb-icon">▦</span> K×O Grid <span class="sb-caret">▾</span></summary>
      <div class="sb-subs">
        <a href="{base}index.html#grid" class="sb-sub sb-sub-overview">All 12 cells →</a>
        {cell_items}
      </div>
    </details>

    <details class="sb-group"{cell_open}>
      <summary class="sb-item"><span class="sb-icon">K</span> Knowledge Source (K-only) <span class="sb-caret">▾</span></summary>
      <div class="sb-subs">
        {k_axis_items}
      </div>
    </details>

    <details class="sb-group"{cell_open}>
      <summary class="sb-item"><span class="sb-icon">O</span> Operational Objective (O-only) <span class="sb-caret">▾</span></summary>
      <div class="sb-subs">
        {o_axis_items}
      </div>
    </details>

    <details class="sb-group"{dom_open}>
      <summary class="sb-item"><span class="sb-icon">△</span> Domains <span class="sb-caret">▾</span></summary>
      <div class="sb-subs">
        <a href="{base}index.html#domains" class="sb-sub sb-sub-overview">All domains →</a>
        {dom_items}
      </div>
    </details>

    <a href="{base}topics/method.html" class="sb-item{cls("topics/method")}"><span class="sb-icon">⚙</span> Methods <span class="sb-count">{len(by_type.get("Method", []))}</span></a>
    <a href="{base}topics/benchmark.html" class="sb-item{cls("topics/benchmark")}"><span class="sb-icon">📊</span> Benchmarks <span class="sb-count">{len(by_type.get("benchmark", []))}</span></a>
    <a href="{base}topics/dataset.html" class="sb-item{cls("topics/dataset")}"><span class="sb-icon">○</span> Datasets <span class="sb-count">{len(by_type.get("dataset", []))}</span></a>
    <a href="{base}topics/summary.html" class="sb-item{cls("topics/summary")}"><span class="sb-icon">📖</span> Surveys <span class="sb-count">{len(by_type.get("summary", []))}</span></a>

    <hr class="sb-rule">

    <a href="{base}insights.html" class="sb-item{cls("insights")}"><span class="sb-icon">💡</span> Insights</a>
    <a href="{base}browse.html" class="sb-item{cls("browse")}"><span class="sb-icon">🔍</span> Browse all</a>

    <hr class="sb-rule">

    <a href="{base}llms.txt" class="sb-item sb-quiet" title="LLM-friendly index"><span class="sb-icon">📄</span> llms.txt</a>
    <a href="https://github.com/yerimoh/ScienceRAGServey" class="sb-item sb-quiet" target="_blank" rel="noopener"><span class="sb-icon">⌥</span> GitHub ↗</a>
  </nav>
</aside>
'''


def page_head(title, base='', desc='Scientific RAG Hub — a curated catalog of retrieval-augmented generation systems for scientific discovery.', current=''):
    # Cache-bust the CSS using the file's mtime so browsers always pull the latest after a rebuild.
    css_mtime = int((ROOT / 'static/style.css').stat().st_mtime)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} — Scientific RAG Hub</title>
<meta name="description" content="{esc(desc)}">
<link rel="stylesheet" href="{base}static/style.css?v={css_mtime}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ctext y='52' font-size='52'%3E%F0%9F%94%AC%3C/text%3E%3C/svg%3E">
</head>
<body>
<button class="sb-toggle" aria-label="Open navigation" onclick="document.body.classList.toggle('sb-open')">☰</button>
{sidebar(base=base, current=current)}
<div class="sb-backdrop" onclick="document.body.classList.remove('sb-open')"></div>
<main class="with-sidebar">
'''


def page_foot(base=''):
    js_mtime = int((ROOT / 'static/footnotes.js').stat().st_mtime)
    return f'''</main>
<footer class="site-footer">
  <div class="wrap">
    <p>
      <strong>Scientific RAG Hub</strong> — companion catalog to the TPAMI 2026 survey
      <em>"Scientific Retrieval-Augmented Generation: A Survey through Knowledge Source and Scientific Mission"</em>
      by Oh et al. (Vision and Learning Lab, Seoul National University).
    </p>
    <p class="links">
      <a href="{base}llms.txt">llms.txt</a> ·
      <a href="{base}llms-full.txt">llms-full.txt</a> ·
      <a href="{base}data/papers.json">papers.json</a> ·
      <a href="{base}about.html">About</a>
    </p>
  </div>
</footer>
<script src="{base}static/footnotes.js?v={js_mtime}"></script>
</body>
</html>
'''

PAGE_FOOT = page_foot()  # back-compat for callers that still use the constant


def paper_card(p, base='', axis_scope=None):
    title = esc(p.get('title') or p.get('bib_key', '?'))
    url = p.get('paper_link') or ''
    venue = esc(p.get('venue', ''))
    year = esc(p.get('year', ''))
    method = esc(p.get('method', ''))
    note = (p.get('note') or p.get('ko_note') or '').strip()
    if len(note) > 280:
        note = note[:277] + '…'
    note = esc(note)
    cells = p.get('ko_cells', [])
    domains = p.get('domain', [])
    typ = p.get('type', '')
    modality = p.get('modality', [])
    bib_key = p.get('bib_key', '')
    paper_fn = bib_key.replace(':', '_').replace('/', '_') + '.html'
    has_summary = bib_key and (ROOT / 'papers' / paper_fn).exists()

    if url:
        title_html = f'<a href="{esc(url)}" target="_blank" rel="noopener">{title} ↗</a>'
    else:
        title_html = title
    meta_parts = []
    if method and method != title:
        meta_parts.append(f'<span class="meta-method">{method}</span>')
    if venue:
        meta_parts.append(f'<span class="meta-venue">{venue}</span>')
    if year:
        meta_parts.append(f'<span class="meta-year">{year}</span>')
    meta = ' · '.join(meta_parts)

    tag_html = []
    for c in cells:
        tag_html.append(f'<a href="{base}cell/{c}.html" class="tag tag-cell" title="{c}">{cell_label(c)}</a>')
    subsec = p.get('subsection')
    if subsec:
        subs_list = subsec if isinstance(subsec, list) else [subsec]
        allowed = axis_subsections(axis_scope)
        for s in subs_list:
            if not s: continue
            if allowed is not None and s not in allowed: continue
            tag_html.append(f'<span class="tag tag-sub">{esc(s)}</span>')
    for d in domains:
        tag_html.append(f'<a href="{base}domain/{d}.html" class="tag tag-domain">{DOMAIN_EMOJI.get(d, "")}{esc(DOMAIN_LABELS.get(d, d))}</a>')
    if typ and typ != 'unknown':
        tag_html.append(f'<a href="{base}topics/{typ.lower()}.html" class="tag tag-type">{esc(TYPE_LABELS.get(typ, typ))}</a>')
    for m in modality:
        if m and m != 'Text':
            tag_html.append(f'<span class="tag tag-mod">{esc(m)}</span>')
    if p.get('cross_source'):
        tag_html.append('<span class="tag tag-xs">★ cross-source</span>')

    summary_link = (f'<a href="{base}papers/{paper_fn}" class="card-summary-link">Summary →</a>'
                    if has_summary else '')

    _subsec_val = p.get("subsection", "") or ""
    if isinstance(_subsec_val, list):
        _subsec_items = [s for s in _subsec_val if s]
    elif _subsec_val:
        _subsec_items = [_subsec_val]
    else:
        _subsec_items = []
    _allowed = axis_subsections(axis_scope)
    if _allowed is not None:
        _subsec_items = [s for s in _subsec_items if s in _allowed]
    subsec_attr = f' data-sub="{esc(" | ".join(_subsec_items))}"'
    return f'''<article class="card"{subsec_attr}>
  <h3 class="card-title">{title_html}</h3>
  {f'<div class="card-meta">{meta}</div>' if meta else ''}
  {f'<p class="card-note">{note}</p>' if note else ''}
  <div class="card-tags">{''.join(tag_html)}</div>
  {summary_link}
</article>
'''


# ---------- index.html ----------
def render_index():
    parts = [page_head('Home', base='', current='home')]
    parts.append(f'''
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">AI for Science · Retrieval-Augmented Generation</p>
    <h1>The catalog of scientific RAG systems, organized by Knowledge × Mission.</h1>
    <p class="lede">
      <strong>{len(papers)}</strong> methods, benchmarks, and datasets across
      <strong>{len(by_dom)}</strong> scientific domains —
      classified by a dual-axis taxonomy of Knowledge Source (K) × Operational Objective (O).
      Companion to the TPAMI 2026 survey by Oh et al.
    </p>
    <div class="hero-search">
      <input id="q" type="search" placeholder="Search by title, method, dataset, venue, or tag…" autofocus>
      <span class="hero-search-hint">↵ to filter on <a href="browse.html">Browse</a></span>
    </div>
    <div class="hero-cta">
      <a href="#grid" class="btn">Explore K×O grid</a>
      <a href="browse.html" class="btn btn-secondary">Browse all {len(papers)}</a>
      <a href="about.html" class="btn btn-ghost">Read about the taxonomy</a>
    </div>
  </div>
</section>

<section id="grid" class="ko-grid-section">
  <div class="wrap">
    <h2 class="section-title">The K×O Grid — 12 cells</h2>
    <p class="section-sub">
      Each cell pairs a <em>knowledge source</em> (K, row) with an <em>operational objective</em> (O, column).
      Cell counts include cross-listed cross-source papers. Sparse cells <strong>[K3.O3]</strong> and
      <strong>[K4.O3]</strong> are explicit frontier opportunities in §11.
    </p>
    <table class="ko-grid">
      <thead>
        <tr>
          <th class="corner"></th>
''')
    for O in ['O1', 'O2', 'O3']:
        on, od = O_LABELS[O]
        parts.append(f'          <th class="o-head"><span class="cell-axis">{O}</span> {esc(on)}<span class="cell-axis-desc">{esc(od)}</span></th>\n')
    parts.append('        </tr>\n      </thead>\n      <tbody>\n')

    for K in ['K1', 'K2', 'K3', 'K4']:
        kn, kd = K_LABELS[K]
        parts.append(f'        <tr>\n          <th class="k-head"><span class="cell-axis">{K}</span> {esc(kn)}<span class="cell-axis-desc">{esc(kd)}</span></th>\n')
        for O in ['O1', 'O2', 'O3']:
            cell = f'{K}.{O}'
            ps = by_cell.get(cell, [])
            n = len(ps)
            heat = 'heat-zero' if n == 0 else 'heat-low' if n < 5 else 'heat-mid' if n < 20 else 'heat-high'
            top = sorted(ps, key=year_sort)[:3]
            top_html = '\n'.join(
                f'<li>{esc((p.get("method") or p.get("title") or "?")[:60])}</li>' for p in top
            )
            frontier = ' frontier' if (n <= 3 and K in ('K3', 'K4') and O == 'O3') else ''
            parts.append(f'''          <td class="ko-cell {heat}{frontier}">
            <a href="cell/{cell}.html" class="cell-link">
              <span class="cell-id">[{cell}]</span>
              <span class="cell-count">{n}</span>
              <ul class="cell-top">{top_html}</ul>
            </a>
          </td>
''')
        parts.append('        </tr>\n')
    parts.append('      </tbody>\n    </table>\n  </div>\n</section>\n')

    # Domains row
    parts.append('''
<section id="domains" class="domains-section">
  <div class="wrap">
    <h2 class="section-title">By scientific domain</h2>
    <div class="domain-grid">
''')
    for d, label in DOMAIN_LABELS.items():
        if d not in by_dom:
            continue
        n = len(by_dom[d])
        parts.append(f'''      <a href="domain/{d}.html" class="domain-card">
        <span class="domain-emoji">{DOMAIN_EMOJI.get(d, "")}</span>
        <span class="domain-name">{esc(label)}</span>
        <span class="domain-count">{n} entries</span>
      </a>
''')
    parts.append('    </div>\n  </div>\n</section>\n')

    # Type row
    parts.append('''
<section class="types-section">
  <div class="wrap">
    <h2 class="section-title">By resource type</h2>
    <div class="type-grid">
''')
    for t, label in TYPE_LABELS.items():
        if t not in by_type:
            continue
        n = len(by_type[t])
        parts.append(f'      <a href="topics/{t.lower()}.html" class="type-card"><strong>{esc(label)}</strong><span>{n}</span></a>\n')
    parts.append('    </div>\n  </div>\n</section>\n')

    # Flagships strip
    flagships_file = ROOT / 'build/flagships.json'
    flagships = json.loads(flagships_file.read_text()).get('flagships', [])
    by_bib = {p.get('bib_key'): p for p in papers}
    parts.append('''
<section class="flagship-section">
  <div class="wrap">
    <h2 class="section-title">Flagship systems — start here</h2>
    <p class="section-sub">Nine papers that either set the modern bar (Nature, NeurIPS, AAAI) or open a structural gap. <a href="insights.html#flagships">See full Insights →</a></p>
    <div class="flagship-strip">
''')
    for f in flagships:
        p = by_bib.get(f['bib_key'], {})
        url = p.get('paper_link') or ''
        big = f['headline_stats'][0]
        title = esc(p.get('title') or f['name'])
        title_link = f'<a href="{esc(url)}" target="_blank" rel="noopener">{title}</a>' if url else title
        parts.append(f'''      <article class="fl-mini">
        <div class="fl-mini-big"><span class="fl-mini-num">{esc(big[0])}</span><span class="fl-mini-label">{esc(big[1])}</span></div>
        <h3 class="fl-mini-name">{esc(f['name'])}</h3>
        <p class="fl-mini-tag">{esc(f['tagline'])}</p>
        <div class="fl-mini-meta"><a href="cell/{f['cell']}.html" class="tag tag-cell" title="{f['cell']}">{cell_label(f['cell'])}</a> <span class="muted">{esc(f['venue'])}</span></div>
        <p class="fl-mini-cite">{title_link}</p>
      </article>
''')
    parts.append('    </div>\n  </div>\n</section>\n')

    # Recent additions
    recent = sorted([p for p in papers if str(p.get('year', '')).isdigit() and int(p['year']) >= 2025], key=year_sort)[:9]
    parts.append('''
<section class="recent-section">
  <div class="wrap">
    <h2 class="section-title">Recently added (2025-2026)</h2>
    <div class="card-grid">
''')
    for p in recent:
        parts.append(paper_card(p))
    parts.append('    </div>\n  </div>\n</section>\n')

    # Inline search JS hook
    parts.append('''
<script>
document.getElementById('q')?.addEventListener('keydown', e => {
  if (e.key === 'Enter') {
    const q = encodeURIComponent(e.target.value);
    window.location.href = 'browse.html?q=' + q;
  }
});
</script>
''')
    parts.append(PAGE_FOOT)
    (ROOT / 'index.html').write_text(''.join(parts))


# ---------- about.html ----------
def render_about():
    cell_counts = '\n'.join(
        f'    <tr><th>{c}</th><td>{len(by_cell.get(c, []))}</td><td>{esc(K_LABELS[c.split(".")[0]][0])} × {esc(O_LABELS[c.split(".")[1]][0])}</td></tr>'
        for K in ['K1', 'K2', 'K3', 'K4'] for O in ['O1', 'O2', 'O3'] for c in [f'{K}.{O}']
    )
    body = f'''
<section class="prose">
  <div class="wrap">
    <h1>About Scientific RAG Hub</h1>
    <p class="lede">
      A curated catalog of <strong>{len(papers)} retrieval-augmented generation</strong> systems,
      benchmarks, and datasets across the sciences — the companion resource to the TPAMI 2026 survey
      <em>"Scientific Retrieval-Augmented Generation: A Survey through Knowledge Source and Scientific Mission."</em>
    </p>

    <h2>The K×O taxonomy</h2>
    <p>
      We argue that scientific RAG is a <em>deterministic engine</em> constrained by physical laws,
      stoichiometric exactness, and experimental protocols — not by the probabilistic semantic proximity
      on which general-purpose RAG depends. Two axes capture what most shapes a scientific RAG system:
    </p>
    <h3>Knowledge Source (K) — what you draw upon</h3>
    <ul>
      <li><strong>K1 Primary Literature</strong> — peer-reviewed papers, preprints, scientific corpora.</li>
      <li><strong>K2 Curated Knowledge Base</strong> — community-maintained structured records (PubChem, RCSB PDB, Materials Project…).</li>
      <li><strong>K3 Observational & Experimental</strong> — image, spectra, sequencing, time-series modalities.</li>
      <li><strong>K4 Tacit Knowledge</strong> — institutional memory, lab protocols, private EHRs, industry process docs. ★ Novelty axis.</li>
    </ul>
    <h3>Operational Objective (O) — what you do with it</h3>
    <ul>
      <li><strong>O1 Ground</strong> — single-source grounding (retrieve · cite · answer).</li>
      <li><strong>O2 Synthesis</strong> — multi-source integration, claim verification.</li>
      <li><strong>O3 Hypothesis</strong> — generate new candidates (molecules, mechanisms, parameters).</li>
    </ul>

    <h2>Why this taxonomy</h2>
    <p>
      Existing RAG surveys classify systems by retriever-generator pipeline. That view misses what most
      shapes a <em>scientific</em> RAG system: the epistemic tier of the source and the scientific operation
      performed on it. The K×O grid surfaces structural patterns invisible to pipeline-centric views —
      dense cells (e.g. <strong>[K1.O1]</strong> medical QA, <strong>[K2.O3]</strong> drug/catalyst generation),
      and frontier cells (<strong>[K3.O3]</strong>, <strong>[K4.O3]</strong>) where opportunity remains.
    </p>

    <h2>Cell distribution</h2>
    <table class="ko-stat">
      <thead><tr><th>Cell</th><th>Count</th><th>K × O</th></tr></thead>
      <tbody>
{cell_counts}
      </tbody>
    </table>

    <h2>Five Unique Requirements of Scientific RAG</h2>
    <ol>
      <li><strong>Mandatory Claim Attribution</strong> — every claim traceable to source unit.</li>
      <li><strong>Relational Knowledge Coupling</strong> — facts in webs (PDB ↔ UniProt ↔ ChEMBL); traverse couplings.</li>
      <li><strong>Source Reliability Tiering</strong> — paper / preprint / curated / lab-note carry different epistemic weight.</li>
      <li><strong>Protocol-level Reproducibility</strong> — enough method detail for expert to reproduce.</li>
      <li><strong>Domain-Native Representations</strong> — SMILES, InChI, FASTA, LaTeX, CIF, DICOM — no text flattening.</li>
    </ol>

    <h2>How to use the catalog</h2>
    <ul>
      <li><a href="index.html#grid">K×O Grid</a> — pick a cell to see all systems landing there.</li>
      <li><a href="index.html#domains">Domains</a> — browse by scientific field.</li>
      <li><a href="browse.html">Browse</a> — full searchable, filterable catalog.</li>
      <li><a href="llms.txt">/llms.txt</a> · <a href="llms-full.txt">/llms-full.txt</a> — LLM-friendly indices.</li>
      <li><a href="data/papers.json">papers.json</a> — full machine-readable dump (one JSON, all metadata).</li>
    </ul>

    <h2>Survey Construction Pipeline</h2>
    <p>The following diagram shows how the catalog and companion survey were built end-to-end.</p>

    <div class="pipeline-diagram">
      <!-- Row 1: Sources -->
      <div class="pipe-row pipe-row-sources">
        <div class="pipe-node pipe-node-src">
          <div class="pipe-icon">📄</div>
          <div class="pipe-label">Literature<br><span class="pipe-sub">arXiv · PubMed · ACL · NeurIPS…</span></div>
        </div>
        <div class="pipe-node pipe-node-src">
          <div class="pipe-icon">🗂</div>
          <div class="pipe-label">Notion DB<br><span class="pipe-sub">{len(papers)} papers tracked</span></div>
        </div>
        <div class="pipe-node pipe-node-src">
          <div class="pipe-icon">📚</div>
          <div class="pipe-label">references.bib<br><span class="pipe-sub">master bibliography</span></div>
        </div>
      </div>

      <div class="pipe-arrow-down">▼</div>

      <!-- Row 2: Classification -->
      <div class="pipe-row pipe-row-classify">
        <div class="pipe-node pipe-node-classify pipe-wide">
          <div class="pipe-icon">🔬</div>
          <div class="pipe-label"><strong>K × O Dual-Axis Classification</strong></div>
          <div class="pipe-classify-grid">
            <div class="pipe-axis pipe-axis-k">
              <div class="pipe-axis-label">K — Knowledge Source</div>
              <div class="pipe-axis-items">
                <span class="pipe-pill pipe-k1">K1 Primary Lit</span>
                <span class="pipe-pill pipe-k2">K2 Curated KB</span>
                <span class="pipe-pill pipe-k3">K3 Obs/Exp</span>
                <span class="pipe-pill pipe-k4">K4 Tacit</span>
              </div>
            </div>
            <div class="pipe-axis-times">×</div>
            <div class="pipe-axis pipe-axis-o">
              <div class="pipe-axis-label">O — Operational Objective</div>
              <div class="pipe-axis-items">
                <span class="pipe-pill pipe-o1">O1 Ground</span>
                <span class="pipe-pill pipe-o2">O2 Synthesis</span>
                <span class="pipe-pill pipe-o3">O3 Hypothesis</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="pipe-arrow-down">▼</div>

      <!-- Row 3: 12-cell grid -->
      <div class="pipe-row pipe-row-grid">
        <div class="pipe-node pipe-node-grid pipe-wide">
          <div class="pipe-icon">▦</div>
          <div class="pipe-label"><strong>12-Cell K×O Taxonomy</strong></div>
          <div class="pipe-mini-grid">
            {"".join(
              f'<a href="cell/{K}.{O}.html" class="pipe-cell pipe-cell-{"h" if len(by_cell.get(f"{K}.{O}",[]))>=10 else "m" if len(by_cell.get(f"{K}.{O}",[]))>=3 else "l"}" title="{K}.{O}: {len(by_cell.get(f"{K}.{O}",[])) } entries">'
              f'<span class="pipe-cell-id">{K}·{O}</span>'
              f'<span class="pipe-cell-n">{len(by_cell.get(f"{K}.{O}",[]))}</span>'
              f'</a>'
              for K in ["K1","K2","K3","K4"] for O in ["O1","O2","O3"]
            )}
          </div>
          <div class="pipe-grid-legend">
            <span class="pipe-cell-dot pipe-cell-h"></span> ≥10 &nbsp;
            <span class="pipe-cell-dot pipe-cell-m"></span> 3–9 &nbsp;
            <span class="pipe-cell-dot pipe-cell-l"></span> 0–2 (frontier)
          </div>
        </div>
      </div>

      <div class="pipe-arrow-down">▼</div>

      <!-- Row 4: Outputs -->
      <div class="pipe-row pipe-row-outputs">
        <div class="pipe-node pipe-node-out">
          <div class="pipe-icon">🌐</div>
          <div class="pipe-label">This Site<br><span class="pipe-sub">Browse · Filter · Search</span></div>
        </div>
        <div class="pipe-node pipe-node-out">
          <div class="pipe-icon">📖</div>
          <div class="pipe-label">TPAMI Survey<br><span class="pipe-sub">Oh et al. 2026</span></div>
        </div>
        <div class="pipe-node pipe-node-out">
          <div class="pipe-icon">📄</div>
          <div class="pipe-label">papers.json<br><span class="pipe-sub">machine-readable</span></div>
        </div>
      </div>
    </div>

    <h2>Methodology</h2>
    <p>
      Entries are sourced from a Notion-tracked literature database curated by the Vision and Learning Lab,
      cross-referenced against the survey's master bibliography. K×O assignments are author-verified for
      138 papers via full Notion fetch; the remaining ~44 are tagged provisionally pending re-verification.
      Cross-source papers (e.g. <strong>MedGraphRAG</strong> spanning K1+K2+K4) appear in multiple cells.
    </p>

    <h2>Contributing</h2>
    <p>
      Missing entries, mis-classifications, or new systems? Open an issue or PR on the
      GitHub repo. The build is fully deterministic — edit <code>data/ko_assignments.json</code>
      (or the source Notion DB) and re-run <code>build/render_html.py</code>.
    </p>

    <h2>Cite</h2>
    <pre><code>@article{{oh2026sciragsurvey,
  title   = {{Scientific Retrieval-Augmented Generation: A Survey through
             Knowledge Source and Scientific Mission}},
  author  = {{Oh, Yerim and others}},
  journal = {{IEEE Transactions on Pattern Analysis and Machine Intelligence}},
  year    = {{2026}}
}}</code></pre>
  </div>
</section>
'''
    (ROOT / 'about.html').write_text(page_head('About', current='about') + body + PAGE_FOOT)


# ---------- browse.html (client-side filter) ----------
def render_browse():
    domain_opts = '\n'.join(f'<option value="{d}">{esc(DOMAIN_LABELS[d])} ({len(by_dom[d])})</option>' for d in DOMAIN_LABELS if d in by_dom)
    type_opts = '\n'.join(f'<option value="{t}">{esc(TYPE_LABELS[t])} ({len(by_type[t])})</option>' for t in TYPE_LABELS if t in by_type)
    cell_opts = '\n'.join(f'<option value="{K}.{O}">[{K}.{O}] {esc(K_LABELS[K][0])} × {esc(O_LABELS[O][0])} ({len(by_cell.get(K+"."+O, []))})</option>' for K in ['K1','K2','K3','K4'] for O in ['O1','O2','O3'])
    from collections import Counter
    sub_counts = Counter()
    for p in papers:
        s = p.get('subsection') or ''
        if isinstance(s, list):
            for v in s:
                if v: sub_counts[v] += 1
        elif s:
            sub_counts[s] += 1
    sub_opts = '\n'.join(f'<option value="{esc(s)}">{esc(s)} ({n})</option>' for s, n in sorted(sub_counts.items(), key=lambda x: -x[1]))
    body = f'''
<section class="browse-hero">
  <div class="wrap">
    <h1>Browse all {len(papers)} entries</h1>
    <p class="lede">Filter by K×O cell, subsection, domain, type, or year.</p>
    <div class="filters">
      <input id="q" type="search" placeholder="Search…" autofocus>
      <select id="f-cell"><option value="">All K×O cells</option>{cell_opts}</select>
      <select id="f-sub"><option value="">All subsections</option>{sub_opts}</select>
      <select id="f-domain"><option value="">All domains</option>{domain_opts}</select>
      <select id="f-type"><option value="">All types</option>{type_opts}</select>
      <select id="f-year">
        <option value="">All years</option>
        <option value="2026">2026</option>
        <option value="2025">2025</option>
        <option value="2024">2024</option>
        <option value="2023">2023</option>
        <option value="<2023">≤ 2022</option>
      </select>
      <button id="f-reset" type="button">Reset</button>
      <span id="result-count" class="result-count"></span>
    </div>
  </div>
</section>

<section class="browse-list">
  <div class="wrap">
    <div id="cards" class="card-grid"></div>
    <p id="empty" class="empty" hidden>No matching entries — try a broader search.</p>
  </div>
</section>

<script src="static/search.js"></script>
'''
    (ROOT / 'browse.html').write_text(page_head('Browse', base='', current='browse') + body + PAGE_FOOT)


# ---------- cell/<K>.<O>.html ----------
SECTION_OVERVIEWS = {
    'K1.O1': {
        'subsection': 'Literature-grounded Answering',
        'subsubsec_id': 'subsubsec:kxo_k1o1',
        'paragraph': r'''A system operating under the \textcolor{Oaxis}{\textsc{Ground}} objective retrieves information over PubMed~\cite{canese2013pubmed}, full-text articles, or open-access corpora to utilize \textcolor{Kaxis}{\textsc{Primary Literature}}, producing either a closed-form verdict or a cited paragraph anchored to the retrieved sources so that its factual accuracy and citation fidelity can be rigorously evaluated. The methodologies developed for this intersection include retrieval-augmented generation (RAG) frameworks such as MEDRAG~\cite{DBLP:conf/acl/Xiong0LZ24}, BioRAG~\cite{DBLP:journals/corr/abs-2408-01107}, and RAG$^2$~\cite{DBLP:conf/naacl/SohnPYPHSKK25} on the closed-form side, alongside PaperQA~\cite{DBLP:journals/corr/abs-2312-07559}, OpenScholar~\cite{asai2026synthesizing}, and Clinfo.ai~\cite{DBLP:journals/corr/abs-2310-16146} on the long-form citation side. Activity within this domain follows from the parallel growth of multiple-choice and short-answer benchmarks, dense and hybrid retrievers optimized for scientific text, and citation-based evaluations that facilitate automated verification.''',
        'evidence': {
            'canese2013pubmed': 'PubMed — NCBI biomedical literature index (≈36M citations). Foundational substrate for medical/biological RAG: free-text abstracts indexed under MeSH, with ~1M new papers/year.',
            'DBLP:conf/acl/Xiong0LZ24': 'MEDRAG / MIRAGE: "Benchmarking Retrieval-Augmented Generation for Medicine" — 7,663 multiple-choice questions across 5 medical QA datasets (MMLU-Med, MedQA-US, MedMCQA, PubMedQA, BioASQ-Y/N); zero-shot + question-only retrieval (ACL Findings 2024 pp.6233-6251).',
            'DBLP:journals/corr/abs-2408-01107': 'BioRAG: "A RAG-LLM Framework for Biological Question Reasoning" — 22M+ PubMed abstracts + MeSH classifier + 5-step iterative RAG with 10 external sources. Evaluated on GeneTuring 9 sub-tasks + MedMCQA + College Biology/Medicine (arXiv:2408.01107).',
            'DBLP:conf/naacl/SohnPYPHSKK25': 'RAG² (Rationale-Guided RAG): perplexity-trained filtering model + LLM-generated rationale queries + balanced retrieval over 4 corpora (PubMed/PMC/textbooks/guidelines). Evaluated on three closed-book medical QA benchmarks: MedQA, MedMCQA, MMLU-Med (NAACL 2025 pp.12739-12753).',
            'DBLP:journals/corr/abs-2312-07559': 'PaperQA (Lála et al., FutureHouse): agent-based RAG over full-text scientific articles, sentence-level claim attribution. Beats GPT-4 by 30 points on closed-book PubMedQA (86.3% vs 57.9%); introduces LitQA benchmark requiring full-text synthesis (arXiv:2312.07559).',
            'asai2026synthesizing': 'OpenScholar (Asai et al., Nature 2026 / arXiv:2411.14199): retrieval-augmented LM over 45M open-access papers; SCHOLARQABENCH with 2,967 expert queries + 208 long-form answers. GPT-4o hallucinates citations 78-90%, OPENSCHOLAR-8B beats GPT-4o by 5% in correctness with human-expert citation accuracy.',
            'DBLP:journals/corr/abs-2310-16146': 'Clinfo.ai (Lozano, Fleming, Chiang, Shah — Stanford): open-source clinical QA WebApp + abstractive summarization task. Releases PubMedRS-200: 200 questions + answers derived from published systematic reviews (arXiv:2310.16146).',
        },
    },
    'K3.O3': {
        'subsection': 'Weakly-verified Hypothesis Generation',
        'subsubsec_id': 'subsubsec:o3-weakverifier',
        'paragraph': r'''A final form of hypothesis is one in which the system generates a candidate that no strong external verifier can directly check, so that evaluation falls back to downstream task accuracy, expert validation, or recovery against a held-out reference rather than to docking, database lookup, or simulation. The output is typically a literature-derived hypothesis, such as a cellular-response prediction, a biomedical link prediction, or a molecular structure inferred from a non-textual signal, and the absence of an in-loop verifier means that novelty and plausibility carry more of the evaluation burden than physical correctness does. Evaluation in this setting consists of distributional similarity for predicted perturbation responses, held-out edge recovery for link-prediction tasks, and Top-K accuracy or Tanimoto similarity against held-out reference structures for measurement-derived candidates, instantiated on retrieval-augmented gene-perturbation cellular response prediction~\cite{DBLP:journals/corr/abs-2603-07233} over the Replogle-Nadig single-gene perturbation subset~\cite{replogle2022mapping} of the Perturb-seq atlas, against the PerturBench benchmark~\cite{DBLP:journals/corr/abs-2408-10609} which standardizes four generalization regimes for cellular perturbation analysis and against the held-out perturbation evaluation protocol introduced by GEARS~\cite{roohani2024gears} on Norman 2019 dual-gene combinations~\cite{norman2019exploring}, on biomedical link prediction over OpenBioLink~\cite{DBLP:journals/bioinformatics/BreitOAS20} and OGB-biokg~\cite{DBLP:conf/nips/HuFZDRLCL20}, and on MS/MS-driven molecular discovery in the MassSpecGym benchmark~\cite{DBLP:conf/nips/BushuievBJYKSHW24} with three challenges spanning de novo molecular structure generation, molecule retrieval, and spectrum simulation. These metrics certify that the generated hypotheses recover known cases or align with expert intuition, but the absence of a strong external verifier leaves the K3.O3 and K4.O3 cells of the catalog largely empty, a sparsity we revisit in \S\ref{sec:frontiers} as a concrete frontier for future scientific RAG.''',
        'evidence': {
            'DBLP:journals/corr/abs-2603-07233': 'PT-RAG (Perturbation-aware Two-stage RAG): GenePT semantic retrieval + Gumbel-Softmax cell-type-aware selection. Outperforms STATE and vanilla RAG on Replogle-Nadig single-gene perturbation in distributional similarity W1, W2 (arXiv:2603.07233 §Abstract).',
            'replogle2022mapping': 'Genome-scale Perturb-seq atlas — foundational single-cell perturbation dataset across thousands of essential genes; substrate for PT-RAG (Replogle et al., Cell 2022).',
            'DBLP:journals/corr/abs-2408-10609': 'PerturBench: "comprehensive framework for modeling single cell transcriptomic responses to perturbations, aimed at standardizing benchmarking in this rapidly evolving field" with RMSE + rank metrics across four generalization regimes (arXiv:2408.10609 §Abstract).',
            'roohani2024gears': 'GEARS: GNN integrating gene-gene knowledge graph with perturbation embedding. Trained on Norman 2019 (102 single + 131 two-gene). Metrics: MSE on top-20 DEGs, Pearson correlation, Precision@10 for GI prediction (Nat. Biotechnol. 42:927-935, 2024).',
            'norman2019exploring': 'Norman et al. 2019 Science: 287 dual-CRISPRi gene-pair perturbations in K562 cells. Defined "GI manifold" via rich single-cell phenotypes — the canonical dual-gene held-out evaluation substrate (Science 365:786-793, 2019).',
            'DBLP:journals/bioinformatics/BreitOAS20': 'OpenBioLink: "a large-scale, high-quality and highly challenging biomedical link prediction benchmark to transparently and reproducibly evaluate" embedding methods. Leakage-controlled held-out edge recovery (Bioinformatics 36:4097-4098, 2020).',
            'DBLP:conf/nips/HuFZDRLCL20': 'OGB suite (NeurIPS 2020) — includes ogbl-biokg for biomedical KG link prediction (drug-disease-protein edges) with hits@K public leaderboard. Same authors as GEARS (Leskovec lab).',
            'DBLP:conf/nips/BushuievBJYKSHW24': 'MassSpecGym: 231K MS/MS spectra of 29K molecules with leakage-controlled MCES splits. Three challenges: de novo molecular structure generation, molecule retrieval, spectrum simulation (NeurIPS 2024 / arXiv:2410.23326 §Intro).',
        },
    },
    'K2.O3': {
        'subsection': 'Simulation-verified Materials Discovery',
        'subsubsec_id': 'subsubsec:o3-simulation',
        'paragraph': r'''A third form of hypothesis is one in which the system proposes new material candidates and a physics-based simulator serves as the external verifier, returning thermodynamic stability and reaction-energy profiles through density functional theory or end-to-end computational results through executed scientific code. The output is either a candidate crystal, a relaxed adsorbate-surface configuration, or a metal-organic framework selected for a sorbent target, and novelty is measured against an existing materials database while validity is measured against the simulator's physical predictions. Evaluation in this setting consists of stable-crystal classification with \(F_1\) and discovery-acceleration factor on the WBM corpus of about 257K candidate structures in Matbench Discovery~\cite{riebesell2025matbench}, validity and coverage of generated crystals on the MP-20, Carbon-24, and Perov-5 splits in CDVAE~\cite{DBLP:conf/iclr/XieFGBJ22}, lowest-energy adsorbate-surface identification rate with roughly \(2{,}000\times\) simulator-time speedup over about 1,000 catalyst surfaces and about 100K configurations in ADsorbML~\cite{lan2023adsorbml}, sorbent-screening targets backed by about 38M density-functional calculations over 8,400 metal-organic frameworks in ODAC23~\cite{sriram2024odac23}, foundation machine-learning interatomic potential training and evaluation splits drawn from about 110M density-functional calculations with WBM-disjoint test sets in OMat24~\cite{DBLP:journals/corr/abs-2410-12771}, physics-aware tests of force smoothness, phase transitions, gas adsorption, and vacancy migration beyond DFT-error metrics in MLIP Arena~\cite{DBLP:journals/corr/abs-2509-20630}, multi-verifier coverage across about 1,500 tasks and eleven categories in JARVIS-Leaderboard~\cite{choudhary2024jarvis}, and 102 executable-code tasks drawn from 44 peer-reviewed publications in ScienceAgentBench~\cite{DBLP:journals/corr/abs-2410-05080}. These benchmarks certify that proposed candidates pass simulation-based checks at orders-of-magnitude greater throughput than traditional high-throughput screening, but density functional theory and code execution themselves rely on functionals, parameter choices, and software assumptions whose limits the simulator cannot diagnose from within.''',
        'evidence': {
            'riebesell2025matbench': 'WBM 215,488 unique prototypes after cleaning, 32,942 stable. Top model eqV2 S DeNS reaches F1=0.815 with DAF=5.042 (arXiv:2308.14920 §2.1 + Table 1).',
            'DBLP:conf/iclr/XieFGBJ22': 'Three datasets: Perov-5 (18,928 perovskites, 56 elements, 5 atoms/cell), Carbon-24 (10,153 C-only, 6-24 atoms), MP-20. Metrics: Validity (>0.5 Å), COV-R/COV-P, EMD (arXiv:2110.06197 §5).',
            'lan2023adsorbml': 'Open Catalyst Dense: 989 unique adsorbate-surface systems × 105,714 configurations. Balanced ML+SP (k=3, eSCN-MD-Large): 87.36% success × 2,290× DFT speedup (arXiv:2211.16486 §Abstract + Fig. 3).',
            'sriram2024odac23': '4,942 pristine + 3,470 defective + 114 ultrastable MOFs. 170K converged adsorption energies, 38M+ single-point DFT, 400M core-hours. OC20-style S2EF/IS2RE/IS2RS tasks (arXiv:2311.00341 §Methods).',
            'DBLP:journals/corr/abs-2410-12771': '118M structures total: 100M train / 5M val / 5M ID-test + WBM-disjoint test + OOD-Elemental 619K. F1 > 0.9 stability, MAE 20 meV/atom formation energy. All top Matbench leaderboard models adopted OMat24 (arXiv:2410.12771 §2).',
            'DBLP:journals/corr/abs-2509-20630': 'Four physics-aware categories: Asymptotic (EOS on 1,000 WBM + diatomic PEC), Stability & Reactivity (NVT/NPT MD on RM24, H2 combustion), Distribution Shifts, Thermodynamic Properties (arXiv:2509.20630 §2 + Fig. 1).',
            'choudhary2024jarvis': '274 benchmarks, 1,281 contributions, 152 methods, 8M+ data points across AI/ES/FF/QC/EXP categories. Naming convention: Category-Subcategory-Target-Dataset-Split-Metric (arXiv:2306.11688 §Abstract).',
            'DBLP:journals/corr/abs-2410-05080': '102 tasks from 44 peer-reviewed publications across 4 disciplines (Bioinformatics, Computational Chemistry, GIS, Psychology). Each task: instruction + dataset + expert knowledge + annotated program. Best agent: 32.4% independent (arXiv:2410.05080 §2).',
        },
    },
}


def render_overview_section(cell_key, papers_by_key, base='../'):
    """Render a survey section overview paragraph with footnote-popover citations."""
    o = SECTION_OVERVIEWS.get(cell_key)
    if not o:
        return ''
    text = o['paragraph']
    evidence_map = o.get('evidence', {})
    cite_order = []

    def cite_repl(m):
        key = m.group(1)
        if key not in cite_order:
            cite_order.append(key)
        n = cite_order.index(key) + 1
        return f'<sup class="footnote-ref" id="fnref-ov{n}"><a href="#fn-ov{n}">{n}</a></sup>'

    html_text = re.sub(r'\\cite\{([^}]+)\}', cite_repl, text)
    html_text = html_text.replace('~', '&nbsp;')
    html_text = re.sub(r'\\\(([^)]+)\\\)', r'<em>\1</em>', html_text)
    html_text = html_text.replace(r'{,}', ',').replace(r'\times', '×')

    fn_items = []
    for i, key in enumerate(cite_order, 1):
        p = papers_by_key.get(key, {})
        title = p.get('title', key)
        method = p.get('method', '')
        safe_key = key.replace(':', '_').replace('/', '_')
        ev = evidence_map.get(key, '')
        label = method or title or key
        body = f'<p><strong>{esc(label)}</strong>'
        if title and title != label:
            body += f' — <em>{esc(title)}</em>'
        body += '</p>'
        if ev:
            body += f'<p>{esc(ev)}</p>'
        # Prefer in-site summary if a .md/.html exists; otherwise external paper link
        summary_path = ROOT / 'papers' / f'{safe_key}.html'
        if summary_path.exists():
            body += f'<p><a href="{base}papers/{safe_key}.html">Full summary &rarr;</a></p>'
        elif p.get('paper_link'):
            body += f'<p><a href="{esc(p["paper_link"])}" target="_blank" rel="noopener">Source &uarr;</a></p>'
        fn_items.append(f'<li id="fn-ov{i}">{body}</li>')

    fn_html = '<section class="footnotes overview-fns"><h3>Citations</h3><ol>' + ''.join(fn_items) + '</ol></section>'

    return f'''
<section class="cell-overview">
  <div class="wrap">
    <h2 class="ov-title">Section overview &mdash; § {esc(o['subsection'])}</h2>
    <p class="ov-sub">Click any superscript chip to see the verbatim evidence for that citation. <em>(Survey §{esc(o.get('subsubsec_id', ''))})</em></p>
    <div class="ov-paragraph">
      <p>{html_text}</p>
    </div>
    {fn_html}
  </div>
</section>'''


def render_cell_pages():
    for K in ['K1', 'K2', 'K3', 'K4']:
        for O in ['O1', 'O2', 'O3']:
            cell = f'{K}.{O}'
            ps = sorted(by_cell.get(cell, []), key=year_sort)
            kn, kd = K_LABELS[K]
            on, od = O_LABELS[O]

            other_cells_nav = '\n'.join(
                f'<a href="{c}.html" class="pill {"current" if c == cell else ""}" title="{c}">{cell_label(c)}</a>'
                for c in [f'{kk}.{oo}' for kk in ['K1','K2','K3','K4'] for oo in ['O1','O2','O3']]
            )

            cards = '\n'.join(paper_card(p, base='../', axis_scope=O) for p in ps) or '<p class="empty">No verified entries in this cell yet — see <a href="../about.html#methodology">methodology</a> and the survey §11 frontier discussion.</p>'
            sf = subsec_filter_html(ps, prefix=f'cell{cell}', axis_scope=O, cell_key=cell)
            overview_html = render_overview_section(cell, papers_by_key, base='../')

            # Cell-tier badge (Active / Emerging / Frontier) from §4 K×O Cross-Tab Analysis
            tier_info = CELL_TIERS.get(cell)
            tier_badge = ''
            if tier_info:
                tier, tier_name = tier_info
                tier_class = f'cell-tier-{tier.lower()}'
                tier_badge = f'<div class="cell-tier-row"><span class="cell-tier {tier_class}">{tier} cell</span> <span class="cell-tier-name">{esc(tier_name)}</span></div>'

            body = f'''
<section class="cell-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../index.html#grid">← K×O Grid</a></p>
    <h1><span class="cell-id-big">[{cell}]</span> {esc(kn)} <span class="times">×</span> {esc(on)}</h1>
    {tier_badge}
    <p class="lede"><strong>{len(ps)}</strong> entries.</p>
    <div class="cell-axis-pair">
      <div class="axis-card axis-k">
        <span class="axis-tag">K {K[1]}</span>
        <h3>{esc(kn)}</h3>
        <p>{esc(kd)}</p>
      </div>
      <div class="axis-card axis-o">
        <span class="axis-tag">O {O[1]}</span>
        <h3>{esc(on)}</h3>
        <p>{esc(od)}</p>
      </div>
    </div>
    <div class="cell-nav">{other_cells_nav}</div>
  </div>
</section>

{overview_html}

<section class="cell-list">
  <div class="wrap">
    {sf}
    <div class="card-grid">{cards}</div>
  </div>
</section>
'''
            (ROOT / 'cell' / f'{cell}.html').write_text(page_head(f'[{cell}] {kn} × {on}', base='../', current=f'cell/{cell}') + body + page_foot('../'))

    # ---------- K-only axis pages (cell/K1.html etc.) ----------
    for K in ['K1', 'K2', 'K3', 'K4']:
        ps = sorted(by_cell.get(K, []), key=year_sort)
        kn, kd = K_LABELS[K]
        cards = '\n'.join(paper_card(p, base='../', axis_scope=K) for p in ps) or '<p class="empty">No K-only entries yet.</p>'
        sf = subsec_filter_html(ps, prefix=f'kaxis{K}', axis_scope=K)
        body = f'''
<section class="cell-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../index.html#grid">← K×O Grid</a></p>
    <h1><span class="cell-id-big">[{K}]</span> {esc(kn)}</h1>
    <p class="lede"><strong>{len(ps)}</strong> K-axis-only entries (datasets / knowledge sources without paired O).</p>
    <div class="cell-axis-pair">
      <div class="axis-card axis-k">
        <span class="axis-tag">K {K[1]}</span>
        <h3>{esc(kn)}</h3>
        <p>{esc(kd)}</p>
      </div>
    </div>
  </div>
</section>

<section class="cell-list">
  <div class="wrap">
    {sf}
    <div class="card-grid">{cards}</div>
  </div>
</section>
'''
        (ROOT / 'cell' / f'{K}.html').write_text(page_head(f'[{K}] {kn}', base='../', current=f'cell/{K}') + body + page_foot('../'))

    # ---------- O-only axis pages (cell/O1.html etc.) ----------
    for O in ['O1', 'O2', 'O3']:
        # Aggregate all papers from every K×O cell + bare O-only entries
        seen_bk = set()
        ps = []
        for K in ['K1', 'K2', 'K3', 'K4']:
            for p in by_cell.get(f'{K}.{O}', []):
                bk = p.get('bib_key') or id(p)
                if bk not in seen_bk:
                    seen_bk.add(bk)
                    ps.append(p)
        for p in by_cell.get(O, []):
            bk = p.get('bib_key') or id(p)
            if bk not in seen_bk:
                seen_bk.add(bk)
                ps.append(p)
        ps = sorted(ps, key=year_sort)
        on, od = O_LABELS[O]
        sf = subsec_filter_html(ps, prefix=f'oaxis{O}', axis_scope=O)
        cards = '\n'.join(paper_card(p, base='../', axis_scope=O) for p in ps) or '<p class="empty">No entries yet.</p>'
        # K-cell breakdown pills
        o_cells_nav = '\n'.join(
            f'<a href="../cell/{K}.{O}.html" class="pill" title="{K}.{O}">{cell_label(K+"."+O)} {len(by_cell.get(K+"."+O, []))}</a>'
            for K in ['K1', 'K2', 'K3', 'K4']
        )
        body = f'''
<section class="cell-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../index.html#grid">← K×O Grid</a></p>
    <h1><span class="cell-id-big">[{O}]</span> {esc(on)}</h1>
    <p class="lede"><strong>{len(ps)}</strong> entries with <strong>{esc(on)}</strong> objective (all K sources).</p>
    <div class="cell-axis-pair">
      <div class="axis-card axis-o">
        <span class="axis-tag">O {O[1]}</span>
        <h3>{esc(on)}</h3>
        <p>{esc(od)}</p>
      </div>
    </div>
    <div class="cell-nav">{o_cells_nav}</div>
  </div>
</section>

<section class="cell-list">
  <div class="wrap">
    {sf}
    <div class="card-grid">{cards}</div>
  </div>
</section>
'''
        (ROOT / 'cell' / f'{O}.html').write_text(page_head(f'[{O}] {on}', base='../', current=f'cell/{O}') + body + page_foot('../'))


# ---------- domain/<d>.html ----------
def render_domain_pages():
    for d, label in DOMAIN_LABELS.items():
        if d not in by_dom:
            continue
        ps = sorted(by_dom[d], key=year_sort)
        # Cell breakdown within domain
        dom_cells = Counter()
        for p in ps:
            for c in p.get('ko_cells', []):
                dom_cells[c] += 1
        breakdown = ''.join(
            f'<a href="../cell/{c}.html" class="pill" title="{c}">{cell_label(c)} {dom_cells[c]}</a>'
            for c in sorted(dom_cells, key=lambda x: -dom_cells[x])
        )
        cards = '\n'.join(paper_card(p, base='../') for p in ps)
        body = f'''
<section class="domain-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../index.html#domains">← Domains</a></p>
    <h1>{DOMAIN_EMOJI.get(d, "")} {esc(label)}</h1>
    <p class="lede"><strong>{len(ps)}</strong> entries in the {esc(label.lower())} domain.</p>
    {f'<div class="cell-breakdown"><span class="muted">K×O distribution:</span> {breakdown}</div>' if breakdown else ''}
  </div>
</section>

<section class="domain-list">
  <div class="wrap">
    <div class="card-grid">{cards}</div>
  </div>
</section>
'''
        (ROOT / 'domain' / f'{d}.html').write_text(page_head(label, base='../', current=f'domain/{d}') + body + page_foot('../'))


# ---------- topics/<type>.html ----------
def render_type_pages():
    for t, label in TYPE_LABELS.items():
        if t not in by_type:
            continue
        ps = sorted(by_type[t], key=year_sort)
        cards = '\n'.join(paper_card(p, base='../') for p in ps)
        body = f'''
<section class="domain-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../index.html">← Home</a></p>
    <h1>{esc(label)}</h1>
    <p class="lede"><strong>{len(ps)}</strong> entries of type <code>{esc(t)}</code>.</p>
  </div>
</section>

<section class="domain-list">
  <div class="wrap">
    <div class="card-grid">{cards}</div>
  </div>
</section>
'''
        (ROOT / 'topics' / f'{t.lower()}.html').write_text(page_head(label, base='../', current=f'topics/{t.lower()}') + body + page_foot('../'))


# ---------- insights.html ----------
def render_insights():
    flagships_file = ROOT / 'build/flagships.json'
    fdata = json.loads(flagships_file.read_text())
    flagships = fdata['flagships']
    paper_by_bib = {p.get('bib_key'): p for p in papers}

    # K × Domain matrix
    kd = defaultdict(int)
    for p in papers:
        for d in p.get('domain', []):
            if not d:
                continue
            for c in p.get('ko_cells', []):
                K = c.split('.')[0]
                kd[(K, d)] += 1
    domains_ordered = ['bio', 'chem', 'medical', 'material', 'physics', 'earth', 'astronomy']
    max_kd = max(kd.values()) if kd else 1

    def kd_heat_style(v, vmax):
        if v == 0: return 'background:var(--cell-zero);color:var(--fg-faint);'
        t = v / vmax
        if t < .25: return 'background:var(--cell-low);'
        if t < .55: return 'background:var(--cell-mid);'
        return 'background:var(--cell-high);color:var(--cell-high-fg);'

    kd_rows = ''
    from urllib.parse import quote_plus
    for K in ['K1', 'K2', 'K3', 'K4']:
        kn = K_LABELS[K][0]
        cells_html = ''
        for d in domains_ordered:
            v = kd.get((K, d), 0)
            q = quote_plus(f'{K} {DOMAIN_LABELS.get(d, d)}')
            cells_html += f'<td style="{kd_heat_style(v, max_kd)}"><a href="browse.html?q={q}" class="kd-link" title="{K} × {esc(DOMAIN_LABELS.get(d, d))}: {v} entries">{v}</a></td>'
        kd_rows += f'<tr><th><span class="cell-axis">{K}</span> {esc(kn)}</th>{cells_html}</tr>\n'
    kd_head = '<tr><th></th>' + ''.join(f'<th>{DOMAIN_EMOJI.get(d,"")} {esc(DOMAIN_LABELS[d])}</th>' for d in domains_ordered) + '</tr>'

    # Yearly growth (stacked by primary K)
    yc = defaultdict(lambda: defaultdict(int))  # year → K → count
    for p in papers:
        y = p.get('year')
        if not str(y).isdigit():
            continue
        y = int(y)
        if y < 2018:
            continue
        primary = p.get('ko_primary')
        K = primary.split('.')[0] if primary else '?'
        yc[y][K] += 1
    years = sorted(yc)
    max_year_total = max(sum(yc[y].values()) for y in years) if years else 1
    bar_w = 80
    gap = 14
    chart_h = 260
    chart_w = len(years) * (bar_w + gap) + 60
    bars = []
    K_COLORS = {'K1': '#b8431f', 'K2': '#1f7a4d', 'K3': '#6a3acb', 'K4': '#d4992a', '?': '#999'}
    K_COLOR_LABELS = {'K1': 'Primary Lit', 'K2': 'Curated KB', 'K3': 'Obs/Exp', 'K4': 'Tacit', '?': 'Unassigned'}
    x = 50
    for y in years:
        total = sum(yc[y].values())
        # stack from bottom
        cy = chart_h - 30
        for K in ['K4', 'K3', 'K2', 'K1', '?']:
            c = yc[y].get(K, 0)
            if c == 0:
                continue
            h = (c / max_year_total) * (chart_h - 70)
            cy -= h
            bars.append(f'<rect x="{x}" y="{cy}" width="{bar_w}" height="{h:.1f}" fill="{K_COLORS[K]}" opacity="0.92"><title>{y} · {K}: {c}</title></rect>')
        bars.append(f'<text x="{x+bar_w/2}" y="{chart_h-12}" text-anchor="middle" font-size="12" fill="var(--fg-muted)">{y}</text>')
        bars.append(f'<text x="{x+bar_w/2}" y="{chart_h-30-(total/max_year_total)*(chart_h-70)-6}" text-anchor="middle" font-size="11" font-weight="700" fill="var(--fg)">{total}</text>')
        x += bar_w + gap
    legend = ''.join(f'<span class="lg-chip" style="background:{K_COLORS[k]};color:white">{k} {esc(K_COLOR_LABELS[k])}</span>' for k in ['K1','K2','K3','K4'] if any(yc[y].get(k,0) for y in years))
    timeline_svg = f'<svg viewBox="0 0 {chart_w} {chart_h}" width="100%" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Scientific RAG paper growth by year, stacked by Knowledge Source axis">{"".join(bars)}</svg>'

    # Flagship cards
    fl_cards = []
    for f in flagships:
        p = paper_by_bib.get(f['bib_key'], {})
        url = p.get('paper_link') or ''
        stats_html = ''.join(f'<div class="fl-stat"><span class="fl-num">{esc(s[0])}</span><span class="fl-label">{esc(s[1])}</span></div>' for s in f['headline_stats'])
        title_link = f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(p.get("title","") or f["name"])} ↗</a>' if url else esc(p.get('title','') or f['name'])
        cell = f['cell']
        fl_cards.append(f'''
        <article class="fl-card">
          <div class="fl-head">
            <h3 class="fl-name">{esc(f['name'])}</h3>
            <a href="cell/{cell}.html" class="tag tag-cell">{cell}</a>
          </div>
          <p class="fl-tagline">{esc(f['tagline'])}</p>
          <div class="fl-stats">{stats_html}</div>
          <p class="fl-subtitle">{esc(f['subtitle'])}</p>
          <p class="fl-why"><strong>Why it matters.</strong> {esc(f['why'])}</p>
          <p class="fl-cite">{title_link} · <span class="muted">{esc(f['venue'])}</span></p>
        </article>''')

    # Cross-source papers
    xs_papers = [p for p in papers if p.get('cross_source') or len(p.get('ko_cells', [])) > 1]
    xs_cards = '\n'.join(paper_card(p) for p in xs_papers[:12])

    # Frontier cells
    frontier_K3O3 = by_cell.get('K3.O3', [])
    frontier_K4O3 = by_cell.get('K4.O3', [])
    f33 = '\n'.join(paper_card(p) for p in frontier_K3O3) or '<p class="empty">No verified entries — this cell is a structural gap.</p>'
    f43 = '\n'.join(paper_card(p) for p in frontier_K4O3) or '<p class="empty">No verified entries — this cell is a structural gap.</p>'

    body = f'''
<section class="insights-hero">
  <div class="wrap">
    <p class="eyebrow">Insights · The shape of scientific RAG</p>
    <h1>What the {len(papers)}-paper catalog reveals.</h1>
    <p class="lede">
      Six lenses on the field — flagship demonstrations, the unique requirements that distinguish
      scientific from general RAG, where coverage is dense, where the white space is,
      and the seven directions where the next breakthroughs are most likely.
    </p>
    <nav class="insights-toc">
      <a href="#flagships">Flagships</a>
      <a href="#requirements">5 Requirements</a>
      <a href="#growth">Growth</a>
      <a href="#kd">K×Domain</a>
      <a href="#bridges">Cross-source</a>
      <a href="#frontiers">Frontiers</a>
      <a href="#directions">Future</a>
    </nav>
  </div>
</section>

<section id="flagships" class="prose-section">
  <div class="wrap">
    <h2 class="section-title">Flagships — papers that move the field</h2>
    <p class="section-sub">Nine systems chosen for the largest measured gains or the clearest demonstration of a structural pattern.</p>
    <div class="fl-grid">{''.join(fl_cards)}</div>
  </div>
</section>

<section id="requirements" class="prose-section alt-bg">
  <div class="wrap">
    <h2 class="section-title">The 5 unique requirements of scientific RAG</h2>
    <p class="section-sub">General-purpose RAG ranks by semantic proximity. Scientific RAG must obey stricter, often quantitative, demands.</p>
    <div class="req-grid">
      <div class="req-card req-1">
        <div class="req-num">1</div>
        <h3>Mandatory Claim Attribution</h3>
        <p>Every claim traceable to a source unit — sentence-level, page-level, or claim-graph.</p>
        <p class="req-evidence">OpenScholar 0% hallucination · PaperQA sentence-level citing · R2AG-Climate 4-dim faithfulness</p>
      </div>
      <div class="req-card req-2">
        <div class="req-num">2</div>
        <h3>Relational Knowledge Coupling</h3>
        <p>Facts live in webs (PDB ↔ UniProt ↔ ChEMBL). Retrieval must traverse couplings, not just rank entities.</p>
        <p class="req-evidence">CLADD 2-hop PrimeKG · MedGraphRAG 3-tier · BIORAG NCBI cross-DB</p>
      </div>
      <div class="req-card req-3">
        <div class="req-num">3</div>
        <h3>Source Reliability Tiering</h3>
        <p>Papers, preprints, curated DBs, lab notes — each carries different epistemic weight. RAG must reflect this.</p>
        <p class="req-evidence">MEDRAG RRF over 4 corpora · Rationale-Guided RAG balanced retrieval · MITRA 2-tier abstracts→full-text</p>
      </div>
      <div class="req-card req-4">
        <div class="req-num">4</div>
        <h3>Protocol-level Reproducibility</h3>
        <p>Outputs must include enough method detail for an expert to reproduce — not just a summary.</p>
        <p class="req-evidence">AP Lab Protocols · RHIC DAPP · MatClaw 99% API-call accuracy · MITRA full-method docs</p>
      </div>
      <div class="req-card req-5">
        <div class="req-num">5</div>
        <h3>Domain-Native Representations</h3>
        <p>SMILES, InChI, FASTA, LaTeX, CIF, DICOM. No flattening to text — the chemistry of the structure matters.</p>
        <p class="req-evidence">Rag2Mol/TaLiRAGen/f-RAG SMILES+3D · HoneyComb CIF · MMed-RAG DICOM</p>
      </div>
    </div>
  </div>
</section>

<section id="growth" class="prose-section">
  <div class="wrap">
    <h2 class="section-title">Growth by year, stacked by Knowledge Source</h2>
    <p class="section-sub">
      The 2024–2025 explosion is dominated by <strong style="color:#b8431f">K1 primary-literature</strong> systems
      (medical QA, scientific synthesis). <strong style="color:#1f7a4d">K2 curated-KB</strong> work follows, while
      <strong style="color:#d4992a">K4 tacit</strong> systems remain rare — most are 2025–2026 firsts.
    </p>
    <div class="chart-frame">{timeline_svg}</div>
    <p class="chart-legend">{legend}</p>
  </div>
</section>

<section id="kd" class="prose-section alt-bg">
  <div class="wrap">
    <h2 class="section-title">K × Domain — where each Knowledge Source lives</h2>
    <p class="section-sub">
      Medicine spans all four K tiers. Chemistry leans on K2 curated KBs. Physics is K1+K4 (institutional memory).
      Earth science is K1-heavy. Cells link to a filtered Browse view.
    </p>
    <table class="kd-grid">
      <thead>{kd_head}</thead>
      <tbody>{kd_rows}</tbody>
    </table>
  </div>
</section>

<section id="bridges" class="prose-section">
  <div class="wrap">
    <h2 class="section-title">Cross-source bridges — papers that span multiple K tiers</h2>
    <p class="section-sub">
      <strong>{len(xs_papers)}</strong> systems bridge multiple knowledge sources. The most ambitious — MedGraphRAG —
      stitches K1 (MedC-K papers) + K2 (UMLS/ICD ontology) + K4 (MIMIC IV private EHR) in one pipeline.
      These prove that the K axis is not a partition but a graph.
    </p>
    <div class="card-grid">{xs_cards}</div>
    <p class="see-more"><a href="browse.html" class="btn btn-secondary">Browse all cross-source systems →</a></p>
  </div>
</section>

<section id="frontiers" class="prose-section alt-bg">
  <div class="wrap">
    <h2 class="section-title">Frontier cells — where the white space is</h2>
    <p class="section-sub">
      The K×O grid surfaces two near-empty cells. Both involve the most ambitious operation (O3 Hypothesis)
      paired with the harder-to-access sources (K3 raw modalities, K4 tacit knowledge).
    </p>
    <div class="frontier-pair">
      <div class="frontier-col">
        <h3><span class="cell-id-big">[K3.O3]</span> Observational × Hypothesis <span class="muted">({len(frontier_K3O3)} entry)</span></h3>
        <p>Spectra → molecule, imaging → diagnosis-hypothesis, sequencing → mechanism. Today, only mass-spectrometry-to-molecule attempts exist.</p>
        <div class="card-grid">{f33}</div>
      </div>
      <div class="frontier-col">
        <h3><span class="cell-id-big">[K4.O3]</span> Tacit × Hypothesis <span class="muted">({len(frontier_K4O3)} entries)</span></h3>
        <p>Hypothesis generation grounded in lab logs, internal collaboration notes, or industry process databases. Nearly virgin territory.</p>
        <div class="card-grid">{f43}</div>
      </div>
    </div>
  </div>
</section>

<section id="directions" class="prose-section">
  <div class="wrap">
    <h2 class="section-title">Seven directions for the next scientific RAG generation</h2>
    <p class="section-sub">Each entry is a "From → To" transition the field is starting to make. Drawn from §11 of the survey.</p>
    <div class="dir-grid">
      <div class="dir-card">
        <span class="dir-num">1</span>
        <h3>Underutilized → Activated Authoritative Sources <span class="dir-star">★ main insight</span></h3>
        <p>Dozens of authoritative DBs (Reaxys, Aspen, NIST Mass Spec, ChemProt) are <em>indexed nowhere</em> for RAG. Activating them is the single largest unclaimed win.</p>
        <p class="dir-ev">RHIC DAPP · MITRA · DUNE-GPT show the playbook for physics; chemistry/materials lag.</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">2</span>
        <h3>Primary Literature → Tacit Sources</h3>
        <p>Most domains lack a single K4 system. The institutional memory of labs, collaborations, and industry holds 10×+ more knowledge than papers.</p>
        <p class="dir-ev">K4 is ~9 papers today out of 138 — likely 50-65 once private datasets are surveyed.</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">3</span>
        <h3>Ground → Hypothesis</h3>
        <p>From "answer with citations" to "propose a molecule and have the docking score verify it." Generate-then-verify closed loops.</p>
        <p class="dir-ev">f-RAG → Vina · Rag2Mol → docking · CLADD agent verifier · HEA → DFT.</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">4</span>
        <h3>Closed → Sandboxed Sources</h3>
        <p>HIPAA, IP, and security forbid sending corpora to commercial LLMs. On-prem RAG with 4-bit local models is the only path.</p>
        <p class="dir-ev">MITRA 4-bit · DUNE-GPT Fermilab intranet · MedRAG-CPDD private EHR.</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">5</span>
        <h3>Static → Streaming Living Sources</h3>
        <p>PubMed adds 1M papers/year. Crystal structure DBs update daily. Indices must stream, not snapshot.</p>
        <p class="dir-ev">BIORAG NCBI live API · OpenScholar Semantic Scholar live.</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">6</span>
        <h3>Synthetic Contamination → Synthetic Grounding</h3>
        <p>Generated content is poisoning future corpora. The defense: use synthetic data as <em>training scaffolding</em>, not retrieval ground truth.</p>
        <p class="dir-ev">OpenScholar synthetic SFT (clean) · LitQA anti-contamination post-cutoff papers.</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">7</span>
        <h3>Single-Modality → Multi-Modality Fusion</h3>
        <p>Real scientific reasoning interleaves text, equations, structures, images. Multimodal retrieval over scientific media is the bottleneck.</p>
        <p class="dir-ev">MMed-RAG · Patho-AgenticRAG · AlzheimerRAG · RS-RAG span the modality bridge.</p>
      </div>
    </div>
  </div>
</section>
'''
    (ROOT / 'insights.html').write_text(page_head('Insights', base='', desc='The five requirements of scientific RAG, K×Domain coverage map, paper growth timeline, cross-source bridges, and frontier opportunities.', current='insights') + body + PAGE_FOOT)


def _clean_prop_val(val):
    """Clean up property values: strip Python list brackets, skip trivial N/A."""
    val = val.strip()
    # Strip Python list notation: ['Text'] → Text, ['Image', 'Text'] → Image, Text
    if val.startswith('[') and val.endswith(']'):
        inner = val[1:-1]
        items = [s.strip().strip("'\"") for s in inner.split(',')]
        val = ', '.join(i for i in items if i)
    return val


def _prop_block_to_table(md_content):
    """Pre-process Notion-style property block into an HTML table.

    Detects consecutive ``**Key**: value`` lines (no blank lines between them)
    and replaces that block with a ``<div class="prop-table">`` so they render
    nicely. Skips rows whose value is N/A or empty.
    """
    PROP_KEYS = {
        'DB', 'DB size', 'DB Open/Private', 'Modality',
        'Retriever', 'Eval Task', 'Eval Metric', 'Method Name',
    }
    # Keys to skip when value is N/A (infrastructure-only fields)
    SKIP_NA = {'Retriever', 'Eval Task', 'Eval Metric'}

    prop_re = re.compile(r'^\*\*([^*]+)\*\*:\s*(.*)')
    lines = md_content.split('\n')
    out = []
    i = 0
    while i < len(lines):
        m = prop_re.match(lines[i])
        if m and m.group(1) in PROP_KEYS:
            rows = []
            while i < len(lines):
                pm = prop_re.match(lines[i])
                if pm and pm.group(1) in PROP_KEYS:
                    key_raw = pm.group(1)
                    val = _clean_prop_val(pm.group(2))
                    # Skip uninformative N/A rows
                    if key_raw in SKIP_NA and val.lower().startswith('n/a'):
                        i += 1
                        continue
                    if not val:
                        i += 1
                        continue
                    key = html.escape(key_raw)
                    rows.append(f'<tr><td class="prop-key">{key}</td><td class="prop-val">{val}</td></tr>')
                    i += 1
                else:
                    break
            if rows:
                out.append('<table class="prop-table">\n' + '\n'.join(rows) + '\n</table>\n')
            # if all rows were skipped, emit nothing
        else:
            out.append(lines[i])
            i += 1
    return '\n'.join(out)


def render_paper_pages():
    """Render papers/<bib_key>.html from papers/<bib_key>.md (Notion summaries)."""
    import mistune
    md_renderer = mistune.create_markdown(escape=False, plugins=['table','strikethrough','footnotes','url'])
    papers_by_key = {p['bib_key']: p for p in papers if p.get('bib_key')}
    papers_dir = ROOT / 'papers'
    if not papers_dir.exists():
        print('  papers/ dir missing — skipping summary pages')
        return
    count = 0
    for md_file in sorted(papers_dir.glob('*.md')):
        bib_key_fn = md_file.stem  # filename without .md, with _ instead of :/
        matching = None
        for bk, p in papers_by_key.items():
            if bk.replace(':','_').replace('/','_') == bib_key_fn:
                matching = p; break
        if not matching:
            continue
        title = matching.get('title') or bib_key_fn
        md_content = md_file.read_text()
        # Strip YAML frontmatter
        if md_content.startswith('---'):
            end = md_content.find('---', 3)
            if end > 0:
                md_content = md_content[end+3:].lstrip()
        # Convert Notion property block → HTML table
        md_content = _prop_block_to_table(md_content)
        # Ensure blank lines around HTML block boundaries
        md_content = re.sub(r'(</table>)\s*\n(#)', r'\1\n\n\2', md_content)
        md_content = re.sub(r'(\n#{1,6} [^\n]+)\n(<table)', r'\1\n\n\2', md_content)
        md_content = re.sub(r'(</table>)\s*\n([^\n#<\s-])', r'\1\n\n\2', md_content)
        body_html = md_renderer(md_content)
        url = matching.get('paper_link') or ''
        url_link = f'<a href="{esc(url)}" target="_blank" rel="noopener" class="ext-link">Paper ↗</a>' if url else ''
        cells = matching.get('ko_cells', [])
        cell_tags = ''.join(f'<a href="../cell/{c}.html" class="tag tag-cell" title="{c}">{cell_label(c)}</a>' for c in cells)
        subsec = matching.get('subsection', '')
        subsec_tag = f'<span class="tag tag-sub">{esc(subsec)}</span>' if subsec else ''
        domains = matching.get('domain', [])
        dom_tags = ''.join(f'<a href="../domain/{d}.html" class="tag tag-domain">{DOMAIN_EMOJI.get(d,"")}{esc(DOMAIN_LABELS.get(d,d))}</a>' for d in domains)
        body = f'''
<section class="paper-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../browse.html">← All papers</a></p>
    <h1>{esc(title)}</h1>
    <div class="paper-hero-meta">
      <span class="meta-venue">{esc(matching.get('venue',''))}</span>
      <span class="meta-year">{esc(matching.get('year',''))}</span>
      {url_link}
    </div>
    <div class="paper-tags">{cell_tags}{subsec_tag}{dom_tags}</div>
  </div>
</section>
<section class="paper-body">
  <div class="wrap">
    <article class="paper-markdown">
      {body_html}
    </article>
  </div>
</section>
'''
        out_fn = bib_key_fn + '.html'
        (papers_dir / out_fn).write_text(page_head(esc(title), base='../', current=f'papers/{bib_key_fn}') + body + page_foot('../'))
        count += 1
    print(f'  papers/*.html ({count} summaries)')


if __name__ == '__main__':
    render_paper_pages()   # First, so paper_card() can detect summary pages
    render_index()
    render_about()
    render_browse()
    render_insights()
    render_cell_pages()
    render_domain_pages()
    render_type_pages()
    print('Wrote all HTML pages.')
    print(f'  index.html, about.html, browse.html, insights.html')
    print(f'  cell/*.html ({len(by_cell)} cells)')
    print(f'  domain/*.html ({len([d for d in DOMAIN_LABELS if d in by_dom])} domains)')
    print(f'  topics/*.html ({len([t for t in TYPE_LABELS if t in by_type])} types)')
