---
title: "Seeing the Forest Through the Trees: Knowledge Retrieval for Streamlining Particle Physics Analysis"
bib_key: "mcgreivy2025seeing"
year: 2025
domain: physics
type: method
venue: arXiv preprint (arXiv:2509.06855)
paper_link: https://arxiv.org/abs/2509.06855
---
# Seeing the Forest Through the Trees: Knowledge Retrieval for Streamlining Particle Physics Analysis

mcgreivy2025seeing | 2025 | arXiv preprint | method | [physics] | [paper](https://arxiv.org/abs/2509.06855)

**DB**: LHCb experiment corpus (CERN)
**DB size**: 명시 안됨; LHCb 실험 내부 문서·논문 코퍼스
**DB Open/Private**: Internal (LHCb 실험 내부 문서), 코드 오픈소스
**Modality**: ['Text']
**Retriever**: SciTreeRAG (계층적 트리 구조), SciGraphRAG (지식 그래프)
**Eval Task**: 입자물리학 문헌 질의응답 (전문가 평가)
**Eval Metric**: 질적 평가 (컨텍스트 품질, 문서 간 관계 커버리지)
**Method Name**: SciTreeRAG + SciGraphRAG

> arXiv preprint | 2025 | method | physics
#### 한 줄 요약
LHCb 실험의 문서 코퍼스를 대상으로, 표준 RAG의 국소적 청크 매칭 한계를 극복하는 두 가지 구조화 검색 시스템 제안. **SciTreeRAG**: 물리학 논문의 계층 구조(섹션 트리)를 활용하여 문서 간 맥락 연결 강화. **SciGraphRAG**: LLM으로 코퍼스를 지식 그래프로 변환, 글로벌 교차 문서 관계 검색. 비전문가의 LHC 공개 데이터 분석 지원을 목표로 한다.

#### 개발/구축 배경
**기존 방법의 한계**
- 표준 RAG: 의미적으로 유사한 텍스트 청크를 매칭하지만 관련 정보가 여러 섹션에 분산될 때 맥락 분절(fragmented representation) 발생
- 전체 문서 컨텍스트: 긴 물리학 논문에서 토큰 한계 초과, 불필요 정보 포함
- 입자물리학은 실험별 고유 방법론·기호·용어로 도메인 특화 지식 필요

**이 시스템이 필요한 이유**
- 대규모·장기 실험 협업(LHCb ~1,600명 협력자)의 방법론·편집 검토 가속화
- 비전문가가 공개된 LHC 데이터를 LLM 기반 시스템으로 분석 가능하도록 지원
- INSPIRE-HEP 문헌과 내부 기술 문서를 통합하여 교차 문서 전문 지식 접근

#### 방법론
**SciTreeRAG**:
1. 물리학 논문의 계층 구조(섹션·소절 트리) 파싱
2. 트리 노드별 요약 생성 및 부모-자식 맥락 연결
3. 쿼리 시 계층적 트리 순회로 집중적(focused)이고 맥락 풍부한 청크 검색

**SciGraphRAG**:
1. LLM으로 코퍼스 내 엔티티(입자, 알고리즘, 파라미터)와 관계 추출
2. 지식 그래프 구축
3. 쿼리를 그래프 탐색으로 변환, 표준 RAG로 놓치는 글로벌 도메인 연결 검색

#### 실험 설정
- **코퍼스**: LHCb 실험 문서·논문
- **응용**: 방법론 리뷰, 편집 표준 확인, 비전문가 데이터 분석 지원
- **LLM 백본**: GPT-4 계열 (명시 안됨)
- **평가**: 전문가 질적 평가 (수치 벤치마크 없음)

#### 주요 결과
- SciTreeRAG: 표준 RAG 대비 더 집중적이고 맥락이 풍부한 답변 생성 (전문가 평가)
- SciGraphRAG: 문서 간 글로벌 도메인 연결(표준 RAG에서 놓치는) 검색 가능
- LHCb 코퍼스에서 개념 증명(proof-of-concept) 성공

#### 한계점
- 수치 벤치마크 없음 — 전문가 질적 평가만으로 객관적 비교 어려움
- LHCb 내부 문서 코퍼스에 한정 — 다른 실험/도메인으로의 일반화 미검증
- 지식 그래프 구축 비용 (LLM 기반 추출) 대규모 코퍼스에서 높음
- SciGraphRAG의 그래프 품질은 LLM 추출 정확도에 의존

## 관련 정보
- **논문**: [https://arxiv.org/abs/2509.06855](https://arxiv.org/abs/2509.06855)
