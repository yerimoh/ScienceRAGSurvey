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

## 한 줄 요약
하버드 의대 안과에서 수집한 **SLO 안저(fundus) 이미지 10,000장 + 임상 노트 10,000건**(녹내장 진단)을 6가지 보호 속성(인종/성별/민족/언어/혼인상태/연령)으로 라벨링한 최초의 **fair medical vision-language 데이터셋(Harvard-FairVLMed)**. 더불어 Sinkhorn 거리 기반 최적전송으로 인구통계학적 격차를 완화하는 **FairCLIP** 방법론을 함께 제안.

## 제작 배경
**문제 인식 (Abstract 발췌)**
> "Fairness is a critical concern in deep learning, especially in healthcare, where these models influence diagnoses and treatment decisions. Although fairness has been investigated in the vision-only domain, the fairness of medical vision-language (VL) models remains unexplored due to the scarcity of medical VL datasets for studying fairness."

기존 vision-only fairness 데이터셋(Fitzpatrick17k, HAM10000, ODIR-2019, PAPILA 등)은 모두 텍스트가 없어 VL 모델 fairness 평가 불가. CheXpert/MIMIC-CXR/PadChest는 텍스트가 있으나 인구통계 속성이 *age, gender* 정도로 한정. **Harvard-FairVLMed는 fundus image + clinical note + 6개 protected attribute**를 모두 갖춘 최초 사례.

**의학적 배경**: 녹내장은 망막 신경섬유층(RNFL) 손상으로 인한 시야 결손이 진행되는 질환. 인종(Black), 성별(Female), 연령(고령)에 따라 유병률이 크게 다른 것으로 알려져 — fairness 측정에 적합한 도메인.

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Cohort 수집 (Massachusetts Eye and Ear, Harvard)
  10,000 환자, 환자당 1건 SLO fundus image + 1건 clinical note
  Visual Field (VF) test로 진단 ground truth 생성:
    ┌─ Non-glaucoma: VF mean deviation ≥ -1 dB,
    │                 정상 VF glaucoma hemifield test, 정상 PSD
    └─ Glaucoma:     VF mean deviation < -3 dB,
                     비정상 VF glaucoma hemifield test, 비정상 PSD

Step 2 — 임상 노트 비식별화 (3-stage)
  Stage 1: Microsoft Presidio 자동 익명화 → PHI를 placeholder 치환
  Stage 2: 규칙 기반 매칭으로 Presidio 미탐지 PHI(physical address 등) 추가 제거
  Stage 3: 4명의 의학 전문가가 수동 검증
  결과: 노트 길이 11–332 words, 평균 147 words

Step 3 — 6개 protected attribute 수집
  Race        : Asian (819) / Black (1,491) / White (7,690)
  Gender      : Female 56.3% / Male 43.7%
  Ethnicity   : Non-Hispanic 90.6% / Hispanic 4.0% / Unspecified 5.4%
  Language    : English 92.5% / Spanish 1.7% / Other 0.8% / Unknown 5.0%
  Marital     : Married/Partnered 57.4% / Single 26.4% / others
  Age         : mean 60.9 ± 16.2 years

Step 4 — 데이터 분할
  Train  7,000 | Val 1,000 | Test 2,000

Step 5 — 평가 메트릭 정의
  AUC        ↑ ROC 곡선 아래 면적 (전체 진단 성능)
  ES-AUC     ↑ Equity-Scaled AUC = AUC / (1 + Σ|AUC-AUCₐ|)
  DPD        ↓ Demographic Parity Difference
  DEOdds     ↓ Difference in Equalized Odds
  Group-wise AUC: 각 subgroup별 AUC
