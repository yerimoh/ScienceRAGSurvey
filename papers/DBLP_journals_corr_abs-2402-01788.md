---
title: "LitLLM: A Toolkit for Scientific Literature Review"
bib_key: "DBLP:journals/corr/abs-2402-01788"
year: 2024
domain: general
type: Method
venue: arXiv
paper_link: https://arxiv.org/abs/2402.01788
---
# LitLLM: A RAG Toolkit for Scientific Literature Review
> arXiv 2024 | Method | general

## 한 줄 요약
LitLLM은 사용자 abstract를 입력받아 후보 참고문헌 검색 → 재랭킹 → related work 생성을 수행하는 모듈식 RAG 툴킷으로, 검색 기반 grounding과 plan 기반 제어 생성으로 환각·구식 정보 문제를 완화해 문헌 리뷰 초안 작성을 돕는다.

## 시스템 구조 (LitLLM Architecture)
세 모듈로 구성되며 각 컴포넌트의 LLM을 자유롭게 교체할 수 있다.
- **(1) Retrieval:** Semantic Scholar API·OpenAlex API 사용. LLM이 입력 abstract를 검색 키워드로 요약(사용자가 키워드·seed paper 추가 가능). 관련도·인용수·연도로 정렬.
- **(2) Re-ranking:** 초록 기반 검색의 낮은 정밀도를 보완. 핵심은 instructional permutation generation(RankGPT 계열) — 후보 목록을 한꺼번에 주고 관련도 내림차순 순열을 LLM이 생성. 보조로 debate-style(포함 찬반 논거 + 확률) 랭킹.
- **(3) Plan-based Generation:** zero-shot RAG 생성과, "plan"(문장 수 + 줄별 인용 기술)으로 출력 구조를 제어하는 plan-based 생성 지원.
- **(4) Toolkit/UI:** React 인터페이스(초록 입력, 키워드 표시, 재랭킹 결과, sentence plan 입력, related work 출력). LLM은 GPT-3.5-turbo·GPT-4(교체 가능).

## 동작 파이프라인 (inference)
1. 사용자가 abstract 입력.
2. LLM이 검색 키워드로 요약(+사용자 키워드/seed paper).
3. Semantic Scholar/OpenAlex로 후보 검색.
4. LLM permutation(또는 debate-style)으로 재랭킹.
5. (선택) sentence plan 입력.
6. zero-shot 또는 plan-based로 related work 초안 생성.

## 주요 결과/기능
- 정량 벤치마크 수치는 보고되지 않음. 연구자 5인 대상 예비 사용자 연구 수행.
- 정성 피드백: zero-shot은 더 풍부, plan-based는 자기 논문에 더 맞춤·접근성 높음.
- 검색·재랭킹·생성 각 단계 LLM 교체 가능한 모듈식 설계, 정렬 옵션 제공.

## 한계점
- 질의·검색 논문 모두 초록만 사용(전문 ingest는 향후 과제).
- 검색 API 범위 한정(Google Scholar 등 확장 필요).
- 5인 규모 예비 연구만, 경쟁 시스템 대비 정량 벤치마크 부재.
- 생성 결과의 환각 주의 및 LLM 사용 공개 권고.

## 관련 정보
- arXiv: 2402.01788 (https://arxiv.org/abs/2402.01788)
- 프로젝트: https://litllm.github.io · 데모 영상 https://youtu.be/E2ggOZBAFw0
