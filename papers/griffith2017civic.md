---
title: "CIViC is a community knowledgebase for expert crowdsourcing the clinical interpretation of variants in cancer"
bib_key: "griffith2017civic"
year: 2017
domain: medical
type: dataset
venue: Nature Genetics
paper_link: https://doi.org/10.1038/ng.3774
---
# CIViC is a community knowledgebase for expert crowdsourcing the clinical interpretation of variants in cancer

griffith2017civic | 2017 | Nature Genetics | dataset | [medical] | [paper](https://doi.org/10.1038/ng.3774)

**DB**: CIViC (Clinical Interpretation of Variants in Cancer)
**DB size**: hundreds of variants and genes at publication time; grows through continuous community curation
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: CIViC REST API / civicdb.org web interface

> Nature Genetics | 2017 | dataset | medical
#### 📌 TL;DR
An open-source, open-access cancer precision-medicine knowledge base that builds therapeutic, prognostic, diagnostic, and predisposing clinical interpretations of cancer variants through expert crowdsourcing, with a curator-editor verification workflow.

#### 🎯 Background
**Limitations of existing infrastructure**
- The clinical interpretation of cancer variants was scattered across individual papers and internal laboratory systems, making systematic access difficult
- Existing DBs such as OncoKB and JAX-CKB were curated in a closed manner by a small number of specialized institutions; community contribution was not possible
- The evidence sources for the clinical significance of the same variant could not be tracked transparently

**Why this system is needed**
- To keep pace with the rapid advance of cancer precision medicine, distributed curation by a worldwide community of experts is required
- The four clinical variant roles — predictive, prognostic, diagnostic, and predisposing — must be managed in an integrated way

#### 🔨 Architecture
CIViC has a wiki-style curation workflow.
- **Evidence Item**: the unit of an individual variant-clinical association; a single literature source + clinical-significance label
- **Variant**: a specific variant within a gene (SNV, insertion/deletion, fusion, etc.)
- **Gene**: the gene entry to which a variant belongs
- **Curator → Editor → Approval** three-stage workflow; published after editor review

Four clinical roles: **Predictive** (predicting therapeutic response), **Prognostic** (prognosis), **Diagnostic** (diagnostic classification), **Predisposing** (genetic predisposition)

#### 📥 Access
| Method | Description |
|---|---|
| CIViC REST API | api.civicdb.org — query genes, variants, and evidence items; publicly free |
| Web interface | civicdb.org — search, curation, visualization |
| Data download | nightly TSV/VCF dumps; fully open access |

#### 📤 Data formats
- Evidence Item (variant-clinical association + literature PMC/PMID)
- Variant summary (variant description + aggregation of associated entries)
- VCF-format variant files
- Open-source code (GitHub: griffithlab/civic-client)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Clinical role categories | Predictive, Prognostic, Diagnostic, Predisposing (4 types) |
| Curation workflow | curator submission → editor review → approval |
| License | CC0 (public domain) |
| Code license | MIT |
| Operating institution | Washington University in St. Louis (Griffith Lab) |

#### ⚠️ Limitations
- Due to the nature of community curation, entries are concentrated on certain well-known genes (EGFR, BRAF, KRAS, etc.)
- The limited number of editors can cause time delays in reviewing new entries
- Coverage is low for rare cancers and rare variants due to a lack of supporting literature
- The distinction between somatic and germline may lack consistency across entries

## Related links
- **Paper**: [Griffith et al., Nature Genetics 2017](https://doi.org/10.1038/ng.3774)
