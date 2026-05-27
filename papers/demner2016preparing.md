---
title: Preparing a Collection of Radiology Examinations for Distribution and Retrieval
bib_key: demner2016preparing
year: 2016
domain: medical
type: benchmark
venue: JAMIA (Journal of the American Medical Informatics Association)
paper_link: https://doi.org/10.1093/jamia/ocv080
---
# IU-Xray / Open-i: Indiana University Chest X-ray Collection

> JAMIA 2016 (vol. 23, no. 2, pp. 304–310) | Benchmark Dataset | medical (radiology)
> Demner-Fushman, Kohli, Rosenman, Shooshan, Rodriguez, Antani, Thoma, McDonald — NLM / Indiana University School of Medicine
> DBLP: `journals/jamia/Demner-FushmanK16` · PMID 26133894 · PMC4750497

## 한 줄 요약
인디애나 대학교 병원 시스템에서 수집한 **흉부 X-ray 7,470장 + 방사선과 free-text 리포트 3,955건**을 비식별화·MeSH/RadLex 수동 어노테이션하여 NLM Open-i 플랫폼으로 공개한 최초의 공개 방사선 검사 컬렉션. **MIMIC-CXR와 함께 방사선 보고서 생성·검색 RAG의 표준 평가 쌍**으로 활용된다.

## 제작 배경
**왜 이 데이터셋이 필요했나**
> "Clinical documents made available for secondary use play an increasingly important role in discovery of clinical knowledge, development of research methods, and education. An important step in facilitating secondary use of clinical document collections is easy access to descriptions and samples that represent the content of the collections."

기존 임상 컬렉션의 한계:
- 대부분 텍스트 또는 이미지 **한쪽만** 공개 — 멀티모달 학습 불가
- 소규모이고 i2b2 등 특별 챌린지 참가자에게만 접근 가능
- 과거 공개되었던 코퍼스(예: Bioscope)는 후속 관리 부재로 더 이상 접근 불가
- 한 연구자의 코멘트(논문 인용): *"it would be good to [see] … at least a sample of the documents in the collection to decide if I want to request it."*

