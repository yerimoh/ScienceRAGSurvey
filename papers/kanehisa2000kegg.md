---
title: "KEGG: kyoto encyclopedia of genes and genomes"
bib_key: "kanehisa2000kegg"
year: 2000
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/28.1.27
---
# KEGG: kyoto encyclopedia of genes and genomes

kanehisa2000kegg | 2000 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/28.1.27)

**DB**: KEGG (Kyoto Encyclopedia of Genes and Genomes)
**DB size**: 3 core databases (GENES, PATHWAY, LIGAND) — a gene catalog of all completely sequenced genomes as of the paper
**DB Open/Private**: Open (freely available)
**Modality**: ['Text']
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: KEGG API / FTP (http://www.genome.ad.jp/kegg/)

> Nucleic Acids Research | 2000 | dataset | bio
#### 📌 TL;DR
A bioinformatics knowledge base that links genomic information with higher-order functional information, composed of three databases: GENES (gene catalog), PATHWAY (cellular pathways), and LIGAND (chemical compounds and enzyme reactions).

#### 🎯 Background
**Limitations of existing infrastructure**
- Genome sequencing projects produce large volumes of gene sequences, but a systematic means of linking them to cell-level functions was lacking
- An integrated database was needed to bridge the gap between sequence information and higher-order functional information such as metabolic pathways and signal transduction

**Why this system is needed**
- Supports systematic analysis that links genes of completely sequenced genomes to functional pathways
- Enables comparative analysis of functionally conserved cross-species pathways (pathway motifs) and prediction of gene function
- Supports genome map exploration, comparative genome analysis, and expression map browsing through Java-based visualization tools

#### 🔨 Architecture
KEGG is composed of three core databases: (1) **GENES** — a gene catalog of all completely sequenced genomes, updated daily, (2) **PATHWAY** — graphical representations of cellular processes such as metabolism, membrane transport, signal transduction, and the cell cycle, (3) **LIGAND** — information on chemical compounds, enzyme molecules, and enzyme reactions. Conserved subpathway (pathway motif) information is provided as ortholog group tables.

#### 📥 Access
| Method | Description |
|---|---|
| Web interface | http://www.genome.ad.jp/kegg/ — free browser access |
| Java tools | Genome map exploration, genome comparison, expression map manipulation |
| FTP | Full dataset download |

#### 📤 Data formats
- Gene catalog (GENES database)
- Pathway graphical representations (PATHWAY database)
- Compound, enzyme, and reaction information (LIGAND database)
- Ortholog group tables (pathway motifs)

#### 📊 Key statistics (as reported in the paper)
| Item | Value |
|---|---|
| Genomes included | All completely sequenced genomes + some partial genomes |
| Data updates | Updated daily |
| Main components | 3 DBs: GENES, PATHWAY, LIGAND |

#### ⚠️ Limitations
- As a foundational paper from 2000, the number of completely sequenced genomes was very small compared to the present
- Cellular pathway information relies on manual curation, which limits how quickly newly discovered pathways are incorporated
- The LIGAND compound database was centered on enzyme reactions at the time, so information on small-molecule drugs was limited

## Related links
- **Paper**: [KEGG: kyoto encyclopedia of genes and genomes](https://doi.org/10.1093/nar/28.1.27)
