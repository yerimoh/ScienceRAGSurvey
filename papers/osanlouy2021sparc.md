---
title: "The SPARC DRC: building a resource for the autonomic nervous system community"
bib_key: "osanlouy2021sparc"
year: 2021
domain: medical, bio
type: dataset
venue: Frontiers in Physiology
paper_link: https://doi.org/10.3389/fphys.2021.693735
---
# The SPARC DRC: building a resource for the autonomic nervous system community

osanlouy2021sparc | 2021 | Frontiers in Physiology | dataset | [medical, bio] | [paper](https://doi.org/10.3389/fphys.2021.693735)

**DB**: SPARC (Stimulating Peripheral Activity to Relieve Conditions) Data and Resource Center
**DB size**: Exact count not specified in the paper — a collection of curated datasets from the SPARC consortium
**DB Open/Private**: Open (sparc.science)
**Modality**: Image (organ scaffolds, 2D flatmaps), Structured Table (experimental data, mathematical models)
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: SPARC data portal (sparc.science)

> Frontiers in Physiology | 2021 | dataset | medical, bio

#### 📌 TL;DR
The Data and Resource Center (DRC) of the NIH-funded SPARC program curates and annotates experimental data, mathematical models, and simulation tools for the mammalian autonomic nervous system, and delivers them to the neuromodulation research community through Google Maps-style 2D flatmaps and 3D organ scaffolds.

#### 🎯 Background
**Limitations of existing infrastructure**
- Autonomic nervous system data are scattered, making integrated search and cross-species comparison impossible
- No access path to computational models for developing neuromodulation devices
- No standardized resource for maps of autonomic anatomical connectivity

**Why this system is needed**
- Need to integrate the experimental data and models of the NIH-SPARC program into a single knowledge base
- Need a neuromodulation hypothesis-testing platform for autonomic neuroscientists and medical device manufacturers

#### 🔨 Architecture
Led by the Auckland Bioengineering Institute. Data and mathematical models provided by the SPARC consortium are curated and annotated and integrated into a single knowledge base. Includes a semantic search interface + Google Maps-style 2D flatmaps (showing connectivity) + 3D anatomical organ scaffolds (a common coordinate framework for cross-species comparison). Implements pipelines for data upload, curation, image segmentation, flatmap registration, and web portal display. Supports neuromodulation hypothesis testing through connection to online computational facilities.

#### 📥 Access
| Method | Description |
|---|---|
| SPARC portal | https://sparc.science — free public access |
| DOI | https://doi.org/10.3389/fphys.2021.693735 |

#### 📤 Data formats
- 2D flatmap connectivity maps (neural circuit diagrams)
- 3D anatomical organ scaffolds
- Experimental data (electrophysiology, imaging, etc.)
- Mathematical models and simulation files

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Funding agency | **NIH (SPARC program)** |
| Main focus | **Mammalian autonomic nervous system** |
| Portal features | **Semantic search, 2D flatmaps, 3D scaffolds** |

#### ⚠️ Limitations
- Exact dataset counts and number of species not specified in the paper
- Data curation and annotation quality varies by contributing institution
- Scaffolds for some organs and species are incomplete

## Related links
- **Paper**: [The SPARC DRC: building a resource for the autonomic nervous system community](https://doi.org/10.3389/fphys.2021.693735)
