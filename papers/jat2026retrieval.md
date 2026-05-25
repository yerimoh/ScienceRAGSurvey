---
title: "Retrieval-Augmented Question Answering over Scientific Literature for the Electron-Ion Collider"
bib_key: "jat2026retrieval"
year: 2026
domain: physics
type: Method
venue: arXiv 2026
paper_link: https://arxiv.org/abs/2604.02259
---
# Retrieval-Augmented Question Answering over Scientific Literature for the Electron-Ion Collider

jat2026retrieval | 2026 | arXiv 2026 | Method | [physics] | [paper](https://arxiv.org/abs/2604.02259)

**Retriever**: Dense retrieval over arXiv EIC articles (local, in-house database)
**Eval Task**: Domain-specific QA on EIC experiment (experimental nuclear physics)
**Eval Metric**: Benchmark dataset evaluation (custom EIC QA benchmark)
**Method Name**: EIC-RAG QA (local LLaMA-based)
**Modality**: Text (arXiv EIC scientific literature)

> arXiv 2026 | 2026 | Method | physics
#### 📌 한 줄 요약
EIC(전자-이온 충돌기) 관련 arXiv 논문에 인덱싱된 자체 데이터베이스를 구축하고 오픈소스 LLaMA 모델로 답변을 생성하는 로컬 배포 RAG 질의응답 시스템으로, 독점 모델 의존도를 제거하고 미출판 데이터의 외부 전송 없이 비용 효율적인 도메인 특화 QA를 구현한다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 선행 연구(RAGS4EIC, arXiv:2403.15729)는 독점 모델과 클라우드 호스팅 외부 지식 베이스에 의존하여 데이터 프라이버시 우려 존재
- 비용 및 인터넷 연결 의존도가 높아 자원 제약 환경에서 사용 불가

**이 시스템이 필요한 이유**
- 미출판 EIC 과학 데이터·정보의 공개 도메인 전송 방지
- 비용 효율적인 자원 제약 환경에서의 도메인 특화 QA 솔루션 필요

#### 🔨 시스템 구성
EIC 실험 관련 arXiv 논문에 인덱싱된 자체 데이터베이스를 구축한다. 오픈소스 LLaMA 모델을 로컬에 배포하여 답변 생성에 사용한다. 이전 RAGS4EIC(독점 모델 + 클라우드 외부 지식 베이스)의 연장선상에 있으며, 로컬 배포로 데이터 프라이버시를 확보한다. 미래 개선으로 이종 EIC 출판물·보고서로 지식 베이스 확장 및 LangGraph 파이프라인 업그레이드를 계획한다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| 지식 베이스 | EIC 관련 arXiv 논문 (로컬 인덱스) |
| LLM | LLaMA (오픈소스, 로컬 배포) |
| 평가 | 자체 EIC QA 벤치마크 |
| 주요 장점 | 데이터 프라이버시, 비용 효율, 자원 제약 환경 적합 |

#### ⚠️ 한계점
- arXiv EIC 논문에 한정되어 기관 내부 문서·보고서는 미포함
- LLaMA 기반 오픈소스 모델의 성능이 GPT-4 등 상용 모델보다 낮을 수 있음
- 로컬 배포를 위한 초기 HW 설정 비용 필요

## 관련 정보
- **논문 (arXiv)**: [https://arxiv.org/abs/2604.02259](https://arxiv.org/abs/2604.02259)
- **선행 연구 (RAGS4EIC)**: [https://arxiv.org/abs/2403.15729](https://arxiv.org/abs/2403.15729)
