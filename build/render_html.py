#!/usr/bin/env python3
"""Render the full HTML site from data/papers.json.

Outputs:
  index.html               , landing page with K×O grid + search
  about.html               , survey context + methodology
  browse.html              , full paper browser with client-side filter
  cell/<K>.<O>.html        , 12 K×O cell pages
  domain/<dom>.html        , 8 domain pages
  topics/<type>.html       , 4 type pages (method/benchmark/dataset/survey)
"""
import html
import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from urllib.parse import quote as _q

ROOT = Path('/gallery_millet/yerim.oh/ScienceRAGServey/site')
papers = json.loads((ROOT / 'data/papers.json').read_text())
# Paper Table 3 (tab:method_systems), extracted by build/extract_method_systems.py. Drives the
# at-a-glance pipeline table shown atop each cell / axis page. Optional: sites built without it
# just skip the table.
_ms_path = ROOT / 'data/method_systems.json'
METHOD_SYSTEMS = json.loads(_ms_path.read_text()) if _ms_path.exists() else []
# Paper Table 1 (knowledge sources = the K axis: data) and Table 2 (benchmarks = the O axis:
# tasks), extracted by build/extract_tables.py. Each axis page shows the table matching its
# own semantics: K pages the data resources, O pages the benchmarks.
_ks_path = ROOT / 'data/knowledge_sources.json'
KNOWLEDGE_SOURCES = json.loads(_ks_path.read_text()) if _ks_path.exists() else []
_bm_path = ROOT / 'data/benchmarks.json'
BENCHMARKS = json.loads(_bm_path.read_text()) if _bm_path.exists() else []
# §4 / §5 prose (substrate intros + sub-subsections with the named resources; task
# descriptions), extracted verbatim-cleaned by build/extract_axis_prose.py. This is the
# survey's actual body text, so the K/O pages match main2.tex rather than a summary.
_ap_path = ROOT / 'data/axis_prose.json'
AXIS_PROSE = json.loads(_ap_path.read_text()) if _ap_path.exists() else {}
K_PROSE = {s['code']: s for s in AXIS_PROSE.get('K', {}).get('substrates', [])}
O_PROSE = {t['name']: t for t in AXIS_PROSE.get('O', {}).get('tasks', [])}

# ---------- Reference tables ----------
# Taxonomy mirrors the survey (Oh et al.). The K axis is the *retrieval substrate*, the
# native form in which a source stores its knowledge, which fixes the retrieval operation it
# permits (§4). The O axis is the *operational objective*, three rungs ordered by how far the
# ground truth sits from the corpus (§5). Internal codes K1–K4 / O1–O3 are kept for URL and
# file-path stability; only their MEANING changed from the earlier epistemic taxonomy.
#   K1 = Textual, K2 = Relational, K3 = Structured-entity, K4 = Perceptual
#   O1 = Grounding, O2 = Synthesis, O3 = Discovery
K_LABELS = {
    'K1': ('Textual', 'Prose record of science, papers, abstracts, clinical notes, guidelines. Matched by embedding or lexical search over passages.'),
    'K2': ('Relational', 'Curated graphs of scientific relations, UMLS, PrimeKG, DRKG, STRING, KEGG, citation graphs. Reached by entity linking and traversal.'),
    'K3': ('Structured-entity', 'The objects of science as data, molecules, 3D structures, and property records (ChEMBL, PubChem, PDB, Materials Project). Reached by structural or property query.'),
    'K4': ('Perceptual', 'Raw instrument output, images, spectra, sequencing, time-series (MIMIC-CXR, MassBank, sky surveys). Reachable only through a learned cross-modal encoder.'),
}
O_LABELS = {
    'O1': ('Grounding', 'Answer a question whose gold already lies in the corpus, retrieve, cite, answer. (Question Answering.)'),
    'O2': ('Synthesis', 'Integrate evidence no single source states, verify claims and synthesize the literature. (Claim Verification, Literature Synthesis.)'),
    'O3': ('Discovery', 'Propose an output the corpus does not contain, judged by an external verifier. (Property Prediction, Molecular Design, Materials Discovery, Hypothesis Generation.)'),
}
# The seven task families of §5, grouped under the three O rungs.
TASK_RUNG = {
    'Question Answering': 'O1',
    'Cross-modal Grounding': 'O1',
    'Claim Verification': 'O2',
    'Literature Synthesis': 'O2',
    'Property Prediction': 'O3',
    'Molecular Design': 'O3',
    'Materials Discovery': 'O3',
    'Hypothesis Generation': 'O3',
}
# The seven §5 tasks in survey order, each with a dedicated page (parallel to the
# K substrate pages). Grouped by rung for the sidebar.
TASK_ORDER = [
    'Question Answering',
    'Claim Verification', 'Literature Synthesis',
    'Property Prediction', 'Molecular Design', 'Materials Discovery', 'Hypothesis Generation',
]


def task_slug(name):
    return name.lower().replace(' ', '-')
DOMAIN_LABELS = {
    'bio': 'Biology', 'chem': 'Chemistry', 'medical': 'Medicine',
    'material': 'Materials Science', 'physics': 'Physics', 'earth': 'Earth Science',
    'astronomy': 'Astronomy', 'Quantum': 'Quantum', 'general': 'General Science',
}
DOMAIN_EMOJI = {
    'bio': '🧬', 'chem': '⚗️', 'medical': '🩺', 'material': '🪨',
    'physics': '⚛️', 'earth': '🌍', 'astronomy': '🔭', 'Quantum': '🌀', 'general': '📚',
}
# Some catalog entries carry non-canonical domain slugs; fold them onto the slug that has a
# page so domain tags and links never 404.
DOMAIN_ALIAS = {'chemistry': 'chem', 'materials': 'material', 'multi': 'general'}
TYPE_LABELS = {
    'Method': 'Methods', 'benchmark': 'Benchmarks',
    'dataset': 'Datasets', 'summary': 'Surveys',
}

# O-side subsection chips = the seven task families of §5, grouped by their rung.
O_SUBSECTIONS = {
    'O1': {'Question Answering', 'Cross-modal Grounding'},
    'O2': {'Claim Verification', 'Literature Synthesis'},
    'O3': {'Property Prediction', 'Molecular Design', 'Materials Discovery', 'Hypothesis Generation'},
}
# K-side subsection chips = the resource groups within each substrate (§4).
K_SUBSECTIONS = {
    'K1': {'General & domain literature', 'Preprint literature', 'Institution-private corpora'},
    'K2': {'Concept-relation graphs', 'Literature-derived graphs'},
    'K3': {'Molecule & structure libraries', 'Property databases'},
    'K4': {'Medical & biological imaging', 'Spectral libraries', 'Instrument arrays & time series'},
}
# Per-cell allow-list of subsection chips, overriding axis_subsections() when present.
CELL_SUBSECTIONS = {}
# Cell-tier labels, the maturity landscape of §8 (ssec:kxo_crosstab). Capability is
# ACTIVE where the substrate admits a mature matching operation and the task an automatic
# score, EMERGING where a single component lags, and FRONTIER (dormant) where the verifier,
# retriever, or substrate does not yet exist. (tier, label_for_hero_chip)
CELL_TIERS = {
    # Textual (K1)
    'K1.O1': ('Active',   'Literature Grounding'),
    'K1.O2': ('Active',   'Literature Synthesis'),
    'K1.O3': ('Dormant','Literature-grounded Ideation'),
    # Relational (K2)
    'K2.O1': ('Active',   'Knowledge-graph QA'),
    'K2.O2': ('Emerging', 'Knowledge-graph Synthesis'),
    'K2.O3': ('Emerging', 'Relational Hypothesis'),
    # Structured-entity (K3)
    'K3.O1': ('Active',   'Structured-entity Lookup'),
    'K3.O2': ('Dormant','Structured Synthesis (open)'),
    'K3.O3': ('Emerging', 'Structure-based Design'),
    # Perceptual (K4)
    'K4.O1': ('Emerging', 'Cross-modal Grounding'),
    'K4.O2': ('Dormant','Perceptual Synthesis (open)'),
    'K4.O3': ('Dormant','Signal-to-structure Discovery'),
}

# Per-cell paper allow-list, the bib_keys actually CITED in each K×O subsubsection of
# the survey draft (ver/2/main.tex, latest prose revision). Comment blocks and %-comments
# were excluded, so e.g. PhoPile (only in a \begin{comment} block) is NOT here.
# When a cell appears here, the cell page renders ONLY these papers, in main.tex citation
# order, instead of every Notion-DB-tagged paper. Keys absent from papers.json (software /
# infra refs such as pymatgen, atomate2) are silently skipped at render time.
# K4.O2 and K4.O3 share the combined "Tacit-driven Synthesis and Hypothesis" paragraph;
# K1.O3 merges the strong- and weak-verifier paragraphs. K3.O2 has no draft paragraph (empty).
# Per-cell authoritative system lists, transcribed directly from the survey's assembly
# figure (Fig. 2), which is the paper's own substrate × task grid. Keys are (substrate, rung):
#   K1 Textual, K2 Relational, K3 Structured-entity, K4 Perceptual
#   O1 Grounding, O2 Synthesis, O3 Discovery
# Where a cell holds more than one task family, the tasks are noted in a comment. Keys absent
# from papers.json (bib-only refs) are silently skipped at render time.
CELL_PAPERS = {
    # Textual, Question Answering / Literature Synthesis / Hypothesis Generation
    'K1.O1': ['DBLP:conf/acl/Xiong0LZ24', 'DBLP:conf/pasc/GokdemirSBWHHSA25', 'DBLP:conf/emnlp/FrisoniMMV22', 'DBLP:journals/corr/abs-2603-09800', 'DBLP:journals/bioinformatics/JeongSSK24', 'DBLP:journals/corr/abs-2408-01107', 'DBLP:conf/naacl/SohnPYPHSKK25', 'DBLP:journals/corr/abs-2312-07559', 'DBLP:conf/acl/ChenLJWG0025', 'DBLP:conf/ecir/AteiaK25', 'zhang2024honeycomb'],
    'K1.O2': ['DBLP:journals/corr/abs-2402-01788', 'iyer2024pathfinder', 'DBLP:conf/nips/WangGYZZ0ZD0W0Z24', 'DBLP:conf/cikm/BesrourHS025', 'DBLP:journals/corr/abs-2310-16146', 'DBLP:conf/acl/YanFYX00Z25', 'DBLP:journals/corr/abs-2409-13740', 'asai2026synthesizing', 'wang2025accelerating'],
    'K1.O3': ['DBLP:conf/acl/0005DJH24', 'DBLP:conf/naacl/BaekJCH25', 'DBLP:conf/iclr/0001LGXLOPCZ25', 'DBLP:conf/emnlp/LiXGZLYZJXDRZFB25'],
    # Relational, Question Answering / Literature Synthesis / Hypothesis Generation
    'K2.O1': ['DBLP:journals/bioinformatics/SomanRMASPVCSRI24', 'DBLP:conf/acl/0006WS24', 'DBLP:conf/bionlp/YangLMZKLCCCML24', 'DBLP:conf/acl/WuZQCXMJG25', 'DBLP:conf/acl/Jiang0XQFWTDC0W25', 'DBLP:conf/iclr/00010GLGCZ25'],
    'K2.O2': ['DBLP:conf/sigir/HuLD0A0025'],
    'K2.O3': ['DBLP:conf/naacl/LiCJ25'],
    # Structured-entity, Question Answering (O1) / Molecular Design + Materials Discovery (O3)
    'K3.O1': ['DBLP:journals/bioinformatics/JinYCL24', 'DBLP:conf/emnlp/ChiangHCR25'],
    'K3.O2': [],
    'K3.O3': ['DBLP:conf/nips/LeeKV0RPVN24', 'DBLP:journals/bib/ZhangPHCM25', 'nan2026taliragen', 'DBLP:conf/iclr/0001NQXBA23', 'DBLP:journals/corr/abs-2603-15712'],
    # Perceptual, Cross-modal QA (O1) / Molecular Design + Property Prediction (O3)
    'K4.O1': ['DBLP:journals/corr/abs-2411-16523', 'DBLP:journals/corr/abs-2510-01558', 'DBLP:conf/iclr/0005ZLWSWZ0Y25', 'DBLP:conf/emnlp/XiaZLZLLZY24', 'DBLP:conf/naacl/SunZHX25', 'DBLP:conf/aaai/ZhangGZZCZZYB26'],
    'K4.O2': [],
    'K4.O3': ['DBLP:conf/icml/Huang0ZQYZZZWY24', 'DBLP:journals/corr/abs-2506-14488', 'DBLP:conf/iclr/WangCLH25'],
}
# Per-system task family (one of the seven of §5), for the assembly-figure core systems.
# Drives the O-side subsection chip and the correct rung during the central remap.
CORE_SYSTEM_TASK = {
    # Textual
    'DBLP:conf/acl/Xiong0LZ24': 'Question Answering', 'DBLP:conf/pasc/GokdemirSBWHHSA25': 'Question Answering',
    'DBLP:conf/emnlp/FrisoniMMV22': 'Question Answering', 'DBLP:journals/corr/abs-2603-09800': 'Question Answering',
    'DBLP:journals/bioinformatics/JeongSSK24': 'Question Answering', 'DBLP:journals/corr/abs-2408-01107': 'Question Answering',
    'DBLP:conf/naacl/SohnPYPHSKK25': 'Question Answering', 'DBLP:journals/corr/abs-2312-07559': 'Question Answering',
    'DBLP:conf/acl/ChenLJWG0025': 'Question Answering', 'DBLP:conf/ecir/AteiaK25': 'Question Answering',
    'zhang2024honeycomb': 'Question Answering',
    'DBLP:journals/corr/abs-2402-01788': 'Literature Synthesis', 'iyer2024pathfinder': 'Literature Synthesis',
    'DBLP:conf/nips/WangGYZZ0ZD0W0Z24': 'Literature Synthesis', 'DBLP:conf/cikm/BesrourHS025': 'Literature Synthesis',
    'DBLP:journals/corr/abs-2310-16146': 'Literature Synthesis', 'DBLP:conf/acl/YanFYX00Z25': 'Literature Synthesis',
    'DBLP:journals/corr/abs-2409-13740': 'Literature Synthesis', 'asai2026synthesizing': 'Literature Synthesis',
    'wang2025accelerating': 'Literature Synthesis',
    'DBLP:conf/acl/0005DJH24': 'Hypothesis Generation', 'DBLP:conf/naacl/BaekJCH25': 'Hypothesis Generation',
    'DBLP:conf/iclr/0001LGXLOPCZ25': 'Hypothesis Generation', 'DBLP:conf/emnlp/LiXGZLYZJXDRZFB25': 'Hypothesis Generation',
    # Relational
    'DBLP:journals/bioinformatics/SomanRMASPVCSRI24': 'Question Answering', 'DBLP:conf/acl/0006WS24': 'Question Answering',
    'DBLP:conf/bionlp/YangLMZKLCCCML24': 'Question Answering', 'DBLP:conf/acl/WuZQCXMJG25': 'Question Answering',
    'DBLP:conf/acl/Jiang0XQFWTDC0W25': 'Question Answering', 'DBLP:conf/iclr/00010GLGCZ25': 'Question Answering',
    'DBLP:conf/sigir/HuLD0A0025': 'Literature Synthesis', 'DBLP:conf/naacl/LiCJ25': 'Hypothesis Generation',
    # Structured-entity
    'DBLP:journals/bioinformatics/JinYCL24': 'Question Answering', 'DBLP:conf/emnlp/ChiangHCR25': 'Question Answering',
    'DBLP:conf/nips/LeeKV0RPVN24': 'Molecular Design', 'DBLP:journals/bib/ZhangPHCM25': 'Molecular Design',
    'nan2026taliragen': 'Molecular Design', 'DBLP:conf/iclr/0001NQXBA23': 'Molecular Design',
    'DBLP:journals/corr/abs-2603-15712': 'Materials Discovery',
    # Perceptual
    'DBLP:journals/corr/abs-2411-16523': 'Cross-modal Grounding', 'DBLP:journals/corr/abs-2510-01558': 'Cross-modal Grounding',
    'DBLP:conf/iclr/0005ZLWSWZ0Y25': 'Cross-modal Grounding', 'DBLP:conf/emnlp/XiaZLZLLZY24': 'Cross-modal Grounding',
    'DBLP:conf/naacl/SunZHX25': 'Cross-modal Grounding', 'DBLP:conf/aaai/ZhangGZZCZZYB26': 'Cross-modal Grounding',
    'DBLP:conf/icml/Huang0ZQYZZZWY24': 'Molecular Design', 'DBLP:journals/corr/abs-2506-14488': 'Molecular Design',
    'DBLP:conf/iclr/WangCLH25': 'Property Prediction',
}

