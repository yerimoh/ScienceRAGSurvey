---
title: "Patho-AgenticRAG: Towards Multimodal Agentic Retrieval-Augmented Generation for Pathology VLMs via Reinforcement Learning"
bib_key: DBLP:conf/aaai/ZhangGZZCZZYB26
year: 2026
domain: medical
type: Method
venue: AAAI 2026
paper_link: https://arxiv.org/abs/2508.02258
---
# Patho-AgenticRAG

> AAAI 2026 (vol. 40, no. 35, pp. 29921–29929) | Method | medical (pathology)
> Zhang, Guo, H.Zhang, P.Zhang, Chen, S.Zhang, Z.Zhang, Yi, Bu
> DBLP: `conf/aaai/ZhangGZZCZZYB26`

## 한 줄 요약
600권 이상의 병리학 교과서에서 페이지 단위 멀티모달 임베딩(ColQwen2)으로 구축한 20만 페이지 규모의 지식 베이스와, GRPO 강화학습으로 훈련한 아젠틱 라우터(Qwen3-4B)를 결합해 병리 VLM의 환각을 억제하는 멀티모달 RAG 시스템. PathMMU-test에서 78.32%, MedXpertQA에서 60.00%(+38pp)를 달성.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 병리학 교과서 지식 베이스 구축
  600권 이상 권위 있는 병리학 교과서 → ~300,000페이지 수집
  커버·서문·목차·참고문헌 제거 → 200,000+ 고품질 페이지 보존
  19개 해부학 카테고리로 파티셔닝:
    bone/soft tissue, cytology, GI, hematology, infectious diseases,
    oral/head/neck, urinary/reproductive, breast, endocrine,
    general pathology, histology, pediatric, skin, CNS,
    female reproductive, gross sampling, IHC, ophthalmology, respiratory
  임베딩: ColQwen2 (텍스트+이미지 통합 벡터 공간, 페이지 단위)
  벡터 DB: Milvus + HNSW 인덱싱

Step 2 — 라우터 훈련 데이터 구성
  Quilt-VQA + Path-VQA 훈련 세트에서 질문 선별
  ┌─ Patho-R1-7B 정답 → 2,200개 (RAG 불필요 학습 신호)
  └─ Patho-R1-7B 오답 → 2,200개 (RAG 필요 학습 신호)
  합계: 4,400 샘플

  QwenMax로 각 샘플에 대한 전문가 설계 프롬프트 기반
  ground-truth 4-단계 의사결정 경로 생성:
    Decision 1: RAG 호출 여부
    Decision 2: 쿼리 분해 수
    Decision 3: 조직 특화 분류기 활성화 여부
    Decision 4: 검색 해부학 파티션 선택

  SFT 400개 / GRPO RL 4,000개로 분할

Step 3 — 라우터 학습 (Qwen3-4B)
  Phase A — SFT: 400개 샘플, 3 epoch, LR=1e-5 (vision tower frozen)
  Phase B — GRPO: 4,000개 샘플, 3 epoch, actor LR=1e-6 / critic LR=1e-5
  Hardware: 8× NVIDIA RTX 4090

  계층적 보상 함수 (max 4점):
  ┌─ Decision 1 오류: 0점 (조기 종료)
  ├─ Decision 1 정답(RAG 불필요): 4점
  ├─ Decision 1 정답(RAG 필요): 1점 → Decision 2 정답: +1점
  └─ Decision 3+4 정답: 추가 1~2점 → 최대 4점

Step 4 — 인퍼런스 파이프라인
  쿼리 [이미지+텍스트]
       ↓
  Agentic Router (Qwen3-4B)
    → RAG 필요? No → Patho-R1-7B 직접 답변
    → RAG 필요? Yes → 쿼리 분해 (N개)
       ↓
  ColQwen2 인코딩 → Milvus HNSW 검색
  Patho-Fusion 리랭킹 (text-doc × image-doc 스코어링)
       ↓
  상위 페이지 + 원본 쿼리 → Patho-R1-7B → 최종 답변

