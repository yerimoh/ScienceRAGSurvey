---
title: "Europe PMC in 2023"
bib_key: "europepmc2024"
year: 2024
domain: medical, bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad1085
---
# Europe PMC in 2023

europepmc2024 | 2024 | Nucleic Acids Research | dataset | [medical, bio] | [paper](https://doi.org/10.1093/nar/gkad1085)

**DB**: Europe PMC open-access life science literature database
**DB size**: 42M+ abstracts, 9M+ full-text articles, 650K+ preprints (as of September 15, 2023)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Europe PMC REST API / Bulk download

> Nucleic Acids Research | 2024 | dataset | medical, bio
#### 📌 TL;DR
An open-access life science literature platform operated by EMBL-EBI and supported by 37 international research funding agencies. It provides **more than 42 million** abstracts and **more than 9 million** full-text articles, and offers for free via a RESTful API **more than 650,000** preprints collected from **31 preprint servers** along with **more than 2 billion** text-mining annotations.

#### 🎯 Background
**Limitations of existing infrastructure**
- The need for infrastructure that integrates and freely provides open-access life science literature
- The proliferation of preprint servers makes it difficult to search across the latest pre-peer-review research in an integrated way
- The absence of publicly available structured annotation data for text mining

**Why this system is needed**
- Core infrastructure designated as an ELIXIR Core Data Resource and a Global Core Biodata Resource
- Aggregates, as open access, the research outputs funded by 37 international research funding agencies
- Expanded preprint integration from 9 servers in 2018 to 31 servers in 2023

#### 🔨 Architecture
An open-access platform hosted by EMBL-EBI. Content is updated daily and provides rich metadata linked to more than 60 life science databases, citations, funding, protocols, and peer-review materials. Through Unpaywall it links free full-text access to more than 13 million publications. Preprint inclusion criteria (newly established in March 2023): all conditions must be met, namely free access, life science as the main content, having a screening procedure, a plagiarism and misconduct policy, a minimum of at least 30 items, and provision of machine-readable metadata. New code such as the text-mining API is released as open source on GitLab (POSI adopted in 2022).

#### 📥 Access
| Method | Description |
|---|---|
| Website | europepmc.org — browser-based exploration |
| REST API | RESTful API — free, daily updates |
| Bulk download | 5.7M open-access articles (PDF/XML), updated weekly, quarterly archives |

#### 📤 Data formats
- Abstracts, full text (open-access articles), metadata (title, authors, journal, PMID/PMCID/DOI)
- Text-mining annotations 20B+: gene/protein names, organisms, diseases, chemicals
- Preprint Evaluations API: peer-review report metadata based on the DocMaps framework
- Article Status Monitor: tracking the publication lifecycle (CSV export, POST REST API)
- Institutional ROR ID mapping (41% of institutions, 80%+ of grant PIs)

#### 📊 Key statistics (per the paper)
| Item | Figure |
|---|---|
| Total abstracts | **42M+** (as of September 15, 2023) |
| Full-text articles | **9M+** (as of September 15, 2023) |
| Preprints (total) | **650,000+** (as of September 15, 2023) |
| Preprints (with full text) | **53,624** (as of September 15, 2023) |
| COVID-19 preprint full text | **65,000+** |
| Integrated preprint servers | **31** (as of 2023) |
| Text-mining annotations | **2B+** |
| Open-access PDF bulk download | **5.7M** |
| Supporting funding agencies | **37** |
| Unpaywall full-text links connected | **13M+** |

#### ⚠️ Limitations
- **Tracking preprint retraction/removal**: possible only for preprints that have full text; the retraction status of preprints indexed with abstracts only cannot be tracked centrally
- **No preprint version linking**: on servers that reuse DOIs across versions, such as bioRxiv and medRxiv, links between versions cannot be established
- **Limitations in preprint-to-journal-article matching**: mapping between a preprint and its final published article may fail when the authors or title have changed substantially

## Related links
- **Paper**: [https://doi.org/10.1093/nar/gkad1085](https://doi.org/10.1093/nar/gkad1085)