# Full-text fact-check of the systems cited in each cell's main.tex paragraph.
# Verified 2026-05-31 against paper bodies (arXiv HTML / ACL / Crossref), NOT abstracts.
# bib_key -> {verdict, evidence (verbatim-quote-grounded), source}. Rendered as a clickable
# footnote on the cell page (popover via static/footnotes.js) so the claim's original-text
# evidence is one click away instead of the raw paper link. See ver/2/factcheck_kxo_k1o1.md.
FACTCHECK = {
    'DBLP:conf/acl/Xiong0LZ24': {
        'verdict': '✅ Accurate, closed-form',
        'evidence': 'MEDRAG is “a toolkit with systematic implementations of RAG for medical QA” (§4); its evaluation “tasks are all composed of multi-choice questions” (§3.2), retrieving over PubMed, StatPearls, textbooks and Wikipedia. (MEDRAG = the system; MIRAGE = its benchmark.)',
        'source': 'ACL Findings 2024, pp. 6233–6251, arXiv:2402.13178',
    },
    'DBLP:journals/corr/abs-2408-01107': {
        'verdict': '✅ Accurate, closed-form',
        'evidence': 'BioRAG is “a novel Retrieval-Augmented Generation (RAG) with the Large Language Models (LLMs) framework” (§2) retrieving over “a corpus of 22,371,343 high-quality, processed PubMed abstracts” (§2.1) for closed-form biological QA (GeneTuring, MedMCQA, College Biology/Medicine).',
        'source': 'CoRR 2024, arXiv:2408.01107',
    },
    'DBLP:conf/naacl/SohnPYPHSKK25': {
        'verdict': '✅ Accurate, closed-form',
        'evidence': 'RAG² (“RAtionale-Guided Retrieval Augmented Generation”) uses LLM-generated rationales as retrieval queries plus a perplexity-trained filter, for multiple-choice medical QA (MedQA, MedMCQA, MMLU-Med) over four balanced corpora, PubMed, PMC, textbooks, clinical guidelines (§3.4).',
        'source': 'NAACL 2025, pp. 12739–12753, arXiv:2411.00300',
    },
    'DBLP:journals/corr/abs-2312-07559': {
        'verdict': '✅ Accurate, long-form citation',
        'evidence': 'PaperQA “performs information retrieval across full-text scientific articles” and, via a “map summarization step … followed by a reduce step,” returns cited long-form answers with per-sentence “citation markers” (§3); LitQA is its separate “50 multiple-choice” eval benchmark (§4).',
        'source': 'CoRR 2023, arXiv:2312.07559',
    },
    'asai2026synthesizing': {
        'verdict': '✅ Accurate, long-form citation',
        'evidence': 'OpenScholar is a “retrieval-augmented LM that answers scientific queries by identifying relevant passages from 45 million open-access papers and synthesizing citation-backed responses,” evaluated on ScholarQABench (2,967 expert queries, 208 long-form answers). Cite key is for the Nature 2026 version (not DBLP-indexed; arXiv = 2411.14199).',
        'source': 'Nature 650:857–863, 2026, DOI 10.1038/s41586-025-10072-4',
    },
    'DBLP:journals/corr/abs-2310-16146': {
        'verdict': '✅ Accurate, long-form citation (output form)',
        'evidence': 'Clinfo.ai is “an open-source WebApp that answers clinical questions based on dynamically retrieved scientific literature” (PubMed), producing a “Literature Summary” whose “ordered list, with each number … corresponding to a citation” attributes each finding to its source; releases PubMedRS-200. (Caveat: answer scored by summarization metrics, not citation precision/recall.)',
        'source': 'CoRR 2023, arXiv:2310.16146, PSB 2024',
    },
    # --- K4.O1 (Private-document Retrieval), verified 2026-05-31 against full bodies. See factcheck_kxo_k4o1.md ---
    'DBLP:journals/corr/abs-2603-09800': {
        'verdict': '✅ Accurate, retrieval-grounded',
        'evidence': 'MITRA is “a Retrieval-Augmented Generation (RAG) based system” over the “Compact Muon Solenoid (CMS) … internal documentation,” “hosted on-premise” for privacy. It explicitly beats an “Okapi BM25” baseline on paraphrased queries by wide margins (P@1 0.75 vs 0.13, MRR 0.81 vs 0.35, NDCG@5 0.88 vs 0.59); generation-step evaluation is left to future work.',
        'source': 'CoRR 2026, arXiv:2603.09800 (DBLP-verified)',
    },
    'rafique2025large': {
        'verdict': '⚠️ Name/corpus accurate, no BM25 comparison',
        'evidence': 'DUNE-GPT is “a prototype framework that leverages LLMs and RAG” for “natural-language querying of DUNE’s internal documentation and technical resources” (Fermilab on-premise). It reports only a single preliminary figure, “retrieves relevant documentation with high accuracy (∼70%)”, and makes NO BM25/sparse-baseline comparison. ⚠️ Paper is real on arXiv (2601.05278) but NOT indexed by DBLP; bib key is a hand-made arXiv entry.',
        'source': 'arXiv:2601.05278 (2026), not in DBLP',
    },
    'DBLP:journals/corr/abs-2509-09688': {
        'verdict': '⚠️ Reports deployment + qualitative QA, not retrieval metrics',
        'evidence': 'The RHIC “Data and Analysis Preservation Plan (DAPP)” assistant (the paper names the plan DAPP; the assistant itself is unnamed) indexes “documentation, workflows, and software” (~1 ExaByte) via RAG + Model Context Protocol. It reports “deployment, computational performance” and a QUALITATIVE expert-grounded comparison of Llama3.3-70B / Mistral-Large / ChatGPT-o3, NO retrieval-quality metrics and NO BM25 comparison; a formal benchmark “is currently in progress.”',
        'source': 'CoRR 2025, arXiv:2509.09688 (DBLP-verified)',
    },
    'DBLP:journals/corr/abs-2406-12881': {
        'verdict': '✅ Accurate, retrieval-grounded',
        'evidence': 'A multi-facility study: “Electronic logbooks contain valuable information about activities and events concerning their associated particle accelerator facilities” (DESY, BESSY, Fermilab’s ADEL, BNL, SLAC, LBNL, CERN). It implements RAG (“q→retrieve(q)→generate(q,𝒟)→a”) to ground answers in these institution-private operational logbooks.',
        'source': 'CoRR 2024, arXiv:2406.12881 (DBLP-verified)',
    },
    'mehta2023copilots': {
        'verdict': '✅ Accurate, retrieval-grounded',
        'evidence': 'An operational copilot using “Retrieval-Augmented Generation (RAG)” over institution-private text logs from the DIII-D and Alcator C-Mod tokamak fusion experiments; it “answers operator queries using retrieved experimental logs rather than generating hypothetical decisions”, i.e. grounding, not action/hypothesis generation. ⚠️ NeurIPS 2023 AI4Science workshop paper, NOT indexed by DBLP.',
        'source': 'NeurIPS 2023 Workshop AI4Science, OpenReview yGVChrbJ4E, not in DBLP',
    },
    'rehm2025accgpt': {
        'verdict': '✅ Accurate, retrieval-grounded',
        'evidence': 'AccGPT is an on-premise “knowledge retrieval chatbot” that lets an LLM “reference an external knowledge base, such as CERN’s internal documentation” (e5-large-v2 embeddings) before answering, single-corpus grounding over institution-private docs. ⚠️ EPJ Web of Conferences (CHEP 2024) proceedings, NOT indexed by DBLP.',
        'source': 'EPJ Web Conf 337:01279, 2025, DOI 10.1051/epjconf/202533701279, not in DBLP',
    },
    'DBLP:conf/nips/BushuievBJYKSHW24': {
        'verdict': '⚠️ Accurate on facts, but it is a benchmark, not a framework, and de novo generation is generation, not retrieval',
        'evidence': 'MassSpecGym is “the first comprehensive benchmark for the discovery and identification of molecules from MS/MS data”, a dataset (231k spectra over 29k structures), NOT a RAG method/framework. It defines three challenges: “de novo molecular structure generation, molecule retrieval, and spectrum simulation”; only the second is retrieval-based, so the de novo task the paragraph foregrounds generates (does not “retrieve across spectra”) a structure from one spectrum. De novo generation is scored by Top-k accuracy, Top-k MCES and Top-k Tanimoto; published baselines reach Top-1 accuracy 0.00 (“none of the baselines achieve an accuracy above zero”).',
        'source': 'NeurIPS 2024 Datasets & Benchmarks, arXiv:2410.23326 (DBLP-verified)',
    },
    # --- K2.O3 (Simulation-verified Materials Design), verified 2026-05-31 against full bodies. See factcheck_kxo_k2o3.md ---
    'DBLP:journals/corr/abs-2603-15712': {
        'verdict': '✅ Accurate, strong K2.O3 fit',
        'evidence': 'Grounds an LLM on “a curated database of 50,000+ validated materials” (Materials Project + NOMAD + OC20; two-stage cosine + chemical-filter retrieval, k=20), “generated over 250 catalyst candidates with an 82% thermodynamic stability rate,” verified by DFT (VASP 6.3 PBE+U, convex hull E_hull<50 meV/atom). Best composition “Fe0.2Co0.2Ni0.2Ir0.1Ru0.3 achieves 0.285V limiting potential.” Genuine RAG → new candidates → DFT-verified. (Byline “AI Scientists” is a genuine DBLP-registered autonomous-agent author, not a fabrication.)',
        'source': 'CoRR 2026, arXiv:2603.15712 (DBLP-verified)',
    },
    'zhang2026matclaw': {
        'verdict': '⚠️ Misclassified, real K2 code-RAG, but NOT O3 / not simulation-verified',
        'evidence': 'MatClaw genuinely uses RAG over the source code of pymatgen, atomate2, jobflow, dpdata, DeePMD-kit (BM25 + 3-query RRF), “rais[ing] per-step API-call accuracy to ~99%.” BUT it generates NO new material candidates (full-text counts: candidate=0, novel=0), all demos run on the existing material CuInP2S6, and it does NOT verify with external simulation: “All three tasks use the pre-trained DeePMD model … rather than DFT calculations.” The phrase “workflow success rate” does not appear (per-task Success/Failure table only). → fails the O3 (new-candidate) and simulation-verified axes; belongs in a K2 code-library-RAG / agentic-workflow class, not K2.O3.',
        'source': 'CoRR 2026, arXiv:2604.02688 (DBLP-verified)',
    },
    'ong2013python': {
        'verdict': '✅ Real software citation, metadata correct',
        'evidence': 'pymatgen: Ong et al., “Python Materials Genomics (pymatgen)…”, Computational Materials Science 68:314–319 (2013), doi 10.1016/j.commatsci.2012.10.028. Verified via ScienceDirect; title/venue/volume/pages/year/DOI all match.',
        'source': 'Comput. Mater. Sci. 68:314–319, 2013 (software ref; not in DBLP)',
    },
    'ganose2025_atomate2': {
        'verdict': '✅ Real software citation, metadata correct',
        'evidence': 'atomate2: Ganose et al., “Atomate2: modular workflows for materials science”, Digital Discovery 4:1944–1973 (2025), doi 10.1039/D5DD00019J. Verified via RSC; title/venue/year/DOI match.',
        'source': 'Digital Discovery 4:1944–1973, 2025 (software ref; not in DBLP)',
    },
    'rosen2024jobflow': {
        'verdict': '✅ Real software citation, metadata correct',
        'evidence': 'jobflow: Rosen et al., “Jobflow: Computational Workflows Made Simple”, JOSS 9(93):5995 (2024), doi 10.21105/joss.05995. Verified via JOSS; all fields match.',
        'source': 'JOSS 9(93):5995, 2024 (software ref; not in DBLP)',
    },
    'doi:10.1021/acs.jcim.5c01767': {
        'verdict': '✅ Real software citation, metadata correct',
        'evidence': 'dpdata: Zeng et al., “dpdata: A Scalable Python Toolkit for Atomistic Machine Learning Data Sets”, J. Chem. Inf. Model. 65(21):11497–11504 (2025), doi 10.1021/acs.jcim.5c01767. Verified via ACS/PubMed; all fields match.',
        'source': 'J. Chem. Inf. Model. 65(21):11497–11504, 2025 (software ref; not in DBLP)',
    },
    'Wang_ComputPhysCommun_2018_v228_p178': {
        'verdict': '✅ Real software citation, metadata correct',
        'evidence': 'DeePMD-kit: Wang, Zhang, Han, E, “DeePMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics”, Comput. Phys. Comm. 228:178–184 (2018), doi 10.1016/j.cpc.2018.03.016. Verified via ScienceDirect/arXiv:1712.03641; all fields match.',
        'source': 'Comput. Phys. Comm. 228:178–184, 2018 (software ref; not in DBLP)',
    },
    # --- K1.O3 (Weak-verifier Hypothesis), verified 2026-06-01 against full bodies + real DBLP. See factcheck below ---
    'DBLP:conf/iclr/0001LGXLOPCZ25': {
        'verdict': '✅ Accurate, K1.O3 weak-verifier',
        'evidence': 'MOOSE-Chem retrieves inspiration papers from a chemistry-literature corpus (“3000 most cited chemistry papers published in Nature”), K1, not a curated KB. Retrieval is one of three core subtasks (retrieve inspirations / compose / rank). It GENERATES novel chemistry hypotheses, judged by rediscovering held-out high-impact 2024 findings (TOMATO-Chem), a weak verifier, no docking/sim. Method-primary (benchmark is enabling infrastructure).',
        'source': 'ICLR 2025, OpenReview X9OfMNNepI (DBLP-verified)',
    },
    'DBLP:conf/acl/0005DJH24': {
        'verdict': '✅ Accurate, K1.O3 weak-verifier',
        'evidence': 'SciMON retrieves “inspirations” from a paper corpus (“67,408 ACL Anthology papers”) plus citation/KG neighbors built from that corpus (K1). Retrieval is the core input stage (genuine RAG). It generates new ideas grounded in literature and “iteratively optimizes for novelty against prior work”, weak verifier. Method paper.',
        'source': 'ACL 2024, pp. 279–299, doi 10.18653/v1/2024.acl-long.18 (DBLP-verified)',
    },
    'DBLP:conf/naacl/BaekJCH25': {
        'verdict': '✅ Accurate, K1.O3 weak-verifier',
        'evidence': 'ResearchAgent augments a core paper with “relevant publications by connecting information over an academic graph” plus “entities … from a knowledge store derived from … concepts mined across numerous papers”, both literature-derived (K1, not an external curated KB). It “defines novel problems, proposes methods and designs experiments,” refined by LLM ReviewingAgents (weak verifier, no external confirmation). Method paper.',
        'source': 'NAACL 2025, pp. 6709–6738, doi 10.18653/v1/2025.naacl-long.342 (DBLP-verified)',
    },
    'DBLP:conf/emnlp/LiXGZLYZJXDRZFB25': {
        'verdict': '✅ Accurate, K1.O3 weak-verifier',
        'evidence': 'Chain-of-Ideas retrieves papers via the Semantic Scholar API and organizes citations into a forward/backward “evolution chain” (K1 literature), then extrapolates the next research idea (genuine RAG, improving on vanilla RAG). Evaluated with “Idea Arena,” a human-preference-aligned novelty protocol, weak verifier. Method-primary (Idea Arena is the secondary contribution).',
        'source': 'EMNLP 2025 Findings, pp. 8971–9004, ACL Anthology 2025.findings-emnlp.477 (DBLP-verified)',
    },
}
# Cells whose papers show the fact-check footnote chip on the cell page.
# Emptied per user request (chip removed from the UI); FACTCHECK data above is
# retained for the report / future use. Add a cell key here to re-enable its chips.
# Fact-check footnotes were tied to the earlier epistemic cell meanings; disabled under the
# substrate × objective taxonomy until re-verified against the new cell definitions.
FACTCHECKED_CELLS = set()


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

