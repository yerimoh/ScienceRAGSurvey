---
title: "HEPData: A Repository for High Energy Physics Data"
bib_key: "DBLP:journals/corr/MaguireHW17"
year: 2017
domain: physics
type: dataset
venue: Journal of Physics Conference Series (arXiv:1704.05473)
paper_link: https://arxiv.org/abs/1704.05473
---
# HEPData: A Repository for High Energy Physics Data

DBLP:journals/corr/MaguireHW17 | 2017 | Journal of Physics Conference Series | dataset | [physics] | [paper](https://arxiv.org/abs/1704.05473)

**DB**: HEPData — open-access repository for high-energy physics experimental data
**DB size**: Data points underlying several thousand publications (as of 2017); currently ~20,000+ records (model knowledge)
**DB Open/Private**: Open
**Modality**: ['Table', 'Plot data', 'Numerical arrays']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: HEPData REST API / hepdata_lib (Python)

> Journal of Physics Conference Series | 2017 | dataset | physics
#### TL;DR
A paper describing the modern rebuild of the Durham High Energy Physics Database (HEPData). It is the only numerical data archive in high-energy physics that preserves, in machine-readable form, the numerical results (scattering cross-sections, distributions, correlation matrices) of particle-physics experimental papers accumulated over **more than 40 years**. Since 2015 it has been completely rewritten on top of Invenio v3 and is served at hepdata.net.

#### Background
**Limitations of the existing infrastructure**
- The legacy platform (hepdata.cedar.ac.uk), which started at Durham SPIRES/HEPData in the 1960s, lacks modern features
- Numerical results of papers existed only in figures and PDFs, making re-analysis and reuse impossible
- No standardization of data formats — researchers had to manually digitize figures

**Why this system is needed**
- The complex measurement results of LHC experiments (ATLAS, CMS, LHCb, ALICE) — multi-dimensional distributions, covariance matrices, systematic uncertainties — need structured preservation
- Machine-readable data is essential for reinterpretation, statistical combination, and model-independent limit setting
- Serves as the high-energy-physics community's standard data-sharing platform

#### Architecture
A digital library framework based on Invenio v3. Open source (published on GitHub). YAML/JSON-based HEPData submission format. Direct linking to InspireHEP, arXiv, and DOI. Per-figure data table structure (including x-axis, y-axis, uncertainties, and units). Supports ROOT, YODA, CSV, and JSON downloads.

#### Data types provided
- **Cross-sections**: differential (per energy, per angle) and total cross-sections
- **Distributions**: invariant mass, transverse momentum, and rapidity-variable distributions
- **Correlation matrices**: covariance and correlation matrices (for statistical combination)
- **Exclusion limits**: supersymmetry and dark-matter search results
- **Efficiencies/acceptances**: per-analysis selection efficiencies and geometric acceptances

#### Access
| Method | Description |
|---|---|
| hepdata.net | Web browsing, download, visualization |
| HEPData REST API | Returns JSON/YAML |
| hepdata_lib | Python library (submission and reading) |
| ROOT/YODA files | Direct download |

#### Key statistics (based on the 2017 paper + model knowledge)
| Item | Value |
|---|---|
| Number of papers (as of 2017) | **Several thousand** (several thousand publications) |
| Operating period | **40+ years** (started at Durham in the 1970s) |
| Current number of records | **~20,000+** records (model knowledge, 2025) |
| Public software | GitHub (open source) |
| Connected systems | InspireHEP, arXiv, DOI |

#### Limitations
- Data from earlier legacy papers requires manual entry or digitization — incompleteness
- Papers whose data was not extracted from figures are not registered in HEPData
- Limits in fully representing the structure of complex multi-dimensional distributions (e.g., 2D variable scans)
- Currently not used at all as a retrieval corpus in RAG systems (pointing out the survey's K3 gap)

## Related links
- **Paper**: [https://arxiv.org/abs/1704.05473](https://arxiv.org/abs/1704.05473)
- **HEPData**: [https://hepdata.net](https://hepdata.net)
