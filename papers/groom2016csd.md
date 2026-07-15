---
title: "The Cambridge Structural Database"
bib_key: "groom2016csd"
year: 2016
domain: chem
type: dataset
venue: Acta Crystallographica Section B
paper_link: https://doi.org/10.1107/S2052520616003954
---
# The Cambridge Structural Database

groom2016csd | 2016 | Acta Crystallographica Section B | dataset | [chem] | [paper](https://doi.org/10.1107/S2052520616003954)

**DB**: CSD (Cambridge Structural Database)
**DB size**: 800,000 entries (2016, CSD community service)
**DB Open/Private**: Open (community service) / Subscription (full functionality)
**Modality**: ['Structured']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: CSD (operated by CCDC, CSD community web service)

> Acta Crystallographica Section B | 2016 | dataset | chem
#### 📌 TL;DR
The CSD is the complete record of crystal structures of small organic and metal-organic molecules that the CCDC (Cambridge Crystallographic Data Centre) has operated for more than 50 years. As of 2016 it contains 800,000 entries, making it a fundamental resource of structural chemistry.

#### 🎯 Background
**Limitations of existing infrastructure**
- Published crystal structure data was scattered across the supplementary materials of individual journals, making unified access and reuse difficult
**Why this system is needed**
- A single authoritative repository for structural chemistry data is needed to standardize the sharing of published crystal structures
- Standard identifiers and linking services are needed to improve the reusability and discoverability of data

#### 🔨 Architecture
Published crystal structures of small organic and metal-organic molecules are entered after being processed both computationally (automatically) and by expert editors (manually). Reliably linking chemical identity with experimental data is the key quality-control step. Through CSD Communications, structures can be deposited directly even without a journal paper. The use of standard identifiers provides linking services with other resources.

#### 📥 Access
| Method | Description |
|---|---|
| CSD community web service | Free, accessible to educational institutions worldwide |
| CCDC software | Mercury, ConQuest, etc. (institutional license) |
| API | CCDC API (programmatic access) |
| Third-party software | Integration with various molecular modeling software |

#### 📤 Data formats
- CIF (Crystallographic Information File) - structure data standard
- 3D coordinates and crystal symmetry information
- Chemical structures (linked with SMILES, InChI)

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| CSD community service entries | 800,000 |
| Total entries (table reported in the paper) | 363,372 → 731,675 (2014→2015 cumulative) |
| Number of associated papers | 232,858 → 408,899 |
| Annual new entries | 34,030 → 60,122 |
| Fraction with R-factor < 10% | 92~94% |

#### ⚠️ Limitations
- Full functionality and data usage require an institutional license
- Polymer and protein structures are separated out into the PDB
- The vast scale of 800,000 entries requires specialized tools for systematic data mining

## Related links
- **Paper**: [The Cambridge Structural Database](https://doi.org/10.1107/S2052520616003954)
