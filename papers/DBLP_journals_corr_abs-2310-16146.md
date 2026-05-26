---
title: CLINFO.AI - An Open-Source Retrieval-Augmented Large Language Model System for Answering Medical Questions Using Scientific Literature
bib_key: DBLP:journals/corr/abs-2310-16146
year: 2024
domain: medical
type: benchmark
venue: PSB (Pacific Symposium on Biocomputing)
paper_link: https://arxiv.org/abs/2310.16146
---
# CLINFO.AI / PubMedRS-200

> PSB 2024 | Method + Benchmark | medical
> Lozano, Min, Bhatt, Cilliers, Vasan, Chen, Sang, Yerlan, Bacares, Yung, Falakaflaki, Perez, Liu, Haber — Stanford / UCSF / UC Davis
> DBLP: `journals/corr/abs-2310-16146`

## 한 줄 요약
PubMed 체계적 문헌 고찰(Systematic Review) **200건**의 제목(질문)과 결론(정답)으로 구성한 **PubMedRS-200** 벤치마크와, PubMed RAG + IEEE 스타일 인용 합성을 수행하는 오픈소스 의료 RAG 시스템 **Clinfo.AI**를 함께 제안. 요약 품질을 UniEval·COMET·CTC로 평가하며 GPT-4에 근접한 UniEval Overall 0.840을 달성.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 소스 선정 (체계적 문헌 고찰)
  임상의들이 근거 중심 의학에 활용하는 Systematic Review(SR)를 기준 채택
  이유: 인간 전문가가 이미 관련 문헌을 필터링하고 결론 도출 → Gold Standard로 적합

Step 2 — PubMed SR 검색 (Entrez API)
  다양한 의학 하위 분야를 커버하는 SR 검색
  필터: 제목(Title)에 명시적 질문(물음표) 형태가 포함된 논문만 선택

Step 3 — 수동 품질 검증
  저자 2명이 질문-결론 쌍을 독립적으로 검토
  초록의 Results·Conclusions 섹션 텍스트를 정제 → 정답(Answer) 구성

Step 4 — 최종 데이터셋 구성
  ┌──────────────────────────┬─────────────────────────────┐
  │ 필드                     │ 설명                         │
  ├──────────────────────────┼─────────────────────────────┤
  │ Question                 │ SR 논문 제목 (질문 형태)      │
  │ Answer                   │ Results/Conclusions 정제본   │
  │ Context                  │ Introduction 기반 배경 정보  │
  │ References               │ SR에서 참조한 PubMed IDs    │
  │ Topic / Subtopic         │ 의료 전문과목 및 세부 분야    │
  │ Published Date           │ 논문 출판일                  │
  ├──────────────────────────┼─────────────────────────────┤
  │ 최종 문항 수              │ 200건                        │
  └──────────────────────────┴─────────────────────────────┘

Step 5 — Clinfo.AI 시스템 구성
  PubMed 실시간 검색(Entrez API) → BM25 + 의미론적 검색
  LLM이 검색된 초록들을 IEEE 스타일 인용 포함 단락으로 합성
  Synthesis + TL;DR 두 가지 출력 형식 제공

Step 6 — 평가 프로토콜
  Restricted 조건: 질문 날짜 이전 발표 논문만 사용
  Source Dropped 조건: SR의 참조 논문 제외 후 평가 (지식 누출 방지)
  자동 지표: UniEval, COMET, CTC (source-augmented)
            BERTScore, ROUGE-L, METEOR (source-free)
```

---

## 실제 문항 예시

### 임상 의학 (예시 1)
> **Q.** Does high-grade dysplasia/carcinoma in situ of the biliary duct margin affect the prognosis of extrahepatic cholangiocarcinoma?
>
> **A. (SR 결론 요약)** Evidence is mixed; some studies suggest association with local recurrence and negative prognosis. Invasive carcinoma at the margin is a stronger negative prognostic factor.

### 수술·중재 (예시 2)
> **Q.** Is laparoscopic cholecystectomy safe in patients with liver cirrhosis?
>
> **A. (SR 결론 요약)** Feasible with careful patient selection (Child-Pugh A/B); complication rates are higher than in non-cirrhotic patients.

---

## 주요 평가 결과 (Unrestricted 조건, UniEval Overall)

| 시스템 | UniEval Overall |
|---|---|
| GPT-4 단독 (RAG 없음) | 0.860 |
| Elicit | 0.713 |
| StatPearls Semantic Scholar | 0.728 |
| **Clinfo.AI Synthesis + TL;DR** | **0.840** |

GPT-4 단독 대비 RAG 강화 Clinfo.AI가 근접한 성능을 달성. ROUGE-L·BERTScore 기준으로도 베이스라인 대비 우위.

---

## 한계점
- SR의 결론이 최신 연구로 인해 달라질 수 있어 날짜 기준 평가가 복잡
- 200문항은 통계적 안정성을 담보하기에 소규모
- 자동화된 LLM 평가 지표(UniEval 등)가 의학적 정확성을 완전히 반영하지 못할 수 있음
- 개방형 답변 형식 → 자동 정확도 채점 불가, 지표가 요약 품질에 집중

---

## 관련 정보
- **논문**: [arXiv:2310.16146](https://arxiv.org/abs/2310.16146)
- **PSB 2024**: Pacific Symposium on Biocomputing 2024
- **DBLP**: [journals/corr/abs-2310-16146](https://dblp.org/rec/journals/corr/abs-2310-16146.html)
- **벤치마크 이름**: PubMedRS-200 (200 PubMed Systematic Reviews)