**해결책**: 텍스트(리포트) + 이미지(DICOM) + 수동 MeSH 코딩을 묶어 **Open-i 검색 인터페이스**로 즉시 브라우징 가능한 형태로 공개.

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 데이터 수집 (Indiana University Hospitals, IRB 승인 OHSRP# 5357)
  대상: posterior-anterior (PA) chest x-ray 외래 검사
  소스: Indiana Network for Patient Care
  조건: 환자 1인당 1건, Findings/Impression/Indication 섹션 모두 명시
  초기 수집: 4,000 studies → 섹션 누락 4건 제외 = 3,996

Step 2 — 리포트 자동 비식별화 (Regenstrief Scrubber)
  대상: HIPAA identifier + accession number
  결과: 100% precision (수동 검증 시 누락 0건)
  평균 9.5 단어/리포트 제거 (전체 길이 77.1 → 67.6)
    └─ 대부분 footer 또는 날짜 (8단어)
  Findings + Impression 섹션에서는 1단어만 제거 (2.5%)

Step 3 — DICOM 자동 비식별화
  RSNA Clinical Trials Processor + DICOM Supplement 142
  → 헤더에 PHI 없음 (수동 검증 완료)
  픽셀에는 일부 잔존:
    └─ 2/3996 환자 (0.05%)에서 PII 발견 (스캔된 필름 origin)

Step 4 — DICOM 픽셀 수동 검토
  8명의 독립 검토자, 각 이미지를 2명씩 inspect (8,121 이미지 전수)
  검토 기준:
    (a) HIPAA identifier (환자 이름, 병원 번호, 완전 날짜)
    (b) implanted medical device의 식별 코드
    (c) 잠재적 재식별 가능 부위:
        - 턱 윤곽/이빨 (375 환자, 2-3개 인접 어금니로 94.3% 식별 가능)
        - 두개골/얼굴 (18 환자)
        - 보석류 (39 환자)
  pacemaker/defibrillator: 107 환자에서 발견, 67%가 alphanumeric 식별자 노출
    └─ 단, 환자 직접 식별 불가능한 product ID로 판단 — 보존

Step 5 — 최종 필터링
  41 studies (1%) 완전 제거
    └─ HIPAA PII 노출 2 studies + 재식별 위험 이미지 651장
  → 최종 공개: 3,955 리포트 + 7,470 DICOM 이미지

Step 6 — MeSH + RadLex 수동 어노테이션
  코더 2명 (의학정보학 훈련: medical librarian + MD) 독립 코딩
  불일치 시 제3자 (D.D.F., MD) 중재
  2-pass:
    Pass 1: normal / not-normal 분류 (정상 1,526건 = 38%)
    Pass 2: 모든 positive finding을 MeSH 우선, 없으면 RadLex 코드로 부여
  부정·hedging 처리:
    "no nodules or masses" → 미코딩 (음성 단언은 제외)
    "Calcified hilar lymph XXXX" → calcinosis/hilum/lymph nodes (양성)
  결과: 101 MeSH + 76 RadLex codes 사용, 50개 최빈 코드가 68.1% 커버

Step 7 — Lucene + UMLS 동의어 확장 인덱싱
  5개 검색 섹션: Indications / Findings / Impression / Manual codes / MTI codes
  추가로 MTI(Medical Text Indexer) 자동 코딩 병행 (MetaMap + Neg-Ex 음성 필터링)
  Open-i: openi.nlm.nih.gov — 20,000+ 일일 사용자
```

## Input (입력 / 데이터셋 구성)

**기본 통계**
| 항목 | 수치 |
|---|---:|
| 최종 리포트 수 | **3,955건** |
| 최종 DICOM 이미지 수 | **7,470장** |
| 정상(normal) 리포트 | 1,526건 (38%) |
| 비정상(not normal) 리포트 | 2,470건 (62%) |
| 평균 리포트 길이 | 77.1 단어 |
| 평균 Findings+Impression 길이 | 39 단어 |
| MeSH 코드 사용 수 | 101 |
| RadLex 코드 사용 수 | 76 |
| 코딩된 finding 총수 | 6,907 |

**비정상 리포트 Top-10 코드 (Table 1)**
| 코드 | 출처 | 건수 | 비율 |
|---|---|---:|---:|
| Cardiomegaly | MeSH | 375 | 15.1% |
| Pulmonary atelectasis | MeSH | 347 | 14.0% |
| Calcified granuloma | MeSH/RadLex | 284 | 11.5% |
| Aorta/tortuous | MeSH/RadLex | 253 | 10.2% |
| Lung/hypoinflated | MeSH/RadLex | 245 | 9.9% |
| Opacity/lung base | RadLex | 203 | 8.2% |
| Pleural effusion | MeSH | 172 | 6.9% |
| Lung/hyperinflation | MeSH/RadLex | 164 | 6.6% |
| Cicatrix/lung | MeSH | 148 | 5.9% |
| Calcinosis/lung | MeSH | 141 | 5.7% |

## Output (정답/레이블 형식)
**5개 검색 가능 섹션 (Lucene fields)**
1. **Indications** — 검사 사유 (mean 6 words)
2. **Findings** — 영상 관찰 (mean 39 words for findings+impression)
3. **Impression** — 진단 요약
4. **Manual encoding** — 수동 MeSH/RadLex 코드
5. **MTI encoding** — 자동 코드 (MTI + MetaMap + Neg-Ex)

후처리 표현 예: `infiltrate/lung/upper lobe/left` (descriptor + qualifier 결합)

## 예시 사례 (논문 원문 직접 인용)

### 📄 수동 어노테이션 사례 — Impression → MeSH/RadLex 변환 (논문 본문 발췌)
> "any sentence in Findings or Impression that contains this term, for example, 'Impression: left upper lobe infiltrate,' was coded as `infiltrate/lung/upper lobe/left`."
>
> "We coded old findings if they were discussed in the report. For example, we coded 'Calcified hilar lymph XXXX' as `calcinosis/hilum/lymph nodes`."

### 🩺 실제 리포트 발췌 (Figure 1 캡션 — 의도적으로 인용 가능한 실 예시)
> Figure 1 caption: "A sample radiology report with manual and MTI annotations. Terms removed by the automatic text scrubber are replaced with XXXX. 'COPD' in the impression section is annotated with the MeSH term 'Pulmonary Disease, Chronic Obstructive.' 'Scarring' is translated to MeSH term 'Cicatrix.'"
>
> ⇒ 즉 **"COPD" → Pulmonary Disease, Chronic Obstructive** / **"Scarring" → Cicatrix** 동의어 매핑이 수동 코더에 의해 명시되어 retrieval expansion이 가능.

### 🔍 Retrieval 사례 — 검색기준의 한계 (pneumonia 쿼리, Discussion 발췌)
> "Both judges judged the following impression relevant to pneumonia: 'Focal airspace disease in the right middle lobe. This is most concerning for pneumonia,' but the manual annotation had only one code: Airspace Disease/lung/middle lobe/right/focal. Pneumonia is mentioned only once in this report and in the field that has less weight than the manual codes; therefore the report was ranked too low to contribute to the results of text searches with manual annotation."
>
> ⇒ **수동 코딩이 만능이 아님**을 보여주는 케이스 — 본문은 hedging("most concerning for…")으로 표현되었으나 코더는 단정 가능한 finding만 코딩.

### ⚠️ Relevance Judgement 3-point scale 예시
> "We evaluated relevance on a three-point scale: relevant; maybe relevant (e.g., if it is not clear if the patient has atelectasis: 'patchy left lower lobe airspace disease, possibly atelectasis or pneumonia'); and not relevant (e.g., if the impression stated 'no pneumonia')."

## 주요 평가 결과 (Retrieval Experiment, 30 ImageCLEF queries 2008–2013)

**Table 2 발췌** — 30개 쿼리 평균 (841 distinct records retrieved, 쿼리당 2~73건):
| 검색 전략 | Precision@10 | Inferred Avg Precision |
|---|---:|---:|
| Impression + Findings (text only) | 0.370 | 0.393 |
| MTI 자동코드 only | 0.240 | 0.208 |
| MTI 자동코드 + Text | 0.410 | 0.417 |
| Manual codes only | 0.393 | 0.315 |
| **Manual codes + Text** | **0.470*** | **0.536*** |
| Manual + MTI + Text | 0.473* | 0.524* |

`*` = text alone 대비 통계적으로 유의 (Wilcoxon signed-rank). P@10 37→47%, Avg Precision 39.3→53.6%.

**Inter-annotator agreement** (relevance judging on 30 queries):
- 3점 척도 (relevant / maybe relevant / not relevant): **Cohen's κ = 0.85**
- 이진 척도 (relevant vs definitely not): **κ = 0.90**

## 한계점
- **소규모** (3,955건) — MIMIC-CXR(227,835건)에 비해 약 60배 작음. 학습용보단 evaluation/few-shot용에 적합.
- **단일 뷰 유형** (PA + lateral 외래)에 한정.
- **수동 코딩의 일관성 한계**: hedging/uncertainty가 풍부한 방사선 리포트는 코더 간 합의가 어렵고, 예시처럼 *"most concerning for pneumonia"*가 미코딩되는 경우 발생.
- **MeSH/RadLex 어휘 한계**: "thoracic spine"이 MeSH "Thoracic Vertebrae"의 동의어로 등록되어 있지 않아 MTI가 미스. 수동 코더는 식별했으나 자동화는 한계.
- **원 논문 목적은 정보 검색(IR)** — 자동 보고서 생성·RAG는 후속 연구의 적용. 학습용 train/val/test split은 표준 정의 부재.
- **DICOM 비식별화의 픽셀-레벨 잔존 위험**: 0.05% 환자에서 발견된 PII는 모두 *스캔된 필름* 출처 — 동일 파이프라인이 디지털 원생 이미지에서는 안전.

## 관련 정보
- **논문 (JAMIA)**: [doi:10.1093/jamia/ocv080](https://doi.org/10.1093/jamia/ocv080)
- **PMC**: [PMC4750497](https://pmc.ncbi.nlm.nih.gov/articles/PMC4750497/)
- **PubMed**: [PMID 26133894](https://pubmed.ncbi.nlm.nih.gov/26133894/)
- **공개 검색 인터페이스 (Open-i)**: [openi.nlm.nih.gov](https://openi.nlm.nih.gov/)
- **Open-i API**: [openi.nlm.nih.gov/services.php](https://openi.nlm.nih.gov/services.php)
- **원본 DICOM 요청**: [openi.nlm.nih.gov/contactus.php](https://openi.nlm.nih.gov/contactus.php)
- **연관 데이터셋 (MIMIC-CXR)**: Johnson et al. 2019 Sci Data — 방사선 보고서 생성 RAG의 표준 쌍
