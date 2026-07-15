---
title: "The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies"
bib_key: "kirklin2015open"
year: 2015
domain: material
type: dataset
venue: npj Computational Materials
paper_link: https://doi.org/10.1038/npjcompumats.2015.10
---
# The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies

kirklin2015open | 2015 | npj Computational Materials | dataset | [material] | [paper](https://doi.org/10.1038/npjcompumats.2015.10)

**DB**: Open Quantum Materials Database (OQMD)
**DB size**: nearly 300,000 DFT total energy calculations (per the paper)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: OQMD REST API, www.oqmd.org/download

> npj Computational Materials | 2015 | dataset | material
#### 📌 TL;DR
The 2015 expansion report of OQMD, containing roughly 300,000 DFT total energy calculations, systematically assesses DFT accuracy through the largest-scale comparison against 1,670 experimental formation energies and predicts ~3,200 new stable compounds.

#### 🎯 Background
**Limitations of existing infrastructure**
- Since the first OQMD report in 2013 (saal2013), the scale has expanded from about 200,000 to 300,000 entries
- Systematic verification of the error characteristics of DFT calculations was lacking, and the largest-scale comparison against experimental values was needed
- A data foundation was needed for large-scale prediction of new stable compounds

**Why this system is needed**
- Releasing the entire database without restriction (www.oqmd.org/download) to maximize its use by the materials science community
- Assessing the practical contribution of DFT error by also analyzing the deviation among experimental measurements

#### 🔨 Architecture
A large-scale DFT (VASP, GGA-PBE) calculation database composed of compounds listed in the ICSD (Inorganic Crystal Structure Database) and element-wise decorations of common crystal structure prototypes. It assesses thermodynamic stability through convex hull analysis and is also used to predict the existence of as-yet-unrealized compounds.

#### 📥 Access
| Method | Description |
|---|---|
| Full download | www.oqmd.org/download — unrestricted and free |
| Web interface | www.oqmd.org — structure and energy queries |
| REST API | programmatic access |

#### 📤 Data formats
- DFT total energies and formation energies (eV/atom)
- Optimized crystal structures (lattice constants, atomic positions)
- Thermodynamic stability (convex hull analysis)
- Predicted compound stability data

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Total number of DFT calculations | **~300,000** (nearly 300,000, per the paper) |
| Compared experimental formation energies | **1,670** (largest DFT vs experiment comparison) |
| Mean absolute error (DFT vs experiment) | **0.096 eV/atom** |
| Deviation among experimental values (MAE) | **0.082 eV/atom** |
| Predicted new stable compounds | **~3,200** (unrealized compounds) |

#### ⚠️ Limitations
- Systematic error of the GGA-PBE functional yields an average error of about 0.1 eV/atom relative to experimental formation energies
- The uncertainty of the experimental measurements themselves (0.082 eV/atom) makes it difficult to separate out the DFT error
- Dynamical stability and finite-temperature effects are not included
- Accuracy limitations for the f-electron series and strongly correlated transition-metal oxides

## Related links
- **Paper**: [The OQMD: assessing the accuracy of DFT formation energies (npj Comput. Mater., 2015)](https://doi.org/10.1038/npjcompumats.2015.10)
