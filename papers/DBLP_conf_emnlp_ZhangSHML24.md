---
title: "HoneyComb: A Flexible LLM-Based Agent System for Materials Science"
bib_key: "DBLP:conf/emnlp/ZhangSHML24"
year: 2024
domain: material
type: dataset
venue: Findings of EMNLP 2024
paper_link: https://doi.org/10.18653/v1/2024.findings-emnlp.192
---
# HoneyComb: A Flexible LLM-Based Agent System for Materials Science

DBLP:conf/emnlp/ZhangSHML24 | 2024 | Findings of EMNLP 2024 | dataset | [material] | [paper](https://doi.org/10.18653/v1/2024.findings-emnlp.192)

**DB**: MatSciKB (Materials Science Knowledge Base)
**DB size**: 문헌 기반 큐레이션된 구조적 지식 컬렉션 (규모 수치 논문 미기재)
**DB Open/Private**: Open (코드 공개)
**Modality**: ['Text']
**Retriever**: 적응형 retriever (지식 소스 vs 도구 선택)
**Eval Task**: Materials science QA, 계산 과제, 특성 예측
**Eval Metric**: 정확도 (task별 베이스라인 대비)
**Method Name**: HoneyComb LLM 에이전트 시스템

> Findings of EMNLP 2024 | 2024 | dataset | material
#### 📌 한 줄 요약
재료과학 전용 LLM 에이전트 시스템 HoneyComb이 구축한 큐레이션 지식 베이스(MatSciKB)로, 신뢰할 수 있는 재료과학 문헌을 구조화한 검색 기반 지식 소스이며 Materials Project 등 외부 DB 접근을 위한 ToolHub와 결합된다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 범용 LLM은 재료과학의 복잡한 계산 과제와 특성화 요구를 처리하지 못함
- 기존 LLM은 구식 암묵적 지식에 의존하여 부정확성과 환각(hallucination) 발생
- 재료과학 전용 QA, 특성 예측, 계산 태스크를 통합하는 에이전트 시스템 부재

**이 시스템이 필요한 이유**
- 재료과학 문헌으로부터 고품질 지식을 큐레이션하여 검색 기반 정확도 향상
- Inductive Tool Construction 방법으로 재료과학 전용 API 도구 자동 생성·분해·정제
- 태스크에 따라 지식 소스(MatSciKB)와 도구(ToolHub) 중 적절한 것을 선택하는 적응형 retriever 적용

#### 🔨 시스템 구성
HoneyComb은 MatSciKB(지식 소스), ToolHub(계산 도구), 적응형 retriever의 세 모듈로 구성된다. MatSciKB는 신뢰할 수 있는 재료과학 문헌(논문, 교재 등)을 구조화한 텍스트 형태의 큐레이션 지식 컬렉션이다. ToolHub는 Inductive Tool Construction(ITC) 방법으로 Materials Project API 등 재료과학 도구를 자동 래핑한다. Retriever는 입력 쿼리 성격에 따라 MatSciKB 검색(사실적 질문) 또는 ToolHub 실행(계산 요청)을 선택한다.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| GitHub | 코드 및 MatSciKB 공개 예정 (논문 기준) |
| ACL Anthology | https://aclanthology.org/2024.findings-emnlp.192 |
| arXiv | arXiv:2409.00135 |

#### 📤 제공 데이터 형식
- MatSciKB: 구조화된 텍스트 지식 (재료과학 문헌 기반)
- ToolHub: 재료과학 API 도구 집합 (Materials Project 등)
- 평가 벤치마크: 재료과학 QA, 계산 태스크

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 논문 발표 | Findings of EMNLP 2024, pp. 3369–3382 |
| 시스템 구성 모듈 | 3개 (MatSciKB, ToolHub, Retriever) |
| 성능 | 다양한 재료과학 태스크에서 베이스라인 대비 유의미하게 향상 |
| arXiv ID | 2409.00135 |

#### ⚠️ 한계점
- MatSciKB의 구체적 크기(항목 수, 커버리지)가 논문에 명시되지 않음
- 특정 재료과학 도메인(나노, 폴리머 등)에 대한 커버리지 불균형 가능성
- ToolHub는 Materials Project 등 외부 API에 의존하므로 API 가용성에 취약
- 재료과학 이외 도메인 확장성은 아직 검증 단계

## 관련 정보
- **논문**: [HoneyComb: A Flexible LLM-Based Agent System for Materials Science (EMNLP Findings, 2024)](https://doi.org/10.18653/v1/2024.findings-emnlp.192)
- **arXiv**: [arXiv:2409.00135](https://arxiv.org/abs/2409.00135)
