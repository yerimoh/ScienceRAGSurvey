---
title: FairCLIP - Harnessing Fairness in Vision-Language Learning
bib_key: luo2024fairclip
year: 2024
domain: medical
type: benchmark
venue: CVPR 2024
paper_link: https://arxiv.org/abs/2403.19949
---
# FairCLIP / Harvard-FairVLMed

> CVPR 2024 (pp. 12289–12301) | Benchmark Dataset + Method | medical (ophthalmology)
> Luo, Shi, Khan, Afzal, Huang, Yuan, Tian, Song, Kouhana, Elze, Fang, Wang
> Harvard Ophthalmology AI Lab (Massachusetts Eye and Ear / Harvard Medical School) + NYU
> DBLP: `conf/cvpr/Luo0KA0Y0SKE0024` · arXiv:2403.19949

## TL;DR
The first **fair medical vision-language dataset (Harvard-FairVLMed)**, consisting of **10,000 SLO fundus images + 10,000 clinical notes** (glaucoma diagnosis) collected at the Harvard Medical School ophthalmology department, labeled with 6 protected attributes (race/gender/ethnicity/language/marital status/age). In addition, it proposes the **FairCLIP** methodology, which mitigates demographic disparities via Sinkhorn-distance-based optimal transport.

## Background
**Problem statement (excerpt from Abstract)**
> "Fairness is a critical concern in deep learning, especially in healthcare, where these models influence diagnoses and treatment decisions. Although fairness has been investigated in the vision-only domain, the fairness of medical vision-language (VL) models remains unexplored due to the scarcity of medical VL datasets for studying fairness."

Existing vision-only fairness datasets (Fitzpatrick17k, HAM10000, ODIR-2019, PAPILA, etc.) all lack text, making VL model fairness evaluation impossible. CheXpert/MIMIC-CXR/PadChest do have text, but their demographic attributes are limited to roughly *age, gender*. **Harvard-FairVLMed is the first case that has all of fundus image + clinical note + 6 protected attributes.**

**Medical background**: Glaucoma is a disease in which visual field defects progress due to damage to the retinal nerve fiber layer (RNFL). Its prevalence is known to vary greatly by race (Black), gender (Female), and age (elderly) — making it a domain well suited for measuring fairness.

## Construction Methodology

```
Step 1 — Cohort collection (Massachusetts Eye and Ear, Harvard)
  10,000 patients, 1 SLO fundus image + 1 clinical note per patient
  Diagnostic ground truth generated via Visual Field (VF) test:
    ┌─ Non-glaucoma: VF mean deviation ≥ -1 dB,
    │                 normal VF glaucoma hemifield test, normal PSD
    └─ Glaucoma:     VF mean deviation < -3 dB,
                     abnormal VF glaucoma hemifield test, abnormal PSD

Step 2 — De-identification of clinical notes (3-stage)
  Stage 1: Microsoft Presidio automatic anonymization → replace PHI with placeholders
  Stage 2: Rule-based matching to further remove PHI (physical address, etc.) missed by Presidio
  Stage 3: Manual verification by 4 medical experts
  Result: note length 11–332 words, average 147 words

Step 3 — Collection of 6 protected attributes
  Race        : Asian (819) / Black (1,491) / White (7,690)
  Gender      : Female 56.3% / Male 43.7%
  Ethnicity   : Non-Hispanic 90.6% / Hispanic 4.0% / Unspecified 5.4%
  Language    : English 92.5% / Spanish 1.7% / Other 0.8% / Unknown 5.0%
  Marital     : Married/Partnered 57.4% / Single 26.4% / others
  Age         : mean 60.9 ± 16.2 years

Step 4 — Data split
  Train  7,000 | Val 1,000 | Test 2,000

Step 5 — Definition of evaluation metrics
  AUC        ↑ area under the ROC curve (overall diagnostic performance)
  ES-AUC     ↑ Equity-Scaled AUC = AUC / (1 + Σ|AUC-AUCₐ|)
  DPD        ↓ Demographic Parity Difference
  DEOdds     ↓ Difference in Equalized Odds
  Group-wise AUC: AUC per subgroup
```

**Core of the FairCLIP algorithm** (excerpt from paper §4)
> "This is achieved by minimizing the disparity between the probability distributions of M_{i,i}, which represents the correlation between visual and language features, across different racial groups (or other attribute-)..."
- Align the distribution of the in-batch visual-text similarity scores `M_{i,i}` by protected attribute
- Minimize the **Sinkhorn distance** between the overall distribution and the group distribution (CLIP loss + Sinkhorn regularizer)

## Input (input / dataset composition)

