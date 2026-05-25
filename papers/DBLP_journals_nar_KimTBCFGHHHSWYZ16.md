---
title: "PubChem Substance and Compound databases"
bib_key: "DBLP:journals/nar/KimTBCFGHHHSWYZ16"
year: 2016
domain: chem
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkv951
---
# PubChem Substance and Compound databases

DBLP:journals/nar/KimTBCFGHHHSWYZ16 | 2016 | Nucleic Acids Research | dataset | [chem] | [paper](https://doi.org/10.1093/nar/gkv951)

**DB**: PubChem (Substance, Compound, BioAssay)
**DB size**: 157M+ substance descriptions, 60M unique structures, 1M+ bioassay descriptions (as of Sep 2015)
**DB Open/Private**: Open
**Modality**: ['Text', 'Structured']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: PubChem REST API (PUG-REST, PUG-View)

> Nucleic Acids Research | 2016 | dataset | chem
#### 📌 한 줄 요약
미국 NIH가 운영하는 공개 화학 정보 저장소로 SMILES, InChI, CAS 식별자 등을 포함한 화합물·물질·바이오어세이 데이터를 통합 제공한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 화학 물질 정보가 여러 독립적 저장소에 분산되어 있어 통합 검색이 어려웠음
- 생물 활성 데이터와 화학 구조 정보 간 연결이 체계적으로 이루어지지 않았음
**이 시스템이 필요한 이유**
- NIH Molecular Libraries Roadmap Initiative의 일환으로, 화학 정보의 공공 접근성 확보 필요
- 구조 기반 검색, 유사도 검색, 생물 활성 조회를 단일 인터페이스로 제공

#### 🔨 시스템 구성
세 개의 상호 연결된 데이터베이스(Substance, Compound, BioAssay)로 구성된다. Substance DB는 기여자가 제출한 원시 화학 정보를, Compound DB는 표준화된 고유 구조를, BioAssay DB는 실험적 생물 활성 데이터를 저장한다. 구조 표준화 파이프라인을 통해 중복 제거 및 SMILES/InChI 변환이 자동으로 수행된다. PubChem3D와 PubChemRDF(RDF 형식 데이터) 파생 자원도 포함된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| PUG-REST API | RESTful API로 CID, SMILES, InChI 등으로 검색 및 다운로드 |
| PUG-View | 구조화된 뷰 데이터 조회 API |
| FTP 다운로드 | SDF, SMILES, XML, ASN.1 포맷 전체 덤프 제공 |
| 웹 인터페이스 | pubchem.ncbi.nlm.nih.gov 텍스트/구조 검색 |

#### 📤 제공 데이터 형식
- SMILES (canonical 및 isomeric)
- InChI / InChIKey
- SDF (2D/3D 구조)
- XML, ASN.1
- RDF (PubChemRDF)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| Substance 기록 | 157M+ (2015년 9월 기준) |
| 고유 화합물 구조 | 60M |
| 바이오어세이 기술 | 1M+ |
| 단백질 타겟 | ~10,000 |
| 특허-화합물 링크 | 329M+ |

#### ⚠️ 한계점
- 기여자 제출 데이터 품질 편차가 크며 표준화 과정에서 일부 정보 손실 가능
- 초당 3회 이상의 API 요청은 서버 과부하 우려로 제한됨
- 대용량 요청(수백만 건)에는 배치 처리 방식이 필요

## 관련 정보
- **논문**: [PubChem Substance and Compound databases](https://doi.org/10.1093/nar/gkv951)
