---
title: "gPROMS: Advanced process modeling software"
bib_key: "gproms"
year: 1990
domain: chem
type: dataset
venue: PSE (Process Systems Enterprise) / Siemens (Commercial Software)
paper_link: https://www.siemens.com/global/en/products/automation/industry-software/gproms.html
---
# gPROMS

gproms | 1990 | PSE/Siemens (Commercial Software) | dataset | [chem] | [website](https://www.siemens.com/global/en/products/automation/industry-software/gproms.html)

**DB**: gPROMS built-in physical-property database (integrates with INFOCHEM Multiflash or CAPE-OPEN-based thermodynamic packages)
**DB size**: N/A (licensed software, no public figures)
**DB Open/Private**: Subscription (commercial license)
**Modality**: Tabular
**Retriever**: N/A (K4 commercial simulator — no directly queryable API)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: gPROMS (PSE/Siemens)

> PSE/Siemens | ~1990 | dataset | chem
#### 📌 TL;DR
An advanced process modeling platform developed by Process Systems Enterprise (PSE, now a Siemens subsidiary). It supports first-principles modeling based on differential-algebraic equations (DAE) and embeds precise thermodynamic and transport-phenomena parameters, making it useful for high-fidelity simulation of battery, pharmaceutical, and refining processes.

#### 🎯 Background
**Limitations of existing process simulators**
- Steady-state simulators such as Aspen Plus and Pro/II center on simplified shortcut models, so their implementation of first-principles dynamic models is limited
- Precise modeling of complex physicochemical phenomena such as pharmaceutical crystallization, battery electrode reactions, and membrane separation requires a DAE-based platform

**gPROMS's positioning**
- "Advanced Process Modeling" domain: supports first-principles modeling at a level of precision one step above Aspen Plus/Pro/II
- An industry standard in battery cell design (gPROMS FormulatedProducts), pharmaceutical processes (gPROMS Pharmaceutical), and LNG liquefaction processes

#### 🔨 Architecture
- **Modeling language**: proprietary DAE-based equation-oriented modeling language (gML)
- **Thermodynamic package**: integrates external physical-property engines such as Multiflash and Aspen Properties through the CAPE-OPEN interface
- **Optimization engine**: built-in model-based optimization (MBO) and parameter estimation capabilities
- **Physical-property database**: phase-equilibrium and transport parameters based on INFOCHEM Multiflash

#### 📥 Access
| Method | Description |
|---|---|
| gPROMS GUI | Model construction and execution based on Process Builder |
| Python API | gPROMS ModelBuilder Python Interface |
| CAPE-OPEN | Integration with other platforms through the standard CAPE-OPEN interface |

#### 📤 Data formats
- Simulation results: state-variable profiles (temporal/spatial distributions)
- Parameter estimation results: kinetic parameters, physical-property parameters
- Optimization reports: design variables and objective-function values

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| First commercial release | ~early 1990s (PSE founded in 1991) |
| Current owner | Siemens AG (acquired PSE in 2019) |
| Public database size | Not disclosed (commercial license) |

**NOTE**: The `gproms` entry has no bib entry in references.bib (missing citation).

#### ⚠️ Limitations
- Building first-principles models requires specialized chemical-engineering knowledge, resulting in a high barrier to entry
- The built-in physical-property database can only be accessed indirectly through the CAPE-OPEN standard and cannot be integrated directly with a RAG system
- In small research-lab settings, the license cost is a burden

## Related links
- **Website**: [Siemens gPROMS](https://www.siemens.com/global/en/products/automation/industry-software/gproms.html)
- **PSE original**: [PSE gPROMS](https://www.psenterprise.com/products/gproms)
- **K4 classification**: Embedded in software — advanced process modeling tacit knowledge (DAE parameters, physical-property correlations) is embedded in the software
- **BIB status**: no bib entry in references.bib — needs to be added