**Comparison with existing fairness datasets (Table 1)**
| Dataset | Modality | Images | Patients | Attributes | Text |
|---|---|---:|---:|---|---|
| Fitzpatrick17k | Skin Photos | 16,012 | 1,373 | Skin type | ✗ |
| HAM10000 | Dermatoscopy | 9,948 | – | Age; Gender | ✗ |
| ODIR-2019 | Color Fundus | 8,000 | 5,000 | Age; Gender | ✗ |
| PAPILA | Color Fundus | 488 | 244 | Age; Gender | ✗ |
| Harvard-GDP | OCT | 1,000 | 1,000 | Age; Gender; Race; Ethnicity | ✗ |
| CheXpert | CXR + Report | 222,793 | 65,240 | Age; Gender; Race | ✓ (Description) |
| MIMIC-CXR | CXR + Report | 370,955 | 65,079 | Age; Gender; Race | ✓ (Description) |
| **Harvard-FairVLMed** | **SLO Fundus + Note** | **10,000** | **10,000** | **6 attributes** | **✓ (Description + Non-Imaging Clinical Info)** |

**Clinical note length distribution (Fig 4a, appendix)**: 11–332 words, **average 147 words**

## Output (Task & evaluation metrics)

**Primary task**: glaucoma vs non-glaucoma binary classification (zero-shot or linear-probing on VL model)
**Secondary**: fairness measurement per each of the 6 protected attributes

| Metric | Direction | Definition |
|---|---|---|
| AUC | ↑ | overall diagnostic performance |
| ES-AUC | ↑ | `AUC / (1 + Σ\|AUC - AUC_a\|)` — fairness-adjusted AUC |
| DPD | ↓ | Demographic Parity Difference |
| DEOdds | ↓ | Difference in Equalized Odds |
| Group-wise AUC | – | AUC per subgroup (Asian/Black/White, Female/Male, etc.) |

## Example cases (direct quotation from paper Figure 1)

Figure 1 of the paper presents pairs of **SLO fundus image + clinical note for a non-glaucoma patient and a glaucoma patient, respectively**. The actual text of the notes after de-identification:

### 🔬 Non-Glaucoma case (Figure 1, left)
> **SLO Fundus Image** + Clinical Note:
> > "Attending targets maintaining IOP ≤ 18 mmHg in both eyes without glaucoma meds, prescribes artificial tears, schedules follow-up for comprehensive eye evaluation, and confirms the accuracy of the scribe's notes."

→ This patient has intraocular pressure (IOP) within the normal range at ≤ 18 mmHg, no glaucoma medication, and only artificial tears prescribed → **non-glaucoma**.

### 🔬 Glaucoma case (Figure 1, right)
> **SLO Fundus Image** + Clinical Note:
> > "Suspected disc damage in right eye due to inflammation, not clearly progressive glaucoma; treatment for damage prevention ongoing; patient stable on Timolol with follow-up appointments scheduled."

→ Suspected optic nerve disc damage, being stabilized with Timolol (β-blocker, IOP-lowering) → **glaucoma category** (VF mean deviation < -3 dB).

### 🧬 Diagnostic criteria (excerpt from paper body)
> "The subjects are categorized into non-glaucoma (visual function measured by visual field (VF) test is normal: VF mean deviation ≥ -1 dB and normal VF glaucoma hemifield test and pattern standard deviation (PSD) results) and glaucoma categories (visual function measured by VF test is abnormal: VF mean deviation < -3 dB and abnormal VF glaucoma hemifield test and PSD results)."

### 🧑‍⚕️ Dataset diversity (excerpt from paper §3)
> "Harvard-FairVLMed contains records for 10,000 patients, each paired with an SLO fundus image and a clinical note for diagnosing Glaucoma, along with fine-grained protected attributes such as age, gender, race, ethnicity, preferred language, and marital status."

> "Gender-wise, females constitute 56.3% of the subjects, with the remainder being males. The ethnic distribution is highlighted by 90.6% Non-Hispanic, 4.0% Hispanic, and 5.4% unspecified. In terms of preferred language, 92.5% of the subjects prefer English, 1.7% prefer Spanish, 0.8% prefer other languages, and 5.0% remain unknown."

## Key evaluation results

### Zero-shot Fairness analysis (excerpt from Table 2, 4 VL models × 4 attributes, linear probing)

