---
title: MIMIC-CXR - A De-identified Publicly Available Database of Chest Radiographs with Free-text Reports
bib_key: PhysioNet-mimic-cxr-2.1.0
year: 2019
domain: medical
type: benchmark
venue: Scientific Data (Nature) + PhysioNet
paper_link: https://physionet.org/content/mimic-cxr/2.1.0/
---
# MIMIC-CXR v2.1.0

> Scientific Data 2019 + PhysioNet | Benchmark Dataset | medical (radiology)
> Johnson et al. — Beth Israel Deaconess Medical Center / MIT

## 한 줄 요약
Beth Israel Deaconess Medical Center(2011–2016) 응급실의 흉부 X-ray **377,110장** + 방사선과 리포트 **227,835건**을 HIPAA Safe Harbor 규정에 맞게 비식별화하여 공개한 대규모 방사선 영상 데이터셋. 자동 보고서 생성·임상 NLP·RAG 평가의 표준 벤치마크.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 수집
  병원 PACS(Picture Archiving and Communication System)에서 DICOM 이미지 추출
  EHR에서 방사선과 리포트 추출 (2011–2016, BIDMC 응급실)

Step 2 — DICOM 이미지 비식별화
  ┌─ RSNA Clinical Trials Processor (DICOM 헤더)
  └─ OCR (tesseract v3.05.02) → burned-in 텍스트 PHI 블랙박스 처리
  날짜: 2100–2200년대로 시프트
  환자 ID: 10M–19M 범위 난수 재배정
  수동 검토: 6,900장 검증, PHI 0건

Step 3 — 리포트 비식별화
  규칙 기반 + 신경망 혼합 → PHI를 "___" 대체
  검증: 9,770/9,778 PHI 토큰 탐지 (99.99% 정확도)

Step 4 — 이미지 포맷 변환
  DICOM → JPEG (quality 95, histogram equalization)
  원본 임상 해상도 보존 (리사이즈 없음)

Step 5 — NLP 레이블 추출 (14개)
  CheXpert + NegBio 앙상블로 리포트 자유 텍스트 분석
  ┌──────────────────────────────────────────┐
  │ 1. No Finding    8. Pneumonia            │
  │ 2. Enlarged Cardiomediastinum  9. Atelectasis   │
  │ 3. Cardiomegaly  10. Pneumothorax        │
  │ 4. Lung Lesion   11. Pleural Effusion    │
  │ 5. Lung Opacity  12. Pleural Other       │
  │ 6. Edema         13. Fracture            │
  │ 7. Consolidation 14. Support Devices     │
  └──────────────────────────────────────────┘
  각 레이블 상태: Positive / Negative / Uncertain / Disagreement

Step 6 — 최종 공개 (PhysioNet v2.1.0)
  IRB 면제 승인 후 PhysioNet을 통해 공개
```

---

## 데이터셋 통계

| 항목 | 수치 |
|---|---|
| 총 이미지 | 377,110장 |
| 영상 연구(study) | 227,835건 |
| 고유 환자 수 | 65,379명 |
| 수집 기간 | 2011–2016 |
| 기관 | Beth Israel Deaconess Medical Center |

**촬영 뷰 분포:**
| 뷰 | 비율 |
|---|---|
| PA + Lateral (정면+측면) | 65.94% |
| Portable AP (침상 촬영) | 33.49% |
| 특수 촬영 | 0.57% |

**분할:**
| 분할 | 이미지 수 | 환자 수 |
|---|---|---|
| Train | 368,960 | 64,586 |
| Validation | 2,991 | 500 |
| Test | 5,159 | 293 |

---

## 리포트 형식 예시 (실제 비식별화 예시)

```
FINAL REPORT

EXAMINATION: CHEST (PA AND LAT)
INDICATION: ___ year old woman with ?pleural effusion // ?pleural effusion
TECHNIQUE: Chest PA and lateral
COMPARISON: ___

FINDINGS:
Cardiac size cannot be evaluated. Large left pleural effusion is new.
Small right effusion is new. The upper lungs are clear. Right lower lobe
opacities are better seen in prior CT. There is no pneumothorax.

IMPRESSION:
Large left and small right pleural effusions, new.
```

리포트 구조: **Indication → Technique → Comparison → Findings → Impression**
`___` = 비식별화로 제거된 정보 (환자 나이, 날짜, 이름 등)

---

## RAG 평가 벤치마크로서의 활용

| 태스크 | 평가 메트릭 |
|---|---|
| 자동 방사선 보고서 생성 | BLEU, ROUGE, CIDEr, METEOR (NLP) + 임상 정확도 메트릭 |
| 비정상 흉부 이미지 분류 | AUC, F1 (14개 레이블) |
| 멀티모달 RAG 검색 | Retrieval P/R/nDCG |

대표 RAG 시스템: CEMRAG (개념 강화 멀티모달 RAG), LaB-RAG (레이블 부스팅 RAG)

---

## 한계점
- 단일 기관(BIDMC) 데이터 → 일반화 편향 가능
- 흉부 X-ray에 한정 (CT, MRI 미포함)
- 레이블이 NLP 자동 추출 → 전문가 수동 검증 아님

---

## 관련 정보
- **PhysioNet**: [mimic-cxr v2.1.0](https://physionet.org/content/mimic-cxr/2.1.0/)
- **논문 (Scientific Data)**: [doi:10.1038/s41597-019-0322-0](https://doi.org/10.1038/s41597-019-0322-0)
- **GitHub**: [MIT-LCP/mimic-cxr](https://github.com/MIT-LCP/mimic-cxr)
- **이 데이터셋을 사용한 RAG 논문**: IU-Xray와 함께 방사선 보고서 생성 RAG의 표준 쌍
