---
title: "ChEMBL: towards direct deposition of bioassay data"
bib_key: "DBLP:journals/nar/MendezGBCVFMMMN19"
year: 2019
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gky1075
---
# ChEMBL: towards direct deposition of bioassay data

DBLP:journals/nar/MendezGBCVFMMMN19 | 2019 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gky1075)

**DB**: ChEMBL Release 24
**DB size**: 15M+ 바이오활성 측정치, 1.8M 화합물, 8,200+ 단백질 타겟
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: ChEMBL web interface + REST API + data deposition system

> Nucleic Acids Research | 2019 | dataset | chem
#### 📌 한 줄 요약
ChEMBL Release 24는 바이오어세이 직접 기탁 시스템, 완전히 재설계된 웹 인터페이스, 강화된 어세이 세부 포착 기능을 도입하여 15M+ 바이오활성 측정치를 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 저널 논문이 아닌 데이터셋은 기탁 경로가 없어 공개 접근이 어려웠음
- 어세이 세부 정보(세포주, 조직, 유기체) 포착이 불완전했음
**이 시스템이 필요한 이유**
- 특허 바이오활성 데이터(BindingDB 교환), 오픈소스 말라리아 데이터 등 비문헌 데이터 통합 필요
- 어세이 메타데이터 표준화로 데이터 재활용성 향상

#### 🔨 시스템 구성
67,000개 이상 문헌·특허에서 추출한 데이터와 직접 기탁 데이터셋을 통합한다. 어세이는 1,600개 세포주, 500 조직/기관, 3,600 유기체로 주석된다. 신규 기탁 시스템으로 보충 데이터셋 제출 가능. 새 웹 인터페이스는 인터랙티브 필터링, Heatmap, Sunburst 시각화를 지원한다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | 재설계된 인터랙티브 검색·필터링 UI |
| REST API | JSON/XML 기반 구조·타겟·바이오활성 조회 |
| 데이터 다운로드 | Oracle, PostgreSQL, SQLite, RDF, SDF, FASTA |
| 기탁 시스템 | DOI 부여 데이터셋 직접 업로드 |

#### 📤 제공 데이터 형식
- 화합물 구조 (SMILES, InChI)
- 바이오활성 측정치 (IC50, Ki, EC50, kd, kon, koff 포함)
- 타겟 서열 (FASTA)
- RDF 형식

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 바이오활성 측정치 | 15M+ |
| 화합물 | 1.8M |
| 단백질 타겟 | 8,200+ (인간 단백질 3,569) |
| 어세이 주석 세포주 | 1,600+ |
| 데이터 추출 문헌·특허 | 67,000+ |

#### ⚠️ 한계점
- 직접 기탁 데이터의 품질 검증 절차가 문헌 추출 대비 덜 엄격할 수 있음
- 데이터베이스 스키마가 문헌 추출 중심으로 설계되어 기탁 데이터 일부 측면 표현 제한

## 관련 정보
- **논문**: [ChEMBL: towards direct deposition of bioassay data](https://doi.org/10.1093/nar/gky1075)
