---
title: Preparing a Collection of Radiology Examinations for Distribution and Retrieval
bib_key: demner2016preparing
year: 2016
domain: medical
type: benchmark
venue: JAMIA (Journal of the American Medical Informatics Association)
paper_link: https://doi.org/10.1093/jamia/ocv080
---
# IU-Xray: Indiana University Chest X-ray Collection

> JAMIA 2016 | Benchmark Dataset | medical (radiology)
> Demner-Fushman et al. — National Library of Medicine / Indiana University
> DBLP: `journals/jamia/Demner-FushmanK16`

## 한 줄 요약
인디애나 대학교 병원 시스템에서 수집한 흉부 X-ray **7,470장** + 방사선과 리포트 **3,955건**을 비식별화·어노테이션하여 공개한 데이터셋. MIMIC-CXR와 함께 **방사선 보고서 생성 RAG의 표준 쌍**으로 활용된다.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 수집
  인디애나 네트워크 환자 케어(Indiana Network for Patient Care)
  2개 병원 시스템에서 흉부 X-ray + 리포트 수집
  조건: 환자 1인당 1건, PA + lateral 뷰, 외래 검사만

Step 2 — 리포트 선별 기준
  Indication / Findings / Impression 세 섹션 명시 필수
  → 4,000건 수집, 4건 제외 → 3,996건

Step 3 — 텍스트 비식별화
  도구: Regenstrief Scrubber (100% precision)
  평균 9.5단어/리포트 제거 (주로 날짜, 리포트 footer)
  임상 섹션(Findings/Impression): 리포트당 ~1단어 제거 (2.5%)

Step 4 — DICOM 이미지 비식별화
  도구: RSNA Clinical Trials Processor
       + DICOM Supplement 142 방법론
  8명의 독립 검토자가 헤더 + 이미지 8,121장 전수 검사
  제거 기준: HIPAA 식별자, 치아/두개골/턱/귀금속 노출

Step 5 — 최종 필터링
  ┌─ 41건 완전 제거 (HIPAA 식별자 포함 4장 + 재식별 가능 이미지 651장)
  └─ 최종: 3,955 리포트 + 7,470 DICOM 이미지

Step 6 — 수동 어노테이션
  2명의 코더가 독립 코딩 → 불일치 시 제3자 중재
  ┌─ MeSH 코드 101개
  └─ RadLex 코드 76개
  + MTI(Medical Text Indexer) 자동 코딩 병행

Step 7 — Open-i 플랫폼 공개
  Lucene 검색 엔진 (UMLS 동의어 확장 포함)
  5개 검색 섹션: Indication / Findings / Impression / 수동코드 / MTI코드
```

---

## 데이터셋 통계

| 항목 | 수치 |
|---|---|
| 최종 리포트 수 | 3,955건 |
| 최종 DICOM 이미지 수 | 7,470장 |
| 정상 검사 | 1,526건 (38%) |
| 비정상 검사 | 2,470건 (62%) |
| 평균 리포트 길이 | 77.1 단어 |
| MeSH 코드 | 101개 |
| RadLex 코드 | 76개 |

**상위 10개 어노테이션 코드 (비정상 리포트 기준):**
| 소견 | 건수 | 비율 |
|---|---|---|
| Cardiomegaly | 375 | 15.1% |
| Pulmonary atelectasis | 347 | 14.0% |
| Calcified granuloma | 284 | 11.5% |
| Tortuous aorta | 253 | 10.2% |
| Lung hypoinflation | 245 | 9.9% |
| Lung base opacity | 203 | 8.2% |
| Pleural effusion | 172 | 6.9% |
| Lung hyperinflation | 164 | 6.6% |
| Cicatrix/lung | 148 | 5.9% |
| Calcinosis/lung | 141 | 5.7% |

---

## 리포트 형식 예시

**소견(Findings) 예시:**
> "left upper lobe infiltrate" → MeSH: infiltrate/lung/upper lobe/left

**인상(Impression) 예시:**
> "Focal airspace disease in the right middle lobe. This is most concerning for pneumonia"

리포트 구조: **Indications → Findings → Impression**

---

## 검색(Retrieval) 평가 결과

30개 ImageCLEF 쿼리(2008–2013) 기준:

| 검색 전략 | Precision@10 | Avg Precision |
|---|---|---|
| 텍스트만 | 0.370 | 0.393 |
| MTI 자동코드만 | 0.240 | 0.208 |
| 수동코드만 | 0.393 | 0.315 |
| **수동코드 + 텍스트** | **0.470** | **0.536** |

수동 코딩 + 텍스트 조합이 텍스트 단독 대비 유의미하게 우수 (P≤.05 precision; P≤.01 avg precision)
Inter-rater agreement: Cohen's κ = 0.85 (3점 척도) / κ = 0.90 (이진 척도)

---

## 한계점
- 소규모 (3,955건) — MIMIC-CXR(227,835건)에 비해 소용량
- 단일 뷰 유형(PA + lateral) 위주
- 리포트가 영어 기반 임상 약어·헤징 표현 풍부 → NLP 난이도 높음
- 원 논문 목적은 정보 검색(IR) — 보고서 생성 RAG는 후속 연구의 적용

---

## 관련 정보
- **논문 (JAMIA)**: [doi:10.1093/jamia/ocv080](https://doi.org/10.1093/jamia/ocv080)
- **PMC**: [PMC5009925](https://pmc.ncbi.nlm.nih.gov/articles/PMC5009925/)
- **데이터셋 (Open-i)**: [openi.nlm.nih.gov](https://openi.nlm.nih.gov/)
- **이 데이터셋을 사용한 RAG 논문**: MIMIC-CXR와 함께 방사선 보고서 생성 RAG 표준 벤치마크