**Race attribute — the impact of pre-training on fairness:**
| Model | DPD ↓ | DEOdds ↓ | AUC ↑ | ES-AUC ↑ | Asian | Black | White |
|---|---:|---:|---:|---:|---:|---:|---:|
| CLIP | 5.30 ± 0.63 | 14.00 ± 1.01 | 77.27 | 72.43 | 79.74 | 73.60 | 77.82 |
| CLIP-FT (finetuned on FairVLMed) | 4.01 ± 0.47 | 9.57 ± 0.83 | 80.27 | 74.70 | 82.19 | 75.67 | 81.20 |
| BLIP2 | 9.44 ± 0.65 | 10.62 ± 0.22 | 73.81 | 68.88 | 76.28 | 69.55 | 74.22 |
| BLIP2-FT | 8.30 ± 0.36 | 10.91 ± 0.32 | 80.10 | 73.81 | 82.09 | 74.43 | 80.97 |

→ **The Asian group has the highest diagnostic performance across all models**, and the Black group the lowest.

### Effect of the FairCLIP methodology (excerpt from Table 3, ViT-B/16 basis, zero-shot)

**Race attribute:**
| Model | DPD ↓ | DEOdds ↓ | AUC ↑ | ES-AUC ↑ |
|---|---:|---:|---:|---:|
| CLIP (ViT-B/16) | 15.35 ± 6.50 | 15.11 ± 5.01 | 67.84 ± 0.90 | 61.67 ± 0.63 |
| **FairCLIP (ViT-B/16)** | **6.07 ± 2.44** | **10.50 ± 2.73** | **70.24 ± 1.26** | **65.50 ± 2.60** |
| CLIP (ViT-L/14) | 10.10 ± 9.44 | 10.79 ± 10.41 | 67.83 ± 2.92 | 63.53 ± 1.83 |
| FairCLIP (ViT-L/14) | 17.79 ± 4.86 | 18.30 ± 2.07 | 69.88 ± 2.00 | 66.54 ± 1.73 |

→ On ViT-B/16, DPD **decreased by 60%** (15.35 → 6.07), DEOdds **decreased by 30%**, and both AUC and ES-AUC improved.

**Gender attribute:**
| Model | DPD ↓ | DEOdds ↓ | AUC ↑ | ES-AUC ↑ |
|---|---:|---:|---:|---:|
| CLIP (ViT-B/16) | 4.34 ± 0.66 | 9.95 ± 0.64 | 67.84 ± 0.90 | 63.21 ± 0.83 |
| **FairCLIP (ViT-B/16)** | **0.84 ± 0.25** | **2.97 ± 2.07** | **69.76 ± 2.49** | **65.39 ± 2.39** |

→ DPD **decreased by 80%** (4.34 → 0.84), DEOdds **decreased by 70%**.

### Key findings (excerpt from paper §5.2)
> "In terms of racial subgroups, Asian patients consistently have the highest diagnostic performance, whereas Black patients have the lowest. Across genders, male patients are consistently better diagnosed than female patients."
>
> "non-Hispanic patients make up 90.6% of our dataset, potentially leading to improved performance in this subgroup. However, this is unlikely to be the only factor responsible for these performance disparities since the Asian, Male, and Spanish subgroups exhibit superior performances despite being the minority subgroups. This indicates that the pre-training of these models could potentially play a role in the biases exhibited by these models."

## Limitations
- **Single institution** (Massachusetts Eye and Ear) → possible regional/demographic bias. Multi-country/multi-institution validation is needed.
- **Racial distribution imbalance**: White 76.9% vs Black 14.9% vs Asian 8.2% — the lack of absolute numbers is a cause of increased variance in fairness measurement.
- **Specialized for glaucoma diagnosis** — generalization to other ophthalmic diseases such as diabetic retinopathy and macular degeneration is unverified.
- **Limited to SLO images** (Color fundus, OCT, fundus photography, etc. not included) — multi-modality ophthalmology fairness is a follow-up task.
- **Clinical notes are short** (average 147 words) — rich context such as patient history or family history is absent → some diagnostic clues may not be in the notes.
- **FairCLIP does not consistently improve across all attributes** — Race/Gender clearly improve, but there are cases where DPD increases for Ethnicity/Language (Table 3).

## Related links
- **Paper (CVPR 2024)**: [arXiv:2403.19949](https://arxiv.org/abs/2403.19949)
- **CVPR Open Access**: [openaccess.thecvf.com/.../FairCLIP](https://openaccess.thecvf.com/content/CVPR2024/html/Luo_FairCLIP_Harnessing_Fairness_in_Vision-Language_Learning_CVPR_2024_paper.html)
- **GitHub**: [Harvard-Ophthalmology-AI-Lab/FairCLIP](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP)
- **Dataset**: [Harvard-FairVLMed10K](https://ophai.hms.harvard.edu/datasets/harvard-fairvlmed10k)
- **Presidio de-identification tool**: [github.com/microsoft/presidio](https://github.com/microsoft/presidio)
- **Follow-up RAG research using this dataset**: used as a seed dataset for medical VL fairness benchmarks
