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

> CVPR 2024 (pp. 12289–12301) | Benchmark + Method | medical (ophthalmology)
> Luo, Shi, Khan, Afzal, Huang, Yuan, Tian, Song, Kouhana, Elze, Fang, Wang
> Massachusetts Eye and Ear / Harvard Medical School
> DBLP: `conf/cvpr/Luo0KA0Y0SKE0024`

## 한 줄 요약
하버드 의대 안과에서 수집한 SLO 안저 이미지 **10,000장** + 임상 노트로 구성된 **Harvard-FairVLMed** 데이터셋과, 이를 기반으로 인구통계학적 공정성을 개선하는 **FairCLIP** 방법론을 함께 제안. 녹내장(Glaucoma) 분류에서 6개 보호 속성의 공정성을 측정·개선.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 수집
  Massachusetts Eye and Ear (Harvard Medical School), 2015–2022
  SLO(Scanning Laser Ophthalmoscopy) 안저 이미지 + 임상 노트 수집
  총 10,000명 환자 기록 (각 환자 1건)

Step 2 — 레이블 생성 (녹내장 진단 기준)
  시야 검사(Visual Field, VF) 결과 기반:
  ┌─ 정상(Non-glaucoma): VF mean deviation ≥ -1 dB, 정상 결과
  └─ 녹내장(Glaucoma):   VF mean deviation < -3 dB, 비정상 결과

Step 3 — 임상 노트 비식별화 (3단계)
  1) Microsoft Presidio 자동 익명화 (민감정보 → placeholder)
  2) 미탐지 보호정보 대상 규칙 기반 매칭
  3) 4명의 의학 전문가 수동 검증

Step 4 — 보호 속성 수집
  ┌─ Race: Asian / Black / White
  ├─ Gender: Female / Male
  ├─ Ethnicity: Non-Hispanic / Hispanic / Unspecified
  ├─ Preferred Language: English / Spanish / Other / Unknown
  ├─ Marital Status: Married / Single / Divorced / Widowed / Other
  └─ Age: mean 60.9 ± 16.2세

Step 5 — 데이터 분할
  ┌──────────┬──────────┐
  │ Train    │  7,000   │
  │ Val      │  1,000   │
  │ Test     │  2,000   │
  │ 합계     │ 10,000   │
  └──────────┴──────────┘
```

---

## SLO 안저 촬영이란?

**SLO (Scanning Laser Ophthalmoscopy)**: 레이저를 이용해 망막을 고해상도로 스캔하는 안과 촬영법. 녹내장의 시신경 손상(optic nerve damage)과 망막 신경섬유층(RNFL) 이상을 평가하는 데 활용됨.

임상 노트: 11–332단어 (평균 147단어), 시각 소견 기반 진단·치료 계획 포함.

---

## 보호 속성 분포

| 속성 | 그룹 | 비율/건수 |
|---|---|---|
| Race | Asian | 819명 |
| | Black | 1,491명 |
| | White | 7,690명 |
| Gender | Female | 56.3% |
| | Male | 43.7% |
| Ethnicity | Non-Hispanic | 90.6% |
| | Hispanic | 4.0% |
| Language | English | 92.5% |
| | Spanish | 1.7% |
| Marital | Married/Partnered | 57.4% |
| | Single | 26.4% |

---

## 평가 메트릭 정의

| 메트릭 | 방향 | 설명 |
|---|---|---|
| **AUC** | ↑ 높을수록 좋음 | 전체 진단 성능 (ROC 곡선 아래 면적) |
| **ES-AUC** | ↑ 높을수록 좋음 | `AUC / (1 + Σ\|AUC - AUCₐ\|)` — 공정성 반영 AUC |
| **DPD** | ↓ 낮을수록 좋음 | Demographic Parity Difference (예측 격차) |
| **DEOdds** | ↓ 낮을수록 좋음 | Difference in Equalized Odds (기회 균등 격차) |

---

## 주요 평가 결과 (Zero-shot, ViT-B/16)

**Race 속성 기준:**
| 모델 | DPD ↓ | DEOdds ↓ | AUC ↑ | ES-AUC ↑ |
|---|---|---|---|---|
| CLIP | 15.35 ± 6.50 | 15.11 ± 5.01 | 67.84 ± 0.90 | 61.67 ± 0.63 |
| **FairCLIP** | **6.07 ± 2.44** | **10.50 ± 2.73** | **70.24 ± 1.26** | **65.50 ± 2.60** |

**Gender 속성 기준:**
| 모델 | DPD ↓ | DEOdds ↓ | AUC ↑ | ES-AUC ↑ |
|---|---|---|---|---|
| CLIP | 4.34 ± 0.66 | 9.95 ± 0.64 | 67.84 | 63.21 |
| **FairCLIP** | **0.84 ± 0.25** | **2.97 ± 2.07** | **69.76** | **65.39** |

Race 기준 DPD: 15.35 → 6.07 (60% 개선), DEOdds: 15.11 → 10.50

---

## 한계점
- 단일 기관(Massachusetts Eye and Ear) 데이터 → 지역·인구 편향 가능
- White 환자 비율 76.9%로 불균형
- 녹내장 진단에 특화 → 타 안과 질환 일반화 미검증
- SLO 이미지에 한정 (OCT, fundus photography 등 미포함)

---

## 관련 정보
- **논문 (CVPR 2024)**: [arXiv:2403.19949](https://arxiv.org/abs/2403.19949)
- **CVPR Open Access**: [OpenCVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Luo_FairCLIP_Harnessing_Fairness_in_Vision-Language_Learning_CVPR_2024_paper.html)
- **GitHub**: [Harvard-Ophthalmology-AI-Lab/FairCLIP](https://github.com/Harvard-Ophthalmology-AI-Lab/FairCLIP)
- **데이터셋**: [Harvard-FairVLMed10K](https://ophai.hms.harvard.edu/datasets/harvard-fairvlmed10k)
