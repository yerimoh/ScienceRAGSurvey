---
title: "CIViC is a community knowledgebase for expert crowdsourcing the clinical interpretation of variants in cancer"
bib_key: "griffith2017civic"
year: 2017
domain: medical
type: dataset
venue: Nature Genetics
paper_link: https://doi.org/10.1038/ng.3774
---
# CIViC is a community knowledgebase for expert crowdsourcing the clinical interpretation of variants in cancer

griffith2017civic | 2017 | Nature Genetics | dataset | [medical] | [paper](https://doi.org/10.1038/ng.3774)

**DB**: CIViC (Clinical Interpretation of Variants in Cancer)
**DB size**: 출판 시점 수백 개 변이·유전자; 지속적 커뮤니티 큐레이션으로 성장
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: CIViC REST API / civicdb.org 웹 인터페이스

> Nature Genetics | 2017 | dataset | medical
#### 📌 한 줄 요약
암 변이의 치료적·예후적·진단적·소인적 임상 해석을 전문가 크라우드소싱으로 구축하는 오픈소스·오픈액세스 암 정밀 의학 지식 베이스로, 큐레이터-편집자 검증 워크플로를 갖춘다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 암 변이의 임상적 해석이 개별 논문과 내부 실험실 시스템에 분산되어 있어 체계적 접근이 어려웠다
- OncoKB, JAX-CKB 등 기존 DB는 소수 전문 기관이 폐쇄적으로 큐레이션; 커뮤니티 기여 불가
- 같은 변이의 임상적 의미에 대한 근거 출처를 투명하게 추적할 수 없었다

**이 시스템이 필요한 이유**
- 암 정밀 의학의 빠른 발전 속도에 맞추려면 전 세계 전문가 커뮤니티의 분산 큐레이션이 필요하다
- 치료적(predictive), 예후적(prognostic), 진단적(diagnostic), 소인적(predisposing) 4가지 변이 임상 역할을 통합 관리해야 한다

#### 🔨 시스템 구성
CIViC는 위키 방식의 큐레이션 워크플로를 갖는다.
- **Evidence Item**: 개별 변이-임상 연관의 단위; 하나의 문헌 근거 + 임상 유의성 레이블
- **Variant**: 유전자 내 특정 변이 (SNV, 삽입/삭제, 융합 등)
- **Gene**: 변이가 속하는 유전자 항목
- **큐레이터 → 편집자 → 승인** 3단계 워크플로; 편집자 검토 후 공개

임상 역할 4가지: **Predictive** (치료 반응 예측), **Prognostic** (예후), **Diagnostic** (진단 분류), **Predisposing** (유전적 소인)

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| CIViC REST API | api.civicdb.org — 유전자·변이·근거 항목 쿼리; 공개 무료 |
| 웹 인터페이스 | civicdb.org — 검색, 큐레이션, 시각화 |
| 데이터 다운로드 | nightly TSV/VCF 덤프; 완전 오픈액세스 |

#### 📤 제공 데이터 형식
- Evidence Item (변이-임상 연관 + 문헌 PMC/PMID)
- Variant summary (변이 기술 + 연관 항목 집계)
- VCF 형식 변이 파일
- Open-source code (GitHub: griffithlab/civic-client)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 임상 역할 범주 | Predictive, Prognostic, Diagnostic, Predisposing (4가지) |
| 큐레이션 워크플로 | 큐레이터 제출 → 편집자 검토 → 승인 |
| 라이선스 | CC0 (공개 도메인) |
| 코드 라이선스 | MIT |
| 운영 기관 | Washington University in St. Louis (Griffith Lab) |

#### ⚠️ 한계점
- 커뮤니티 큐레이션 특성상 특정 유명 유전자(EGFR, BRAF, KRAS 등)에 항목이 집중
- 편집자 수 제한으로 신규 항목 검토에 시간 지연 발생 가능
- 희귀 암·희귀 변이는 근거 문헌 부족으로 커버리지 낮음
- 체세포·생식세포 구분이 항목별로 일관성이 부족할 수 있음

## 관련 정보
- **논문**: [Griffith et al., Nature Genetics 2017](https://doi.org/10.1038/ng.3774)
