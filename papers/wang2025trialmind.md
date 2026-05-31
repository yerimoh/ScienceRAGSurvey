---
title: "Accelerating clinical evidence synthesis with large language models"
bib_key: "wang2025trialmind"
year: 2025
domain: medical
type: Method
venue: npj Digital Medicine
paper_link: https://doi.org/10.1038/s41746-025-01840-7
---
# TrialMind: LLM Pipeline for Clinical Evidence Synthesis
> npj Digital Medicine 2025 | Method | medical

## 한 줄 요약
TrialMind는 임상 근거 합성의 핵심 단계인 문헌 검색 → 스크리닝 → 데이터 추출 → 근거 합성을 LLM으로 수행하는 인간-AI 협업(human-in-the-loop) 파이프라인으로, 각 단계 중간 산출물을 사용자가 검토·수정할 수 있게 설계해 체계적 문헌고찰 워크플로를 가속한다.

## 시스템 구조 (TrialMind Architecture)
주 backbone은 GPT-4(gpt-4-0125-preview). 근거 합성을 4개 모듈로 분해한다.
1. **Literature search:** PICO 요소를 입력받아 Boolean 쿼리 생성 후 PubMed 검색.
2. **Literature screening:** 적격 기준에 따라 후보 연구의 관련성 평가·순위화.
3. **Data extraction:** 연구 특성·임상 결과지표 추출(원문 위치 연결).
4. **Evidence synthesis:** 추출 결과를 표준화해 meta-analysis·forest plot으로 통합.

파이프라인 전반에 In-Context Learning, RAG(검색된 abstract로 프롬프트 보강), Chain-of-Thought를 결합한다. **Human-in-the-loop:** 적격 기준 편집, 추출 데이터의 원문 위치 검증, 집계 전략 조정이 가능해 단계 간 오류 전파를 차단.

## 동작 파이프라인 (inference)
1. **검색:** PICO → ICL로 Boolean 쿼리 생성, RAG+CoT로 용어 보강(식별→필터링→확장) → PubMed 제출.
2. **스크리닝:** 적격 기준 생성(편집 가능) → 후보를 기준별 −1/0/+1로 병렬 평가·합산해 순위화(상위 2,000개 대상, 근거 동반).
3. **추출:** 일반 필드는 전체 문서에서 값+위치 추출. 결과는 (i) 식별(CoT) → (ii) 수치 추출 → (iii) LLM이 Python 코드 생성·실행해 표준화 효과측정치 산출.
4. **합성:** 표준화 수치를 R 'meta' 패키지로 집계해 forest plot·통합 추정치 생성.

## 주요 결과
| 단계/지표 | TrialMind | 비교군 |
|---|---|---|
| 검색 Recall(평균) | 0.782 | GPT-4 0.073 / Human 0.187 |
| 스크리닝 상위 100 내 목표 포착 | >80% | — |
| 결과 추출 정확도(Immunotherapy) | 0.70 | GPT-4 0.54 |
| 결과 추출 정확도(Hyperthermia) | 0.84 | GPT-4 0.52 |
| 결과 추출 best baseline 대비 | 중앙값 1.50배 | — |

근거 합성 인간 평가(승률, 5개 연구): 87.5/100/62.5/62.5/81.2%. User study: 스크리닝 recall +71.4%·시간 −44.2%, 추출 정확도 +23.5%·시간 −63.4%.

## 한계점
- 결과(result) 추출이 가장 약한 고리(부정확/추출실패/환각). 'overall response'와 'complete response' 같은 정의 혼동에서 환각 발생.
- 표준화·합성의 forest plot은 인간 전문가가 R로 수행(수동 검증 전제).
- 평가가 4개 암 치료 영역에 한정.

## 관련 정보
- arXiv: 2406.17755 · DOI: 10.1038/s41746-025-01840-7 (npj Digital Medicine 2025)
- 저자: Zifeng Wang, Lang Cao, Benjamin Danek, Qiao Jin, Zhiyong Lu 외
- 데이터 TrialReviewBench: 4개 암 치료 영역 체계적 문헌고찰 100건 + 임상연구 2,220건 주석
