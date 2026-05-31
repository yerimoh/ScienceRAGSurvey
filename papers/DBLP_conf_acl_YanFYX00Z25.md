---
title: "SurveyForge: On the Outline Heuristics, Memory-Driven Generation, and Multi-dimensional Evaluation for Automated Survey Writing"
bib_key: "DBLP:conf/acl/YanFYX00Z25"
year: 2025
domain: general
type: Method
venue: ACL
paper_link: https://arxiv.org/abs/2503.04629
---
# SurveyForge: Outline-Heuristic, Memory-Driven Survey Generation
> ACL 2025 | Method | general

## 한 줄 요약
SurveyForge는 인간이 쓴 서베이의 구조를 휴리스틱으로 학습해 개요를 생성하고, 메모리 기반 검색 에이전트(SANA)로 고품질 참고문헌을 확보한 뒤 섹션을 병렬 생성·정제해 자동으로 학술 서베이를 작성하는 프레임워크다.

## 시스템 구조 (SurveyForge Architecture)
두 개의 지식 베이스를 사용한다: arXiv CS 약 600,000편(제목·초록)의 Research Paper DB와, 약 20,000편 리뷰에서 추출한 계층 개요의 Survey Outline DB.

- **(A) Outline Heuristics — 인간 서베이에서 구조 학습:** 주제 T에 대해 관련 논문과 인간 서베이 개요를 함께 검색하고, 인간 개요를 데모로 제공해 1차 개요 생성 → 섹션별 재검색으로 2차 개요 생성 → 병합. (개요 품질: 휴리스틱 미사용 81.78 → 도메인 특화 개요 사용 86.67.)
- **(B) Memory-driven Scholar Navigation Agent (SANA):** ① Memory for Sub-query(MS) — 메모리를 컨텍스트로 복잡 쿼리를 서브쿼리로 분해, ② Memory for Retrieval(MR) — 전체 DB 대신 개요 연관 메모리로 후보 검색(섹션 간 고립·중복 방지), ③ Temporal-aware Reranking(TRE) — 관련성·인용 영향력·최신성을 2년 버킷으로 균형 재랭킹.
- **섹션 생성:** 재랭킹된 문헌으로 서브섹션을 병렬 생성 → 초안 결합 → LLM 정제로 중복 제거·통합.

## 동작 파이프라인 (inference)
1. 주제 입력 → 논문·인간 개요 검색.
2. 휴리스틱으로 1차 개요 → 섹션별 재검색 후 2차 개요 → 병합.
3. SANA: 서브쿼리 분해(MS) → 메모리 기반 검색(MR) → 시간·인용·관련성 재랭킹(TRE).
4. 서브섹션 병렬 생성 → 결합 → 정제 → 최종 서베이.
- 효율(GPT-4o mini): 약 $0.43/서베이, 약 10분.

## 주요 결과
평가 벤치마크 **SurveyBench**(CS 10개 주제, 인간 서베이 ~100편), 지표 SAM-R/O/C.

| Model | Method | Reference Cov. | Outline | Content Avg |
|---|---|---|---|---|
| GPT-4o mini | AutoSurvey | 0.2035 | 83.10 | 75.05 |
| GPT-4o mini | **SurveyForge** | **0.4236** | **86.62** | **77.06** |
| Human | — | 0.6294 | 87.62 | — |

Win-rate(vs AutoSurvey): Outline 73~75%, Content 69~70%(PhD 20인 평가, Cohen's κ 0.65~0.72). Ablation: MR+MS+TRE가 최고(Reference Cov. 0.397).

## 한계점
- 여러 출처 간 관계 분석·종합 능력이 부족(요약은 강하나 비교·진화 분석 약함).
- LLM 환각으로 부정확 인용·주장이 간헐 발생.
- 인간 저자 특유의 비판적 사고·독창성 결여.

## 관련 정보
- arXiv: 2503.04629 (https://arxiv.org/abs/2503.04629) · ACL 2025
- 코드: https://github.com/Alpha-Innovator/SurveyForge · 데이터 SurveyBench(HuggingFace U4R/SurveyBench)