```

**FairCLIP 알고리즘 핵심** (논문 §4 발췌)
> "This is achieved by minimizing the disparity between the probability distributions of M_{i,i}, which represents the correlation between visual and language features, across different racial groups (or other attribute-)..."
- batch 내 visual-text similarity score `M_{i,i}`의 분포를 protected attribute별로 정렬
- 전체 분포 vs. group 분포의 **Sinkhorn distance** 최소화 (CLIP loss + Sinkhorn regularizer)

## Input (입력 / 데이터셋 구성)

**기존 fairness 데이터셋과의 비교 (Table 1)**
| 데이터셋 | 모달리티 | 이미지 | 환자 | 속성 | 텍스트 |
|---|---|---:|---:|---|---|
| Fitzpatrick17k | Skin Photos | 16,012 | 1,373 | Skin type | ✗ |
| HAM10000 | Dermatoscopy | 9,948 | – | Age; Gender | ✗ |
| ODIR-2019 | Color Fundus | 8,000 | 5,000 | Age; Gender | ✗ |
| PAPILA | Color Fundus | 488 | 244 | Age; Gender | ✗ |
| Harvard-GDP | OCT | 1,000 | 1,000 | Age; Gender; Race; Ethnicity | ✗ |
| CheXpert | CXR + Report | 222,793 | 65,240 | Age; Gender; Race | ✓ (Description) |
| MIMIC-CXR | CXR + Report | 370,955 | 65,079 | Age; Gender; Race | ✓ (Description) |
| **Harvard-FairVLMed** | **SLO Fundus + Note** | **10,000** | **10,000** | **6개 속성** | **✓ (Description + Non-Imaging Clinical Info)** |

**임상 노트 길이 분포 (Fig 4a, 부록)**: 11–332 words, **평균 147 words**

## Output (Task & 평가 지표)

**Primary task**: glaucoma vs non-glaucoma binary classification (zero-shot or linear-probing on VL model)
**Secondary**: 6개 보호 속성별 공정성 측정

| 지표 | 방향 | 정의 |
|---|---|---|
| AUC | ↑ | 전체 진단 성능 |
| ES-AUC | ↑ | `AUC / (1 + Σ\|AUC - AUC_a\|)` — 공정성 보정 AUC |
| DPD | ↓ | Demographic Parity Difference |
| DEOdds | ↓ | Difference in Equalized Odds |
| Group-wise AUC | – | subgroup별 AUC (Asian/Black/White, Female/Male 등) |

## 예시 사례 (논문 Figure 1 원문 직접 인용)

논문 Figure 1은 **non-glaucoma 환자와 glaucoma 환자 각각에 대한 SLO fundus image + clinical note** 쌍을 제시한다. 비식별화 후 노트의 실제 텍스트:

### 🔬 Non-Glaucoma 사례 (Figure 1, 좌측)
> **SLO Fundus Image** + Clinical Note:
> > "Attending targets maintaining IOP ≤ 18 mmHg in both eyes without glaucoma meds, prescribes artificial tears, schedules follow-up for comprehensive eye evaluation, and confirms the accuracy of the scribe's notes."

→ 이 환자는 안압(IOP, intraocular pressure)이 ≤ 18 mmHg로 정상 범위, 녹내장 약물 미투여, 인공 누액만 처방 → **non-glaucoma**.

### 🔬 Glaucoma 사례 (Figure 1, 우측)
> **SLO Fundus Image** + Clinical Note:
> > "Suspected disc damage in right eye due to inflammation, not clearly progressive glaucoma; treatment for damage prevention ongoing; patient stable on Timolol with follow-up appointments scheduled."

→ 시신경 디스크 손상 의심, Timolol(β-blocker, IOP-lowering)로 안정화 중 → **glaucoma 카테고리** (VF mean deviation < -3 dB).

### 🧬 진단 기준 (논문 본문 발췌)
> "The subjects are categorized into non-glaucoma (visual function measured by visual field (VF) test is normal: VF mean deviation ≥ -1 dB and normal VF glaucoma hemifield test and pattern standard deviation (PSD) results) and glaucoma categories (visual function measured by VF test is abnormal: VF mean deviation < -3 dB and abnormal VF glaucoma hemifield test and PSD results)."

### 🧑‍⚕️ 데이터셋 다양성 (논문 §3 발췌)
> "Harvard-FairVLMed contains records for 10,000 patients, each paired with an SLO fundus image and a clinical note for diagnosing Glaucoma, along with fine-grained protected attributes such as age, gender, race, ethnicity, preferred language, and marital status."

> "Gender-wise, females constitute 56.3% of the subjects, with the remainder being males. The ethnic distribution is highlighted by 90.6% Non-Hispanic, 4.0% Hispanic, and 5.4% unspecified. In terms of preferred language, 92.5% of the subjects prefer English, 1.7% prefer Spanish, 0.8% prefer other languages, and 5.0% remain unknown."

## 주요 평가 결과

### Zero-shot Fairness 분석 (Table 2 발췌, 4가지 VL 모델 × 4가지 속성, linear probing)

**Race 속성 — pre-training이 fairness에 미치는 영향:**
| 모델 | DPD ↓ | DEOdds ↓ | AUC ↑ | ES-AUC ↑ | Asian | Black | White |
|---|---:|---:|---:|---:|---:|---:|---:|
| CLIP | 5.30 ± 0.63 | 14.00 ± 1.01 | 77.27 | 72.43 | 79.74 | 73.60 | 77.82 |
| CLIP-FT (FairVLMed로 finetune) | 4.01 ± 0.47 | 9.57 ± 0.83 | 80.27 | 74.70 | 82.19 | 75.67 | 81.20 |
| BLIP2 | 9.44 ± 0.65 | 10.62 ± 0.22 | 73.81 | 68.88 | 76.28 | 69.55 | 74.22 |
| BLIP2-FT | 8.30 ± 0.36 | 10.91 ± 0.32 | 80.10 | 73.81 | 82.09 | 74.43 | 80.97 |

→ **Asian 그룹이 모든 모델에서 가장 높은 진단 성능**, Black 그룹이 가장 낮음.

### FairCLIP 방법론의 효과 (Table 3 발췌, ViT-B/16 기준, zero-shot)

**Race 속성:**
| 모델 | DPD ↓ | DEOdds ↓ | AUC ↑ | ES-AUC ↑ |
|---|---:|---:|---:|---:|
| CLIP (ViT-B/16) | 15.35 ± 6.50 | 15.11 ± 5.01 | 67.84 ± 0.90 | 61.67 ± 0.63 |
| **FairCLIP (ViT-B/16)** | **6.07 ± 2.44** | **10.50 ± 2.73** | **70.24 ± 1.26** | **65.50 ± 2.60** |
| CLIP (ViT-L/14) | 10.10 ± 9.44 | 10.79 ± 10.41 | 67.83 ± 2.92 | 63.53 ± 1.83 |
| FairCLIP (ViT-L/14) | 17.79 ± 4.86 | 18.30 ± 2.07 | 69.88 ± 2.00 | 66.54 ± 1.73 |

→ ViT-B/16에서 DPD **60% 감소** (15.35 → 6.07), DEOdds **30% 감소**, AUC와 ES-AUC 모두 향상.

**Gender 속성:**
| 모델 | DPD ↓ | DEOdds ↓ | AUC ↑ | ES-AUC ↑ |
|---|---:|---:|---:|---:|
| CLIP (ViT-B/16) | 4.34 ± 0.66 | 9.95 ± 0.64 | 67.84 ± 0.90 | 63.21 ± 0.83 |
| **FairCLIP (ViT-B/16)** | **0.84 ± 0.25** | **2.97 ± 2.07** | **69.76 ± 2.49** | **65.39 ± 2.39** |

→ DPD **80% 감소** (4.34 → 0.84), DEOdds **70% 감소**.

### 핵심 발견 (논문 §5.2 발췌)
> "In terms of racial subgroups, Asian patients consistently have the highest diagnostic performance, whereas Black patients have the lowest. Across genders, male patients are consistently better diagnosed than female patients."
>
> "non-Hispanic patients make up 90.6% of our dataset, potentially leading to improved performance in this subgroup. However, this is unlikely to be the only factor responsible for these performance disparities since the Asian, Male, and Spanish subgroups exhibit superior performances despite being the minority subgroups. This indicates that the pre-training of these models could potentially play a role in the biases exhibited by these models."

## 한계점
- **단일 기관**(Massachusetts Eye and Ear) → 지역·인구 편향 가능. 다국가/다기관 검증 필요.
- **인종 분포 불균형**: White 76.9% vs Black 14.9% vs Asian 8.2% — 절대 수의 부족이 fairness 측정 분산 증가의 원인.
- **녹내장 진단에 특화** — 당뇨망막병증·황반변성 등 타 안과 질환 일반화 미검증.
- **SLO 이미지에 한정** (Color fundus, OCT, fundus photography 등 미포함) — 다중 모달리티 ophthalmology fairness는 후속 과제.
- **임상 노트가 짧음** (평균 147 words) — 환자 history나 가족력 등 풍부한 컨텍스트 부재 → 일부 진단 단서는 노트에 없을 수 있음.
- **FairCLIP가 모든 속성에서 일관되게 개선되지 않음** — Race/Gender는 명확히 개선되나 Ethnicity/Language에서는 DPD 증가하는 경우 존재 (Table 3).

## 관련 정보
- **논문 (CVPR 2024)**: [arXiv:2403.19949](https://arxiv.org/abs/2403.19949)
- **CVPR Open Access**: [openaccess.thecvf.com/.../FairCLIP](https://openaccess.thecvf.com/content/CVPR2024/html/Luo_FairCLIP_Harnessing_Fairness_in_Vision-Language_Learning_CVPR_2024_paper.html)
- **GitHub**: [Harvard-Ophthalmology-AI-Lab/FairCLIP](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP)
- **데이터셋**: [Harvard-FairVLMed10K](https://ophai.hms.harvard.edu/datasets/harvard-fairvlmed10k)
- **Presidio 비식별화 도구**: [github.com/microsoft/presidio](https://github.com/microsoft/presidio)
- **이 데이터셋을 사용한 후속 RAG 연구**: medical VL fairness benchmarks의 시드 데이터셋으로 활용