# Authoritative per-paper classifications transcribed from the paper's own tables, so every
# system the survey actually cites lands where the paper puts it (not where the modality
# heuristic guesses). PAPER_BENCH = Table 2 (benchmarks): key -> (substrate, task family).
# PAPER_DB = the §4 knowledge-source table (databases): key -> substrate only (no objective).
PAPER_BENCH = {
    'jin-etal-2019-pubmedqa': ('K1', 'Question Answering'),
    'zaki2024mascqa': ('K1', 'Question Answering'),
    'welbl-etal-2017-crowdsourcing': ('K1', 'Question Answering'),
    'auer2023sciqa': ('K2', 'Question Answering'),
    'DBLP:conf/eccv/SunWZZCZZWLZLLLY24': ('K4', 'Question Answering'),
    'DBLP:journals/corr/abs-2003-10286': ('K4', 'Question Answering'),
    'PhysioNet-mimic-cxr-2.1.0': ('K4', 'Question Answering'),
    'DBLP:conf/emnlp/WaddenLLWZCH20': ('K1', 'Claim Verification'),
    'DBLP:conf/emnlp/WaddenLKCBWH22': ('K1', 'Claim Verification'),
    'DBLP:journals/corr/abs-2310-16146': ('K1', 'Literature Synthesis'),
    'DBLP:conf/emnlp/LuDC20': ('K2', 'Literature Synthesis'),
    'DBLP:journals/corr/WuRFGGPLP17': ('K3', 'Property Prediction'),
    'DBLP:conf/nips/HuangFG0RLCXSZ21': ('K3', 'Property Prediction'),
    'zhou2019cafa': ('K3', 'Property Prediction'),
    'roohani2024gears': ('K3', 'Property Prediction'),
    'DBLP:journals/corr/abs-2408-10609': ('K3', 'Property Prediction'),
    'DBLP:journals/bioinformatics/BreitOAS20': ('K2', 'Property Prediction'),
    'DBLP:conf/nips/HuFZDRLCL20': ('K2', 'Property Prediction'),
    'DBLP:conf/nips/BushuievBJYKSHW24': ('K4', 'Property Prediction'),
    'DBLP:journals/jcisd/FrancoeurMSJISK20': ('K3', 'Molecular Design'),
    'gao2022sample': ('K3', 'Molecular Design'),
    'lan2023adsorbml': ('K3', 'Materials Discovery'),
    'DBLP:journals/corr/abs-2509-20630': ('K3', 'Materials Discovery'),
    'DBLP:journals/corr/abs-2410-05080': ('K3', 'Materials Discovery'),
    'riebesell2025framework': ('K3', 'Materials Discovery'),
    # rows whose names carry parentheses/specials (missed by the strict table parse)
    'krithara2023bioasq': ('K1', 'Literature Synthesis'),
    'liu2025researchbench': ('K1', 'Hypothesis Generation'),
    'liu2025hypobench': ('K1', 'Hypothesis Generation'),
    'xiong2025truthhypo': ('K2', 'Hypothesis Generation'),
}
PAPER_DB = {
    'DBLP:journals/corr/abs-2205-01833': 'K2', 'DBLP:conf/acl/LoWNKW20': 'K2',
    'canese2013pubmed': 'K1', 'europepmc2024': 'K1', 'kurtz2000nasa': 'K1', 'inspirehep': 'K1',
    'georef': 'K1', 'lee2023climate': 'K1', 'scopus': 'K1', 'webofscience': 'K1',
    'DBLP:journals/qss/HerzogHK20': 'K1', 'embase': 'K1', 'rafique2025large': 'K1',
    'bodenreider2004unified': 'K2', 'chandak2023building': 'K2', 'ioannidis2020drkg': 'K2',
    'DBLP:journals/nar/SzklarczykSMJBK16': 'K2', 'kanehisa2000kegg': 'K2', 'milacic2024reactome': 'K2',
    'ashburner2000gene': 'K2',
    'DBLP:journals/nar/GaultonBBCDHLMMAO12': 'K3', 'irwin2012zinc': 'K3',
    'DBLP:journals/nar/KimTBCFGHHHSWYZ16': 'K3', 'DBLP:journals/nar/BermanWFGBWSB00': 'K3',
    'DBLP:journals/nar/VaradiADNNYYSWL22': 'K3', 'varadi2024alphafold': 'K3',
    'jain2013commentary': 'K3', 'saal2013materials': 'K3',
    'ramakrishnan2014quantum': 'K3', 'DBLP:journals/nar/LiuLWJG07': 'K3',
    'demner2016preparing': 'K4', 'petersen2010alzheimer': 'K4', 'york2000sloan': 'K4',
    'vallenari2023gaia': 'K4', 'mast': 'K4', 'DBLP:conf/mss/KoblerBCH95': 'K4',
    'eyring2016overview': 'K4', 'cernopendata': 'K4',
}


# ---------- Central taxonomy remap ----------
# Every paper carries an assignment from the earlier epistemic taxonomy (Primary Literature /
# Curated KB / Observational / Tacit  ×  Ground / Synthesis / Hypothesis). We remap each paper
# onto the survey's published taxonomy, retrieval SUBSTRATE (§4) × OBJECTIVE rung (§5), once,
# in place, so every downstream aggregation (grid, cell pages, browse, insights) reflects it.
#   Substrate: K1 Textual, K2 Relational, K3 Structured-entity, K4 Perceptual
#   Rung:      O1 Grounding, O2 Synthesis, O3 Discovery
# The assembly-figure core systems (CELL_PAPERS / CORE_SYSTEM_TASK) are authoritative and pin
# their own substrate, rung, and task; the long tail is mapped by modality, then by the old tag.
CORE_CELL = {}
for _cell, _keys in CELL_PAPERS.items():
    for _k in _keys:
        CORE_CELL.setdefault(_k, _cell)

MODALITY_SUBSTRATE = {
    'KG': 'K2',
    'SMILES': 'K3', '3D Structure': 'K3', 'Structured Table': 'K3',
    'Image': 'K4', 'CSV': 'K4',
    'Text': 'K1',
}
# When a paper mixes modalities, the harder-to-index (non-textual) substrate defines it.
SUBSTRATE_PRIORITY = ['K4', 'K3', 'K2', 'K1']


def _substrate_for(p):
    subs = {MODALITY_SUBSTRATE[m] for m in (p.get('modality') or []) if m in MODALITY_SUBSTRATE}
    for s in SUBSTRATE_PRIORITY:
        if s in subs:
            return s
    old = (p.get('ko_primary') or '')
    oldK = old.split('.')[0] if old else ''
    doms = p.get('domain') or []
    if oldK == 'K3':   # old Observational & Experimental -> Perceptual
        return 'K4'
    if oldK == 'K4':   # old Tacit corpora are textual documents -> Textual
        return 'K1'
    if oldK == 'K2':   # old Curated KB -> Structured-entity for physical-science DBs, else Relational
        return 'K3' if any(d in ('chem', 'material', 'physics') for d in doms) else 'K2'
    return 'K1'


def _rung_for(p):
    for c in (p.get('ko_cells') or []):
        if '.O' in c:
            return 'O' + c.split('.O', 1)[1][0]
    prim = p.get('ko_primary') or ''
    if '.O' in prim:
        return 'O' + prim.split('.O', 1)[1][0]
    if prim[:1] == 'O' and prim[1:2].isdigit():
        return prim[:2]
    return None


def _task_for(substrate, rung, p):
    old_subs = p.get('subsection') or []
    if isinstance(old_subs, str):
        old_subs = [old_subs]
    j = ' '.join(old_subs).lower()
    if rung == 'O1':
        return 'Cross-modal Grounding' if substrate == 'K4' else 'Question Answering'
    if rung == 'O2':
        return 'Claim Verification' if ('verif' in j or 'claim' in j or 'contra' in j) else 'Literature Synthesis'
    if rung == 'O3':
        if 'docking' in j or 'molecul' in j:
            return 'Molecular Design'
        if 'material' in j or 'simulation' in j or 'dft' in j or 'catalyst' in j:
            return 'Materials Discovery'
        if 'prediction' in j or 'database-verified' in j or 'property' in j:
            return 'Property Prediction'
        if 'hypothesis' in j or 'weak' in j or 'idea' in j:
            return 'Hypothesis Generation'
        return {'K3': 'Molecular Design', 'K4': 'Property Prediction'}.get(substrate, 'Hypothesis Generation')
    return None


for p in papers:
    # Normalize domain slugs onto their canonical page (dedup, preserve order).
    if p.get('domain'):
        _seen_dom = set()
        _norm = []
        for _d in p['domain']:
            _d = DOMAIN_ALIAS.get(_d, _d)
            if _d and _d not in _seen_dom:
                _seen_dom.add(_d)
                _norm.append(_d)
        p['domain'] = _norm
    bib = p.get('bib_key')
    if bib in CORE_CELL:                       # Fig. 2 assembly (methods), highest authority
        substrate, rung = CORE_CELL[bib].split('.')
        task = CORE_SYSTEM_TASK.get(bib)
    elif bib in PAPER_BENCH:                    # Table 2 (benchmarks), substrate + task
        substrate, task = PAPER_BENCH[bib]
        rung = TASK_RUNG.get(task)
    elif bib in PAPER_DB:                       # §4 knowledge-source table (databases), substrate only
        substrate, rung, task = PAPER_DB[bib], None, None
    else:                                       # long tail not cited by the survey, modality heuristic
        substrate = _substrate_for(p)
        rung = _rung_for(p)
        task = _task_for(substrate, rung, p) if rung else None
    if rung:
        newcell = f'{substrate}.{rung}'
        p['ko_cells'] = [newcell]
        p['ko_primary'] = newcell
    else:
        p['ko_cells'] = [substrate]
        p['ko_primary'] = substrate
    p['subsection'] = [task] if task else []

# ---------- Group ----------
by_cell = defaultdict(list)
by_dom = defaultdict(list)
by_type = defaultdict(list)
papers_by_key = {}
for p in papers:
    if p.get('bib_key'):
        papers_by_key[p['bib_key']] = p
    _axis_seen = set()
    for c in p.get('ko_cells', []):
        by_cell[c].append(p)
        # Also populate the single-axis buckets (K-only / O-only) so those pages and the
        # sidebar counts show every paper of a substrate or rung, not only the cell it lands in.
        if '.' in c:
            for part in c.split('.'):
                if part and part not in _axis_seen:
                    _axis_seen.add(part)
                    by_cell[part].append(p)
    for d in p.get('domain', []):
        by_dom[d].append(p)
    by_type[p.get('type', 'unknown')].append(p)


def cell_count(c):
    """Number of papers shown on a K×O cell page. Uses the main.tex citation
    allow-list (CELL_PAPERS) when present so sidebar/grid counts match the page,
    otherwise falls back to the full Notion-DB tagging."""
    if c in CELL_PAPERS:
        return sum(1 for k in CELL_PAPERS[c] if k in papers_by_key)
    return len(by_cell.get(c, []))


def axis_papers(axis):
    """Papers shown on a K-only (K1..K4) or O-only (O1..O3) aggregate page.

    Aligned to main2.tex: returns the deduplicated union of the curated per-cell
    allow-lists (CELL_PAPERS) whose cell falls under this axis, in cell order and
    then main.tex citation order. This keeps the K1/K2/… and O1/O2/O3 pages a clean
    roll-up of their cells instead of dumping every heuristically-tagged paper
    (which previously bloated K1 to 100+ off-topic entries)."""
    ps, seen = [], set()
    for cell, keys in CELL_PAPERS.items():
        K, O = cell.split('.')
        if axis not in (K, O):
            continue
        for k in keys:
            p = papers_by_key.get(k)
            if p is not None and k not in seen:
                seen.add(k)
                ps.append(p)
    return ps


def axis_count(axis):
    return len(axis_papers(axis))


def task_system_count(task):
    """Papers tagged with this §5 task family (subsection), matching browse ?sub=."""
    return sum(1 for p in papers if task in (p.get('subsection') or []))


# ---------- At-a-glance systems table (paper Table 3) ----------
_ms_by_key = {s['bib_key']: s for s in METHOD_SYSTEMS}
COUPLING_ORDER = ['Open', 'Self-check', 'External-verify', 'Closed-loop']
COUPLING_DESC = {
    'Open': 'retrieve and generate once, output returned unchecked',
    'Self-check': 'critiques its own draft, consulting only the retrieved evidence',
    'External-verify': 'an outside process scores the finished output once',
    'Closed-loop': 'the verifier runs inside the loop and drives refinement',
}
K_SHORT = {'K1': 'Txt', 'K2': 'Rel', 'K3': 'Str', 'K4': 'Prc'}
O_SHORT = {
    'Question Answering': 'QA', 'Literature Synthesis': 'LS', 'Claim Verification': 'CV',
    'Hypothesis Generation': 'HG', 'Molecular Design': 'MD', 'Materials Discovery': 'MtD',
    'Property Prediction': 'PP', 'Cross-modal Grounding': 'CmG',
}


def _system_name_html(s, base):
    """System name, linked to its on-site summary page if one exists, else to the
    external paper, else plain."""
    bib = s['bib_key']
    fn = bib.replace(':', '_').replace('/', '_') + '.html'
    label = esc(s['name'])
    if (ROOT / 'papers' / fn).exists():
        return f'<a href="{base}papers/{fn}">{label}</a>'
    p = papers_by_key.get(bib)
    link = p.get('paper_link') if p else None
    if link:
        return f'<a href="{esc(link)}" target="_blank" rel="noopener">{label}</a>'
    return label


def systems_table_html(bib_keys, base='../', caption=None):
    """Compact pipeline table for the given systems, mirroring the survey's Table 3
    (System | K | Construction φ | Matching s | Integration G | Verifier V | O),
    grouped by depth of verifier coupling. Renders nothing if no system on the page
    appears in the extracted table."""
    rows = [_ms_by_key[k] for k in bib_keys if k in _ms_by_key]
    if not rows:
        return ''
    by_couple = defaultdict(list)
    for r in rows:
        by_couple[r.get('coupling') or 'Open'].append(r)

    body_rows = []
    for coup in COUPLING_ORDER:
        group = by_couple.get(coup)
        if not group:
            continue
        body_rows.append(
            f'<tr class="sys-group"><td colspan="7"><span class="sys-coupling">{esc(coup)}</span>'
            f'<span class="sys-coupling-desc">{esc(COUPLING_DESC.get(coup, ""))}</span></td></tr>'
        )
        for s in group:
            k = s.get('K', '')
            o_full = s.get('O', '')
            o_rung = s.get('O_rung', '')
            body_rows.append(
                '<tr>'
                f'<td class="sys-name">{_system_name_html(s, base)}</td>'
                f'<td><span class="sys-k sys-k-{k.lower()}" title="{esc(K_LABELS.get(k, (k,))[0])}">{esc(K_SHORT.get(k, k))}</span></td>'
                f'<td>{esc(s.get("construction", ""))}</td>'
                f'<td>{esc(s.get("matching", ""))}</td>'
                f'<td>{esc(s.get("integration", ""))}</td>'
                f'<td>{esc(s.get("verifier", ""))}</td>'
                f'<td><span class="sys-o sys-o-{o_rung.lower()}" title="{esc(o_full)}">{esc(O_SHORT.get(o_full, o_full))}</span></td>'
                '</tr>'
            )
    cap = f'<figcaption class="sys-cap">{esc(caption)}</figcaption>' if caption else ''
    return f'''
<figure class="sys-table-wrap">
  {cap}
  <div class="sys-table-scroll">
    <table class="sys-table">
      <thead><tr>
        <th>System</th><th>K</th><th>Construction <span class="sys-sym">φ</span></th>
        <th>Matching <span class="sys-sym">s</span></th><th>Integration <span class="sys-sym">𝒢</span></th>
        <th>Verifier <span class="sys-sym">𝒱</span></th><th>O</th>
      </tr></thead>
      <tbody>{"".join(body_rows)}</tbody>
    </table>
  </div>
</figure>'''


