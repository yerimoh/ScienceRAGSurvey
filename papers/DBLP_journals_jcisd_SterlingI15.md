---
title: "ZINC 15 - Ligand Discovery for Everyone"
bib_key: "DBLP:journals/jcisd/SterlingI15"
year: 2015
domain: chem
type: dataset
venue: Journal of Chemical Information and Modeling
paper_link: https://doi.org/10.1021/acs.jcim.5b00559
---
# ZINC 15 - Ligand Discovery for Everyone

DBLP:journals/jcisd/SterlingI15 | 2015 | Journal of Chemical Information and Modeling | dataset | [chem] | [paper](https://doi.org/10.1021/acs.jcim.5b00559)

**DB**: ZINC15
**DB size**: 120M+ purchasable drug-like compounds
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ZINC15 web interface (zinc15.docking.org)

> Journal of Chemical Information and Modeling | 2015 | dataset | chem
#### 📌 TL;DR
ZINC15 contains more than 120 million purchasable drug-like compounds, and integrates links to high-value compounds such as metabolites, drugs, and natural products, access organized by gene and target class, and analysis tools that are friendly to non-experts.

#### 🎯 Background
**Limitations of existing infrastructure**
- Earlier ZINC versions were centered on computational experts, making them difficult for biologists to use
- Compound-target links and biological annotations were lacking
**Why this system is needed**
- An integrated platform that even non-experts can use for ligand discovery is needed
- Build an annotation scheme that links compounds to genes, target classes, and biological activity

#### 🔨 Architecture
It provides about 120 million purchasable drug-like compounds (a quarter of which are available for immediate delivery) in a 3D ready-to-dock format. Links to high-value compounds such as metabolites, approved drugs, natural products, and literature-annotated compounds. Access functionality organized by gene and by major and minor target classes. Integration of tools for ligand annotation, purchasability, targets, and biology links.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | Search and analysis at zinc15.docking.org |
| Subset download | Filter by gene/target and by property, then download |
| 3D format | All molecules provided in ready-to-dock form |

#### 📤 Data formats
- 3D structures (ready-to-dock, MOL2, SDF)
- SMILES
- Biological activity annotations
- Target-compound mappings

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Purchasable drug-like compounds | 120M+ |
| Compounds available for immediate delivery | ~25% (about 30M) |

#### ⚠️ Limitations
- Because it is catalog-based, actual purchasability requires continuous updates
- Some target-compound annotations are based on computational prediction

## Related links
- **Paper**: [ZINC 15 - Ligand Discovery for Everyone](https://doi.org/10.1021/acs.jcim.5b00559)
