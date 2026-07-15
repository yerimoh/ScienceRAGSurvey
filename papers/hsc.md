---
title: "HSC Chemistry: thermodynamic and metallurgical calculation software"
bib_key: "hsc"
year: 1974
domain: material
type: dataset
venue: Metso Outotec (Outotec) (Commercial Software)
paper_link: https://www.mogroup.com/portfolio/hsc-chemistry/
---
# HSC Chemistry

hsc | ~1974 | Metso Outotec (Commercial Software) | dataset | [material] | [website](https://www.mogroup.com/portfolio/hsc-chemistry/)

**DB**: HSC Chemistry built-in thermodynamic database (standard thermodynamic data such as enthalpy, entropy, and heat capacity for approximately 30,000 chemical species)
**DB size**: ~30,000 chemical species (varies by version, undisclosed exact figures)
**DB Open/Private**: Subscription (commercial license)
**Modality**: Tabular
**Retriever**: N/A (K4 commercial simulator — no directly queryable API)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: HSC Chemistry (Metso Outotec)

> Metso Outotec | ~1974 | dataset | material
#### 📌 TL;DR
A metallurgy-focused thermodynamic calculation software developed by Outotec (now Metso Outotec) that embeds thermodynamic data (H, S, Cp) for approximately 30,000 chemical species to compute mass and energy balances, phase equilibria, and Gibbs energy minimization for high-temperature metallurgical processes (smelting, roasting, leaching).

#### 🎯 Background
**Limitations of conventional metallurgical calculations**
- In smelters and mineral processing operations, predicting the equilibrium products of multicomponent high-temperature reactions is impossible to do by hand
- Manually extracting from individual data tables such as JANAF and NIST-JANAF is time-consuming and prone to errors

**Where HSC Chemistry stands**
- The standard metallurgical thermodynamics tool for non-ferrous metal smelting (copper, nickel, lead, zinc), steelmaking, cement, and inorganic chemistry processes
- Specialized in computing high-temperature (hundreds to thousands of degrees) reaction equilibria and Ellingham diagrams

#### 🔨 Architecture
- **Thermodynamic database**: Embeds H°, S°, and Cp(T) polynomial coefficients for ~30,000 chemical species
- **Gibbs energy minimization**: Automatically computes equilibrium products of multicomponent high-temperature reactions
- **Mass and energy balance**: Computes the mass/energy balance of unit processes
- **Eh-pH diagram**: Generates Pourbaix diagrams
- **HSC Sim**: Process simulation module

#### 📥 Access
| Method | Description |
|---|---|
| HSC Chemistry GUI | Input reactions and view results through a Windows-based interface |
| Database search | Search chemical species and look up property values in the built-in DB |
| Spreadsheet integration | Export results via Excel integration |

#### 📤 Data formats
- Reaction equilibrium product composition (mol%)
- Thermodynamic function values (ΔG, ΔH, ΔS, Keq)
- Ellingham diagram, Pourbaix diagram
- Mass and energy balance tables

#### 📊 Key statistics (as reported)
| Item | Value |
|---|---|
| Number of built-in chemical species | ~30,000 (varies by version) |
| Applicable temperature range | 25°C ~ thousands of °C |
| Developer | Metso Outotec (Finland) |
| Public database size | Undisclosed (commercial license) |

**NOTE**: The `hsc` entry has no bib entry in references.bib (missing citation).

#### ⚠️ Limitations
- The built-in thermodynamic database is encapsulated within the software and cannot be directly accessed or queried by external RAG systems
- Metadata on the provenance of the database (original experimental measurements vs. estimated values) is provided only to a limited extent
- For CALPHAD-level calculations of molten alloy systems, multicomponent molten-solution databases such as FactSage are more suitable

## Related links
- **Website**: [Metso Outotec HSC Chemistry](https://www.mogroup.com/portfolio/hsc-chemistry/)
- **K4 classification**: Embedded in software — metallurgical and high-temperature thermodynamic tacit knowledge (chemical species thermodynamic data) is embedded in the software database
- **BIB status**: No bib entry in references.bib — needs to be added
