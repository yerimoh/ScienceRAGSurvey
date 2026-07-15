---
title: "Climate Change 2023: Synthesis Report"
bib_key: "lee2023climate"
year: 2023
domain: earth
type: dataset
venue: IPCC
paper_link: https://www.ipcc.ch/report/ar6/syr/
---
# Climate Change 2023: Synthesis Report

lee2023climate | 2023 | IPCC | dataset | [earth] | [paper](https://www.ipcc.ch/report/ar6/syr/)

**DB**: IPCC Sixth Assessment Report (AR6) Synthesis
**DB size**: Integration of 3 working group reports + 3 special reports (6,841 review comments processed)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: IPCC AR6 Synthesis Report

> IPCC | 2023 | dataset | earth
#### 📌 TL;DR
The Synthesis Report of the IPCC Sixth Assessment Report (AR6), the standard reference document in climate science — an authoritative climate science synthesis document integrating the outputs of Working Groups I, II, and III.

#### 🎯 Background
**Limitations of existing infrastructure**
- Climate science literature is scattered across thousands of individual papers, making it difficult to grasp the comprehensive consensus
- Absence of a single authoritative document that organizes the climate science consensus in a format accessible to policymakers

**Why this system is needed**
- A standard, trusted document in the field that climate science RAG systems (e.g., ChatClimate) use as a reference source
- Functions not as a general bibliographic index but as a synthesis document that the field itself recognizes as the standard
- Provides baseline figures for climate science, such as the average global surface temperature rise over 2011–2020 (+1.1°C relative to 1850–1900)

#### 🔨 Architecture
Published by the IPCC (Intergovernmental Panel on Climate Change). A Core Writing Team of 49, 9 Review Editors, an Extended Writing Team of 7, and 28 Contributing Authors — 93 authors in total. It integrates the assessment reports of 3 working groups and 3 special reports (Global Warming of 1.5°C, Climate Change and Land, and the Ocean and Cryosphere):
- **WGI**: The Physical Science Basis of climate science (2021)
- **WGII**: Impacts, Adaptation, and Vulnerability (2022)
- **WGIII**: Mitigation of Climate Change (2022)

#### 📥 Access
| Method | Description |
|---|---|
| Free PDF | Full text available for free download at ipcc.ch (Summary for Policymakers, Longer Report, and full volume provided separately) |
| Online viewing | Interactive viewing available on the official IPCC website |
| Multilingual | Summary provided in the 6 official UN languages |

#### 📤 Data formats
- Summary for Policymakers (SPM): 19 headline statements (three parts: A, B, C)
- Longer Report
- Full Volume
- Figures and diagrams (including interactive online versions)
- Presentation slide deck

#### 📊 Key statistics (per the paper)
| Item | Figure |
|---|---|
| Core Writing Team | **49** |
| Review Editors | **9** |
| Contributing Authors | **28** |
| Total authors | **93** |
| Number of review comments | **6,841** (governments 6,636 + observers 205) |
| Number of governments participating in review | **47 countries** |
| Number of integrated working groups | **3** (WGI, WGII, WGIII) |
| Number of integrated special reports | **3** |
| Number of headline statements | **19** |
| Baseline temperature rise | **+1.1°C** (2011–2020 vs 1850–1900) |

#### ⚠️ Limitations
- **Not a bibliographic index**: It does not index papers directly and is a synthesis document of published climate science literature — new papers are only reflected after an assessment cycle of roughly 7 years
- **Fixed snapshot**: Based on literature up to 2022, it does not reflect research results published after 2023
- **PDF only**: Since it is not in the form of a structured API or machine-readable database, PDF parsing is required when integrating with a RAG system
- **Not a substitute for peer-reviewed papers**: As it is a synthesis document rather than a bibliographic database of primary research literature, it cannot be used for general literature search purposes

## Related links
- **Paper**: [https://www.ipcc.ch/report/ar6/syr/](https://www.ipcc.ch/report/ar6/syr/)
