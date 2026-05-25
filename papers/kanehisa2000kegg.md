---
title: "KEGG: kyoto encyclopedia of genes and genomes"
bib_key: "kanehisa2000kegg"
year: 2000
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/28.1.27
---
# KEGG: kyoto encyclopedia of genes and genomes

kanehisa2000kegg | 2000 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/28.1.27)

**DB**: KEGG (Kyoto Encyclopedia of Genes and Genomes)
**DB size**: 3개 핵심 데이터베이스 (GENES, PATHWAY, LIGAND) — 논문 기준 완전 해독된 전체 게놈의 유전자 카탈로그
**DB Open/Private**: Open (무료 공개)
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: KEGG API / FTP (http://www.genome.ad.jp/kegg/)

> Nucleic Acids Research | 2000 | dataset | bio
#### 📌 한 줄 요약
게놈 정보와 고차원 기능 정보를 연결하는 생물정보학 지식 베이스로, GENES(유전자 카탈로그), PATHWAY(세포 경로), LIGAND(화합물 및 효소 반응) 세 데이터베이스로 구성된다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 유전체 서열 분석 프로젝트가 대량의 유전자 서열을 생산하지만, 이를 세포 수준의 기능과 연결하는 체계적 수단이 부족했다
- 서열 정보와 대사 경로, 신호 전달 등 고차원 기능 정보 사이의 간극을 메울 통합 데이터베이스가 필요했다

**이 시스템이 필요한 이유**
- 완전 해독된 게놈의 유전자를 기능적 경로와 연결하는 체계적 분석 지원
- 종간 기능 보존 경로(pathway motif)의 비교 분석 및 유전자 기능 예측 가능
- Java 기반 시각화 도구로 게놈 지도, 비교 게놈 분석, 발현 지도 탐색 지원

#### 🔨 시스템 구성
KEGG는 세 가지 핵심 데이터베이스로 구성된다: (1) **GENES** — 완전 해독된 모든 게놈의 유전자 카탈로그, 일일 갱신, (2) **PATHWAY** — 대사, 막 수송, 신호 전달, 세포 주기 등 세포 과정의 그래픽 표현, (3) **LIGAND** — 화합물, 효소 분자, 효소 반응 정보. 보존 서브경로(pathway motif) 정보는 직교 그룹 테이블로 제공된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | http://www.genome.ad.jp/kegg/ — 무료 브라우저 접근 |
| Java 도구 | 게놈 지도 탐색, 게놈 비교, 발현 지도 조작 |
| FTP | 전체 데이터셋 다운로드 |

#### 📤 제공 데이터 형식
- 유전자 카탈로그 (GENES 데이터베이스)
- 경로 그래픽 표현 (PATHWAY 데이터베이스)
- 화합물·효소·반응 정보 (LIGAND 데이터베이스)
- 직교 그룹 테이블 (경로 모티프)

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 수록 게놈 | 완전 해독된 전체 게놈 + 일부 부분 게놈 |
| 데이터 갱신 | 매일 업데이트 |
| 주요 구성 요소 | GENES, PATHWAY, LIGAND 3개 DB |

#### ⚠️ 한계점
- 2000년 당시 기반 논문으로, 완전 해독된 게놈 수가 현재에 비해 매우 적었다
- 세포 경로 정보는 수작업 큐레이션에 의존하여 신규 발견 경로의 반영 속도에 제한이 있다
- LIGAND 화합물 데이터베이스는 당시 효소 반응 중심으로 소분자 약물 정보가 제한적이었다

## 관련 정보
- **논문**: [KEGG: kyoto encyclopedia of genes and genomes](https://doi.org/10.1093/nar/28.1.27)
