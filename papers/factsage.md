---
title: "FactSage: thermochemical software suite"
bib_key: "factsage"
year: 1976
domain: material
type: dataset
venue: GTT-Technologies / CRCT (Commercial Software)
paper_link: https://www.factsage.com
---
# FactSage

factsage | 1976 | GTT-Technologies/CRCT (Commercial Software) | dataset | [material] | [website](https://www.factsage.com)

**DB**: FactSage built-in thermochemical databases (pure-substance FACT-Pure-Substances DB + multicomponent molten-phase solution databases such as FToxid, FTstel, FTsalt)
**DB size**: ~60,000 compounds and numerous multicomponent molten-phase parameter sets (published figures are limited)
**DB Open/Private**: Subscription (commercial license; academic and free basic versions exist)
**Modality**: Tabular
**Retriever**: N/A (K4 commercial simulator — no directly queryable API)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: FactSage (GTT-Technologies / CRCT)

> GTT-Technologies/CRCT | 1976 | dataset | material
#### 📌 TL;DR
A thermochemical software jointly developed and maintained by GTT-Technologies (Germany) and Canada's CRCT (Polytechnique Montréal). It computes CALPHAD-based phase equilibria and Gibbs energy minimization for multicomponent high-temperature reactions in metallurgical, glass, ceramic, and nuclear-fuel processes, and it embeds the most comprehensive thermodynamic databases that the ferrous and non-ferrous metallurgy industries rely on.

#### 🎯 Background
**Limitations of existing thermodynamic computation tools**
- Simple binary and ternary alloy systems can be computed by hand, but multicomponent slag and alloy systems (Fe-Cr-Ni-O-S-...) cannot be computed without a dedicated CALPHAD database
- Pure-component data like JANAF cannot describe the molten-phase behavior of multicomponent mixtures

**FactSage's position**
- The industry standard for CALPHAD methodology: describes the non-ideal solution behavior of molten alloys, slags, and molten salts using models such as the Modified Quasichemical Model (MQM)
- More than 20 dedicated solution databases, including steel (FTstel), oxide slags (FToxid), nuclear fuel (FTnucl), and molten salts (FTsalt)
- The industry standard for steel, aluminum, and copper smelting, glass manufacturing, and predicting reactor nuclear-fuel behavior

#### 🔨 Architecture
- **FACT-Pure-Substances Database**: thermodynamic data for ~60,000 compounds (H, S, Cp, phase-transition enthalpies)
- **Solution Databases**: FToxid (oxides), FTstel (steel), FTsalt (molten salts), FTnucl (nuclear fuel), and others
- **CALPHAD engine**: Gibbs energy minimization-based phase-equilibrium computation (EquiliB, Phase Diagram modules)
- **Process simulation**: reactor simulation (Reaction Web), mixing computation

#### 📥 Access
| Method | Description |
|---|---|
| FactSage GUI | Windows-based modular interface |
| FactSage Web (limited) | Access to basic computations (some features offered free) |
| ChemSheet/Matlab integration | Batch computation via Excel ChemSheet or MATLAB |

#### 📤 Data formats
- Phase-equilibrium results: list of stable phases, compositions (mol%)
- Gibbs energy function values, chemical potentials
- Phase diagrams (binary/ternary/pseudo-binary)
- Physical properties: density, viscosity (in some databases)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| FACT project start | ~1976 (F*A*C*T project) |
| Built-in compound count (Pure-Substances) | ~60,000 |
| Number of solution databases | More than 20 (FToxid, FTstel, FTsalt, etc.) |
| Developing institutions | GTT-Technologies (Germany) + CRCT, Polytechnique Montréal (Canada) |
| Public database size | Not public (commercial license) |

**NOTE**: The `factsage` entry has no bib entry in references.bib (missing citation).

#### ⚠️ Limitations
- The CALPHAD solution databases are based on decades of accumulated experimental data, but the provenance of the parameters is not fully disclosed
- The built-in databases cannot be directly accessed or queried from outside the software (RAG integration is not possible)
- For certain alloy systems or novel materials, validated CALPHAD parameters may be unavailable, which can cause extrapolation errors

## Related links
- **Website**: [FactSage](https://www.factsage.com)
- **K4 classification**: Embedded in software — metallurgical and high-temperature-chemistry tacit knowledge (CALPHAD solution parameters) is embedded in the software's databases
- **BIB status**: No bib entry in references.bib — needs to be added
