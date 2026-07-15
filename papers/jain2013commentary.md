---
title: "Commentary: The Materials Project: A materials genome approach to accelerating materials innovation"
bib_key: "jain2013commentary"
year: 2013
domain: material
type: dataset
venue: APL Materials
paper_link: https://doi.org/10.1063/1.4812323
---
# Commentary: The Materials Project: A materials genome approach to accelerating materials innovation

jain2013commentary | 2013 | APL Materials | dataset | [material] | [paper](https://doi.org/10.1063/1.4812323)

**DB**: Materials Project
**DB size**: DFT property calculations for "all known inorganic materials" per the paper (tens of thousands as of 2013, now grown to over ~150,000)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Materials Project REST API (MPRester), www.materialsproject.org

> APL Materials | 2013 | dataset | material
#### 📌 TL;DR
A core program of the U.S. Materials Genome Initiative: a high-throughput materials database that freely provides DFT-computed properties (electronic structure, stability, elasticity, magnetism, etc.) for all known inorganic materials.

#### 🎯 Background
**Limitations of existing infrastructure**
- Discovering and optimizing new materials requires years of experimental time and high cost
- Computational materials science data is scattered across individual research groups, making reproduction and sharing difficult
- No systematic data infrastructure for exploring new functional materials (batteries, solar cells, catalysts, etc.)

**Why this system is needed**
- Automatically generate and accumulate materials property data at scale via high-throughput DFT calculations
- Need for an open platform for in silico materials design and data-driven discovery
- Demand for a multi-channel access environment supporting both interactive exploration and data mining

#### 🔨 Architecture
Materials Project uses a VASP-based DFT calculation engine to automatically compute many properties of inorganic crystal structures, including electronic structure, formation energy, band gap, elastic constants, magnetic properties, and Li-ion battery insertion voltages. Calculation results are stored in a MongoDB-based database and can be accessed programmatically through the Materials Project API (MPRester). It integrates with the FireWorks workflow engine and the pymatgen open-source library ecosystem.

#### 📥 Access
| Method | Description |
|---|---|
| Web portal | www.materialsproject.org — interactive structure exploration, dashboard |
| REST API | MPRester (Python) — structure/property queries, lookup by material ID (mp-xxx) |
| Data mining | Open dataset download support |

#### 📤 Data formats
- Crystal structures (CIF, POSCAR formats)
- DFT-computed properties: formation energy, band gap, electronic density of states, elastic constants
- Li/Na/K-ion battery insertion voltages, capacity, diffusion coefficients
- Surface energy, work function
- Magnetic moment, magnetic ordering

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Database goal | DFT property calculations for all known inorganic materials |
| Calculation engine | VASP (GGA + U, HSE06 optional) |
| API method | REST API (MPRester), free and open |
| Paper publication year | 2013 (APL Materials vol.1, no.1) |

#### ⚠️ Limitations
- At the time of the paper's publication (2013), the database was relatively small in scale and has since expanded continuously (no specific record count is stated in the paper)
- Because these are DFT-computed values, systematic errors relative to experimental values exist (e.g., GGA underestimates band gaps)
- Focuses primarily on static (0 K) properties; finite-temperature and finite-pressure properties require separate treatment
- Structural stability prediction is central, but it does not guarantee synthesizability

## Related links
- **Paper**: [Commentary: The Materials Project (APL Materials, 2013)](https://doi.org/10.1063/1.4812323)
