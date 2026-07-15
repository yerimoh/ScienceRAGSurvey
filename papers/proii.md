---
title: "Pro/II: Process engineering simulation software"
bib_key: "proii"
year: 1967
domain: chem
type: dataset
venue: AVEVA (formerly SimSci) (Commercial Software)
paper_link: https://www.aveva.com
---
# Pro/II

proii | 1967 | AVEVA (formerly SimSci) (Commercial Software) | dataset | [chem] | [website](https://www.aveva.com)

**DB**: Pro/II built-in thermodynamic and physical-property database (SimSci proprietary property package and DIPPR-based)
**DB size**: N/A (licensed software, no public figures)
**DB Open/Private**: Subscription (commercial license)
**Modality**: Tabular
**Retriever**: N/A (K4 commercial simulator — no directly queryable API)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Pro/II (AVEVA, formerly SimSci)

> AVEVA (formerly SimSci) | 1967 | dataset | chem
#### 📌 TL;DR
A chemical and petrochemical process simulator released by SimSci (now AVEVA) in 1967 that encapsulates thermodynamic and unit-operation knowledge specialized for refining and gas-processing processes in a built-in database.

#### 🎯 Background
**Limitations of existing process design**
- As the petrochemical and refining industries scaled up in the 1960s, demand for complex multi-unit process simulation surged
- A steady-state simulator was needed that could simultaneously solve distillation columns, absorption columns, and heat-exchanger networks as systems of simultaneous equations

**Pro/II's position**
- Alongside Aspen Plus, one of the most widely used process simulators for designing refineries, LNG processing facilities, and petrochemical plants
- In particular, it embeds empirical parameters specialized for refining processes (crude oil distillation, FCC, hydrocracking)

#### 🔨 Architecture
- **Thermodynamic package**: numerous equations of state (SRK, PR, CPA, etc.) and activity coefficient models
- **Unit operations**: a comprehensive unit operation library including distillation, absorption, extraction, reaction, compression, and heat exchange
- **Refining-specific models**: crude assay handling, petroleum-fraction property prediction
- **Physical-property database**: SimSci proprietary DB + DIPPR-based pure-component parameters

#### 📥 Access
| Method | Description |
|---|---|
| AVEVA E3D/Pro/II GUI | Interactive process design environment |
| COM/OLE Automation | Simulation control from external scripts (limited) |
| Batch execution | Command-line execution based on .prz files |

#### 📤 Data formats
- Stream composition and thermodynamic state (temperature, pressure, vapor-liquid fractions)
- Unit-operation performance (separation efficiency, energy consumption)
- Process economic evaluation (CAPEX/OPEX estimation)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Initial release | 1967 (SimSci) |
| Current owner | AVEVA (acquired by Schneider Electric in 2017, spun off independent in 2023) |
| Public database size | Undisclosed (commercial license) |

#### ⚠️ Limitations
- Like Aspen Plus, the built-in knowledge is encapsulated within the software and cannot be directly accessed by external RAG systems
- Refining-specific empirical parameters (such as crude assay correlations) are very poorly documented publicly
- Lack of parameters for new biofuel or novel-material processes

## Related links
- **Website**: [AVEVA Pro/II](https://www.aveva.com/en/products/pro-ii/)
- **K4 classification**: Embedded in software — refining and gas-processing tacit knowledge is embedded in the software parameter base