def prose_html(text):
    """Wrap extracted §4/§5 prose (paragraphs split on blank lines) into <p> blocks."""
    if not text:
        return ''
    return '\n'.join(f'<p>{esc(p.strip())}</p>' for p in text.split('\n\n') if p.strip())


def _res_name_html(r):
    name = esc(r.get('name', ''))
    link = r.get('link')
    return f'<a href="{esc(link)}" target="_blank" rel="noopener">{name}</a>' if link else name


def resource_chips_html(resources, base='../'):
    """The actual data resources as linked chips (each opens the dataset homepage)."""
    if not resources:
        return ''
    items = []
    for r in resources:
        name = esc(r.get('name', ''))
        link = r.get('link')
        if link:
            items.append(f'<a class="res-chip" href="{esc(link)}" target="_blank" rel="noopener">{name}</a>')
        else:
            items.append(f'<span class="res-chip res-chip-plain">{name}</span>')
    return f'<div class="res-chips">{"".join(items)}</div>'


def resource_table_html(resources):
    """A compact per-dataset description table: Dataset (linked) | Description."""
    rows = [r for r in resources if r.get('desc')]
    if not rows:
        return ''
    body = ''.join(
        f'<tr><td class="res-td-name">{_res_name_html(r)}</td>'
        f'<td class="res-td-desc">{esc(r.get("desc", ""))}</td></tr>'
        for r in resources
    )
    return (f'<div class="sys-table-scroll res-table-scroll"><table class="sys-table res-table">'
            f'<thead><tr><th>Dataset</th><th>Description</th></tr></thead>'
            f'<tbody>{body}</tbody></table></div>')


def substrate_resources_html(K, base='../', heading_level='h3'):
    """Short §4 summary for one substrate + its data resources, grouped by
    sub-subsection: linked chips for a quick scan, then a per-dataset description
    table. No long prose — just the key line and the datasets themselves."""
    s = K_PROSE.get(K)
    if not s:
        return ''
    parts = []
    if s.get('summary'):
        parts.append(f'<p class="axis-lede">{esc(s["summary"])}</p>')
    for ss in s.get('subsubs', []):
        note = ss.get('summary', '')
        res = ss.get('resources', [])
        parts.append(
            f'<div class="res-group">'
            f'<{heading_level} class="res-group-title">{esc(ss.get("title", ""))}</{heading_level}>'
            + (f'<p class="res-note">{esc(note)}</p>' if note else '')
            + resource_chips_html(res, base)
            + resource_table_html(res)
            + '</div>'
        )
    return '\n'.join(parts)


def _access_class(access):
    a = (access or '').lower()
    if a.startswith('open'):
        return 'acc-open'
    if a.startswith('comm'):
        return 'acc-comm'
    if a.startswith('restr'):
        return 'acc-restr'
    return 'acc-mixed'


def knowledge_source_table_html(substrate=None, base='../', caption=None):
    """Paper Table 1 — knowledge sources (the data on the K axis), columns
    Resource group | Scale | Access | Notes. If `substrate` (K1..K4) is given, show
    only that substrate's rows; otherwise group all four."""
    rows = [r for r in KNOWLEDGE_SOURCES if substrate is None or r.get('substrate') == substrate]
    if not rows:
        return ''
    body = []
    last_sub = None
    for r in rows:
        if substrate is None and r.get('substrate') != last_sub:
            last_sub = r.get('substrate')
            k = last_sub
            body.append(
                f'<tr class="ks-group"><td colspan="4">'
                f'<span class="sys-k sys-k-{str(k).lower()}">{esc(K_SHORT.get(k, k))}</span>'
                f'<span class="ks-sub-name">{esc(r.get("substrate_name", ""))}</span></td></tr>'
            )
        body.append(
            '<tr>'
            f'<td class="ks-name">{esc(r.get("resource_group", ""))}</td>'
            f'<td class="ks-scale">{esc(r.get("scale", ""))}</td>'
            f'<td><span class="ks-acc {_access_class(r.get("access"))}">{esc(r.get("access", ""))}</span></td>'
            f'<td>{esc(r.get("notes", ""))}</td>'
            '</tr>'
        )
    cap = f'<figcaption class="sys-cap">{esc(caption)}</figcaption>' if caption else ''
    return f'''
<figure class="sys-table-wrap">
  {cap}
  <div class="sys-table-scroll">
    <table class="sys-table ks-table">
      <thead><tr>
        <th>Resource group</th><th>Scale</th><th>Access</th><th>Notes</th>
      </tr></thead>
      <tbody>{"".join(body)}</tbody>
    </table>
  </div>
</figure>'''


def _benchmark_rows(rung=None, tasks=None):
    return [r for r in BENCHMARKS
            if (rung is None or r.get('O_rung') == rung)
            and (tasks is None or r.get('task') in tasks)]


def _benchmark_name_html(r, base):
    """Benchmark name linked to its on-site summary if present, else its homepage/paper."""
    bib = r.get('bib_key', '')
    fn = bib.replace(':', '_').replace('/', '_') + '.html'
    name = esc(r.get('benchmark', ''))
    if (ROOT / 'papers' / fn).exists():
        return f'<a href="{base}papers/{fn}">{name}</a>'
    link = r.get('link') or (papers_by_key.get(bib) or {}).get('paper_link')
    if link:
        return f'<a href="{esc(link)}" target="_blank" rel="noopener">{name}</a>'
    return name


def benchmark_chips_html(rung=None, tasks=None, base='../'):
    """Benchmarks as linked chips (each opens the benchmark's homepage/paper)."""
    rows = _benchmark_rows(rung, tasks)
    if not rows:
        return ''
    items = []
    for r in rows:
        name = esc(r.get('benchmark', ''))
        link = r.get('link')
        if link:
            items.append(f'<a class="res-chip" href="{esc(link)}" target="_blank" rel="noopener">{name}</a>')
        else:
            items.append(f'<span class="res-chip res-chip-plain">{name}</span>')
    return f'<div class="res-chips">{"".join(items)}</div>'


def benchmark_table_html(rung=None, tasks=None, base='../', caption=None, show_group=True):
    """Paper Table 2 — benchmarks (the tasks on the O axis), columns
    Benchmark | Domain | K | Scale | Description, grouped by task family. Filter by
    O rung (O1..O3) or by an explicit list of task names. show_group=False drops the
    per-task header rows (used when an <h3> already labels the task)."""
    rows = _benchmark_rows(rung, tasks)
    if not rows:
        return ''
    by_task = defaultdict(list)
    order = []
    for r in rows:
        t = r.get('task', '')
        if t not in by_task:
            order.append(t)
        by_task[t].append(r)
    body = []
    for t in order:
        if show_group:
            body.append(f'<tr class="bm-group"><td colspan="5"><span class="bm-task">{esc(t)}</span></td></tr>')
        for r in by_task[t]:
            k = r.get('K', '')
            body.append(
                '<tr>'
                f'<td class="sys-name">{_benchmark_name_html(r, base)}</td>'
                f'<td>{esc(r.get("domain", ""))}</td>'
                f'<td><span class="sys-k sys-k-{str(k).lower()}" title="{esc(K_LABELS.get(k, (k,))[0])}">{esc(K_SHORT.get(k, k))}</span></td>'
                f'<td class="ks-scale">{esc(r.get("scale", ""))}</td>'
                f'<td>{esc(r.get("description", ""))}</td>'
                '</tr>'
            )
    cap = f'<figcaption class="sys-cap">{esc(caption)}</figcaption>' if caption else ''
    return f'''
<figure class="sys-table-wrap">
  {cap}
  <div class="sys-table-scroll">
    <table class="sys-table bm-table">
      <thead><tr>
        <th>Benchmark</th><th>Domain</th><th>K</th><th>Scale</th><th>Description</th>
      </tr></thead>
      <tbody>{"".join(body)}</tbody>
    </table>
  </div>
</figure>'''


def objective_tasks_html(rung, base='../', heading_level='h3'):
    """Mirror of substrate_resources_html for the O axis: for each task under this
    rung, a short §5 summary + its benchmarks as chips + a per-benchmark table."""
    tasks = [t['name'] for t in AXIS_PROSE.get('O', {}).get('tasks', []) if t.get('rung') == rung]
    parts = []
    for t in tasks:
        tp = O_PROSE.get(t, {})
        title = f'<a href="{base}cell/{task_slug(t)}.html">{esc(t)}</a>'
        parts.append(
            f'<div class="res-group">'
            f'<{heading_level} class="res-group-title">{title}</{heading_level}>'
            + (f'<p class="res-note">{esc(tp.get("summary", ""))}</p>' if tp.get('summary') else '')
            + benchmark_chips_html(tasks=[t], base=base)
            + benchmark_table_html(tasks=[t], base=base, show_group=False)
            + '</div>'
        )
    return '\n'.join(parts)


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
            n = cell_count(c)
            cell_items += f'<a href="{base}cell/{c}.html" class="sb-sub{cls(f"cell/{c}")}">{cell_label(c)} <span class="sb-count">{n}</span></a>\n'

    # K-axis roll-up pages (K1-K4)
    k_axis_items = ''
    for K in ['K1', 'K2', 'K3', 'K4']:
        n = axis_count(K)
        k_axis_items += f'<a href="{base}cell/{K}.html" class="sb-sub{cls(f"cell/{K}")}">{K_LABELS[K][0]} <span class="sb-count">{n}</span></a>\n'

    # Operational Objective — the seven task families of §5, grouped under the three rungs
    # (grounding, synthesis, discovery) in the order the survey presents them. Each rung
    # header links to its aggregate page; each task links to its own page.
    RUNGS = [
        ('O1', 'Grounding',  ['Question Answering']),
        ('O2', 'Synthesis',  ['Claim Verification', 'Literature Synthesis']),
        ('O3', 'Discovery',  ['Property Prediction', 'Molecular Design', 'Materials Discovery', 'Hypothesis Generation']),
    ]
    task_items = ''
    for O, rung_name, tasks in RUNGS:
        n_rung = axis_count(O)
        task_items += (f'<a href="{base}cell/{O}.html" class="sb-subhead{cls(f"cell/{O}")}">'
                       f'{rung_name} <span class="sb-count">{n_rung}</span></a>\n')
        for t in tasks:
            slug = task_slug(t)
            task_items += (f'<a href="{base}cell/{slug}.html" class="sb-sub sb-task{cls(f"cell/{slug}")}">'
                           f'{esc(t)} <span class="sb-count">{task_system_count(t)}</span></a>\n')

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
      <div class="sb-logo-sub">Vision and Learning Lab, SNU</div>
    </div>
  </a>
  <nav class="sb-nav">
    <a href="{base}index.html" class="sb-item{cls("home")}"><span class="sb-icon">🏠</span> Home</a>
    <a href="{base}about.html" class="sb-item{cls("about")}"><span class="sb-icon">🚀</span> Getting Started</a>

    <details class="sb-group"{cell_open}>
      <summary class="sb-item"><span class="sb-icon">K</span> Knowledge Source <span class="sb-caret">▾</span></summary>
      <div class="sb-subs">
        <a href="{base}cell/knowledge-source.html" class="sb-sub sb-sub-overview{cls("cell/knowledge-source")}">Overview — the data &amp; substrates →</a>
        {k_axis_items}
      </div>
    </details>

    <details class="sb-group"{cell_open}>
      <summary class="sb-item"><span class="sb-icon">O</span> Operational Objective <span class="sb-caret">▾</span></summary>
      <div class="sb-subs">
        <a href="{base}cell/operational-objective.html" class="sb-sub sb-sub-overview{cls("cell/operational-objective")}">Overview — the tasks &amp; rungs →</a>
        {task_items}
      </div>
    </details>

    <details class="sb-group"{cell_open}>
      <summary class="sb-item"><span class="sb-icon">▦</span> Substrate × Objective <span class="sb-caret">▾</span></summary>
      <div class="sb-subs">
        <a href="{base}browse.html" class="sb-sub sb-sub-overview">All 12 cells →</a>
        {cell_items}
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
    <a href="https://github.com/yerimoh/ScienceRAGSurvey" class="sb-item sb-quiet" target="_blank" rel="noopener"><span class="sb-icon">⌥</span> GitHub ↗</a>
  </nav>
</aside>
'''


def page_head(title, base='', desc='Scientific RAG Hub, a curated catalog of retrieval-augmented generation systems for scientific discovery.', current=''):
    # Cache-bust the CSS using the file's mtime so browsers always pull the latest after a rebuild.
    css_mtime = int((ROOT / 'static/style.css').stat().st_mtime)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}, Scientific RAG Hub</title>
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
      <strong>Scientific RAG Hub</strong>, companion catalog to the upcoming survey
      <em>"Scientific Retrieval-Augmented Generation: A Survey and Taxonomy"</em>
      by Oh et al. (Vision and Learning Lab, Seoul National University).
    </p>
    <p class="links">
      <a href="{base}llms.txt">llms.txt</a>
      <a href="{base}llms-full.txt">llms-full.txt</a>
      <a href="{base}data/catalog.json">catalog.json</a>
      <a href="{base}about.html">About</a>
    </p>
  </div>
</footer>
<script src="{base}static/footnotes.js?v={js_mtime}"></script>
</body>
</html>
'''

PAGE_FOOT = page_foot()  # back-compat for callers that still use the constant


def paper_card(p, base='', axis_scope=None, factcheck_id=None):
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
    meta = ', '.join(meta_parts)

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
    # Fact-check footnote chip, clicking opens a popover with verbatim original-text
    # evidence (footnotes.js), instead of jumping to the raw paper link.
    fc_html = ''
    if factcheck_id and bib_key in FACTCHECK:
        verdict = esc(FACTCHECK[bib_key]['verdict'])
        fc_html = (f'<p class="card-factcheck"><a class="footnote-ref" '
                   f'href="#{factcheck_id}" title="source evidence">{verdict}, source ⌖</a></p>')
    return f'''<article class="card"{subsec_attr}>
  <h3 class="card-title">{title_html}</h3>
  {f'<div class="card-meta">{meta}</div>' if meta else ''}
  {f'<p class="card-note">{note}</p>' if note else ''}
  {fc_html}
  <div class="card-tags">{''.join(tag_html)}</div>
  {summary_link}
</article>
'''


