---
title: "QMugs, quantum mechanical properties of drug-like molecules"
bib_key: "isert2022qmugs"
year: 2022
domain: chem
type: dataset
venue: Scientific Data
paper_link: https://doi.org/10.1038/s41597-022-01390-7
---
# QMugs, quantum mechanical properties of drug-like molecules

isert2022qmugs | 2022 | Scientific Data | dataset | [chem] | [paper](https://doi.org/10.1038/s41597-022-01390-7)

**DB**: QMugs (Quantum-Mechanical Properties of Drug-like Molecules)
**DB size**: 665k+ bioactive molecules, ~2M conformers
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: QMugs (GFN2-xTB + DFT/ωB97X-D/def2-SVP)

> Scientific Data | 2022 | dataset | chem
#### 📌 TL;DR
QMugs is an open-access dataset providing semi-empirical (GFN2-xTB) and DFT (ωB97X-D/def2-SVP) level quantum-mechanical properties for over 665k drug-like molecules extracted from ChEMBL.

#### 🎯 Background
**Limitations of existing infrastructure**
- Existing QM datasets such as QM9 are limited to small molecules (nine heavy atoms or fewer), providing insufficient coverage of drug-like molecules
- Absence of a large-scale collection that includes quantum-mechanical property data related to bioactivity
**Why this system is needed**
- Training data needed for developing ML models of QM properties for drug-like molecule sizes (MW 250-700)
- Support for models that learn from multiple levels of theory (semi-empirical + DFT)

#### 🔨 Architecture
Biologically and pharmacologically relevant molecules are extracted from the ChEMBL DB. Geometry optimization and thermodynamic data are computed using the GFN2-xTB semi-empirical method. Atomic and molecular properties are additionally computed at the DFT (ωB97X-D/def2-SVP) level. DFT density matrices and orbital matrices are also included.

#### 📥 Access
| Method | Description |
|---|---|
| ETH Zurich data repository | DOI:10.3929/ethz-b-000482129 |

#### 📤 Data formats
- Optimized molecular geometries (xyz)
- Atomic properties (GFN2-xTB and DFT levels)
- Molecular properties (dipole moment, polarizability, etc.)
- DFT density and orbital matrices

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Number of molecules | 665k+ |
| Number of conformers | ~2M |
| Source DB | ChEMBL |

#### ⚠️ Limitations
- Due to computational cost, large molecules (MW>700) are not included
- Some data, such as DFT density matrices, have very large file sizes, leading to high storage requirements

## Related links
- **Paper**: [QMugs, quantum mechanical properties of drug-like molecules](https://doi.org/10.1038/s41597-022-01390-7)
