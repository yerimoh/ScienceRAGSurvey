---
title: "OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts"
bib_key: "DBLP:journals/corr/abs-2205-01833"
year: 2022
domain: general
type: dataset
venue: arXiv (CoRR)
paper_link: https://arxiv.org/abs/2205.01833
---
# OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts

DBLP:journals/corr/abs-2205-01833 | 2022 | arXiv (CoRR) | dataset | [general] | [paper](https://arxiv.org/abs/2205.01833)

**DB**: OpenAlex scholarly knowledge graph
**DB size**: 209M works, 2,013M authors, 124K venues, 109K institutions, 65K concepts (as of the 2022 paper)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OpenAlex REST API / Full data dump

> arXiv (CoRR) | 2022 | dataset | general
#### 📌 TL;DR
A **fully-open** scholarly knowledge graph launched to fill the gap left after Microsoft Academic Graph (MAG) was discontinued, providing **209 million works**, **2.013 billion** author-identification records, **124 thousand** journals and repositories, **109 thousand** institutions, and **65 thousand** concepts free of charge through a web GUI, a full data dump, and a REST API.

#### 🎯 Background
**Limitations of existing infrastructure**
- The discontinuation of Microsoft Academic Graph (MAG) removed a large-scale public scholarly graph infrastructure
- Commercial databases such as Scopus and Web of Science come with cost and access restrictions, increasing the need for an open alternative

**Why this system is needed**
- Provides a **fully free, fully-open** scholarly knowledge graph to replace MAG
- Structures the five entity types (Works, Authors, Venues, Institutions, Concepts) into an interconnected graph

#### 🔨 Architecture
Integrates numerous sources including Crossref (bibliographic metadata), PubMed (biomedical literature), ORCID (author identifiers), ROR (research organization registry), MAG legacy data, Unpaywall (open-access information), and OpenCitations (citation data) to construct five entities (Works, Authors, Venues, Institutions, Concepts). Concept tagging is automated with a Wikidata-based hierarchical multi-tag classifier. Licensed under CC BY 4.0.

#### 📥 Access
| Method | Description |
|---|---|
| Web-based GUI | Explore directly in the browser |
| Full data dump | Bulk download of the full snapshot |
| REST API | Supports filtering, sorting, and pagination (JSON responses) |

#### 📤 Data formats
- **Works**: Metadata for scholarly works such as journal articles and books (title, authors, citations, etc.)
- **Authors**: Deduplicated author identifiers and profiles
- **Venues**: Information on journals and online repositories
- **Institutions**: ROR-linked research organization records
- **Concepts**: Wikidata-based hierarchical topic classification (multi-tag)
- License: CC BY 4.0 (free reuse including commercial use)

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| Works (scholarly works) | **209M** (as of 2022) |
| Authors (deduplicated) | **2,013M** (as of 2022) |
| Venues (journals/repositories) | **124K** (as of 2022) |
| Institutions | **109K** (as of 2022) |
| Concepts (topic classification) | **65K** (as of 2022) |
| License | CC BY 4.0 |

#### ⚠️ Limitations
- The paper explicitly states that it is "under active development"
- Improving the accuracy and coverage of citation information is described as future work
- The accuracy of author and institution parsing and deduplication needs improvement
- Coverage is uneven across fields (stronger in the STEM disciplines)

## Related links
- **Paper**: [https://arxiv.org/abs/2205.01833](https://arxiv.org/abs/2205.01833)