# The paper's overview figure (Fig. 1) as the main-page centerpiece: what a system retrieves
# (substrate) → how it construct/retrieve/generate/verify → what objective it produces.
PIPELINE_HTML = '''
<section id="overview" class="flow-section">
  <div class="wrap">
    <h2 class="section-title">How a scientific RAG system works</h2>
    <p class="section-sub">
      The survey organizes the field not as a grid of cells but as the <em>pipeline</em> a system runs:
      what knowledge it <strong>retrieves</strong> (the substrate), how it <strong>constructs, retrieves,
      generates, and verifies</strong>, and what <strong>objective</strong> it produces, scored by evaluation.
      Science specializes every stage.
    </p>
    <div class="flow">
      <div class="flow-card flow-k">
        <div class="flow-cap">Knowledge&nbsp;Source</div>
        <a class="flow-chip flow-kc" href="cell/K1.html">Textual</a>
        <a class="flow-chip flow-kc" href="cell/K2.html">Relational</a>
        <a class="flow-chip flow-kc" href="cell/K3.html">Structured-entity</a>
        <a class="flow-chip flow-kc" href="cell/K4.html">Perceptual</a>
      </div>
      <span class="flow-arrow">&rarr;</span>
      <div class="flow-stages">
        <a class="flow-stage" href="about.html#construction"><strong>Construction</strong><span>index each substrate in its own form</span></a>
        <a class="flow-stage" href="about.html#retrieval"><strong>Retrieval</strong><span>match the query to the substrate</span></a>
        <a class="flow-stage" href="about.html#generation"><strong>Generation</strong><span>draft an answer from the evidence</span></a>
        <a class="flow-stage flow-v" href="about.html#verification"><strong>Verification</strong><span>test the output beyond the corpus</span></a>
        <a class="flow-stage flow-e" href="about.html#evaluation"><strong>Evaluation</strong><span>score against ground truth</span></a>
        <div class="flow-loop">&#8635;&nbsp;verifier feedback loop</div>
      </div>
      <span class="flow-arrow">&rarr;</span>
      <div class="flow-card flow-o">
        <div class="flow-cap">Operational&nbsp;Objective</div>
        <a class="flow-chip flow-oc" href="cell/O3.html">Discovery</a>
        <a class="flow-chip flow-oc" href="cell/O2.html">Synthesis</a>
        <a class="flow-chip flow-oc" href="cell/O1.html">Grounding</a>
        <div class="flow-axis-note">&uarr; ground truth farther from the corpus</div>
      </div>
    </div>
    <p class="flow-foot">
      Every stage links to its explanation. Capability concentrates on the <strong>Textual</strong> substrate and
      automatically-checkable tasks, and thins toward non-textual, externally-verified discovery.
    </p>
  </div>
</section>
'''


def _growth_chart_html():
    """Cumulative stacked-area growth of the catalog by year, stacked by resource type.
    Returns (svg_string, legend_html). Everything <2018 is bucketed as '<=2017'."""
    from collections import defaultdict, Counter
    TYPES = [('Method', 'Methods', '#c2185b'),
             ('benchmark', 'Benchmarks', '#1a73e8'),
             ('dataset', 'Datasets', '#12805c')]
    yc = defaultdict(Counter)
    for p in papers:
        y = p.get('year')
        if not str(y).isdigit():
            continue
        yb = 2017 if int(y) < 2018 else int(y)
        yc[yb][p.get('type', 'unknown')] += 1
    years = sorted(yc)
    n = len(years)
    running = Counter()
    upper = {k[0]: [] for k in TYPES}   # cumulative stacked upper boundary per layer
    for y in years:
        for key, _, _ in TYPES:
            running[key] += yc[y].get(key, 0)
        acc = 0
        for key, _, _ in TYPES:
            acc += running[key]
            upper[key].append(acc)
    total_max = upper[TYPES[-1][0]][-1] if n else 1
    W, H = 720, 300
    ml, mr, mt, mb = 46, 14, 16, 30
    pw, ph = W - ml - mr, H - mt - mb

    def X(i):
        return ml + (pw * (i / (n - 1)) if n > 1 else 0)

    def Y(v):
        return mt + ph * (1 - v / total_max)

    s = []
    tick = 100
    t = 0
    while t <= total_max:
        yy = Y(t)
        s.append(f'<line x1="{ml}" y1="{yy:.1f}" x2="{W-mr}" y2="{yy:.1f}" stroke="var(--line)" stroke-width="1"/>')
        s.append(f'<text x="{ml-6}" y="{yy+3:.1f}" text-anchor="end" font-size="10" fill="var(--fg-faint)">{t}</text>')
        t += tick
    lower = [0.0] * n
    for key, label, color in TYPES:
        up = upper[key]
        top = ' '.join(f'{X(i):.1f},{Y(v):.1f}' for i, v in enumerate(up))
        bot = ' '.join(f'{X(i):.1f},{Y(lower[i]):.1f}' for i in range(n - 1, -1, -1))
        s.append(f'<polygon points="{top} {bot}" fill="{color}" fill-opacity="0.85"><title>{label}</title></polygon>')
        lower = up
    topline = ' '.join(f'{X(i):.1f},{Y(upper[TYPES[-1][0]][i]):.1f}' for i in range(n))
    s.append(f'<polyline points="{topline}" fill="none" stroke="var(--fg)" stroke-width="1.5"/>')
    for i, y in enumerate(years):
        lbl = '≤2017' if y == 2017 else str(y)
        s.append(f'<text x="{X(i):.1f}" y="{H-8}" text-anchor="middle" font-size="10" fill="var(--fg-muted)">{lbl}</text>')
    s.append(f'<circle cx="{X(n-1):.1f}" cy="{Y(total_max):.1f}" r="3" fill="var(--fg)"/>')
    s.append(f'<text x="{X(n-1)-6:.1f}" y="{Y(total_max)-7:.1f}" text-anchor="end" font-size="13" font-weight="700" fill="var(--fg)">{int(total_max)} total</text>')
    svg = (f'<svg viewBox="0 0 {W} {H}" width="100%" preserveAspectRatio="xMidYMid meet" role="img" '
           f'aria-label="Cumulative growth of scientific RAG systems by year, stacked by resource type">{"".join(s)}</svg>')
    legend = ''.join(f'<span class="lg-chip" style="background:{c};color:#fff">{lbl}</span>' for _, lbl, c in TYPES)
    return svg, legend


# ---------- index.html ----------
def render_index():
    parts = [page_head('Home', base='', current='home')]
    parts.append(f'''
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">AI for Science and Retrieval-Augmented Generation</p>
    <h1>The catalog of scientific RAG, organized by what it retrieves and what it must produce.</h1>
    <p class="lede">
      <strong>{len(papers)}</strong> methods, benchmarks, and datasets across
      <strong>{len(by_dom)}</strong> scientific domains, mapped onto the survey's two axes:
      the <em>retrieval substrate</em> a system draws on (Textual, Relational, Structured-entity, Perceptual)
      and the <em>operational objective</em> it serves, rising from grounding a known answer to proposing a discovery.
      Companion catalog to the survey by Oh et al.
    </p>
    <div class="hero-search">
      <input id="q" type="search" placeholder="Search by title, method, dataset, venue, or tag…" autofocus>
      <span class="hero-search-hint">↵ to filter on <a href="browse.html">Browse</a></span>
    </div>
    <div class="hero-cta">
      <a href="#overview" class="btn">See how it works</a>
      <a href="browse.html" class="btn btn-secondary">Browse all {len(papers)}</a>
      <a href="about.html" class="btn btn-ghost">Read about the taxonomy</a>
    </div>
  </div>
</section>
''')

    # --- Centerpiece: the paper's pipeline overview (Fig. 1) ---
    parts.append(PIPELINE_HTML)

    # --- Cumulative growth chart (stacked area by resource type) ---
    _gsvg, _gleg = _growth_chart_html()
    parts.append(f'''
<section class="growth-section">
  <div class="wrap">
    <h2 class="section-title">A field growing fast</h2>
    <p class="section-sub">
      Cumulative count of catalogued methods, benchmarks, and datasets by year. Scientific RAG
      accelerates sharply from 2023 onward, led by <strong style="color:#c2185b">methods</strong>, with
      <strong style="color:#1a73e8">benchmarks</strong> following.
    </p>
    <div class="chart-frame">{_gsvg}</div>
    <p class="chart-legend">{_gleg}</p>
    <p class="chart-note">The chart plots entries with a recorded publication year; a handful of undated entries are not shown. See <a href="browse.html">Browse</a> for the full catalog of {len(papers)}.</p>
  </div>
</section>
''')

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

    # What's next, the survey's core message + a pointer to future directions
    parts.append('''
<section class="whatsnext-section">
  <div class="wrap">
    <h2 class="section-title">What's next</h2>
    <p class="section-sub">
      Across the grid, one message stands out. Capability piles up where the substrate is textual and the task
      can be scored automatically, and it thins toward non-textual evidence and externally verified discovery,
      the very abilities an autonomous scientific agent leans on most. The work ahead is less a search for better
      retrievers than making more of science <strong>retrievable</strong> and more of its outputs
      <strong>verifiable</strong>.
    </p>
    <div class="whatsnext-cta">
      <a href="insights.html#directions" class="btn">The road ahead</a>
      <a href="insights.html" class="btn btn-secondary">Read the Insights</a>
    </div>
  </div>
</section>
''')

    # Contributing + Cite (moved here from Getting Started)
    parts.append('''
<section class="contribute-section">
  <div class="wrap">
    <div class="contribute-grid">
      <div class="contribute-card">
        <h2 class="section-title">Contributing</h2>
        <p>
          Missing entries, mis-classifications, or new systems? Open an issue or a pull request on the
          <a href="https://github.com/yerimoh/ScienceRAGSurvey" target="_blank" rel="noopener">GitHub repository</a>.
          The build is fully deterministic, so editing the data files and re-running the render script rebuilds
          every page.
        </p>
      </div>
      <div class="contribute-card">
        <h2 class="section-title">Cite</h2>
        <pre><code>@article{oh2026sciragsurvey,
  title   = {Scientific Retrieval-Augmented Generation: A Survey
             a Survey and Taxonomy},
  author  = {Oh, Yerim and others},
  journal = {TBD},
  year    = {TBD}
}</code></pre>
      </div>
    </div>
  </div>
</section>
''')

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
    body = f'''
<section class="prose">
  <div class="wrap">
    <h1>About Scientific RAG Hub</h1>
    <p class="lede">
      A curated catalog of <strong>{len(papers)} retrieval-augmented generation</strong> systems,
      benchmarks, and datasets across the sciences, the companion resource to the upcoming survey
      <em>"Scientific Retrieval-Augmented Generation: A Survey and Taxonomy."</em>
    </p>

    <figure class="gs-figure">
      <img src="static/science-rag-overview.png" alt="The knowledge sources of scientific RAG arranged as a wheel around a central hub, spanning nine scientific domains" loading="lazy">
      <figcaption>The knowledge sources of scientific RAG, spanning literature, curated databases, structured entities, and raw instrument data across nine domains.</figcaption>
    </figure>

    <h2>The taxonomy: substrate × objective</h2>
    <p>
      Scientific RAG is not general-purpose RAG applied to technical text. It is a constraint-bound system
      answerable to physical laws, stoichiometric exactness, and experimental protocols rather than to the
      approximate semantic proximity on which general RAG depends. Within an embedding space, <em>pH&nbsp;7.2</em>
      and <em>pH&nbsp;7.4</em>, or <em>10&nbsp;mg</em> and <em>100&nbsp;mg</em>, sit next to each other, yet in
      physical execution the difference is decisive. Two demands shape such a system: the knowledge it retrieves
      and the task it must answer.
    </p>
    <h3>Knowledge Source (K): the retrieval substrate</h3>
    <p>A source's native form fixes the retrieval operation it permits. General RAG stays almost entirely on the first substrate; scientific RAG must reach the other three, each costlier to index.</p>
    <ul>
      <li><strong>K1 Textual</strong>, the prose record of science: papers, abstracts, clinical notes, guidelines. Matched by embedding or lexical search over passages.</li>
      <li><strong>K2 Relational</strong>, curated graphs of scientific relations (UMLS, PrimeKG, DRKG, STRING, KEGG, citation graphs). Knowledge lives in the edges, reached by entity linking and traversal.</li>
      <li><strong>K3 Structured-entity</strong>, the objects of science held as data: molecules, 3D structures, and property records (ChEMBL, PubChem, PDB, Materials Project). Reached by structural or property query, not by words.</li>
      <li><strong>K4 Perceptual</strong>, raw instrument output: images, spectra, sequencing, time-series (MIMIC-CXR, MassBank, sky surveys). Nothing is retrievable until a cross-modal encoder connects the signal to a text query.</li>
    </ul>
    <h3>Operational Objective (O): the rung, ordered by distance from the corpus</h3>
    <ul>
      <li><strong>O1 Grounding</strong>, answer a question whose gold already lies in the corpus (Question Answering).</li>
      <li><strong>O2 Synthesis</strong>, integrate evidence no single source states, verifying claims across documents (Claim Verification, Literature Synthesis).</li>
      <li><strong>O3 Discovery</strong>, propose an output the corpus does not contain, judged by an external verifier (Property Prediction, Molecular Design, Materials Discovery, Hypothesis Generation).</li>
    </ul>

    <h2>Why this taxonomy</h2>
    <p>
      Existing RAG surveys classify systems by retriever–generator pipeline or by application domain. That view
      misses the two factors that most constrain scientific inquiry: the fidelity of the grounded evidence and the
      complexity of the scientific objective. Organized by substrate and objective, the field reveals a consistent
      shape. Capability accumulates where a substrate admits a mature matching operation and a task admits an
      automatic score, literature grounding and synthesis over <strong>Textual</strong>, lookup over
      <strong>Relational</strong> and <strong>Structured-entity</strong>, and thins toward non-textual evidence and
      externally verified discovery, where the retriever or the verifier does not yet exist.
    </p>

    <h2 id="pipeline">The scientific RAG pipeline</h2>
    <p>
      Connecting substrate to objective is the method: the pipeline a system runs, specialized to science at
      every stage. A query is turned into a trusted output through five stages, and a verifier can loop the
      output back for another round.
    </p>
    <ul>
      <li id="construction"><strong>Construction</strong>, build the index. Each substrate is indexed in its own form: passages as embeddings, graphs as nodes and edges, molecules as structural fingerprints, signals through a learned encoder.</li>
      <li id="retrieval"><strong>Retrieval</strong>, match the query to the substrate. Relevance is a domain judgment, not topical resemblance: the right passage, the right scaffold, the record whose peaks match.</li>
      <li id="generation"><strong>Generation</strong>, draft an output from the query, the retrieved evidence, and any verifier feedback, in the formats a domain requires.</li>
      <li id="verification"><strong>Verification</strong>, test the output against a signal from beyond the corpus. Systems differ by how deeply the verifier is coupled, from a single unchecked pass to a closed loop that refines against a docking score or a DFT calculation every round.</li>
      <li id="evaluation"><strong>Evaluation</strong>, score the result against ground truth: a fixed gold for grounding, a reference for synthesis, and for discovery an external verifier whose ground truth lies outside any corpus.</li>
    </ul>

    <h2>What makes retrieval scientific</h2>
    <p>Five demands separate a scientific RAG system from general RAG that ranks by semantic proximity alone:</p>
    <ol>
      <li><strong>Traceable attribution</strong>, every claim must trace to a specific source unit, sentence-level, page-level, or as a claim graph.</li>
      <li><strong>Heterogeneous, multi-substrate retrieval</strong>, the corpus spans literature, curated graphs, structured entities, and raw signals, each with its own format and reliability.</li>
      <li><strong>Domain-native representation</strong>, SMILES, InChI, FASTA, CIF, DICOM carry meaning no flattening to text preserves; retrieval must recognize identity across surface forms.</li>
      <li><strong>Protocol-level reproducibility</strong>, an output must carry enough method detail for a domain expert to reproduce it, not merely summarize it.</li>
      <li><strong>External verifier coupling</strong>, for discovery, a docking simulator or DFT calculation, not the language model, decides whether a proposal survives.</li>
    </ol>

    <h2>How to use the catalog</h2>
    <ul>
      <li><a href="browse.html">Browse</a>, filter the full catalog by substrate × objective cell, task, domain, or type.</li>
      <li><a href="index.html#domains">Domains</a>, browse by scientific field.</li>
      <li><a href="browse.html">Browse</a>, full searchable, filterable catalog.</li>
      <li><a href="llms.txt">/llms.txt</a>, <a href="llms-full.txt">/llms-full.txt</a>, LLM-friendly indices.</li>
      <li><a href="data/catalog.json">catalog.json</a>, full machine-readable dump, remapped to the substrate × objective taxonomy (raw source stays at <a href="data/papers.json">papers.json</a>).</li>
    </ul>

    <h2>Survey Construction Pipeline</h2>
    <p>The following diagram shows how the catalog and companion survey were built end-to-end.</p>

    <div class="pipeline-diagram">
      <!-- Row 1: Sources -->
      <div class="pipe-row pipe-row-sources">
        <div class="pipe-node pipe-node-src">
          <div class="pipe-icon">📄</div>
          <div class="pipe-label">Literature<br><span class="pipe-sub">arXiv, PubMed, ACL, NeurIPS…</span></div>
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
          <div class="pipe-label"><strong>Substrate × Objective Classification</strong></div>
          <div class="pipe-classify-grid">
            <div class="pipe-axis pipe-axis-k">
              <div class="pipe-axis-label">K: Retrieval Substrate</div>
              <div class="pipe-axis-items">
                <span class="pipe-pill pipe-k1">K1 Textual</span>
                <span class="pipe-pill pipe-k2">K2 Relational</span>
                <span class="pipe-pill pipe-k3">K3 Structured-entity</span>
                <span class="pipe-pill pipe-k4">K4 Perceptual</span>
              </div>
            </div>
            <div class="pipe-axis-times">×</div>
            <div class="pipe-axis pipe-axis-o">
              <div class="pipe-axis-label">O: Operational Objective</div>
              <div class="pipe-axis-items">
                <span class="pipe-pill pipe-o1">O1 Grounding</span>
                <span class="pipe-pill pipe-o2">O2 Synthesis</span>
                <span class="pipe-pill pipe-o3">O3 Discovery</span>
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
          <div class="pipe-label"><strong>12-Cell Landscape</strong></div>
          <div class="pipe-mini-grid">
            {"".join(
              f'<a href="cell/{K}.{O}.html" class="pipe-cell pipe-cell-{"h" if cell_count(f"{K}.{O}")>=10 else "m" if cell_count(f"{K}.{O}")>=3 else "l"}" title="{K}.{O}: {cell_count(f"{K}.{O}")} entries">'
              f'<span class="pipe-cell-id">{K}.{O}</span>'
              f'<span class="pipe-cell-n">{cell_count(f"{K}.{O}")}</span>'
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
          <div class="pipe-label">This Site<br><span class="pipe-sub">Browse, Filter, Search</span></div>
        </div>
        <div class="pipe-node pipe-node-out">
          <div class="pipe-icon">📖</div>
          <div class="pipe-label">Survey<br><span class="pipe-sub">Oh et al. 2026</span></div>
        </div>
        <div class="pipe-node pipe-node-out">
          <div class="pipe-icon">📄</div>
          <div class="pipe-label">catalog.json<br><span class="pipe-sub">machine-readable</span></div>
        </div>
      </div>
    </div>

    <h2>Methodology</h2>
    <p>
      Entries are curated by the Vision and Learning Lab and cross-referenced against the survey's master
      bibliography. Each system is placed by its <em>retrieval substrate</em>, the native form of what it
      indexes, and by its <em>objective rung</em>. The survey's core systems are pinned to the exact cell they
      occupy in the assembly figure; the wider catalog is mapped by the modality it retrieves over. A system that
      commits to a single substrate occupies a single cell, which is the common case: almost every surveyed system
      retrieves from just one substrate, and cross-substrate retrieval is itself an open frontier (§8).
    </p>
  </div>
</section>
'''
    (ROOT / 'about.html').write_text(page_head('About', current='about') + body + PAGE_FOOT)


