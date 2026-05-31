---
title: "BioRAGent: A Retrieval-Augmented Generation System for Showcasing Generative Query Expansion and Domain-Specific Search for Scientific Q&A"
bib_key: "DBLP:conf/ecir/AteiaK25"
year: 2025
domain: bio, medical
type: Method
venue: ECIR
paper_link: https://doi.org/10.1007/978-3-031-88720-8_1
---
# BioRAGent: Generative Query Expansion RAG for Biomedical Q&A
> ECIR 2025 | Method | bio · medical

## 한 줄 요약
LLM 기반 생성형 query expansion과 PubMed 검색(Elasticsearch/BM25)을 결합한 생물의학 RAG 데모 시스템으로, 검색 과정을 투명하게(확장 쿼리 편집 가능) 노출하고 PubMed ID 인용을 문장 단위로 부착하는 대화형 Q&A 인터페이스를 보여준다. BioASQ 2024 챌린지 참가 경험을 바탕으로 구축되었다.

## 시스템 구조 (BioRAGent Architecture)
Gradio 기반 웹 애플리케이션이며 네 가지 구성요소로 이루어진다.
- **Generative query expansion (LLM):** LLM이 few-shot(3-shot)으로 원 질문에 동의어·연관어를 포함한 확장 쿼리를 생성한다. 사용자는 실행 후 확장 쿼리를 검사·수정할 수 있어 검색이 투명하고 제어 가능하다.
- **Document retrieval & snippet extraction:** Elasticsearch를 검색 엔진으로 쓰며 인덱스는 2023 snapshot의 PubMed 기사(초록·제목)이다. 기본 BM25로 상위 50개 기사를 검색한 뒤, LLM이 few-shot으로 관련 snippet을 추출하고 다시 few-shot으로 질문 관련성에 따라 rerank한다.
- **Answer generation:** 검색된 snippet을 근거로 답변을 생성한다(아래 두 형식).
- **User interface (대화형 UI):** 질문 입력창·검색 버튼, 편집 가능한 확장 쿼리 박스, 인용 유무 두 답변 박스, PubMed 링크가 달린 snippet 목록을 표시한다.

few-shot 예시는 BioASQ training set에서 가져오며, query expansion에서는 highest F1 기준으로 예시를 샘플링한다.

## 동작 파이프라인 (inference)
1. 사용자가 질문 입력 → LLM이 3-shot으로 확장 쿼리 생성(사용자 편집 가능).
2. 확장 쿼리로 Elasticsearch(BM25) 검색 → 상위 50개 PubMed 기사 획득.
3. LLM이 few-shot으로 snippet 추출 → 다시 few-shot으로 질문 관련성에 따라 snippet rerank.
4. snippet에 grounding하여 두 가지 답변 생성:
   - **짧은 단락형 답변** — 검색 정보로 grounding(이 형식이 BioASQ 챌린지에서 사용됨).
   - **인용 포함 단락형 답변** — 문장마다 PubMed ID 형태의 inline citation 부착.
5. UI에 확장 쿼리, 두 답변(인용 유/무), PubMed 직링크가 달린 snippet 목록 표시.

## 평가/구성
- **BioASQ 2024(12th BioASQ challenge)** 참가에서 상용·오픈소스 LLM 모두로 경쟁력 있는 성능을 보였고 여러 1·2위를 차지했다(질의응답 12B Phase A+/Phase B에서 가장 경쟁력). RAG 접근 자체의 평가/공개는 저자들의 BioASQ 2024 참가 선행 연구에 근거한다.
- 사용 LLM: Google **Gemini 1.5 flash 002**(속도·저비용 이유).
- 본 논문은 시스템을 시연하는 **데모 논문**으로, 별도의 정량 수치를 새로 제시하지는 않는다.

## 한계점
- 정량 평가 결과를 새로 제시하지 않는 데모 시스템 논문이다(성능 근거는 BioASQ 2024 선행 참가에 의존).
- 단일 LLM(Gemini 1.5 flash 002) 고정, 라이브 평가/할루시네이션 검증 미내장, 템플릿 정적 구성이 현재 제약(향후 prompt 라이브 편집, hallucination 탐지, 다중 LLM 선택 지원 계획).
- 단일 PubMed 스냅샷(2023)에 한정되며 BM25 + LLM rerank 외 별도 dense retrieval은 사용하지 않는다.

## 관련 정보
- arXiv: 2412.12358 (https://arxiv.org/abs/2412.12358)
- DOI: https://doi.org/10.1007/978-3-031-88720-8_1 (ECIR 2025)
- Demo: https://bioragent.samyateia.de/ · GitHub: https://github.com/SamyAteia/BioRAGent
- 저자: Samy Ateia, Udo Kruschwitz
