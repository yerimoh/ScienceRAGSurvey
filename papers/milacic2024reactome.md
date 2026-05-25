---
title: "The Reactome Pathway Knowledgebase 2024"
bib_key: "milacic2024reactome"
year: 2024
domain: bio
type: dataset
venue: Nucleic Acids Research
paper_link: https://doi.org/10.1093/nar/gkad1025
---
# The Reactome Pathway Knowledgebase 2024

milacic2024reactome | 2024 | Nucleic Acids Research | dataset | [bio] | [paper](https://doi.org/10.1093/nar/gkad1025)

**DB**: Reactome Pathway Knowledgebase
**DB size**: 전체 인간 프로테옴 주석을 목표로 하는 큐레이션 경로 데이터베이스 (Elixir 및 GCBR 핵심 데이터 자원)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: N/A (지식 소스 인프라)
**Eval Task**: N/A
**Eval Metric**: N/A
**Method Name**: Reactome REST API / FTP (https://reactome.org)

> Nucleic Acids Research | 2024 | dataset | bio
#### 📌 한 줄 요약
수작업 큐레이션된 인간 생물학적 경로 데이터베이스로, 정상 및 질병 관련 분자 변환 과정을 단일 일관된 데이터 모델로 표현하며 Elixir 및 GCBR 핵심 생물 데이터 자원으로 지정되어 있다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 기존 생물학적 경로 데이터베이스들은 분자 세부 사항의 수준이 낮거나 특정 종에 국한되어 있었다
- 유전자 발현 프로파일이나 종양 세포 체세포 돌연변이 카탈로그 같은 대규모 데이터에서 기능적 관계를 발견하기 위한 체계적 도구가 필요했다

**이 시스템이 필요한 이유**
- 인간 전체 프로테옴의 분자 변환 과정을 수작업으로 주석하는 디지털 아카이브 구축
- 유전자 발현 데이터, 체세포 돌연변이 카탈로그에서 기능적 관계를 발견하는 분석 도구로 활용
- Gene Ontology 등 관련 자원과의 상호운용성 강화

#### 🔨 시스템 구성
Reactome은 분자 변환을 순서 있는 네트워크로 표현하는 단일 일관된 데이터 모델을 사용한다. 경로는 정상 생물학적 과정과 질병 관련 과정 모두를 포함한다. 2024년 업데이트에서는 전체 인간 프로테옴 주석 진행, 단백질의 질병 유발 유전자 변이 및 소분자 약물의 경로 맥락 주석, 세포·조직 특이적 경로 명시적 주석 지원이 강조된다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| 웹 인터페이스 | https://reactome.org — 경로 브라우저, 분석 도구 |
| REST API | 프로그래밍 방식 데이터 접근 |
| FTP | 전체 데이터셋 bulk 다운로드 |

#### 📤 제공 데이터 형식
- 경로 데이터 (BioPAX, SBML, GPML 형식)
- 유전자-경로 매핑
- 반응별 분자 세부 정보
- Gene Ontology 및 외부 데이터베이스 교차 참조

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 데이터 자원 분류 | Elixir 핵심 데이터 자원, GCBR 핵심 생물 데이터 자원 |
| 대상 종 | 인간 (Homo sapiens) 중심 |
| 목표 | 전체 인간 프로테옴 주석 완성 진행 중 |

#### ⚠️ 한계점
- 수작업 큐레이션에 의존하여 새로운 발견의 반영 속도가 출판 후 지연될 수 있다
- 인간 경로 중심이며, 비인간 생물 종에 대한 직접 큐레이션이 제한적이다
- Gene Ontology 등 다른 자원과의 완전한 상호운용성 달성이 진행 중이다

## 관련 정보
- **논문**: [The Reactome Pathway Knowledgebase 2024](https://doi.org/10.1093/nar/gkad1025)