# ---------- browse.html (client-side filter) ----------
def render_browse():
    domain_opts = '\n'.join(f'<option value="{d}">{esc(DOMAIN_LABELS[d])} ({len(by_dom[d])})</option>' for d in DOMAIN_LABELS if d in by_dom)
    type_opts = '\n'.join(f'<option value="{t}">{esc(TYPE_LABELS[t])} ({len(by_type[t])})</option>' for t in TYPE_LABELS if t in by_type)
    cell_opts = '\n'.join(f'<option value="{K}.{O}">[{K}.{O}] {esc(K_LABELS[K][0])} × {esc(O_LABELS[O][0])} ({cell_count(K+"."+O)})</option>' for K in ['K1','K2','K3','K4'] for O in ['O1','O2','O3'])
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
    <p class="lede">Filter by substrate × objective cell, task, domain, type, or year.</p>
    <div class="filters">
      <input id="q" type="search" placeholder="Search…" autofocus>
      <select id="f-cell"><option value="">All cells</option>{cell_opts}</select>
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
    <p id="empty" class="empty" hidden>No matching entries, try a broader search.</p>
  </div>
</section>

<script src="static/search.js?v={int((ROOT / 'static/search.js').stat().st_mtime)}"></script>
'''
    (ROOT / 'browse.html').write_text(page_head('Browse', base='', current='browse') + body + PAGE_FOOT)


# ---------- cell/<K>.<O>.html ----------
SECTION_OVERVIEWS = {
    # cell_key: { 'subsection': <section title, matches CELL_TIERS>, 'description': <brief 1-2 sentence summary> }
    # The cell hero already prints the K-axis and O-axis definitions; this description
    # adds only what is specific to the intersection. Cards below are grouped automatically.
    'K1.O1': {
        'subsection': 'Literature Grounding',
        'description': 'Answers a question directly over the textual record of science, PubMed, arXiv, full-text papers, by retrieving passages, citing them, and grounding the answer in the corpus that already holds it. The most mature capability in the field: mature retrievers meet automatic scoring, so open generation and light self-checking suffice.',
    },
    'K1.O2': {
        'subsection': 'Literature Synthesis',
        'description': 'Integrates evidence that no single paper states into one cited answer, resolving contradictions across many textual sources. The difficulty shifts from citing one source to verifying every claim against a set of them, so faithfulness and coverage, not exact match, become the score.',
    },
    'K1.O3': {
        'subsection': 'Literature-grounded Ideation',
        'description': 'Uses the literature as a generative prior to propose research ideas, mechanisms, and hypotheses. The dormant rung of the textual substrate: no docking program, simulator, or database can confirm a proposed idea, so systems are judged only by novelty or expert preference, signals that language-model judges themselves overrate.',
    },
    'K2.O1': {
        'subsection': 'Knowledge-graph QA',
        'description': 'Answers by linking a query to entities in a curated relational graph, UMLS, PrimeKG, DRKG, biomedical ontologies, and traversing its typed edges, so the answer lives in the couplings between nodes rather than in any single passage.',
    },
    'K2.O2': {
        'subsection': 'Knowledge-graph Synthesis',
        'description': 'Combines several curated relational sources into one verified answer by walking multi-hop paths across entities and relations (for example drug–gene–disease links). Emerging: retrieval is mature but multi-source graph synthesis under a reliability check is still being built.',
    },
    'K2.O3': {
        'subsection': 'Relational Hypothesis',
        'description': 'Proposes new links or candidates over a relational graph, for example ranking protein–protein interaction pathways for a therapeutic target. Emerging: the graph supplies structure, but the verifier that would confirm a proposed relation beyond the graph is rarely available.',
    },
    'K3.O1': {
        'subsection': 'Structured-entity Lookup',
        'description': 'Grounds an answer in the objects of science held as data, molecules, 3D structures, and property records (ChEMBL, PubChem, PDB, Materials Project), reached by structural or property query and returned as an exact, up-to-date value from an authoritative field.',
    },
    'K3.O2': {
        'subsection': 'Structured Synthesis (open)',
        'description': 'Integrates and cross-checks several structured-entity databases into one answer. A near-empty frontier: few systems yet reconcile heterogeneous structure and property records under a single verified synthesis.',
    },
    'K3.O3': {
        'subsection': 'Structure-based Design',
        'description': 'Retrieves exemplar molecules, fragments, or crystal structures to steer a generative model toward novel candidates, then confirms each with a strong external verifier outside the corpus, molecular docking for ligands, DFT or an ML interatomic potential for materials. The clearest case of a verifier coupled into the loop; the gap to wet-lab confirmation remains the open challenge.',
    },
    'K4.O1': {
        'subsection': 'Cross-modal Grounding',
        'description': 'Grounds an answer in a raw instrument signal, chest X-rays, pathology slides, ECG traces, where retrieval must bridge a non-textual modality to a textual question through a learned cross-modal encoder. Emerging: the encoder that connects signal to text is the component that still lags.',
    },
    'K4.O2': {
        'subsection': 'Perceptual Synthesis (open)',
        'description': 'Integrates and reconciles several observational or experimental modalities into one verified answer. Dormant: raw-signal archives are almost never indexed as a retrieval corpus, so there is no substrate over which to synthesize.',
    },
    'K4.O3': {
        'subsection': 'Signal-to-structure Discovery',
        'description': 'Proposes a scientific object directly from a raw signal, a molecule from an MS/MS spectrum, a diagnosis-hypothesis from an image. One of the sparsest cells: MADGEN retrieves a scaffold keyed on the spectrum and then generates the full structure, but almost all spectrum-to-structure models generate with no retrieval at all. A concrete frontier for scientific RAG.',
    },
}


def render_overview_section(cell_key, papers_by_key, papers_in_cell=None, base='../'):
    """Render a short section description + sub-subsection-grouped paper cards.

    papers_in_cell: list of papers in this cell (for grouping by subsection).
                    If None, falls back to legacy citation-list-based rendering.
    """
    o = SECTION_OVERVIEWS.get(cell_key)
    if not o:
        return ''
    description = o.get('description', '')
    # Legacy paragraph path (only used if no description provided)
    text = o.get('paragraph', '') if not description else ''
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

    # Build hidden footnote items (popover targets) AND visible card grid
    fn_items = []
    card_html = []
    # Infer axis_scope from cell_key (K1.O1 → 'O1', K3 → 'K3', O3 → 'O3')
    axis_scope = cell_key.split('.')[1] if '.' in cell_key else cell_key
    for i, key in enumerate(cite_order, 1):
        p = papers_by_key.get(key, {})
        title = p.get('title', key)
        method = p.get('method', '')
        safe_key = key.replace(':', '_').replace('/', '_')
        ev = evidence_map.get(key, '')
        label = method or title or key
        body = f'<p><strong>{esc(label)}</strong>'
        if title and title != label:
            body += f' &mdash; <em>{esc(title)}</em>'
        body += '</p>'
        if ev:
            body += f'<p>{esc(ev)}</p>'
        summary_path = ROOT / 'papers' / f'{safe_key}.html'
        if summary_path.exists():
            body += f'<p><a href="{base}papers/{safe_key}.html">Full summary &rarr;</a></p>'
        elif p.get('paper_link'):
            body += f'<p><a href="{esc(p["paper_link"])}" target="_blank" rel="noopener">Source &uarr;</a></p>'
        fn_items.append(f'<li id="fn-ov{i}">{body}</li>')
        if p:
            card_html.append(paper_card(p, base=base, axis_scope=axis_scope))

    # If a short `description` is set, build sub-subsection grouped card view (preferred).
    if description:
        from collections import OrderedDict
        groups = OrderedDict()  # subsection name → list of cards
        allowed_subs = axis_subsections(axis_scope, cell_key=cell_key) or set()
        no_sub_cards = []
        for p in (papers_in_cell or []):
            subs = p.get('subsection') or ''
            sub_list = subs if isinstance(subs, list) else [subs]
            sub_list = [s for s in sub_list if s and (not allowed_subs or s in allowed_subs)]
            card_h = paper_card(p, base=base, axis_scope=axis_scope)
            if sub_list:
                # Place card under each matching sub-subsection
                for s in sub_list:
                    groups.setdefault(s, []).append(card_h)
            else:
                no_sub_cards.append(card_h)
        # Sort groups by member count descending so the most populated appears first
        sorted_groups = sorted(groups.items(), key=lambda kv: -len(kv[1]))
        group_html_parts = []
        for sub_name, cards in sorted_groups:
            n = len(cards)
            group_html_parts.append(
                f'<div class="ov-group">'
                f'  <h3 class="ov-group-title">{esc(sub_name)} <span class="ov-group-count">{n}</span></h3>'
                f'  <div class="card-grid">{"".join(cards)}</div>'
                f'</div>'
            )
        if no_sub_cards:
            group_html_parts.append(
                f'<div class="ov-group">'
                f'  <h3 class="ov-group-title ov-group-other">Other <span class="ov-group-count">{len(no_sub_cards)}</span></h3>'
                f'  <div class="card-grid">{"".join(no_sub_cards)}</div>'
                f'</div>'
            )
        groups_html = '\n'.join(group_html_parts) or ''
        return f'''
<section class="cell-overview">
  <div class="wrap">
    <h2 class="ov-title">Section overview &mdash; § {esc(o['subsection'])}</h2>
    <div class="ov-paragraph">
      <p>{esc(description)}</p>
    </div>
    {groups_html}
  </div>
</section>'''

    # ----- Legacy paragraph + footnote-popover path (unused once all overviews have descriptions) -----
    # Hidden popover-target list (visually hidden but in DOM for footnotes.js)
    fn_html = ('<section class="footnotes overview-fns" aria-hidden="true">'
               '<ol>' + ''.join(fn_items) + '</ol></section>')

    cards_block = ('<div class="card-grid ov-cards">' + '\n'.join(card_html) + '</div>') if card_html else ''

    return f'''
<section class="cell-overview">
  <div class="wrap">
    <h2 class="ov-title">Section overview &mdash; § {esc(o['subsection'])}</h2>
    <p class="ov-sub">Click any superscript chip in the paragraph to see verbatim evidence; the cited papers are listed below.</p>
    <div class="ov-paragraph">
      <p>{html_text}</p>
    </div>
    {cards_block}
    {fn_html}
  </div>
