---
title: "The DisGeNET knowledge platform for disease genomics: 2019 update"
bib_key: "DBLP:journals/nar/GonzalezRSRCSF20"
year: 2020
domain: medical
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkz1021
---
# The DisGeNET knowledge platform for disease genomics: 2019 update

DBLP:journals/nar/GonzalezRSRCSF20 | 2020 | Nucleic Acids Research | dataset | [medical] | [paper](https://doi.org/10.1093/nar/gkz1021)

**DB**: DisGeNET (Disease Genomics Network)
**DB size**: 유전자-질환 연관 >1,000,000쌍; 유전자 17,000+, 질환/형질 24,000+, 변이 117,000+
**DB Open/Private**: Open (학술 무료; 상업적 사용 라이선스)
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: DisGeNET REST API / disgenet2r (R 패키지) / Python API

> Nucleic Acids Research | 2020 | dataset | medical
#### 📌 한 줄 요약
전문가 큐레이션 데이터와 문헌 텍스트 마이닝을 통합해 17,000개 이상의 유전자와 24,000개 이상의 질환·형질 사이 100만 개 이상의 유전자-질환 연관 및 117,000개 이상의 변이-질환 연관을 제공하는 질환 유전체학 플랫폼이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 유전자-질환 연관이 OMIM, ClinVar, GWAS Catalog 등 수십 개 이종 소스에 분산되어 통합 조회가 불가능했다
- 큐레이션 DB는 정확하지만 규모가 작고, 텍스트 마이닝 결과는 방대하지만 노이즈가 많았다
- 연관의 근거 출처와 신뢰도 점수가 부재했다

**이 시스템이 필요한 이유**
- 약물 타깃 발굴, 희귀 질환 진단, 다면 발현(pleiotropy) 분석 등에 통합된 유전자-질환 지식이 필요하다
- 표준 점수 체계(DisGeNET score)로 큐레이션·텍스트마이닝 연관의 신뢰도를 정량화할 필요가 있다

#### 🔨 시스템 구성
DisGeNET은 다중 소스에서 유전자-질환·변이-질환 연관을 수집하고 4가지 증거 유형으로 분류한다.
- **Curated**: OMIM, ClinVar, UniProt, Orphanet 등 전문가 큐레이션
- **Inferred**: MGD·RGD 동물 모델에서 추론
- **Literature (text-mined)**: PubMed 초록·전문 자동 추출
- **Animal models**: 마우스/쥐 게놈 모델 연관

**DisGeNET Score**: 소스 신뢰도, 문헌 수, 큐레이션 레벨을 결합한 증거 강도 지수

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| REST API | api.disgenet.com — 유전자·질환·변이 쿼리; 무료 등록 |
| disgenet2r | CRAN 배포 R 패키지; R 환경에서 직접 쿼리 |
| Python API | pip install disgenet2 — Python 통합 |
| TSV 다운로드 | 전체 데이터셋 파일 다운로드 (학술 무료) |

#### 📤 제공 데이터 형식
- 유전자-질환 연관 테이블 (GDA: Gene-Disease Association)
- 변이-질환 연관 테이블 (VDA: Variant-Disease Association)
- DisGeNET score 및 증거 유형 레이블
- UMLS CUI 기반 질환 식별자

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 질환·형질 수 | **24,000개 이상** |
| 유전자 수 | **17,000개 이상** |
| 게놈 변이 수 | **117,000개 이상** |
| 유전자-질환 연관 수 | **1,000,000개 이상** (전체; 큐레이션+문헌마이닝) |
| 소스 통합 수 | 큐레이션 소스 12개 + 문헌 마이닝 포함 |
| 운영 기관 | IMIM (Institut Hospital del Mar d'Investigacions Mèdiques) |

#### ⚠️ 한계점
- 문헌 텍스트마이닝 연관에는 위양성(false positive)이 포함될 수 있으므로 큐레이션 연관과 구분 활용 권장
- 상업적 사용 및 대규모 API 활용은 별도 라이선스 필요
- UMLS CUI 기반 질환 식별로 MeSH·ICD 직접 매핑 시 추가 변환 필요

## 관련 정보
- **논문**: [Piñero González et al., Nucleic Acids Research 2020](https://doi.org/10.1093/nar/gkz1021)
