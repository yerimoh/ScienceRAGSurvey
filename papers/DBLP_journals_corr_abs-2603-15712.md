---
title: "LLM-Driven Discovery of High-Entropy Catalysts via Retrieval-Augmented Generation"
bib_key: "DBLP:journals/corr/abs-2603-15712"
year: 2026
domain: material
type: Method
venue: arXiv 2026
paper_link: https://arxiv.org/abs/2603.15712
---
# LLM-Driven Discovery of High-Entropy Catalysts via Retrieval-Augmented Generation

DBLP:journals/corr/abs-2603-15712 | 2026 | arXiv 2026 | Method | [material] | [paper](https://arxiv.org/abs/2603.15712)

**Retriever**: RAG over 50,000+ materials database (Materials Project, NOMAD, OC20)
**Eval Task**: CO2 reduction catalyst discovery (thermodynamic stability, cost, band gap, mechanical stability, limiting potential)
**Eval Metric**: Thermodynamic stability rate (%), limiting potential (V), cost ($/kg), volcano plot proximity
**Method Name**: HEA-RAG (LLM-RAG for High-Entropy Catalyst Discovery)
**Modality**: Text, Structured materials data

> arXiv 2026 | 2026 | Method | material
#### 📌 TL;DR
Using a GPT-4-based framework grounded via RAG on a database of 50,000+ known materials, the work generates 250+ high-entropy alloy (HEA) CO2 reduction catalyst candidates, achieving 82% thermodynamic stability and a limiting potential of 0.285V, a 25% improvement over IrO2.

#### 🎯 Background
**Limitations of existing approaches**
- Materials discovery requires development cycles of 10-20 years and demands deep domain expertise
- Conventional high-throughput screening (HTS) incurs excessive computational cost when exploring broad chemical spaces

**Why this system is needed**
- Accelerated exploration of chemical space is needed to develop efficient CO2 reduction catalysts
- A system is needed in which the LLM references materials databases in real time and generates candidates under multi-objective constraints (cost, conductivity, stability)

#### 🔨 Architecture
A vector database of 50,000+ known materials is built by integrating the Materials Project, NOMAD, and Open Catalyst 2020 (OC20) datasets. GPT-4 explores the chemical space via RAG over this database, and candidate stability is verified with DFT (density functional theory) calculations. Volcano plot analysis assesses proximity to the theoretical activity optimum.

#### 📊 Key results
| Item | Value |
|---|---|
| Materials database scale | 50,000+ known materials |
| Number of generated catalyst candidates | 250+ |
| Thermodynamic stability rate | 82% |
| Cost/conductivity/mechanical stability achievement | 68% (<$100/kg, band gap<0.1eV, B/G>1.75) |
| Best-performing alloy | Fe0.2Co0.2Ni0.2Ir0.1Ru0.3, limiting potential 0.285V |
| Improvement over IrO2 | 25% improvement |
| Cost-performance optimal alloy | Cr0.2Fe0.2Co0.3Ni0.2Mo0.1, $18/kg |
| Volcano plot proximity rate | 78% of LLM-generated catalysts |
| Computational efficiency | 200x improvement over conventional HTS |

#### ⚠️ Limitations
- The DFT verification step remains computationally intensive
- The actual synthesizability of the high-entropy alloys includes cases that are not verified
- Being specialized for CO2 reduction limits direct transfer to other catalytic application domains

## Related links
- **Paper (arXiv)**: [https://arxiv.org/abs/2603.15712](https://arxiv.org/abs/2603.15712)