</section>'''


def render_cell_pages():
    for K in ['K1', 'K2', 'K3', 'K4']:
        for O in ['O1', 'O2', 'O3']:
            cell = f'{K}.{O}'
            if cell in CELL_PAPERS:
                # Restrict to papers actually cited in this cell's main.tex subsubsection,
                # preserving main.tex citation order. Keys not in papers.json are skipped.
                ps = [papers_by_key[k] for k in CELL_PAPERS[cell] if k in papers_by_key]
            else:
                ps = sorted(by_cell.get(cell, []), key=year_sort)
            kn, kd = K_LABELS[K]
            on, od = O_LABELS[O]

            other_cells_nav = '\n'.join(
                f'<a href="{c}.html" class="pill {"current" if c == cell else ""}" title="{c}">{cell_label(c)}</a>'
                for c in [f'{kk}.{oo}' for kk in ['K1','K2','K3','K4'] for oo in ['O1','O2','O3']]
            )

            # Build cards, attaching a fact-check footnote to any paper with FACTCHECK data.
            cell_safe = cell.replace('.', '').lower()
            card_list, fn_items = [], []
            for i, p in enumerate(ps, 1):
                bk = p.get('bib_key', '')
                fc_id = None
                if cell in FACTCHECKED_CELLS and bk in FACTCHECK:
                    fc_id = f'fn-{cell_safe}-{i}'
                    fc = FACTCHECK[bk]
                    label = esc(p.get('method') or p.get('title') or bk)
                    fn_items.append(
                        f'<li id="{fc_id}"><p><strong>{label}, {esc(fc["verdict"])}</strong></p>'
                        f'<p>{esc(fc["evidence"])}</p>'
                        f'<p class="fn-src">Source: {esc(fc["source"])}, full-text verified</p></li>'
                    )
                card_list.append(paper_card(p, base='../', axis_scope=O, factcheck_id=fc_id))
            cards = '\n'.join(card_list) or '<p class="empty">No verified entries in this cell yet, see <a href="../about.html#methodology">methodology</a> and the survey §11 frontier discussion.</p>'
            # Hidden footnote targets (popover source for footnotes.js)
            factcheck_fns = (f'<section class="footnotes overview-fns" aria-hidden="true"><ol>{"".join(fn_items)}</ol></section>'
                             if fn_items else '')
            sf = subsec_filter_html(ps, prefix=f'cell{cell}', axis_scope=O, cell_key=cell)
            sys_table = systems_table_html(CELL_PAPERS.get(cell, []), base='../',
                                           caption=f'Pipeline at a glance — [{cell}] systems, decomposed by stage (survey Table 3).')

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
    <p class="eyebrow"><a href="../browse.html">← Browse all</a></p>
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

<section class="cell-list">
  <div class="wrap">
    {sys_table}
    {sf}
    <div class="card-grid">{cards}</div>
  </div>
</section>
{factcheck_fns}
'''
            (ROOT / 'cell' / f'{cell}.html').write_text(page_head(f'[{cell}] {kn} × {on}', base='../', current=f'cell/{cell}') + body + page_foot('../'))

    # ---------- K-axis roll-up pages (cell/K1.html etc.) ----------
    for K in ['K1', 'K2', 'K3', 'K4']:
        kn, kd = K_LABELS[K]
        resources = substrate_resources_html(K, base='../')
        ks_table = knowledge_source_table_html(substrate=K, base='../',
                                               caption='Scale and access at a glance (survey Table 1).')
        # systems live on the K×O cell pages, linked as pills rather than dumped as cards
        cell_pills = '\n'.join(
            f'<a href="{K}.{O}.html" class="pill" title="{K}.{O}">{cell_label(K+"."+O)} <span class="pill-n">{cell_count(K+"."+O)}</span></a>'
            for O in ['O1', 'O2', 'O3'])
        body = f'''
<section class="cell-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="knowledge-source.html">← Knowledge Source</a></p>
    <h1><span class="cell-id-big axis-id-k">{K}</span> {esc(kn)}</h1>
  </div>
</section>

<section class="axis-body">
  <div class="wrap">
    {resources}
    {ks_table}
    <div class="axis-systems-link">
      <span class="axis-systems-label">Systems retrieving over this substrate, by objective:</span>
      <div class="cell-nav">{cell_pills}</div>
    </div>
  </div>
</section>
'''
        (ROOT / 'cell' / f'{K}.html').write_text(page_head(f'[{K}] {kn}', base='../', current=f'cell/{K}') + body + page_foot('../'))

    # ---------- O-axis roll-up pages (cell/O1.html etc.) ----------
    for O in ['O1', 'O2', 'O3']:
        on, od = O_LABELS[O]
        tasks_html = objective_tasks_html(O, base='../')
        # systems live on the K×O cell pages, linked as pills rather than dumped as cards
        cell_pills = '\n'.join(
            f'<a href="{K}.{O}.html" class="pill" title="{K}.{O}">{cell_label(K+"."+O)} <span class="pill-n">{cell_count(K+"."+O)}</span></a>'
            for K in ['K1', 'K2', 'K3', 'K4'] if cell_count(f'{K}.{O}')
        )
        body = f'''
<section class="cell-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="operational-objective.html">← Operational Objective</a></p>
    <h1><span class="cell-id-big axis-id-o">{O}</span> {esc(on)}</h1>
    <p class="axis-lede">{esc(od)}</p>
  </div>
</section>

<section class="axis-body o-body">
  <div class="wrap">
    {tasks_html}
    <div class="axis-systems-link">
      <span class="axis-systems-label">Systems reaching this objective, by substrate:</span>
      <div class="cell-nav">{cell_pills}</div>
    </div>
  </div>
</section>
'''
        (ROOT / 'cell' / f'{O}.html').write_text(page_head(f'[{O}] {on}', base='../', current=f'cell/{O}') + body + page_foot('../'))


# ---------- Axis overview pages (cell/knowledge-source.html, cell/operational-objective.html) ----------
# Clicking an axis header in the sidebar lands here: the axis explained as a whole, its own
# reference table (K = data resources, O = task benchmarks), then one subsection per member.
K_OVERVIEW_INTRO = (
    'A <strong>knowledge source</strong> is the data a scientific RAG system retrieves over. '
    'The form in which a source stores its knowledge, its <em>retrieval substrate</em>, fixes what '
    'can be reached from it: text can be reached by text, but a molecule, a graph of typed relations, '
    'or a raw instrument signal shares no words with a query. We organize knowledge sources by that '
    'native form into four substrates. General-domain RAG stays almost entirely on the textual '
    'substrate; scientific RAG must reach the other three, each costlier to index.'
)
O_OVERVIEW_INTRO = (
    'An <strong>operational objective</strong> is the task a system must serve, each operationalized '
    'by a benchmark that fixes the query, corpus, and ground truth. What the task demands sets how far '
    'its ground truth sits from the corpus: some answers lie ready in the corpus as a stored label, '
    'others are proposals it does not contain that only an external verifier can judge. The seven task '
    'families rise across three rungs, from grounding through synthesis to discovery.'
)


def render_axis_overview():
    # ----- Knowledge Source (K axis), §4 of the survey -----
    k_summary = AXIS_PROSE.get('K', {}).get('summary', '') or AXIS_PROSE.get('K', {}).get('intro', '')
    k_intro = f'<p>{esc(k_summary)}</p>' if k_summary else f'<p>{K_OVERVIEW_INTRO}</p>'
    subs = []
    for K in ['K1', 'K2', 'K3', 'K4']:
        kn = K_LABELS[K][0]
        n = axis_count(K)
        subs.append(f'''
<section class="axis-sub" id="{K.lower()}">
  <div class="wrap">
    <div class="axis-sub-head">
      <span class="sys-k sys-k-{K.lower()}">{esc(K_SHORT.get(K, K))}</span>
      <h2>{esc(kn)}</h2>
      <a class="axis-sub-link" href="{K}.html">details &amp; {n} systems →</a>
    </div>
    {substrate_resources_html(K, base='../')}
  </div>
</section>''')
    nav = '\n'.join(
        f'<a href="#{K.lower()}" class="pill">{esc(K_SHORT.get(K, K))} · {esc(K_LABELS[K][0])} <span class="pill-n">{axis_count(K)}</span></a>'
        for K in ['K1', 'K2', 'K3', 'K4'])
    body = f'''
<section class="cell-hero axis-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../browse.html">← Browse all</a></p>
    <h1><span class="cell-id-big axis-id-k">K</span> Knowledge Source</h1>
    <div class="axis-intro">{k_intro}</div>
    <div class="cell-nav">{nav}</div>
  </div>
</section>
{''.join(subs)}
'''
    (ROOT / 'cell' / 'knowledge-source.html').write_text(
        page_head('Knowledge Source', base='../', current='cell/knowledge-source') + body + page_foot('../'))

    # ----- Operational Objective (O axis), §5 of the survey -----
    o_summary = AXIS_PROSE.get('O', {}).get('summary', '') or AXIS_PROSE.get('O', {}).get('intro', '')
    o_intro = f'<p>{esc(o_summary)}</p>' if o_summary else f'<p>{O_OVERVIEW_INTRO}</p>'
    RUNGS = ['O1', 'O2', 'O3']
    osubs = []
    for O in RUNGS:
        on, od = O_LABELS[O]
        n = axis_count(O)
        osubs.append(f'''
<section class="axis-sub o-body" id="{O.lower()}">
  <div class="wrap">
    <div class="axis-sub-head">
      <span class="sys-o sys-o-{O.lower()}">{esc(O)}</span>
      <h2>{esc(on)}</h2>
      <a class="axis-sub-link" href="{O}.html">details &amp; {n} systems →</a>
    </div>
    <p class="axis-lede">{esc(od)}</p>
    {objective_tasks_html(O, base='../')}
  </div>
</section>''')
    onav = '\n'.join(
        f'<a href="#{O.lower()}" class="pill">{esc(O)} · {esc(O_LABELS[O][0])} <span class="pill-n">{axis_count(O)}</span></a>'
        for O in RUNGS)
    obody = f'''
<section class="cell-hero axis-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../browse.html">← Browse all</a></p>
    <h1><span class="cell-id-big axis-id-o">O</span> Operational Objective</h1>
    <div class="axis-intro">{o_intro}</div>
    <div class="cell-nav">{onav}</div>
  </div>
</section>
{''.join(osubs)}
'''
    (ROOT / 'cell' / 'operational-objective.html').write_text(
        page_head('Operational Objective', base='../', current='cell/operational-objective') + obody + page_foot('../'))


