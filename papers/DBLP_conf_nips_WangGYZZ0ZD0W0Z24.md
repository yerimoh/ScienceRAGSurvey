---
title: "AutoSurvey: Large Language Models Can Automatically Write Surveys"
bib_key: "DBLP:conf/nips/WangGYZZ0ZD0W0Z24"
year: 2024
domain: general
type: Method
venue: NeurIPS
paper_link: https://arxiv.org/abs/2406.10252
---
# AutoSurvey: Automatic Survey Writing with LLMs
> NeurIPS 2024 | Method | general

## 한 줄 요약
AutoSurvey는 (1) 검색 → (2) 개요 생성 → (3) 병렬 섹션 초안 → (4) 인용 인지 통합·정제의 4단계 파이프라인으로, LLM의 컨텍스트 한계와 전문성 부족을 우회해 종합적 학술 서베이를 자동 작성하는 시스템이다.

## 시스템 구조 (AutoSurvey Architecture)
- **검색(Retrieval):** RAG 방식. arXiv CS 논문 약 530,000편을 코퍼스로 두고, `nomic-embed-text-v1.5`로 각 논문 제목·초록을 임베딩해 유사도로 랭킹. 초기 1,200편, 서브섹션 단계에서 설명별 60편 검색.
- **개요(outline) 생성:** 초기 검색 논문을 30,000 토큰 청크로 나눠 청크별 개요를 만든 뒤 병합. 섹션 수는 8개로 고정.
- **병렬 섹션 초안:** 작성 LLM은 Claude-3-Haiku(속도·비용). 개요에 따라 각 서브섹션을 병렬 생성하며 참조 논문을 인용.
- **통합·정제(Integration & Refinement):** 인용을 추출해 arXiv 논문에 매핑, 앞뒤 섹션 문맥을 고려해 중복 제거·가독성 향상·인용 정확성 점검.
- **평가용 LLM judge:** GPT-4·Claude-3-Haiku·Gemini-1.5-Pro 조합으로 후보 서베이를 평가해 최고본 선택(N=2).

## 동작 파이프라인 (inference)
1. 주제 입력.
2. 초기 검색(1,200편) + 청크별 개요 생성 → 병합 → 8개 섹션 개요 확정.
3. 서브섹션별 60편 추가 검색 → Claude-3-Haiku가 병렬 초안 작성(인용 포함).
4. 인용 추출·매핑 → 섹션 정제(중복 제거, 인용 점검).
5. Multi-LLM-as-Judge 평가 → 후보 중 최고 서베이 선택.

## 주요 결과
**Citation Quality (64k tokens)**

| 방법 | Recall(%) | Precision(%) |
|---|---|---|
| AutoSurvey | 82.25 | 77.41 |
| Naive RAG | 68.79 | 61.97 |
| Human | 86.33 | 77.78 |

**Content Quality (64k, 5점)**: AutoSurvey Coverage 4.73 / Structure 4.33 / Relevance 4.86 (Human 5.00 / 4.66 / 5.00).
**속도**: AutoSurvey 73.6 surveys/hour vs Human 0.07. 도메인 지식 문제 정확도 직접 답변 대비 +9.2%.

## 한계점
- 인용 recall·content 품질이 인간에 약간 못 미침(특히 recall·structure).
- 섹션 수 8개 고정으로 구조 유연성 제한.
- 검색 코퍼스가 arXiv CS 약 530K편에 한정(도메인 일반화 미검증).
- 초기 단계는 초록만, 초안 단계는 본문 앞부분(~1,500 토큰)만 사용.

## 관련 정보
- arXiv: 2406.10252 (https://arxiv.org/abs/2406.10252) · NeurIPS 2024
- 작성 LLM Claude-3-Haiku / 평가 LLM GPT-4·Claude-3-Haiku·Gemini-1.5-Pro / 임베딩 nomic-embed-text-v1.5
