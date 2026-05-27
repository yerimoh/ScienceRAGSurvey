---
title: MIMIC-CXR - A De-identified Publicly Available Database of Chest Radiographs with Free-text Reports
bib_key: PhysioNet-mimic-cxr-2.1.0
year: 2019
domain: medical
type: benchmark
venue: Scientific Data (Nature) + PhysioNet
paper_link: https://doi.org/10.1038/s41597-019-0322-0
---
# MIMIC-CXR v2.1.0

> Scientific Data (Nature) | 2019 | Benchmark Dataset | medical (radiology)
> Johnson, Pollard, Berkowitz, Greenbaum, Lungren, Deng, Mark, Horng — MIT / Beth Israel Deaconess Medical Center / Stanford / Harvard
> DOI: `10.1038/s41597-019-0322-0` · PhysioNet v2.1.0 (Open-access subset: MIMIC-CXR-JPG)

## 한 줄 요약
Beth Israel Deaconess Medical Center 응급실(2011–2016)에서 수집한 **흉부 X-ray 377,110장 + 방사선과 free-text 리포트 227,835건(고유 환자 65,379명)**을 HIPAA Safe Harbor 규정에 맞게 비식별화하여 공개한 대규모 흉부 영상 데이터셋. 자동 보고서 생성·임상 NLP·멀티모달 RAG 평가의 사실상의 표준 벤치마크.

## 제작 배경
**왜 이 데이터셋이 필요했나**
- 흉부 X-ray는 전 세계에서 가장 빈번한 의료 영상 검사. 그러나 미국 내 방사선 전문의 비율 감소 추세 + 도시-농촌 분포 편향 → 자동 판독 알고리즘 수요 급증.
- 자원이 부족한 지역의 현실:
> "As of 2015, only 11 radiologists served the 12 million people of Rwanda, while the entire country of Liberia, with a population of four million, had only two practicing radiologists."
- 기존 공개 데이터셋(JSRT 247장, ChestX-ray14 112,120장)은 전문의가 작성한 **자유 텍스트 리포트**가 없거나 자동 NLP 레이블만 제공 → 영상-텍스트 멀티모달 학습 불가.
- "A key requirement in the application of these advances to automated chest radiograph analysis is a sufficiently large data set" — MIMIC-CXR는 **이미지 + 리포트 페어**를 대규모로 묶어 공개한 최초 사례.

## 어떻게 만들었나 (Construction Methodology)
**전체 구성**: EHR/PACS 추출 → DICOM 비식별화(헤더 + 픽셀) → 리포트 규칙 기반 PHI 제거 → 수동 검증 → PhysioNet 공개

```
Step 1 — EHR/PACS에서 코호트 구축
  ┌─ BIDMC EHR에 응급실 흉부 X-ray 요청 쿼리 (2011–2016)
  ├─ 환자 식별자만 추출 → 추가로 해당 환자의 흉부 X-ray 전수 추출
  └─ subject_id 재배정: 10,000,000–19,999,999 범위 난수
     study_id 재배정: 50,000,000–59,999,999 범위 난수
     날짜: 환자별 일관된 date shift로 2100–2200년대 매핑
     (계절성 정보는 제거, 환자 내 종단적 시간 관계는 보존)

Step 2 — DICOM 메타데이터 비식별화 (DICOM Standard 2017e)
  Basic Application Level Confidentiality Profile
    + Clean Descriptors Option
    + Retain Longitudinal Temporal Information Modified Dates
    + Clean Pixel Data
    + Clean Graphics
  De-identification: Orthanc v1.0.0 → UUID 기반 새 식별자 생성
  Patient Identity Removed (0012,0062) = "YES"

Step 3 — Burned-in PHI 픽셀 제거
  PACS 영상 중 모달리티에서 굽혀 넣은(burned-in) 텍스트 PHI 존재
  ┌─ 3단계 이진화 (max pixel / min pixel / 고정 텍스트 임계값)
  ├─ Tesseract v3.05.02 OCR로 텍스트 영역 탐지
  ├─ Regex 기반 PHI 분류 (보수적)
  └─ PHI 의심 영역 → 검정 바운딩 박스로 마스킹
     Burned In Annotation (0028,0301) 플래그 "YES"

Step 4 — 리포트 텍스트 비식별화
  XML에서 텍스트 추출 → 헤더/clinical info segment 제거
  규칙 기반 PHI 탐지 (Neamatullah 2008 알고리즘 확장)
  PHI → "_ _ _" (세 underscores)
  Gold standard: 2,238 리포트 수동 어노테이션 (9,778 PHI tokens)
  자동 탐지 실패: 8개 토큰만 누락 (99.92%)
    └─ 영어 사전 단어와 동일한 의사 이름 3개 (예: "Rose"), 오타 1개,
       날짜 typo 2개, initials 2개 → 수동 제거

Step 5 — 픽셀 PHI 검증
  6,900 이미지 수동 검토 (annotator 2명 독립)
  180장이 secondary consensus review로 회부 → 0건 실제 PHI
  주된 false-positive 사유:
    (1) pacemaker 등 implanted device
    (2) 병원 내 위치 표시 (e.g. "MICU")
    (3) 촬영 기술 약어 (e.g. "prt rr slot 11")

Step 6 — PhysioNet 공개 (Credentialed access)
  IRB 면제 (BIDMC), CITI 인증 + data use agreement 필요
  GitHub: MIT-LCP/mimic-cxr (loading 코드 only — 비식별화 코드는 PHI 포함으로 비공개)
```

