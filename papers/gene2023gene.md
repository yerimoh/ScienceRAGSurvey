---
title: "The Gene Ontology knowledgebase in 2023"
bib_key: "gene2023gene"
year: 2023
domain: bio
type: dataset
venue: Genetics
paper_link: https://doi.org/10.1093/genetics/iyad031
---
# The Gene Ontology knowledgebase in 2023

gene2023gene | 2023 | Genetics | dataset | [bio] | [paper](https://doi.org/10.1093/genetics/iyad031)

**DB**: Gene Ontology (GO) Knowledgebase
**DB size**: 3개 구성 요소: GO 온톨로지, GO 주석, GO Causal Activity Models (GO-CAMs)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: GO REST API / 파일 다운로드 (http://geneontology.org)

> Genetics | 2023 | dataset | bio
#### 📌 한 줄 요약
유전자 및 유전자 산물(단백질, 비코딩 RNA)의 기능을 기술하는 GO 지식베이스의 2023년 현황으로, GO 온톨로지, GO 주석, GO-CAM 세 가지 구성 요소와 지속적 확장·검증 방법을 소개한다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 2000년 창립 이후 새로운 생물학적 발견과 함께 GO 용어 및 주석의 지속적 갱신이 필요해졌다
- 단순 유전자-GO 용어 매핑을 넘어 분자 경로의 인과적 활동 모델(GO-CAM) 표현이 필요했다

**이 시스템이 필요한 이유**
- 생명 나무 전체(바이러스 포함)에 걸친 유전자 기능 지식의 포괄적 자원 구축
- GO-CAM을 통해 여러 GO 주석을 연결하는 메커니즘적 경로 모델 제공
- 광범위한 국제 컨소시엄의 QA 검사, 검토, 사용자 피드백을 통한 품질 유지

#### 🔨 시스템 구성
GO 지식베이스는 세 가지 구성 요소로 이루어진다: (1) **GO** — 유전자의 기능적 특성을 기술하는 전산 지식 구조, (2) **GO 주석** — 특정 유전자 산물이 특정 기능적 특성을 갖는다는 증거 기반 진술, (3) **GO Causal Activity Models (GO-CAMs)** — 정의된 관계를 사용하여 여러 GO 주석을 연결하는 분자 '경로'의 메커니즘 모델. 각 구성 요소는 새로운 발견에 따라 지속적으로 확장·수정·갱신된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | http://geneontology.org — 온톨로지 및 주석 탐색 |
| REST API | 프로그래밍 방식 데이터 접근 |
| 파일 다운로드 | OBO, OWL, GAF 등 다양한 형식 |

#### 📤 제공 데이터 형식
- GO 온톨로지 (OBO/OWL 형식)
- GO 주석 파일 (GAF 형식, 증거 코드 포함)
- GO-CAM 모델 (인과적 활동 모델)
- 종별 유전자-GO 매핑

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 구성 요소 수 | **3개** (GO 온톨로지, GO 주석, GO-CAM) |
| 적용 대상 | 생명 나무 전체 생물 + 바이러스 |
| 주요 정보 출처 | 소수 모델 생물체 실험 결과 (대부분 지식 출처) |

#### ⚠️ 한계점
- 대부분의 유전자 기능 지식은 소수의 모델 생물체에서 수행된 실험에서 비롯된다
- 비모델 생물체의 유전자는 주로 전산 추론으로 주석되어 신뢰도가 낮을 수 있다
- GO-CAM 모델은 아직 개발 초기 단계로 전체 생물학적 경로의 완전한 표현에 한계가 있다

## 관련 정보
- **논문**: [The Gene Ontology knowledgebase in 2023](https://doi.org/10.1093/genetics/iyad031)
