---
title: "ChEMBL: a large-scale bioactivity database for drug discovery"
bib_key: "DBLP:journals/nar/GaultonBBCDHLMMAO12"
year: 2012
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkr777
---
# ChEMBL: a large-scale bioactivity database for drug discovery

DBLP:journals/nar/GaultonBBCDHLMMAO12 | 2012 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkr777)

**DB**: ChEMBL (EBI, initial description)
**DB size**: 5.4M 바이오활성 측정치, 1M+ 화합물, 5,200 단백질 타겟
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ChEMBL web interface + data download + web services

> Nucleic Acids Research | 2012 | dataset | chem
#### 📌 한 줄 요약
EBI가 구축한 ChEMBL은 저널 문헌에서 수동 추출한 결합·기능·ADMET 데이터를 포함하는 대규모 오픈 바이오활성 데이터베이스이다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 약물 발견에 필요한 바이오활성 데이터가 논문 전문에 분산되어 있어 계산 가능한 형태로 접근하기 어려웠음
- 화합물 구조와 생물학적 활성 데이터를 통합한 표준화된 공개 DB가 부재했음
**이 시스템이 필요한 이유**
- 화학생물학 및 약물 발견 연구에서 대규모 구조-활성 관계(SAR) 분석 기반 필요
- 계산화학 및 머신러닝 모델 학습용 큐레이션된 바이오활성 데이터셋 수요

#### 🔨 시스템 구성
핵심 의약화학 저널 전문에서 화합물·어세이·바이오활성 정보를 수동으로 추출한다. 화합물 구조는 표준화되고 Standard InChI 기반 식별자가 부여된다. 어세이 기술은 제어 어휘로 매핑되고, 활성 측정치는 표준 형식으로 변환된다. 웹 인터페이스, 데이터 다운로드, 웹 서비스를 통해 제공된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | https://www.ebi.ac.uk/chembldb 텍스트·구조 검색 |
| 데이터 다운로드 | 전체 DB SQL/SDF 다운로드 |
| 웹 서비스 (REST) | 구조·타겟·바이오활성 API |

#### 📤 제공 데이터 형식
- 화합물 구조 (SMILES, InChI, SDF)
- 바이오활성 측정치 (IC50, Ki, EC50 등)
- 타겟 단백질 정보 (UniProt 연동)
- 어세이 기술 (표준화된 어휘)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 바이오활성 측정치 | 5.4M |
| 화합물 | 1M+ |
| 단백질 타겟 | 5,200 |

#### ⚠️ 한계점
- 수동 큐레이션 방식으로 데이터 추가 속도가 제한적
- 논문 전문이 필요하므로 오픈액세스가 아닌 경우 접근 제한 발생
- 초기 버전으로 직접 데이터 기탁(deposition) 기능 미지원

## 관련 정보
- **논문**: [ChEMBL: a large-scale bioactivity database for drug discovery](https://doi.org/10.1093/nar/gkr777)
