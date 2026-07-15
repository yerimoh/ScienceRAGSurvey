---
title: "ZINC: a free tool to discover chemistry for biology"
bib_key: "irwin2012zinc"
year: 2012
domain: chem
type: dataset
venue: Journal of Chemical Information and Modeling
paper_link: https://doi.org/10.1021/ci3001277
---
# ZINC: a free tool to discover chemistry for biology

irwin2012zinc | 2012 | Journal of Chemical Information and Modeling | dataset | [chem] | [paper](https://doi.org/10.1021/ci3001277)

**DB**: ZINC (2012 version)
**DB size**: 20M+ commercially available molecules
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ZINC web interface (zinc.docking.org)

> Journal of Chemical Information and Modeling | 2012 | dataset | chem
#### 📌 TL;DR
ZINC is an open ligand-discovery resource that aggregates more than 20 million commercially available molecules provided in biologically relevant forms, downloadable in ready-to-dock format.

#### 🎯 Background
**Limitations of existing infrastructure**
- Lists of purchasable compounds were fragmented, and in many cases were not prepared in the 3D forms required for docking
- It was difficult for biology researchers to perform compound searches without computational-chemistry expertise
**Why this system is needed**
- A ready-to-use 3D docking-format compound library is needed for virtual screening
- There was no single resource integrating purchasability information with biological-activity annotations

#### 🔨 Architecture
Lists of commercial compounds are collected and converted into 3D biologically relevant forms (including protonation state and tautomer). They can be searched by structure, biological activity, physical properties, vendor, catalog number, name, and CAS number. Functionality to create, edit, share, and download small custom subsets is provided.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | zinc.docking.org structure/property search |
| Subset download | ready-to-dock format (MOL2, SDF, etc.) |
| Custom subset | direct download after filtering |

#### 📤 Data formats
- 3D docking format (MOL2, SDF)
- SMILES
- Physicochemical properties (MW, LogP, HBA/HBD, etc.)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Commercially available molecules | 20M+ |

#### ⚠️ Limitations
- Because it is based on commercial catalogs, actual purchasability varies with the update cycle
- Per-vendor price and lead-time information depends on external links

## Related links
- **Paper**: [ZINC: a free tool to discover chemistry for biology](https://doi.org/10.1021/ci3001277)
