---
notion_id: 355f2dcd-4912-8187-976c-c5f6caf063a5
title: PaperQA - Retrieval-Augmented Generative Agent for Scientific Research
bib_key: DBLP:journals/corr/abs-2312-07559
year: 2023
domain: bio, medical
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2312.07559v2
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# PaperQA: Retrieval-Augmented Generative Agent for Scientific Research

> arXiv | 2023 | Method | bio, medical

## 한 줄 요약
과학 문헌을 동적으로 검색, 추출, 요약하여 환각(Hallucination) 없이 정확하게 출처를 인용하는 에이전트 기반의 RAG 시스템.

## 연구 배경 및 동기
- **기존 방법의 한계점**: 기존 LLM은 환각 현상이 발생하기 쉽고, 학습 데이터 컷오프 이후의 최신 과학적 사실을 알지 못하는 한계가 있음.
- **이 연구가 필요한 이유**: 일반적인 RAG 파이프라인은 고정된 선형 단계로 구성되어 있어, 과학자들이 직면하는 다양하고 복잡한 질문에 유연하게 대응하기 어려움.

## 시스템 아키텍처
1. 사용자 질문 입력
2. **Agent LLM**이 도구 선택
3. **[Search 도구]** 키워드로 논문 검색 및 청크 분할 임베딩
4. **[Gather Evidence 도구]** MMR로 청크 회수 후 Summary LLM이 요약 및 채점
5. **[Answer Question 도구]** Ask LLM으로 사전 지식을 모으고 Answer LLM이 최종 답변 및 인용 생성
6. 에이전트가 검토 후 최종 출력 도출

## 핵심 모듈 상세 설명
- **Search 모듈**: 에이전트가 쿼리를 생성하여 Google Scholar, PubMed 등의 API를 호출. 수집된 논문을 4,000자 단위로 나누고 `text-embedding-ada-002`를 통해 벡터화.
- **Gather Evidence 모듈**: 질문 벡터와 비교하여 MMR 방식으로 텍스트를 불러옴. Summary LLM(GPT-3.5)이 각 청크를 질문 관점에서 요약하고 1에서 10점의 관련성 점수를 부여해 상위 문서를 필터링.
- **Answer Question 모듈**: LLM의 내재적 지식(Ask LLM)과 검색된 증거들을 합쳐 Answer LLM(GPT-4)에 제공. 모델은 반드시 제공된 증거를 기반으로 문장 끝에 인용구를 포함한 답변을 작성.

## 실험 및 평가
- **평가 태스크**: LitQA (자체 제작), PubMedQA, MedQA-USMLE, BioASQ
- **주요 평가 결과**:
	- LitQA 벤치마크에서 기존 상용 도구(Scite, Perplexity 등) 및 베이스라인 모델들을 큰 차이로 앞질렀음.
	- 인간 생의학 전문가 수준의 정답률(69.5% vs 인간 87.9% 정확도)을 달성함.
	- 자체 테스트 결과 환각(Hallucinated citation) 비율이 0%로 측정되어 신뢰성을 크게 높임.

## 핵심 기여
- 검색, 요약, 답변 생성을 독립된 모듈(도구)로 분리하고 이를 LLM 에이전트가 능동적으로 조율하게 함으로써 과학적 질문 해결의 유연성과 정확성을 확보.
- 최신 논문의 전체 텍스트 검색을 강제하는 신규 벤치마크인 'LitQA'를 성공적으로 구축.

## 한계점
- 시스템이 참조하는 원본 논문의 정보 자체가 틀렸을 가능성에는 대처하기 어려움.
- 시간이 지나면서 과학적 사실이 업데이트될 수 있어, 특정 답변의 유효기간이 존재할 수 있음.

## 관련 연구 및 관련 정보
- 논문 링크: [https://arxiv.org/abs/2312.07559v2](https://arxiv.org/abs/2312.07559v2)
