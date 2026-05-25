---
title: "MatClaw: An Autonomous Code-First LLM Agent for End-to-End Materials Exploration"
bib_key: "zhang2026matclaw"
year: 2026
domain: material
type: Method
venue: arXiv 2026
paper_link: https://arxiv.org/abs/2604.02688
---
# MatClaw: An Autonomous Code-First LLM Agent for End-to-End Materials Exploration

zhang2026matclaw | 2026 | arXiv 2026 | Method | [material] | [paper](https://arxiv.org/abs/2604.02688)

**Retriever**: RAG over domain source code (pymatgen, atomate2, jobflow, dpdata, DeePMD-kit)
**Eval Task**: Machine-learning force field training (active learning), Curie temperature prediction, heuristic parameter-space search
**Eval Metric**: Per-step API-call accuracy (~99%), end-to-end task completion
**Method Name**: MatClaw
**Modality**: Code, Text, Computational materials data

> arXiv 2026 | 2026 | Method | material
#### 📌 한 줄 요약
Python 코드를 직접 작성·실행하는 코드 우선(code-first) LLM 에이전트로, 도메인 소스 코드에 대한 RAG와 4층 메모리 아키텍처를 결합하여 ~99% API 호출 정확도와 HPC 클러스터 기반 다중 코드 워크플로 오케스트레이션을 달성하는 재료 탐색 자율 에이전트이다.

#### 🎯 개발/구축 배경
**기존 접근법의 한계**
- 기존 계산 재료과학용 LLM 에이전트는 특정 시뮬레이션 코드에 고정된 파이프라인 아키텍처와 수동 작성 도구 함수에 의존
- 태스크 범위가 확대될수록 도구 함수 수도 급증하는 확장성 문제

**이 시스템이 필요한 이유**
- 여러 도메인 라이브러리(pymatgen, atomate2 등)를 자유롭게 조합하는 멀티 코드 워크플로 자동화 필요
- 다중 일 단위의 긴 워크플로에서 컨텍스트 손실 방지 메모리 관리 필요

#### 🔨 시스템 구성
MatClaw는 사전 정의된 도구 함수 없이 Python을 직접 생성·실행하여 설치된 도메인 라이브러리를 자유롭게 조합한다. **4층 메모리 아키텍처**: 진행 중 컨텍스트 손실을 방지한다. **RAG over 도메인 소스 코드**: pymatgen, atomate2, jobflow, dpdata, DeePMD-kit 소스 코드를 검색하여 per-step API 호출 정확도를 ~99%로 향상시킨다. 원격 HPC 클러스터에서 워크플로를 오케스트레이션한다.

#### 📊 주요 결과
| 항목 | 수치 |
|---|---|
| API 호출 정확도 | ~99% (RAG over domain source code) |
| 지원 라이브러리 | pymatgen, atomate2, jobflow, dpdata, DeePMD-kit |
| 시연 태스크 1 | CuInP2S6 머신러닝 포스 필드 훈련 (active learning) |
| 시연 태스크 2 | Curie 온도 예측 |
| 시연 태스크 3 | 휴리스틱 파라미터 공간 탐색 |
| 코드 생성 신뢰성 | 높음 (강점 확인) |
| tacit 도메인 지식 처리 | 부족 (한계 확인) |

#### ⚠️ 한계점
- 묵시적(tacit) 도메인 지식(적절한 시뮬레이션 타임스케일, 평형화 프로토콜, 샘플링 전략)에서 어려움
- 문헌 자기학습(literature self-learning) 및 전문가 제약 지정으로 이 격차를 부분적으로 보완하지만 완전 자율은 아직 미달
- 다중 일 단위 워크플로에서 중간 오류 복구가 과제

## 관련 정보
- **논문 (arXiv)**: [https://arxiv.org/abs/2604.02688](https://arxiv.org/abs/2604.02688)
