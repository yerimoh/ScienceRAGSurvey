---
title: "Review of Particle Physics"
bib_key: "navas2024review"
year: 2024
domain: physics
type: dataset
venue: Physical Review D
paper_link: https://doi.org/10.1103/PhysRevD.110.030001
---
# Review of Particle Physics

navas2024review | 2024 | Physical Review D | dataset | [physics] | [paper](https://doi.org/10.1103/PhysRevD.110.030001)

**DB**: Review of Particle Physics (RPP) — Particle Data Group (PDG)
**DB size**: 2,717 new measurements from 869 papers (as of the 2024 edition); includes 120 reviews, organized in 2 volumes
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (knowledge-source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PDG data access: pdg.lbl.gov

> Physical Review D | 2024 | dataset | physics
#### 📌 TL;DR
Published biennially by the Particle Data Group, this is the standard reference handbook of particle physics. It evaluates, averages, and summarizes the measured properties of gauge bosons, the Higgs boson, leptons, quarks, mesons, and baryons, and is the single most cited reference work in high-energy physics.

#### 🎯 Background
**Limitations of existing infrastructure**
- Particle physics is structured such that dozens of experimental groups worldwide independently measure the same particle properties
- Centralized curation that evaluates and averages individual measurements in a consistent manner is needed
- There was no comprehensive reference integrating accelerator experiment results with cosmology and astrophysics data

**Why this system is needed**
- Provides standard average values including measurement uncertainties, establishing a common reference point for researchers worldwide
- Also integrates and includes results of hypothetical-particle searches (supersymmetric particles, neutrino masses, dark matter)
- Provides theory reviews (Higgs boson physics, supersymmetry, grand unified theories, neutrino mixing, etc.) merged with experimental data

#### 🔨 Architecture
The PDG is an international collaboration led by Lawrence Berkeley National Laboratory (LBNL) with the participation of particle physicists worldwide. Every 2 years (in odd-numbered years), it collects and evaluates the latest measurement data to compute world-average values of physical quantities and their uncertainties. The 2024 edition (Physical Review D 110, 030001) consists of the Summary Tables (Volume 1) and the Particle Listings plus additional reviews (Volume 2).

#### 📥 Access
| Method | Description |
|---|---|
| Website | pdg.lbl.gov — online data tables, particle summaries |
| PDF/print | Published in Physical Review D (open access) |
| Data files | Supports download of structured data files |

#### 📤 Data formats
- Particle property summary tables (mass, lifetime, decay branching ratios, magnetic moment, etc.)
- Lists of measured values (individual measurements per experiment + weighted average)
- More than 120 review articles (theoretical and experimental topics)
- Overviews of accelerator and detector technology
- Reviews of statistical and probabilistic methodology

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| New measurements in the 2024 edition | **2,717** (based on 869 papers) |
| Number of reviews included | **120** (most updated) |
| Volume organization | **2 volumes** (Volume 1: Summary Tables + 97 reviews; Volume 2: Particle Listings + 23 reviews) |
| Publication cycle | Biennial (even years: electronic edition update; odd years: full publication) |
| Journal | Physical Review D vol.110, no.3 (2024) |

#### ⚠️ Limitations
- As a curated reference handbook, it provides secondary averaged data rather than primary measurement papers
- The biennial publication cycle introduces a time lag in reflecting the latest experimental results
- The averaging methodology (PDG scaling factor, etc.) is standard, but context of individual measurements may be lost
- In text-centric RAG, the intermixing of formulas and units makes automatic parsing difficult

## Related links
- **Paper**: [Review of Particle Physics (Phys. Rev. D 110, 030001, 2024)](https://doi.org/10.1103/PhysRevD.110.030001)
- **PDG website**: [pdg.lbl.gov](https://pdg.lbl.gov)
