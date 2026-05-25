---
title: "Medical Graph RAG: Evidence-based Medical Large Language Model via Graph Retrieval-Augmented Generation"
bib_key: "DBLP:conf/acl/WuZQCXMJG25"
year: 2025
domain: medical
type: method
venue: ACL 2025
paper_link: https://aclanthology.org/2025.acl-long.1381/
---
# Medical Graph RAG: Evidence-based Medical Large Language Model via Graph Retrieval-Augmented Generation

DBLP:conf/acl/WuZQCXMJG25 | 2025 | ACL 2025 | method | [medical] | [paper](https://aclanthology.org/2025.acl-long.1381/)

**DB**: MedC-K (Medical Corpus — Knowledge; UMLS-aligned medical literature retrieval corpus)
**DB size**: 논문 미기재 (UMLS 정렬 의학 문헌 코퍼스)
**DB Open/Private**: Open
**Modality**: ['Text']
**Retriever**: Graph-based retrieval (U-retrieve: UMLS entity→subgraph traversal)
**Eval Task**: Medical VQA (NEJM, Medbullets, JAMA), Medical QA (MedQA, PubMedQA)
**Eval Metric**: Accuracy
**Method Name**: MedGraphRAG

> ACL 2025 | 2025 | method | medical
#### 📌 한 줄 요약
UMLS 지식 그래프를 백본으로 활용하는 그래프 RAG 시스템으로, 의학 문헌 코퍼스(MedC-K)에서 엔티티 기반 서브그래프를 검색해 임상 질의응답의 근거 신뢰성을 높인다.

#### 🎯 개발/구축 배경
**기존 인프라의 한계**
- 기존 의학 RAG 시스템은 텍스트 청크 유사도 검색에 의존해 의학 개념 간 관계를 활용하지 못했다
- 단순 밀집 검색(dense retrieval)은 희귀 질환·복합 임상 조건에서 근거 문서를 누락하는 경향이 있었다
- LLM의 의학 추론은 hallucination이 빈번하고 근거 출처를 추적하기 어려웠다

**이 시스템이 필요한 이유**
- UMLS 기반 그래프 구조로 의학 개념 간 계층·관계를 탐색해 더 풍부한 컨텍스트를 제공할 필요가 있다
- 임상 환경에서는 근거(evidence)의 출처를 명시할 수 있는 설명 가능한 검색이 필수적이다

#### 🔨 시스템 구성
MedGraphRAG는 세 단계로 구성된다.
1. **Entity extraction**: 쿼리에서 의학 개념 추출 후 UMLS에 매핑 (U-retrieve)
2. **Graph traversal**: UMLS 서브그래프를 BFS/DFS로 확장하여 관련 개념·관계 수집
3. **Generation**: 검색된 서브그래프 + 관련 문헌 청크(MedC-K)를 컨텍스트로 LLM 생성

UMLS의 Semantic Network(135 의미 유형)를 그래프 엣지 필터로 활용해 노이즈 제거.

#### 📥 데이터 접근 방법
| 방법 | 설명 |
|---|---|
| GitHub (코드) | https://github.com/JoeyAlvarezMD/MedGraphRAG (공개 코드) |
| MedC-K 코퍼스 | UMLS-aligned corpus; 논문에서 공개 계획 명시 |

#### 📤 제공 데이터 형식
- 의학 개념-문서 매핑 인덱스
- UMLS 서브그래프 JSON
- 생성 응답 + 근거 문서 목록

#### 📊 주요 통계 (논문 기준)
| 항목 | 수치 |
|---|---|
| 평가 벤치마크 | NEJM challenge, Medbullets, JAMA Clinical Challenge, MedQA, PubMedQA |
| 비교 베이스라인 | GraphRAG, NaiveRAG, MedRAG, 등 |
| 게재 | ACL 2025 Long Paper (pp. 28443–28467) |

#### ⚠️ 한계점
- UMLS 매핑 품질에 의존: 어휘 범위 밖 희귀 질환·신흥 의학 용어 처리 제한
- 그래프 탐색 비용이 높아 실시간 임상 시스템 적용에 지연 발생 가능
- MedC-K 코퍼스의 구체적 규모와 구성이 논문에 충분히 기술되지 않음

## 관련 정보
- **논문**: [Wu et al., ACL 2025](https://aclanthology.org/2025.acl-long.1381/)