## Input (입력 / 데이터셋 구성)

**기본 통계**
| 항목 | 수치 |
|---|---|
| 총 이미지 | **377,110장** |
| 영상 study | **227,835건** |
| 고유 환자 | **65,379명** |
| 수집 기간 | 2011–2016 |
| 기관 | Beth Israel Deaconess Medical Center (Boston, MA) |
| 영상 모달리티 | DICOM (원본) + JPEG (MIMIC-CXR-JPG 부속) |
| 평균 리포트 길이 | 145 words / 642 chars |
| 평균 PHI 토큰/리포트 | 4.4 |

**촬영 뷰 분포 (Simon-Leeming Code, Table 1)**
| 코드 | 검사명 | DICOM 수 | 비율 |
|---|---|---:|---:|
| C11 | CHEST (PA AND LAT) | 248,664 | 65.94% |
| C12 | CHEST (PORTABLE AP) | 126,292 | 33.49% |
| PC111 | DX CHEST PORTABLE PICC LINE PLACEMENT | 329 | 0.09% |
| PC171 | DX CHEST PORT LINE/TUBE PLCMT 1 EXAM | 255 | 0.07% |
| PC172 | DX CHEST PORT LINE/TUBE PLCMT 2 EXAMS | 165 | 0.04% |
| 나머지 19개 | | <600 | <0.2% |

**디렉토리 구조** (Table 2 발췌)
```
p10000032/
├── s50414267/                         ← Study folder (anonymized)
│   ├── 02aa804e-bde0afdd-112c0b34-7bc16630-4e384014.dcm
│   └── 174413ec-4ec4c1f7-34ea26b7-c5f994f8-79ef1962.dcm
├── s50414267.txt                      ← Free-text report
├── s53189527/
│   └── ...
```
- patient ID = `p` + 8 digits starting with `1`
- study ID = `s` + 8 digits starting with `5`
- DICOM filename = 40-char hex UUID with dash separators
- 1차 그룹 폴더 `p10/`, `p11/`, ... (디렉토리당 파일 수 폭증 방지)

## Output (정답/레이블 형식)
**MIMIC-CXR-JPG 부속 CheXpert 자동 NLP 레이블 (14개, Stanford CheXpert + NegBio 앙상블)**

| # | Label | # | Label |
|---|---|---|---|
| 1 | No Finding | 8 | Pneumonia |
| 2 | Enlarged Cardiomediastinum | 9 | Atelectasis |
| 3 | Cardiomegaly | 10 | Pneumothorax |
| 4 | Lung Lesion | 11 | Pleural Effusion |
| 5 | Lung Opacity | 12 | Pleural Other |
| 6 | Edema | 13 | Fracture |
| 7 | Consolidation | 14 | Support Devices |

각 레이블 상태: **Positive / Negative / Uncertain / Disagreement**

## 예시 사례 (논문 원문 직접 인용)

### 📄 리포트 형식 — Section 구조 (Methods 발췌)
> "Reports are archived with linebreaks to ensure individual lines are no longer than 79 characters, and contain up to four segments delimited by underscores repeated to the width of the page. The four segments are: an optional addendum, a report header with patient information, clinical information imported from the EHR, and the main body of the report. Only the addendum and main segments of the report are written by the radiologist."
>
> "PHI of any length was consistently replaced with three underscores ('_ _ _'). Study reports are stored in individual text files named using the anonymous study identifier."

