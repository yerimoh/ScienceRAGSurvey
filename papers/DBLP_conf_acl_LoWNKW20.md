---
notion_id: 355f2dcd-4912-8193-8028-d0ee8814f3e4
title: S2ORC - The Semantic Scholar Open Research Corpus
bib_key: DBLP:conf/acl/LoWNKW20
year: 2020
domain: bio, medical, physics
type: dataset
venue: ACL
paper_link: https://arxiv.org/abs/1911.02782
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# S2ORC: The Semantic Scholar Open Research Corpus

> arXiv | 2020 | dataset | bio · medical · physics

## TL;DR
A large-scale, publicly available, machine-readable academic corpus that provides **81.1 million** English scholarly papers, structured full text, and inline citation networks collected from hundreds of academic publishers and digital archives.

## Background and Motivation
**Limitations of existing corpora**
- Existing corpora are either small-scale or confined to specific domains (AAN, PubMed Central, etc.)
- They lack structured full text and inline citation information, making them difficult to use for text mining and citation network analysis

**Why this work is needed**
- A cross-disciplinary, comprehensive, and highly machine-readable academic dataset is needed
- Structuring inline citations, table/figure references, and bibliographic information to support NLP research

## Data Pipeline
```
[Collection from diverse sources such as MAG, arXiv, PubMed, Unpaywall]
      │
      ▼
[PDF/LaTeX processing]
ScienceParse (PDF → metadata & body text)
GROBID (PDF → XML: abstract, sections, captions, inline citations, bibliographic information)
      │
      ▼
[Metadata normalization]
Select the most reliable source → Build canonical data
      │
      ▼
[Filtering]
Remove low-quality entries such as those with no author or text under 100 characters
      │
      ▼
[Bibliography Linking]
Harmonic mean of Jaccard index + Containment metric
→ High-precision mapping of bibliography entries ↔ Paper cluster
      │
      ▼
[Output: S2ORC]
81.1M papers / 380.5M citation links
```

## Core Module Details
### 1. GROBID Parsing and Post-processing
- Separate abstracts, section headers, captions, and inline citations from the XML output
- Correct citation styles in bracket ([2]) or year-name form using regular expressions

### 2. Bibliography Linking
- Uses the **harmonic mean** of the Jaccard index and the Containment metric
- Links bibliography entries to actual paper clusters with high accuracy

### 3. Corpus Composition
| Component | Scale |
|---|---|
| Total papers | 81.1M |
| With abstract | 73.4M |
| With PDF | 28.9M |
| GROBID full text | 8.1M |
| LaTeX full text | 1.5M |
| Citation links | 380.5M |

## Experiments and Evaluation
**Evaluation method**: Build `S2ORC-SCIBERT`, pretrained from scratch on S2ORC text, and compare its performance against the existing `SciBERT`

**Main results (F1)**
| Dataset | Field | Task | S2ORC-SCIBERT |
|---|---|---|---|
| BC5CDR | Biomed | NER | 90.41 ± 0.06 |
| GENIA | Biomed | DEP | 90.80 ± 0.19 |
| ChemProt | Biomed | REL | (see body text) |
| SciERC | CS | NER | 68.93 ± 0.19 |
| SciCite | Biomed & CS | CLS | 84.76 ± 0.37 |

## Key Contributions
1. Release of the **largest publicly available academic corpus for NLP research**, containing full text of 8.1M open-access papers and a 380.5M citation network
2. Provides structuring down to the locations where formulas, tables, and figures are cited within the text (Inline References)
3. Cross-disciplinary coverage: spanning diverse fields such as CS, biomedicine, physics, and mathematics

## Limitations
- Citation context mismatches may occur in the process of grouping the draft and published versions of the same paper into a single Paper cluster
- GROBID parsing errors and LaTeX metadata quality are uneven depending on the author's formatting
- Ambiguity exists in paper clustering

## Related links
- **Paper**: [https://arxiv.org/abs/1911.02782](https://arxiv.org/abs/1911.02782)
- **GitHub**: [https://github.com/allenai/s2orc/](https://github.com/allenai/s2orc/)
