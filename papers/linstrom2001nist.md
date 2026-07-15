---
title: "The NIST Chemistry WebBook: A chemical data resource on the internet"
bib_key: "linstrom2001nist"
year: 2001
domain: chem
type: dataset
venue: Journal of Chemical & Engineering Data
paper_link: https://doi.org/10.1021/je000225m
---
# The NIST Chemistry WebBook: A chemical data resource on the internet

linstrom2001nist | 2001 | Journal of Chemical & Engineering Data | dataset | [chem] | [paper](https://doi.org/10.1021/je000225m)

**DB**: NIST Chemistry WebBook
**DB size**: Not reported in the paper (thermochemistry-data focused; tens of thousands of compounds)
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: NIST Chemistry WebBook (webbook.nist.gov)

> Journal of Chemical & Engineering Data | 2001 | dataset | chem
#### 📌 TL;DR
The NIST Chemistry WebBook is an open chemical data resource provided by the U.S. NIST (National Institute of Standards and Technology), offering unrivaled depth and reliability in the fields of thermochemical and spectroscopic data.

#### 🎯 Background
**Limitations of existing infrastructure**
- Physicochemical data such as thermochemistry and spectroscopy were scattered across multiple NIST publications
- Rapid, integrated data access over the internet was not possible
**Why this system is needed**
- Researchers in chemical engineering, environmental science, and materials science need a single resource to instantly look up standard physicochemical properties
- To broadly distribute NIST's reliable, evaluated data over the internet

#### 🔨 Architecture
It integrates NIST's existing data resources, such as the NIST-JANAF Thermochemical Tables and the NIST Webbook Standard Reference Database, into an internet-accessible form. It can be searched by compound name, chemical formula, CAS registry number, InChI, and more. Supports name, molecular formula, CAS number, and structure search.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | Direct search at webbook.nist.gov |
| JSON API | NIST WebBook JSON API (compound data lookup) |

#### 📤 Data formats
- Thermochemical data (ΔHf°, S°, Cp, etc.)
- Spectroscopic data (IR, MS, NMR, UV-Vis)
- Thermodynamic phase-transition data
- Ionization energy and ion energetics data

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Release year | 1996 (the paper describes the 2001 update) |
| Data types | Thermochemistry, spectroscopy, phase transitions, ionization energy, etc. |

#### ⚠️ Limitations
- Includes both organic and inorganic compounds, but has no bioactivity data for drug-like molecules
- Some older data has limited accuracy compared with modern computational methods
- The data scope is specialized around thermochemistry and spectroscopy

## Related links
- **Official page**: [NIST Chemistry WebBook](https://webbook.nist.gov)
- **Paper**: [The NIST Chemistry WebBook](https://doi.org/10.1021/je000225m)