### 🩺 비식별화된 리포트 (PhysioNet 공식 샘플, MIMIC-CXR 라이선스 예시)
> ```
> FINAL REPORT
> EXAMINATION:  CHEST (PA AND LAT)
> INDICATION:   ___ year old woman with ?pleural effusion // ?pleural effusion
> TECHNIQUE:    Chest PA and lateral
> COMPARISON:   ___
>
> FINDINGS:
> Cardiac size cannot be evaluated. Large left pleural effusion is new.
> Small right effusion is new. The upper lungs are clear. Right lower lobe
> opacities are better seen in prior CT. There is no pneumothorax.
>
> IMPRESSION:
> Large left and small right pleural effusions, new.
> ```
> `___` = PHI(환자 나이·이름·날짜) 자리. 리포트 구조 = **Indication → Technique → Comparison → Findings → Impression**.

### 🔍 픽셀 비식별화 검증 — Secondary review 사유 (Methods §"Validation of de-identification" 발췌)
> "We then manually reviewed the pixel data for 6,900 radiographs. Each image was reviewed by two independent annotators. 180 images were identified for a secondary consensus review; none of which ultimately had PHI. The most common causes for annotators to request consensus review were: (1) existence of a support device such as a pacemaker, (2) text identifying in-hospital location (e.g. 'MICU'), and (3) obscure text relating to radiograph technique (e.g. 'prt rr slot 11')."

### ⚠️ 영상 품질 변동성 (Technical Validation 발췌 — RAG 모델이 마주칠 noise)
> "Aside from view parsing and de-identification of the dataset, no filtering or processing of the images was performed. Consequently, images exhibit a number of phenomena common in daily practice. The quality of images varies, both in terms of technique and in terms of patient positioning (e.g. not all patients are healthy enough to stand for a posterior-anterior radiograph, or sit upright for an anterior-posterior radiograph). Images may unintentionally omit anatomy present in a standard chest radiograph, or have objects that obstruct important anatomy."
>
> Figure 2 캡션: "From left to right: (a) poor patient positioning, (b) black box obscuring potential PHI, (c) secondary collimation to improve image quality, and (d) incorrect image orientation information in the meta-data."

## 주요 평가 결과 (이 데이터셋이 RAG·VLM 벤치마크로 쓰인 후속 연구)

MIMIC-CXR 자체는 학습/평가용 데이터로 공개되며 — 별도 leaderboard 운영은 없음. 후속 연구의 표준 분할은 train 368,960 / val 2,991 / test 5,159 (MIMIC-CXR-JPG split).

| 후속 태스크 | 평가 지표 |
|---|---|
| 자동 방사선 보고서 생성 | BLEU-4, ROUGE-L, CIDEr, METEOR (NLP) + Clinical Efficacy (CE) score |
| 14-label 분류 | AUC-ROC, macro-F1 |
| 영상-텍스트 검색 | R@1/5/10, MRR |
| 멀티모달 RAG (예: CEMRAG, LaB-RAG, MMed-RAG) | 검색 P/R/nDCG + 다운스트림 생성 정확도 |

## 한계점
- **단일 기관**(BIDMC, Boston) → 인종·기기·protocol 편향 가능. CheXpert(Stanford), PadChest(Alicante) 등과의 cross-site 평가 권장.
- **응급실 한정** → 외래·routine 검사와 환자 분포 다름.
- **14 레이블은 자동 NLP 추출** (CheXpert + NegBio) — 전문가 수동 검증 아님. Uncertain/Disagreement 비율 무시할 수 없음.
- **DICOM 비식별화 코드 비공개** ("Due to the use of real patient information during the de-identification process, the code used to prepare the dataset cannot be made publicly available.")
- **흉부 X-ray에 한정** — CT, MRI 미포함. PhysioNet의 다른 데이터셋과 결합 필요.
- **임상 컨텍스트 segment 제거**됨 → 환자 history 기반 추론 불가능. RAG 시스템이 EHR과 별도 페어링 필요.

## 관련 정보
- **논문 (Scientific Data)**: [doi:10.1038/s41597-019-0322-0](https://doi.org/10.1038/s41597-019-0322-0)
- **PhysioNet (DICOM, credentialed)**: [mimic-cxr v2.1.0](https://physionet.org/content/mimic-cxr/2.1.0/)
- **PhysioNet (JPEG 부속, 14 labels 포함)**: [mimic-cxr-jpg v2.1.0](https://physionet.org/content/mimic-cxr-jpg/2.1.0/)
- **GitHub (loading code only)**: [MIT-LCP/mimic-cxr](https://github.com/MIT-LCP/mimic-cxr)
- **문서**: [mimic-cxr.mit.edu](https://mimic-cxr.mit.edu)
- **CheXpert 레이블러**: Irvin et al., AAAI 2019
- **연관 데이터셋 (IU-Xray)**: Demner-Fushman et al. 2016 — 방사선 보고서 생성 RAG의 표준 쌍
