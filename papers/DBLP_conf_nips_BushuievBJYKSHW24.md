---
notion_id: 355f2dcd-4912-81e1-a354-c9c3bae54271
title: MassSpecGym - A benchmark for the discovery and identification of molecules
bib_key: DBLP:conf/nips/BushuievBJYKSHW24
year: 2024
domain: chem
type: benchmark
venue: NeurIPS
paper_link: https://proceedings.neurips.cc/paper_files/paper/2024/hash/c6c31413d5c53b7d1c343c1498734b0f-Abstract-Datasets_and_Benchmarks_Track.html
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# MassSpecGym: A benchmark for the discovery and identification of molecules

> NeurIPS | 2024 | Benchmark | chem

## TL;DR
The first comprehensive benchmark for discovering and identifying molecules from MS/MS tandem mass spectrometry data. It includes 231k spectra and 29k molecules, and provides three challenges (de novo generation, molecular retrieval, spectrum simulation) along with a generalization-demanding split (MCES-based split).

## Background
### Limitations of existing benchmarks
- **Absence of a standard dataset**: prior studies each used different, heterogeneous, non-standardized datasets → results cannot be compared
- **Data leakage problem**: existing Random splits place near-identical molecules with Tanimoto similarity > 0.85 in both train and test → overestimation of model performance
- **Inconsistent evaluation protocols**: different studies use different metrics, splits, and candidate sets
- **Accessibility problem**: preprocessing requires MS domain expertise → high barrier to entry for the ML community
- **Dependence on commercial data**: only license-required datasets like NIST exist, making public reproduction impossible

### Why this benchmark was needed
- Discovering and identifying molecules in biological and environmental samples is central to biomedical and chemical science, yet decoding tandem mass spectra into molecular structures is a hard problem even for experts
- The majority of collected MS/MS spectra remain uninterpreted → limiting the understanding of chemical processes
- The absence of a standard dataset and evaluation criteria for developing ML methods is a persistent bottleneck

## How it was built (Construction Methodology)
**Step 1: Selecting data sources**
Integrating three large public spectral libraries:
- **MoNA (MassBank of North America)**: crowdsourced MS/MS library
- **MassBank**: Europe-centered public spectral library
- **GNPS (Global Natural Products Social Molecular Networking)**: natural-product-centered public DB
- **In-house measured spectra**: self-measured novel spectra (10,000-molecule scale)

Reason for selection: integrating the largest and most diverse public data + extending coverage with self-measurement, without commercial dependence.

**Step 2: Construction pipeline**
```
Raw spectrum collection (MoNA + MassBank + GNPS + in-house)
    ↓
[Metadata normalization]
  - Unify field names, fix incorrect fields
  - Fill in missing SMILES/InChI/InChIKey
  - Derive missing parent mass → from SMILES mass
  - Derive missing adduct → from precursor m/z and parent mass
    ↓
[Quality filtering]
  - Remove where parent mass computed from adduct + precursor m/z ≠ SMILES mass
  - Remove monoisotopic mass mismatches
  - Remove charged-molecule annotations
  - Remove merged spectra from the Brungs et al. MS/MS library
    ↓
[SMILES standardization]
  - Remove compounds that fail standardization
  - Unify to InChIKey including isomer information
    ↓
[Intensity normalization]
  - All spectra: normalize to relative intensity values
  - Standardize instrument type and collision energy
```

**Step 3: Quality verification**
- Confirm balance by visualizing the distribution of metadata attributes for each fold
- Spectrum simulation challenge: use only the subset with all metadata present
- Ensure reproducibility with fully public code and data in a public repository
- Automated preprocessing usable even without MS expertise