Step 5 — 평가 벤치마크
  ┌─────────────────────────┬──────────┬───────────────┐
  │ 벤치마크                 │ 문항수   │ 유형          │
  ├─────────────────────────┼──────────┼───────────────┤
  │ PathMMU-test            │ 8,454    │ MC (5 subset) │
  │  └─ Atlas               │    799   │               │
  │  └─ EduContent          │  1,683   │               │
  │  └─ PathCLS             │  1,632   │               │
  │  └─ PubMed              │  2,787   │               │
  │  └─ SocialPath          │  1,553   │               │
  │ PathMMU-test-tiny       │  1,139   │ MC            │
  │ Path-VQA (YorN)         │  3,362   │ Yes/No        │
  │ Quilt-VQA               │    343   │ Yes/No        │
  │ MedXpertQA (pathology)  │     90   │ 전문가 큐레이션│
  │ OmniMedVQA BRIGHT       │    890   │ VQA           │
  └─────────────────────────┴──────────┴───────────────┘
```

---

## 실제 태스크 형식 예시

PathMMU는 5개 서브도메인 병리 이미지와 함께 제공되는 다지선다 진단 문제이다. 실제 문항 구조:

> **[병리 슬라이드 이미지 첨부]**
>
> **Q.** The image shows a histological section stained with H&E. Which of the following best describes the pathological finding?
>
> (A) Squamous cell carcinoma with keratin pearl formation
> (B) Adenocarcinoma with gland formation
> (C) Small cell carcinoma with nuclear molding
> (D) Large cell carcinoma without specific differentiation

Path-VQA 형식 (Yes/No):

> **[병리 이미지]**
> **Q.** Is there evidence of inflammation in this tissue section?
> **(A) Yes  (B) No**

---

## Patho-Fusion 멀티모달 리랭킹

ColQwen2가 생성한 텍스트-문서 유사도 행렬 T와 이미지-문서 유사도 행렬 I를 결합:

| 검색 방법 | Recall@1 | MRR@5 | NDCG@20 |
|---|---|---|---|
| CoPaLi | 0.640 | 0.703 | 0.769 |
| WeiMoCIR | 0.680 | 0.741 | 0.802 |
| **Patho-Fusion** | **0.720** | **0.777** | **0.827** |

*(100개 전문가 큐레이션 이미지-질문-정답 쌍 기준)*

---

## 주요 평가 결과

**PathMMU Multiple-Choice QA (Table 2)**
| 모델 | PathMMU-test | PathMMU-tiny |
|---|---|---|
| InternVL3-8B | 54.07 | 42.94 |
| Llama-3.2V-11B-cot | 51.81 | 29.94 |
| Qwen2.5VL-7B | 41.18 | 24.86 |
| Patho-R1-7B (base) | 75.34 | 44.63 |
| **Patho-AgenticRAG** | **78.32** | **57.22** |
| 향상 (vs. base) | **+2.98pp** | **+12.59pp** |

**Yes/No VQA 및 전문가 QA (Table 3)**
| 모델 | Path-VQA | MedXpertQA | Quilt-VQA |
|---|---|---|---|
| InternVL2.5-8B | 60.06 | 64.78 | 49.78 |
| Patho-R1-7B (base) | 64.72 | 22.00 | 70.79 |
| **Patho-AgenticRAG** | **75.80** | **60.00** | **90.11** |
| 향상 (vs. base) | **+13.37pp** | **+38.00pp** | **+19.32pp** |

**Ablation — 라우터 학습 전략 (Path-VQA 기준)**
| 구성 | Path-VQA |
|---|---|
| GRPO-only (SFT 없음) | 77.51% |
| SFT-only (400개) | 78.10% |
| **SFT400 + GRPO4k** | **80.34%** |

---

## 한계점
- 평가가 폐쇄형(closed-ended) 태스크에 한정 — 개방형 진단 추론 미평가
- 지식 베이스가 교과서 기반 → 최신 임상 가이드라인·연구 논문 미반영
- 교과서 커버리지에 따른 세부 병리 도메인별 불균형 가능성
- 검색 지연 및 대규모 Milvus 인덱스 운영 비용 미보고
- 병리 도메인 외 타 의료 모달리티(방사선, 안과) 일반화 미검증

---

## 관련 정보
- **논문 (arXiv)**: [arXiv:2508.02258](https://arxiv.org/abs/2508.02258)
- **AAAI 2026**: vol. 40, no. 35, pp. 29921–29929
- **GitHub**: [Wenchuan-Zhang/Patho-AgenticRAG](https://github.com/Wenchuan-Zhang/Patho-AgenticRAG)
- **DBLP**: [conf/aaai/ZhangGZZCZZYB26](https://dblp.org/rec/conf/aaai/ZhangGZZCZZYB26)