# ---------- Per-task pages (cell/question-answering.html etc.) ----------
# One page per §5 task family, structured like a K substrate page: the task explained,
# its benchmarks as chips + a description table, and a link to the systems that reach it.
def render_task_pages():
    for t in TASK_ORDER:
        slug = task_slug(t)
        O = TASK_RUNG.get(t, '')
        on = O_LABELS.get(O, ('',))[0]
        tp = O_PROSE.get(t, {})
        n_sys = task_system_count(t)
        chips = benchmark_chips_html(tasks=[t], base='../')
        table = benchmark_table_html(tasks=[t], base='../', show_group=False,
                                     caption='Benchmarks and their ground truth (survey Table 2).')
        # sibling tasks under the same rung, for lateral nav
        sib = [x for x in TASK_ORDER if TASK_RUNG.get(x) == O]
        sib_nav = '\n'.join(
            f'<a href="{task_slug(x)}.html" class="pill {"current" if x == t else ""}">{esc(x)}</a>'
            for x in sib)
        body = f'''
<section class="cell-hero o-body">
  <div class="wrap">
    <p class="eyebrow"><a href="operational-objective.html">← Operational Objective</a> <span class="crumb-sep">/</span> <a href="{O}.html">{esc(on)}</a></p>
    <h1><span class="cell-id-big axis-id-o">{O}</span> {esc(t)}</h1>
    <div class="axis-prose">{prose_html(tp.get("text", ""))}</div>
    <div class="cell-nav">{sib_nav}</div>
  </div>
</section>

<section class="axis-body o-body">
  <div class="wrap">
    <div class="res-group">
      <h2 class="res-group-title">Benchmarks</h2>
      {chips}
      {table}
    </div>
    <div class="axis-systems-link">
      <a class="axis-systems-cta" href="../browse.html?sub={_q(t)}">Browse the {n_sys} systems evaluated on {esc(t)} →</a>
    </div>
  </div>
</section>
'''
        (ROOT / 'cell' / f'{slug}.html').write_text(
            page_head(esc(t), base='../', current=f'cell/{slug}') + body + page_foot('../'))


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
    {f'<div class="cell-breakdown"><span class="muted">Substrate × Objective:</span> {breakdown}</div>' if breakdown else ''}
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
    K_COLOR_LABELS = {'K1': 'Textual', 'K2': 'Relational', 'K3': 'Structured-entity', 'K4': 'Perceptual', '?': 'Unassigned'}
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
            bars.append(f'<rect x="{x}" y="{cy}" width="{bar_w}" height="{h:.1f}" fill="{K_COLORS[K]}" opacity="0.92"><title>{y}, {K}: {c}</title></rect>')
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
        cell = p.get('ko_primary') if (p.get('ko_primary') and '.' in p.get('ko_primary')) else f['cell']
        fl_cards.append(f'''
        <article class="fl-card">
          <div class="fl-head">
            <h3 class="fl-name">{esc(f['name'])}</h3>
            <a href="cell/{cell}.html" class="tag tag-cell" title="{esc(cell_label(cell))}">{cell}</a>
          </div>
          <p class="fl-tagline">{esc(f['tagline'])}</p>
          <div class="fl-stats">{stats_html}</div>
          <p class="fl-subtitle">{esc(f['subtitle'])}</p>
          <p class="fl-why"><strong>Why it matters.</strong> {esc(f['why'])}</p>
          <p class="fl-cite">{title_link}, <span class="muted">{esc(f['venue'])}</span></p>
        </article>''')

    # Cross-substrate papers, systems whose retrieved evidence spans more than one substrate
    # (by modality), the §8 cross-substrate-retrieval frontier. The survey's marquee bridges
    # (MedGraphRAG, Omni-RAG, LLaMP) are pinned first.
    def _n_substrates(p):
        return len({MODALITY_SUBSTRATE[mo] for mo in (p.get('modality') or []) if mo in MODALITY_SUBSTRATE})
    _pinned = ['DBLP:conf/acl/WuZQCXMJG25', 'DBLP:conf/acl/ChenLJWG0025', 'DBLP:conf/emnlp/ChiangHCR25']
    xs_papers = [papers_by_key[k] for k in _pinned if k in papers_by_key]
    _seen = {p.get('bib_key') for p in xs_papers}
    xs_papers += [p for p in papers if _n_substrates(p) > 1 and p.get('bib_key') not in _seen]
    xs_cards = '\n'.join(paper_card(p) for p in xs_papers[:12])

    # Frontier cells, the survey's white space (§8): dormant literature-grounded ideation and
    # the near-empty signal-to-structure discovery cell.
    frontier_K3O3 = by_cell.get('K1.O3', [])   # Textual × Discovery, ideation, weak verifier
    frontier_K4O3 = by_cell.get('K4.O3', [])   # Perceptual × Discovery, signal-to-structure
    f33 = '\n'.join(paper_card(p) for p in frontier_K3O3) or '<p class="empty">No verified entries, this cell is a structural gap.</p>'
    f43 = '\n'.join(paper_card(p) for p in frontier_K4O3) or '<p class="empty">No verified entries, this cell is a structural gap.</p>'

    body = f'''
<section class="insights-hero">
  <div class="wrap">
    <p class="eyebrow">The shape of scientific RAG</p>
    <h1>What the {len(papers)}-paper catalog reveals.</h1>
    <p class="lede">
      Six lenses on the field, the systems that set the bar, the five demands that make retrieval
      <em>scientific</em>, how the substrates have grown, where each one lives across domains,
      where the white space is, and the challenges the survey lays out as the road ahead.
    </p>
    <nav class="insights-toc">
      <a href="#flagships">Flagships</a>
      <a href="#requirements">5 Demands</a>
      <a href="#growth">Growth</a>
      <a href="#kd">Substrate×Domain</a>
      <a href="#bridges">Cross-substrate</a>
      <a href="#frontiers">Frontiers</a>
      <a href="#directions">Challenges</a>
    </nav>
  </div>
</section>

<section id="flagships" class="prose-section">
  <div class="wrap">
    <h2 class="section-title">Flagships, papers that move the field</h2>
    <p class="section-sub">Nine systems chosen for the largest measured gains or the clearest demonstration of a structural pattern.</p>
    <div class="fl-grid">{''.join(fl_cards)}</div>
  </div>
</section>

<section id="requirements" class="prose-section alt-bg">
  <div class="wrap">
    <h2 class="section-title">Five demands that make retrieval scientific</h2>
    <p class="section-sub">General RAG ranks web text by semantic proximity. Science is governed by physical law, not linguistic flexibility, a transposed digit that merely dents fluency in prose can turn a benign compound toxic. Five demands follow.</p>
    <div class="req-grid">
      <div class="req-card req-1">
        <div class="req-num">1</div>
        <h3>Traceable attribution</h3>
        <p>Every claim must trace to a specific source unit, sentence-level, page-level, or as a claim graph, because fluency alone cannot be trusted.</p>
        <p class="req-evidence">OpenScholar 0% citation hallucination, PaperQA sentence-level attribution</p>
      </div>
      <div class="req-card req-2">
        <div class="req-num">2</div>
        <h3>Heterogeneous, multi-substrate retrieval</h3>
        <p>The corpus is not uniform web text but literature, curated graphs, structured entities, and raw signals, each with its own format and reliability, each reached by a different operation.</p>
        <p class="req-evidence">Textual, Relational, Structured-entity, Perceptual substrates (§4)</p>
      </div>
      <div class="req-card req-3">
        <div class="req-num">3</div>
        <h3>Domain-native representation</h3>
        <p>SMILES, InChI, FASTA, CIF, DICOM carry meaning no flattening to text preserves. Retrieval must recognize a molecule's identity across every surface form it takes.</p>
        <p class="req-evidence">f-RAG / Rag2Mol / RetMol SMILES+3D, MMed-RAG DICOM, LLaMP CIF</p>
      </div>
      <div class="req-card req-4">
        <div class="req-num">4</div>
        <h3>Protocol-level reproducibility</h3>
        <p>An output must carry enough method detail for a domain expert to reproduce it, not merely a readable summary of what was done.</p>
        <p class="req-evidence">MITRA full-method docs, executable / API-grounded pipelines</p>
      </div>
      <div class="req-card req-5">
        <div class="req-num">5</div>
        <h3>External verifier coupling</h3>
        <p>For discovery, a docking simulator or a DFT calculation, not the language model, decides whether a proposal survives. How deeply the verifier is coupled bounds how far a system can reach.</p>
        <p class="req-evidence">f-RAG → docking loop, HEA-catalyst → DFT, IRDiff/Rag2Mol external docking</p>
      </div>
    </div>
  </div>
</section>

<section id="growth" class="prose-section">
  <div class="wrap">
    <h2 class="section-title">Growth by year, stacked by retrieval substrate</h2>
    <p class="section-sub">
      The 2024–2025 surge is led by <strong style="color:#b8431f">Textual</strong> systems (medical QA, literature
      synthesis), with <strong style="color:#6a3acb">Structured-entity</strong> and
      <strong style="color:#1f7a4d">Relational</strong> work following. <strong style="color:#d4992a">Perceptual</strong>
      retrieval, the substrate that needs a learned cross-modal encoder, arrives later and stays thinner, tracking
      the field's concentration on text.
    </p>
    <div class="chart-frame">{timeline_svg}</div>
    <p class="chart-legend">{legend}</p>
  </div>
</section>

<section id="kd" class="prose-section alt-bg">
  <div class="wrap">
    <h2 class="section-title">Substrate × Domain, where each substrate lives</h2>
    <p class="section-sub">
      Medicine spreads across all four substrates. Chemistry and materials lean on the Structured-entity databases
      of molecules and properties. Biology mixes Textual literature with Relational graphs. Physics, earth science,
      and astronomy are Textual- and Perceptual-heavy, instrument archives no one has yet indexed. Cells link to a
      filtered Browse view.
    </p>
    <table class="kd-grid">
      <thead>{kd_head}</thead>
      <tbody>{kd_rows}</tbody>
    </table>
  </div>
</section>

<section id="bridges" class="prose-section">
  <div class="wrap">
    <h2 class="section-title">Cross-substrate systems, the retrieval frontier</h2>
    <p class="section-sub">
      Nearly every surveyed system commits to a single substrate, yet a real scientific question often spans
      several at once, linking a molecule's structure to the literature that discusses it and to the graph
      relations it takes part in. The <strong>{len(xs_papers)}</strong> systems below reach across substrates:
      MedGraphRAG links documents, literature, and a controlled vocabulary into one graph, and Omni-RAG routes a
      query across several heterogeneous stores. None yet matches a query expressed in one substrate against
      evidence keyed in another, the open challenge of §8.
    </p>
    <div class="card-grid">{xs_cards}</div>
    <p class="see-more"><a href="browse.html" class="btn btn-secondary">Browse all cross-substrate systems →</a></p>
  </div>
</section>

<section id="frontiers" class="prose-section alt-bg">
  <div class="wrap">
    <h2 class="section-title">Frontier cells, where the white space is</h2>
    <p class="section-sub">
      Capability concentrates on the Textual substrate and thins toward discovery. The grid surfaces two dormant
      cells where the verifier or the substrate simply does not exist yet, the operations an autonomous AI
      scientist depends on most. A third, Perceptual × Synthesis, has no retrievable substrate at all and is empty.
    </p>
    <div class="frontier-pair">
      <div class="frontier-col">
        <h3><span class="cell-id-big">[K1.O3]</span> Textual × Discovery <span class="muted">({len(frontier_K3O3)} systems)</span></h3>
        <p>Literature-grounded ideation. Systems propose mechanisms and hypotheses from the literature, but no docking program, simulator, or database can confirm an idea, so they are judged only by novelty or expert preference, signals that language-model judges overrate. The one Discovery rung that coupling a verifier cannot yet close.</p>
        <div class="card-grid">{f33}</div>
      </div>
      <div class="frontier-col">
        <h3><span class="cell-id-big">[K4.O3]</span> Perceptual × Discovery <span class="muted">({len(frontier_K4O3)} systems)</span></h3>
        <p>Signal-to-structure discovery, a molecule from a spectrum, a diagnosis-hypothesis from an image. MADGEN retrieves a scaffold keyed on an MS/MS spectrum and generates the full structure, but almost every other spectrum-to-structure model generates with no retrieval at all. The sparsest inhabited cell in the grid.</p>
        <div class="card-grid">{f43}</div>
      </div>
    </div>
  </div>
</section>

<section id="directions" class="prose-section">
  <div class="wrap">
    <h2 class="section-title">The road ahead, three causes of the gaps</h2>
    <p class="section-sub">The survey (§8) reads the thin cells not as one problem but three. Some gaps are already solved in general RAG and only await adaptation; others need components built for science; the rest cannot be closed by architecture at all. The work ahead is less a search for better retrievers than making more of science <em>retrievable</em> and more of its outputs <em>verifiable</em>.</p>
    <div class="dir-grid">
      <div class="dir-card">
        <span class="dir-num">A1</span>
        <h3>Adapt: Reasoning-aware retrieval &amp; reranking</h3>
        <p>Forced retrieval can inject stale or superseded facts, and standard rerankers reward passages that are semantically similar but logically irrelevant. Adapting when-to-retrieve and relevance to scientific epistemology, not surface overlap, is the near-term win.</p>
        <p class="dir-ev">adaptive retrieval, reasoning-utility reranking (SciRerankBench)</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">A2</span>
        <h3>Adapt: Contamination &amp; discovery evaluation</h3>
        <p>Scientific literature is finite, so test items and retrievable documents share one narrow corpus and science cannot fabricate fresh questions. Discovery is always scored against a proxy, a proxy that marks genuinely novel-but-correct output as wrong.</p>
        <p class="dir-ev">post-cutoff contamination control, staged simulation / wet-lab confirmation</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">B1</span>
        <h3>Build: Retrievable substrates <span class="dir-star">★ largest unclaimed win</span></h3>
        <p>Large authoritative archives (AFLOW, OQMD, HEPData, sky surveys) have no query layer for RAG. Activating them needs specialized intermediary layers that encode database schemas and measurement metadata, plus a path from live findings to a queryable index.</p>
        <p class="dir-ev">indexing non-textual archives, streaming, not snapshotting</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">B2</span>
        <h3>Build: Cross-modal identity &amp; cross-substrate retrieval</h3>
        <p>A molecule is a SMILES string, an IUPAC name, and a 3D structure at once; a question in one substrate is often answered by evidence keyed in another. Retrieval must recognize scientific identity across surface forms and fuse matches across all four substrates.</p>
        <p class="dir-ev">modality-spanning encoders, one retriever over Textual+Relational+Structured+Perceptual</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">B3</span>
        <h3>Build: Scientific verifiers &amp; executable RAG</h3>
        <p>Outside molecular docking, verifiers for physical validity barely exist. Reaching discovery needs domain verifiers coupled into generation, uncertainty preserved rather than collapsed, and closed loops that execute tools, fail, and retrieve to recover.</p>
        <p class="dir-ev">constraint checkers, retrieval-augmented error recovery, verifier-free ideation</p>
      </div>
      <div class="dir-card">
        <span class="dir-num">C</span>
        <h3>Beyond technique: Tacit knowledge &amp; access</h3>
        <p>The intuition a scientist acquires at the bench is never written down, and much empirical data is locked behind licensing and privacy law. Better architecture cannot manufacture ground truth that was never recorded or that no system is permitted to read.</p>
        <p class="dir-ev">approximating unrecorded intuition, the human-vs-system access asymmetry</p>
      </div>
    </div>
    <p class="section-sub" style="margin-top:1.4rem">
      <strong>Outlook.</strong> Evidence grounding is the foundation an autonomous AI scientist must stand on, and the cells it depends on most, synthesis and verified discovery, are the least mature. Closing them turns partly on industry: self-driving labs generate the missing data (including negative results), while general RAG infrastructure makes closed corpora searchable in place.
    </p>
  </div>
</section>
'''
    (ROOT / 'insights.html').write_text(page_head('Insights', base='', desc='Flagship systems, the five demands of scientific RAG, substrate growth over time, the substrate×domain map, cross-substrate systems, frontier cells, and the road ahead.', current='insights') + body + PAGE_FOOT)


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


def _slugify(text):
    s = re.sub(r'<[^>]+>', '', text)                      # strip tags
    s = re.sub(r'[^\w\s가-힣-]', '', s, flags=re.U).strip().lower()
    s = re.sub(r'[\s_]+', '-', s)
    return s or 'sec'


def render_paper_pages():
    """Render papers/<bib_key>.html from papers/<bib_key>.md (Notion summaries),
    with a resource-link row (Paper/GitHub/HF model), a hyperlinked table of contents,
    and a BibTeX citation box."""
    import mistune
    md_renderer = mistune.create_markdown(escape=False, plugins=['table','strikethrough','footnotes','url'])
    papers_by_key = {p['bib_key']: p for p in papers if p.get('bib_key')}
    try:
        BIBTEX = json.loads((ROOT / 'data/bibtex.json').read_text())
    except Exception:
        BIBTEX = {}
    papers_dir = ROOT / 'papers'
    if not papers_dir.exists():
        print('  papers/ dir missing, skipping summary pages')
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
        bib_key = matching.get('bib_key', '')
        title = matching.get('title') or bib_key_fn
        raw_md = md_file.read_text()
        md_content = raw_md
        # Strip YAML frontmatter
        if md_content.startswith('---'):
            end = md_content.find('---', 3)
            if end > 0:
                md_content = md_content[end+3:].lstrip()
        # Discover resource links from the summary body (first occurrence of each).
        gh = re.search(r'https?://github\.com/[^\s)\]<>"]+', md_content)
        hf = re.search(r'https?://huggingface\.co/[^\s)\]<>"]+', md_content)
        # Convert Notion property block → HTML table
        md_content = _prop_block_to_table(md_content)
        md_content = re.sub(r'(</table>)\s*\n(#)', r'\1\n\n\2', md_content)
        md_content = re.sub(r'(\n#{1,6} [^\n]+)\n(<table)', r'\1\n\n\2', md_content)
        md_content = re.sub(r'(</table>)\s*\n([^\n#<\s-])', r'\1\n\n\2', md_content)
        body_html = md_renderer(md_content)

        # Add ids to h2/h3 headings and collect a table of contents.
        toc = []
        _seen = {}
        def _hrepl(m):
            lvl, inner = m.group(1), m.group(2)
            slug = _slugify(inner)
            if slug in _seen:
                _seen[slug] += 1; slug = f'{slug}-{_seen[slug]}'
            else:
                _seen[slug] = 0
            toc.append((lvl, slug, re.sub(r'<[^>]+>', '', inner).strip()))
            return f'<h{lvl} id="{slug}">{inner}</h{lvl}>'
        body_html = re.sub(r'<h([23])>(.*?)</h\1>', _hrepl, body_html, flags=re.S)
        toc_html = ''
        if len(toc) >= 3:
            items = ''.join(
                f'<li class="toc-l{lvl}"><a href="#{slug}">{esc(txt)}</a></li>' for lvl, slug, txt in toc)
            toc_html = f'''<nav class="paper-toc" aria-label="On this page">
      <div class="toc-cap">On this page</div>
      <ul>{items}</ul>
    </nav>'''

        url = matching.get('paper_link') or ''
        links = []
        if url:
            links.append(f'<a href="{esc(url)}" target="_blank" rel="noopener" class="res-link res-paper">📄 Paper ↗</a>')
        if gh:
            links.append(f'<a href="{esc(gh.group(0))}" target="_blank" rel="noopener" class="res-link res-code">⌥ GitHub ↗</a>')
        if hf:
            links.append(f'<a href="{esc(hf.group(0))}" target="_blank" rel="noopener" class="res-link res-model">🤗 Model / HF ↗</a>')
        links_html = f'<div class="paper-links">{"".join(links)}</div>' if links else ''

        cells = matching.get('ko_cells', [])
        cell_tags = ''.join(f'<a href="../cell/{c}.html" class="tag tag-cell" title="{c}">{cell_label(c)}</a>' for c in cells)
        subsec = matching.get('subsection', '')
        if isinstance(subsec, list):
            subsec = ', '.join(x for x in subsec if x)
        subsec_tag = f'<span class="tag tag-sub">{esc(subsec)}</span>' if subsec else ''
        domains = matching.get('domain', [])
        dom_tags = ''.join(f'<a href="../domain/{d}.html" class="tag tag-domain">{DOMAIN_EMOJI.get(d,"")}{esc(DOMAIN_LABELS.get(d,d))}</a>' for d in domains)
        typ = matching.get('type', '')
        type_tag = f'<a href="../topics/{typ.lower()}.html" class="tag tag-type">{esc(TYPE_LABELS.get(typ,typ))}</a>' if typ and typ != 'unknown' else ''

        bibtex = BIBTEX.get(bib_key, '')
        cite_html = ''
        if bibtex:
            cite_html = f'''
<section class="paper-cite" id="cite">
  <div class="wrap">
    <h2>Cite</h2>
    <pre class="bibtex"><code>{esc(bibtex)}</code></pre>
  </div>
</section>'''

        body = f'''
<section class="paper-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="../browse.html">← All papers</a></p>
    <h1>{esc(title)}</h1>
    <div class="paper-hero-meta">
      <span class="meta-venue">{esc(matching.get('venue',''))}</span>
      <span class="meta-year">{esc(matching.get('year',''))}</span>
    </div>
    {links_html}
    <div class="paper-tags">{cell_tags}{subsec_tag}{dom_tags}{type_tag}</div>
  </div>
</section>
<section class="paper-body">
  <div class="wrap paper-layout">
    {toc_html}
    <article class="paper-markdown">
      {body_html}
      <p class="paper-cite-jump"><a href="#cite">↓ Cite this ({esc(bib_key)})</a></p>
    </article>
  </div>
</section>{cite_html}
'''
        out_fn = bib_key_fn + '.html'
        (papers_dir / out_fn).write_text(page_head(esc(title), base='../', current=f'papers/{bib_key_fn}') + body + page_foot('../'))
        count += 1
    print(f'  papers/*.html ({count} summaries)')


def write_catalog():
    """Write the remapped catalog (data/papers.json re-tagged onto the survey's substrate ×
    objective taxonomy) to data/catalog.json, which the client-side Browse page consumes.
    data/papers.json stays the untouched source."""
    (ROOT / 'data/catalog.json').write_text(json.dumps(papers, ensure_ascii=False, indent=1))
    print(f'  data/catalog.json ({len(papers)} entries, remapped)')


if __name__ == '__main__':
    render_paper_pages()   # First, so paper_card() can detect summary pages
    render_index()
    render_about()
    render_browse()
    render_insights()
    render_cell_pages()
    render_axis_overview()
    render_task_pages()
    render_domain_pages()
    render_type_pages()
    write_catalog()
    print('Wrote all HTML pages.')
    print(f'  index.html, about.html, browse.html, insights.html')
    print(f'  cell/*.html (12 K×O + K/O axis + overviews + {len(TASK_ORDER)} task pages)')
    print(f'  domain/*.html ({len([d for d in DOMAIN_LABELS if d in by_dom])} domains)')
    print(f'  topics/*.html ({len([t for t in TYPE_LABELS if t in by_type])} types)')
