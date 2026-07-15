---
title: "Quantum chemistry structures and properties of 134 kilo molecules"
bib_key: "ramakrishnan2014quantum"
year: 2014
domain: chem
type: dataset
venue: Scientific Data
paper_link: https://doi.org/10.1038/sdata.2014.22
---
# Quantum chemistry structures and properties of 134 kilo molecules

ramakrishnan2014quantum | 2014 | Scientific Data | dataset | [chem] | [paper](https://doi.org/10.1038/sdata.2014.22)

**DB**: QM9
**DB size**: 133,885 stable small organic molecules (GDB-17 subset with up to 9 heavy atoms)
**DB Open/Private**: Open
**Modality**: ['Structured']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: QM9 (DFT/B3LYP/6-31G(2df,p) computed results)

> Scientific Data | 2014 | dataset | chem
#### 📌 TL;DR
QM9 is a standard quantum-chemistry benchmark dataset providing B3LYP/6-31G(2df,p)-level geometric structures, energies, and electronic and thermodynamic properties for 133,885 organic molecules with up to 9 heavy atoms drawn from the GDB-17 chemical space.

#### 🎯 Background
**Limitations of existing infrastructure**
- No computational dataset existed for systematically exploring chemical space, which grows combinatorially with molecular size
- Absence of a consistent, large-scale dataset for developing hybrid QM/ML methods and analyzing structure-property relationships
**Why this system is needed**
- Need for a standard benchmark to train and validate machine-learning potentials and molecular-property prediction models
- Systematic computational exploration of chemical space for drug discovery and materials design

#### 🔨 Architecture
A 134k subset of molecules composed of the elements C, H, O, N, and F with up to 9 heavy atoms is extracted from the GDB-17 chemical-space database. After PM7 geometry optimization, structures are re-optimized at the B3LYP/6-31G(2df,p) level. Atomization energies, enthalpies, and free energies, dipole moments, polarizabilities, frontier-orbital eigenvalues, and more are computed. G4MP2-level calculations are additionally performed for the 6,095 isomers of the chemical formula C7H10O2.

#### 📥 Access
| Method | Description |
|---|---|
| Public repository | Data download provided via figshare / original authors |
| QM9 format | xyz-format molecular structures + property files |

#### 📤 Data formats
- xyz-format 3D geometric structures
- Scalar properties (energy, enthalpy, free energy, dipole moment, polarizability)
- Vibrational frequencies
- HOMO/LUMO energies and gap

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Number of molecules (total extracted) | 133,885 |
| Number of chemical formulae | 621 stoichiometries |
| Formula with most isomers | C7H10O2 (6,095) |
| Level of theory | DFT/B3LYP/6-31G(2df,p) |

#### ⚠️ Limitations
- Includes only the elements C, H, O, N, and F (excludes S, Br, Cl, I, and metals)
- Includes only small molecules with up to 9 heavy atoms, limiting coverage of drug-like molecules (MW>250)
- 3,054 of the 134k molecules failed geometric-consistency validation

## Related links
- **Paper**: [Quantum chemistry structures and properties of 134 kilo molecules](https://doi.org/10.1038/sdata.2014.22)
