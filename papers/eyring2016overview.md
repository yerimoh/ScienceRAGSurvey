---
title: "Overview of the Coupled Model Intercomparison Project Phase 6 (CMIP6) Experimental Design and Organization"
bib_key: "eyring2016overview"
year: 2016
domain: earth, climate
type: dataset
venue: Geoscientific Model Development
paper_link: https://doi.org/10.5194/gmd-9-1937-2016
---
# Overview of the Coupled Model Intercomparison Project Phase 6 (CMIP6) Experimental Design and Organization

eyring2016overview | 2016 | Geoscientific Model Development | dataset | [earth, climate] | [paper](https://doi.org/10.5194/gmd-9-1937-2016)

**DB**: CMIP6 — Coupled Model Intercomparison Project Phase 6
**DB size**: Petabyte-scale; ~20 PB or more (49 modeling groups worldwide, 100+ climate models; volume is an estimate after actual production)
**DB Open/Private**: Open (publicly distributed via ESGF)
**Modality**: ['NetCDF', 'Simulation output', 'Time series']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: CMIP6 / ESGF (Earth System Grid Federation)

> Geoscientific Model Development | 2016 | dataset | earth, climate
#### TL;DR
A paper on the CMIP6 design and organization that coordinates and integrates Earth System Model (ESM) simulations from climate modeling groups worldwide. It publicly distributes **petabyte-scale** climate simulation data—the scientific basis for the IPCC Sixth Assessment Report (AR6)—via ESGF. It defines standard protocols for simulations of past, present, and future climate scenarios.

#### Background
**Limitations of existing infrastructure**
- CMIP1–5 used individual experimental designs, making inter-model comparison difficult and coverage uneven
- Increasing complexity of Earth System Models after CMIP5 (coupling of carbon cycle, aerosols, ocean biogeochemistry)
- A single-model ensemble cannot distinguish internal variability from model uncertainty

**Why this system is needed**
- A multi-model ensemble standard is needed to establish the scientific basis for IPCC AR6
- Systematic experimental design to answer policy-relevant questions such as detection and attribution of climate change causes, regional impact assessment, and carbon budget estimation
- Integrated coordination of 18 Model Intercomparison Projects (MIPs) such as ScenarioMIP (SSP pathways), HighResMIP, and AerChemMIP

#### Architecture
CMIP6 is led by the WCRP (World Climate Research Programme) and consists of three tiers:
1. **DECK (Diagnostic, Evaluation and Characterization of Klima)**: 4 standard experiments (piControl, historical, AMIP, abrupt4×CO₂) — mandatory for all participating models
2. **Historical simulations**: observation-based forcings for 1850–2014
3. **Optional MIPs**: 21 CMIP6-Endorsed MIPs (ScenarioMIP, HighResMIP, PMIP, AerChemMIP, etc.)

Data distribution: ESGF (Earth System Grid Federation) — a distributed federated archive operating nodes worldwide.

#### Access
| Method | Description |
|---|---|
| ESGF portal | esgf-node.llnl.gov, etc. — web browsing and download |
| ESMValTool | Python-based diagnostic and analysis tool |
| Pangeo | cloud-based access in Zarr format (Google Cloud, AWS) |
| intake-esm | Python catalog-based search |

#### Data formats
- NetCDF-4 (CF Conventions)
- Variables: atmosphere (300+), ocean, sea ice, land, aerosols, carbon cycle
- Temporal resolution: sub-daily to monthly to annual averages
- Spatial resolution: 25km–200km (varies by model)

#### Key statistics
| Item | Value |
|---|---|
| Participating modeling groups | **~49** (worldwide) |
| Number of models | **100+** ESM/GCM |
| Total data volume | **~20 PB** or more (estimated) |
| Number of MIPs | **21** (CMIP6-Endorsed MIPs, confirmed in the paper) |
| DECK experiments | **4** (mandatory) |
| Supported IPCC report | AR6 (2021) |

#### Limitations
- Limited model resolution: mostly around 100km, insufficient for simulating extreme weather events and regional climate (partly addressed in HighResMIP)
- Data volume is very large, making local download by ordinary researchers impractical → cloud-based analysis needed
- Difficult to use directly in a RAG pipeline without domain knowledge of the NetCDF/CF conventions
- Non-uniform variable names and grids across models → standardization processing required

## Related links
- **Paper**: [https://doi.org/10.5194/gmd-9-1937-2016](https://doi.org/10.5194/gmd-9-1937-2016)
- **ESGF portal**: [https://esgf-node.llnl.gov/projects/cmip6/](https://esgf-node.llnl.gov/projects/cmip6/)
