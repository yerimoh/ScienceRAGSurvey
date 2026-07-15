---
title: "An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics"
bib_key: "liu2018integrated"
year: 2018
domain: medical, bio
type: dataset
venue: Cell
paper_link: https://doi.org/10.1016/j.cell.2018.02.052
---
# An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics

liu2018integrated | 2018 | Cell | dataset | [medical, bio] | [paper](https://doi.org/10.1016/j.cell.2018.02.052)

**DB**: TCGA-CDR (The Cancer Genome Atlas Pan-Cancer Clinical Data Resource)
**DB size**: More than 11,000 human tumors, 33 cancer types
**DB Open/Private**: Open (NCI GDC portal)
**Modality**: Genomic, Structured Table (clinical/survival data, multi-platform molecular profiles)
**Retriever**: N/A (knowledge source infrastructure)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: TCGA-CDR / NCI GDC portal

> Cell | 2018 | dataset | medical, bio

#### 📌 TL;DR
Over roughly a decade, this work builds the TCGA Pan-Cancer Clinical Data Resource (TCGA-CDR), which collects clinicopathologic annotations and multi-platform molecular profiles for more than 11,000 patients across 33 cancer types, and defines standardized survival outcome analysis endpoints (OS, PFI, DFI, DSS).

#### 🎯 Background
**Limitations of existing infrastructure**
- TCGA clinical data were separated by cancer type, lacking standardization
- Survival analysis endpoint definitions were inconsistent across cancer types, making comparative studies difficult
- No standardized resource integrated multi-omics data with clinical outcomes

**Why this system is needed**
- A standardized resource is needed for large-scale correlation analysis between genomic features and clinical outcomes
- Consistent analysis is needed based on 4 standard survival endpoints (OS/PFI/DFI/DSS)

#### 🔨 Architecture
Integrates clinicopathologic annotations and multi-platform molecular profiles for more than 11,000 patients across 33 cancer types, collected by the TCGA program over roughly a decade. TCGA-CDR includes 4 major clinical outcome endpoints (overall survival [OS], progression-free interval [PFI], disease-free interval [DFI], disease-specific survival [DSS]). Uses Cox proportional hazards regression models and Kaplan-Meier survival curves. Validated against independent cancer genomics studies.

#### 📥 Access
| Method | Description |
|---|---|
| NCI GDC portal | https://portal.gdc.cancer.gov — free public access |
| Cell paper supplement | https://doi.org/10.1016/j.cell.2018.02.052 (Table S1) |

#### 📤 Data formats
- Standardized clinical data tables (CSV/Excel)
- Survival outcome endpoints (OS, PFI, DFI, DSS)
- Multi-platform molecular profiles (mRNA, miRNA, CNV, methylation, protein)

#### 📊 Key statistics (per the paper)
| Item | Value |
|---|---|
| Total patients/tumors | **More than 11,000** |
| Number of cancer types | **33** |
| Data collection period | **Approximately 10 years** |
| Number of survival endpoints | **4 (OS, PFI, DFI, DSS)** |

#### ⚠️ Limitations
- For some cancer types, certain endpoints (e.g., DFI) have incomplete data
- Heterogeneity of treatment protocols due to the long collection period
- Underrepresentation of certain cancer types (e.g., pediatric cancers)

## Related links
- **Paper**: [An integrated TCGA pan-cancer clinical data resource to drive high-quality survival outcome analytics](https://doi.org/10.1016/j.cell.2018.02.052)