**Step 4: Dataset composition and release**
- **MCES (Maximum Common Edge Subgraph)-based split**: cluster by edit distance between molecular graphs → block near-duplicate leakage of Tanimoto > 0.85
- Split into Train / Validation / Test 3-fold with StratifiedGroupKFold
- Number of spectra: Train >> Validation > Test (to avoid imbalance)
- GitHub: [https://github.com/pluskal-lab/MassSpecGym](https://github.com/pluskal-lab/MassSpecGym)
- HuggingFace: [https://huggingface.co/datasets/roman-bushuiev/MassSpecGym](https://huggingface.co/datasets/roman-bushuiev/MassSpecGym)

## Input
### Current dataset composition
| Item | Scale |
|---|---|
| Total number of MS/MS spectra | **231,000+** |
| Number of unique molecular structures | **29,000+** |
| Sources | MoNA, MassBank, GNPS + in-house |
| Molecule size | small molecules (< ~1,000 Da) |

### Three challenges
| Challenge | Input | Output | Additional variant |
|---|---|---|---|
| **De novo molecule generation** | MS/MS spectrum | molecular structure (SMILES) | chemical-formula-provided version (bonus) |
| **Molecular retrieval** | MS/MS spectrum | ranked list from candidate DB | chemical-formula-provided version (bonus) |
| **Spectrum simulation** | molecular structure (SMILES) | MS/MS spectrum | chemical-formula-provided version (bonus) |

### Provided fields
| Field name | Description |
|---|---|
| `mzs` | array of m/z values (MS/MS peaks) |
| `intensities` | intensity of each peak (normalized) |
| `smiles` | molecular structure (SMILES format) |
| `inchi` | InChI identifier |
| `inchikey` | InChIKey (isomer included) |
| `precursor_mz` | precursor m/z |
| `adduct` | ionization adduct type |
| `collision_energy` | collision energy |
| `instrument_type` | instrument type |

### Featurization methods (ML benchmark only)
| Method | Principle | Applicable challenge |
|---|---|---|
| **Morgan fingerprint** | represent molecular substructures as a bit vector (2048-bit, radius=2) | molecular retrieval, similarity computation |
| **Tanimoto similarity** | ratio of shared bits between two molecules (0~1). 1 = identical molecule | retrieval accuracy evaluation, structural similarity |
| **MCES distance** | maximum common edge subgraph edit distance | data splitting, de novo generation evaluation |
| **Cosine similarity (spectrum)** | cosine similarity of two MS/MS spectra | spectrum simulation evaluation |

### Splitting method
**MCES-based split (not a Random split)**:
- Cluster molecules by MCES distance (distance_threshold=10)
- StratifiedGroupKFold: molecules within the same cluster are placed in the same fold
- → prevents data leakage where similar molecules with Tanimoto > 0.85 appear in both train and test
- A key contribution resolving the leakage problem of the existing 2D InChIKey-based split

## Output (answer format)
| Challenge | Output form | Main evaluation metrics |
|---|---|---|
| De novo generation | SMILES string | Top-k accuracy, MCES distance, Tanimoto similarity |
| Molecular retrieval | ranked list | Hit rate @ rank k (HR@k), Top-1 Tanimoto similarity |
| Spectrum simulation | m/z + intensity array | Cosine similarity, Top-1 retrieval accuracy |

### List of benchmarked models
| Model | Type | Brief description |
|---|---|---|
| **FraGNNet** | GNN (fragmentation DAG) | ICEBERG-based fragmentation graph neural network, spectrum simulation SOTA (31.93%) |
| **ICEBERG** | GNN (fragmentation DAG) | Goldman et al., 57.8% cosine similarity, forward spectrum simulation SOTA |
| **MIST** | Transformer | retrieval via molecular fingerprint prediction; further performance gain when using chemical-formula annotations |
| **CSI:FingerID** | SVM / fingerprint | traditional MS/MS retrieval method, fingerprint-based |
| **DiffMS** | Diffusion + MIST | structure generation via graph diffusion after fingerprint prediction; de novo top-1 2.30% |
| **MARASON** | GNN + Neural Graph Matching | Wang et al. 2025, spectrum simulation 34.03% (+6%) |
| **MassSpecGym baseline** | Transformer | baseline provided by the paper itself, 0% top-1 accuracy on de novo generation |

## Example questions (by challenge)
**[Type 1: Spectrum simulation]**
- Input: molecular structure C₉H₁₁NO₂ (e.g., SMILES of a dopamine derivative)
- Task: predict the MS/MS spectrum (m/z, intensity array)
- Evaluation: cosine similarity between the predicted spectrum vs. the measured spectrum

**[Type 2: Molecular retrieval]**
- Input: measured MS/MS spectrum (m/z=178.0, intensity pattern)
- Task: rank the correct molecular structure from a 29k candidate molecule DB
- Evaluation: HR@1, HR@5, HR@10

**[Type 3: De novo molecule generation]**
- Input: measured MS/MS spectrum + (bonus: chemical formula C₁₀H₁₃NO)
- Task: generate a molecular SMILES from the spectrum alone
- Evaluation: predicted SMILES's 2D InChIKey == ground-truth InChIKey

## Main evaluation results
### Spectrum simulation (Top-1 retrieval accuracy)
| Model | Top-1 acc | Note |
|---|---|---|
| MassSpecGym baseline | ~0% | Transformer baseline |
| FraGNNet | 31.93% | previous SOTA |
| **MARASON** (Wang et al. 2025) | **34.03%** | +6% relative improvement |
| ICEBERG | 57.8% cosine sim | chemical-formula-information-using version |

### De novo molecule generation (Top-1 accuracy)
| Model | Top-1 acc | Note |
|---|---|---|
| Baseline Transformer | 0% | paper's default baseline |
| DiffMS (Bohde et al. 2025) | 2.30% | current Diffusion-based SOTA |

## Limitations
- **Small-molecule bias**: centered on small molecules (< ~1,000 Da) due to the nature of public MS libraries
- **Positive-ion-mode bias**: over-representation of positive ionization adducts such as [M+H]⁺
- **Instrument heterogeneity**: diverse instruments and collision-energy settings affect spectral patterns
- **De novo generation difficulty**: even the current best-performing model reaches only 2.30% → practical use is far off
- **Isomer discrimination limits**: cases exist where MS/MS cannot distinguish stereoisomers of the same 2D structure

## Related links
- **Original paper link (NeurIPS 2024 official)**: [https://proceedings.neurips.cc/paper_files/paper/2024/hash/c6c31413d5c53b7d1c343c1498734b0f-Abstract-Datasets_and_Benchmarks_Track.html](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c6c31413d5c53b7d1c343c1498734b0f-Abstract-Datasets_and_Benchmarks_Track.html)
- **arXiv**: [https://arxiv.org/abs/2410.23326](https://arxiv.org/abs/2410.23326)
- **GitHub**: [https://github.com/pluskal-lab/MassSpecGym](https://github.com/pluskal-lab/MassSpecGym)
- **HuggingFace**: [https://huggingface.co/datasets/roman-bushuiev/MassSpecGym](https://huggingface.co/datasets/roman-bushuiev/MassSpecGym)
- **RAG paper using this benchmark**: Wang, Wang, Manjrekar, Coley (2025) — MARASON, ICML 2025
