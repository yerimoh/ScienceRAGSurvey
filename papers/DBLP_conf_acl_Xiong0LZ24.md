---
notion_id: 355f2dcd-4912-8123-adc6-fa02ef47607e
title: Benchmarking Retrieval-Augmented Generation for Medicine
bib_key: DBLP:conf/acl/Xiong0LZ24
year: 2024
domain: medical, bio
type: dataset
venue: ACL (Findings)
paper_link: 
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Benchmarking Retrieval-Augmented Generation for Medicine

> ACL (Findings) | 2024 | dataset | medical · bio

## 한 줄 요약
의료 도메인 맞춤형 RAG 평가 벤치마크(MIRAGE)와 툴킷(MEDRAG)을 제안. PubMed, StatPearls, Textbooks, Wikipedia를 통합한 MedCorp와 다중 검색기 융합(RRF)이 가장 효과적임을 체계적으로 실증.

## 연구 배경 및 동기
- **기존 방법의 한계**: LLM은 의료 전문 영역에서 환각(Hallucination)과 노후화된 지식 문제를 겪고 있음
- **이 연구가 필요한 이유**: 의학 RAG에서 코퍼스·검색기·LLM의 유연한 구성 요소들을 최적으로 조합하는 Best Practice에 대한 체계적 평가와 가이드라인이 부재

## 시스템 아키텍처
```
[질문(Question) 입력]
      │  (Options 숨김, Question-Only Retrieval)
      ▼
[Retrieval: BM25 / Contriever / SPECTER / MedCPT]
      │
      ▼
[MedCorp 코퍼스 검색]
PubMed (23.9M) + StatPearls (9.3k) + Textbooks (18)
+ Wikipedia (6.5M) → 상위 32개 Snippet 추출
      │
      ▼
[RRF (Reciprocal Rank Fusion)]
다중 검색기 결과 융합 (RRF-2: BM25+MedCPT, RRF-4: 전체)
      │
      ▼
[Generation: GPT-4 / GPT-3.5 / Mixtral / Llama2 등]
검색된 Context + Question + Options 입력
→ Chain-of-Thought 프롬프팅 후 최종 답변
```

## 핵심 모듈 상세 설명
### 1. MIRAGE (평가 벤치마크)
- Zero-shot + Question-Only Retrieval(QOR) 설정 강제
- 5개 데이터셋 통합 7,663개 의료 QA 문항

### 2. MedCorp (통합 코퍼스)
| 코퍼스 | 문서 수 | 특성 |
|---|---|---|
| PubMed | 23.9M | 생의학 논문 |
| StatPearls | 9.3k | 임상 가이드 |
| Textbooks | 18 | 의학 전공 서적 |
| Wikipedia | 6.5M | 일반 지식 |
| **MedCorp 합계** | **30.4M** | **54.2M snippets** |

- 청크: LangChain RecursiveCharacterTextSplitter, 최대 1000자, 평균 221 토큰

### 3. 다중 검색기 융합 (RRF)
- **Lexical(BM25)** + **Semantic(MedCPT, Contriever, SPECTER)** 장점 결합
- RRF-2: BM25 + MedCPT (Biomed 특화 조합)
- RRF-4: BM25 + Contriever + SPECTER + MedCPT (전체)

## 실험 및 평가
**평가 태스크**: MIRAGE (MMLU-Med, MedQA-US, MedMCQA, PubMedQA*, BioASQ-Y/N)

**주요 결과 (MIRAGE 전체 Accuracy)**
| LLM 모델 | CoT 단독 | MEDRAG (MedCorp+RRF-4) | 향상 |
|---|---|---|---|
| GPT-4 | 73.44% | **79.97%** | +6.53%p |
| GPT-3.5 | 60.69% | 71.57% | +10.88%p |
| Mixtral 8x7B | 61.42% | 69.48% | +8.06%p |
| MEDITRON-70B | 57.04% | 60.18% | +3.14%p |
| PMC-LLaMA-13B | 36.82% | 46.52% | +9.70%p |

- GPT-3.5 + MEDRAG가 CoT GPT-4에 근접하는 향상 달성
- Lost-in-the-middle 현상 평가 포함 (정답 문맥 위치에 따른 성능 변화)

## 핵심 기여
1. 의료 영역 RAG 시스템을 위한 최초의 체계적 대규모 벤치마크(MIRAGE)와 툴킷(MEDRAG) 오픈소스 제공
2. 태스크 유형에 따라 최적 코퍼스와 검색기(MedCPT + BM25 조합 등)가 다름을 실험적으로 증명하고 Best Practice 가이드라인 제시

## 한계점
- 가장 기본적인 Vanilla RAG 아키텍처에만 초점 → Active RAG 등 최신 다이나믹 RAG 구조 평가 부족
- PubMed Central 전체 텍스트, 신뢰할 수 있는 FAQ 등 더 다양한 외부 자원이 코퍼스에 제외됨

## 관련 연구 및 관련 정보
- **논문**: (확인 후 추가 필요)
- **GitHub (MEDRAG)**: [https://github.com/Teddy-XiongGZ/MedRAG](https://github.com/Teddy-XiongGZ/MedRAG)
- **GitHub (MIRAGE)**: [https://github.com/Teddy-XiongGZ/MIRAGE](https://github.com/Teddy-XiongGZ/MIRAGE)
