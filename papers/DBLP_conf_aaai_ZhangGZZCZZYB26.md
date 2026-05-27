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
> DBLP: `conf/aaai/ZhangGZZCZZYB26` · arXiv:2508.02258

## 한 줄 요약
600권 이상의 권위 있는 병리학 교과서에서 **페이지 단위 멀티모달 임베딩(ColQwen2)**으로 구축한 **20만+ 페이지 규모의 지식 베이스**와, **GRPO 강화학습**으로 훈련한 4-단계 의사결정 아젠틱 라우터(Qwen3-4B)를 결합해 병리 VLM의 환각을 억제하는 멀티모달 RAG 시스템. PathMMU-test에서 78.32%, **MedXpertQA에서 60.00% (+38pp vs base Patho-R1-7B)** 달성.

## 제작 배경
**병리학 VLM의 한계** (논문 §2 발췌)
> "Reinforcement learning (RL) provides a promising paradigm for aligning the outputs of VLMs with clinical accuracy requirements, especially in high-risk medical domains where hallucinated descriptions can lead to severe consequences."

기존 의료 RAG의 문제:
- **Text-only RAG**: 병리 진단의 핵심인 H&E 염색 패턴·세포 형태·공간 배치 등 **시각 단서를 텍스트로 환원 불가**
- **Static RAG pipeline**: 모든 쿼리에 무차별 검색 → 일반 상식 문제("What stain is used for nuclei?")까지 retrieve 시 latency·noise 증가
- **MMed-RAG·MedRAG 등 기존 medical RAG**: 일반 의학 위주이며 병리 전문성 부족, retrieval 대상이 paper abstract/journal에 한정

**Patho-AgenticRAG의 차별점**:
1. **페이지 단위 multimodal indexing** (ColQwen2): textbook 페이지를 하나의 image-text 통합 벡터로 표현 → text-only chunk 대비 시각 패턴 보존
2. **Agentic Router**: 쿼리별로 RAG 호출 여부·검색 깊이·해부학 파티션·조직 분류기 활성화 여부를 동적 결정
3. **GRPO RL 학습**: SFT만으로 부족한 결정 정확도를 강화학습으로 fine-tune

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 병리학 교과서 지식 베이스 구축
  600+ 권위 있는 병리학 교과서 → ~300,000 페이지 수집
  커버·서문·목차·참고문헌 제거 → 200,000+ 고품질 페이지 보존
  19개 해부학 카테고리로 파티셔닝:
    1. Bone and soft tissue        11. Histology
    2. Cytology                    12. Pediatric pathology
    3. Gastrointestinal (GI)       13. Skin
    4. Hematology                  14. Central nervous system (CNS)
    5. Infectious diseases         15. Female reproductive system
    6. Oral / Head / Neck (ENT)    16. Gross sampling
    7. Urinary / male reproductive 17. Immunohistochemistry (IHC)
    8. Breast                      18. Ophthalmology
    9. Endocrine system            19. Respiratory
   10. General pathology
  임베딩: ColQwen2 — 텍스트+이미지 통합 다중-벡터 표현 (페이지 단위)
  벡터 DB: Milvus + HNSW 인덱싱, 150M+ 벡터

Step 2 — Patho-Fusion 리랭킹 알고리즘 설계
  ColQwen2가 생성한 두 similarity matrix를 결합:
    - S_t ∈ R^{Nt × Nd} : query text token ↔ page document token
    - S_v ∈ R^{Nv × Nd} : query image patch ↔ page document patch
  Patho-Fusion Score (이 논문 고유):
    Score = α · mean(max(S_t[i, :]))    ← CoPaLi-style text relevance
          + β · κ(S_v[i, :])              ← image kurtosis (집중적 시각 관심)
  설계 의도: 시각 modality의 평균 유사도는 무시,
            "특정 영역에 집중된 attention"만 가산점 부여
            → 균일한(noisy) 시각 매칭을 패널티

Step 3 — Agentic Router 훈련 데이터 구성
  Quilt-VQA + Path-VQA 훈련 세트에서 질문 선별
  ┌─ Patho-R1-7B 정답 → 2,200개 (RAG 불필요 학습 신호)
  └─ Patho-R1-7B 오답 → 2,200개 (RAG 필요 학습 신호)
  합계: 4,400 샘플

  QwenMax로 각 샘플에 대한 전문가 설계 프롬프트 기반
  ground-truth 4-단계 의사결정 경로 생성:
    Decision 1: RAG 호출 여부 (Yes/No)
    Decision 2: 쿼리 분해 수 (1, 2, 3, ...)
    Decision 3: 조직 특화 분류기 활성화 여부
    Decision 4: 검색 해부학 파티션 선택 (19개 중)

  SFT 400개 / GRPO RL 4,000개로 분할

Step 4 — 라우터 학습 (Qwen3-4B)
  Phase A — SFT: 400개 샘플, 3 epoch, LR=1e-5 (vision tower frozen)
  Phase B — GRPO: 4,000개 샘플, 3 epoch
                  actor LR=1e-6 / critic LR=1e-5
  Hardware: 8× NVIDIA RTX 4090

  계층적 보상 함수 (max 4점):
  ┌─ Decision 1 오류: 0점 (조기 종료)
  ├─ Decision 1 정답(RAG 불필요): 4점 (단순 질문이므로)
  ├─ Decision 1 정답(RAG 필요): 1점 → Decision 2 정답: +1점
  └─ Decision 3+4 정답: 추가 1~2점 → 최대 4점

Step 5 — 인퍼런스 파이프라인 (Multi-agent Workflow)
  사용자 입력 [이미지+텍스트]
       ↓
  Agentic Router (Qwen3-4B)
    → RAG 필요? No → Patho-R1-7B 직접 답변
    → RAG 필요? Yes → 후보별 sub-task 분해, 해부학 파티션 선택
       ↓
  VRAG Agent — multi-turn retrieval + summarization
    - text-based retrieval (각 후보별 keyword)
    - Patho-Fusion 리랭킹 (text-doc × image-doc kurtosis)
    - iterative 증거 sufficiency 평가
       ↓
  Top-1 page evidence + 원본 쿼리 + comparative instructions
       ↓
  Patho-R1-7B (specialized pathology VLM)
    → contrastive reasoning constrained to evidence
    → 진단 + interpretable justification

Step 6 — 평가 벤치마크 7개
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

## Input (입력) / Output (출력)

**Input**: 병리 이미지 (H&E 염색 슬라이드 등) + 자연어 질문 (객관식 또는 Y/N)
**Output**: 정답 옵션 + (선택적으로) evidence-grounded justification

**Knowledge base**: 200,000+ pathology textbook pages, indexed in Milvus + HNSW
**Vision encoder for routing**: Qwen3-4B (multimodal)
**Vision encoder for retrieval**: ColQwen2 (page-level multi-vector)
**Final VLM (inference engine)**: Patho-R1-7B (pathology-specialized)

## 예시 사례 (논문 Figure 2, Figure 3 — 실제 멀티모달 검색 워크플로우 직접 인용)

### 🔬 Case 1: Multi-turn Retrieval — Monophasic Synovial Sarcoma (Figure 2 발췌)

논문 Figure 2는 실제 query가 시스템 내부에서 어떻게 처리되는지를 단계별로 보여준다.

> **Original Text Query (PathMMU 객관식 문제, Ground Truth: A)**:
> > "This image shows monophasic synovial sarcoma. What are its key histologic features?
> > A. Dense, uniform spindle cells with scant cytoplasm in short, intersecting fascicles.
> > B. Biphasic: glandular epithelium with spindle cell stroma.
> > C. Scattered adipocytes in fibrous stroma with atypia.
> > D. Large polygonal cells with coarse eosinophilic granules."
>
> **VRAG Agent Rewritten Search Query**:
> > "What are the histological features of monophasic synovial sarcoma?"
>
> **Multi-turn Retrieval 결과** (Patho-Fusion score):
> - "Cytologic appearance of Ewing sarcoma/PNET..." (score 0.6638 → text retrieval top1이나 distractor)
> - "Monophasic synovial sarcoma. The tumor..." (0.6558)
> - "...monophasic synovial sarcoma with..." (0.6190)
> - **Final Top1 (after Patho-Fusion rerank)**: "Synovial sarcoma with an adenocarcinoma-like appearance of the epithelial component." (0.6602, 이미지 attention 집중도 가장 높음)
>
> **Sub-VRAG agent thought process (논문 Figure 2)**: text retrieval은 *Ewing sarcoma*를 top1으로 잘못 가져왔으나, image kurtosis term이 *synovial sarcoma* 페이지를 정확히 rerank → 최종 정답 A 도출.

### 🧬 Case 2: 학습 데이터 라벨링 예시 (Appendix, Q1-Q2 발췌)

훈련 데이터의 ground-truth answer 예시:
> **Q1**: "Histological features of invasive lobular carcinoma of the breast, including Indian-file pattern"
> **A1**: "Histological features of invasive lobular carcinoma of the breast include uniform small round tumor cells infiltrating the stroma in a single-file (Indian-file) arrangement and circumferentially around ducts in a target-like pattern."
>
> **Q2**: "How to differentiate ductal, papillary, and mucinous breast carcinoma histologically"
> **A2**: "Histologically, ductal carcinoma shows glandular, papillary, cribriform, or diffuse growth patterns, often forming nests, trabeculae, or cords. Papillary carcinoma is characterized by prom[inent papillary structures...]"

### 🧠 Case 3: RAG-skip 결정 가이드라인 (Appendix prompt 발췌)
> "If the question reflects common knowledge in pathology or histology, such as 'What stain is used for nuclei?' or 'Which cell secretes collagen?', a `<think>` is sufficient, and no tool needs to be called."

→ Router는 *상식 수준 질문*은 RAG 호출 없이 처리, **드문/복잡한 질문**(예: rare 종양 감별)만 vector DB 검색.

## 주요 평가 결과

### Patho-Fusion 리랭킹 성능 (Table 1)
100개 전문가 큐레이션 image-question-answer 쌍 기준:
| 방법 | Rec@1 | Rec@5 | MRR@5 | NDCG@5 | NDCG@20 |
|---|---:|---:|---:|---:|---:|
| CoPaLi (Text) | 0.640 | **0.900** | 0.734 | 0.804 | 0.796 |
| CoPaLi (Image) | 0.060 | 0.220 | 0.112 | 0.174 | 0.359 |
| WeiMoCIR | 0.060 | 0.200 | 0.102 | 0.163 | 0.342 |
| **Patho-Fusion (ours)** | **0.720** | 0.880 | **0.777** | **0.824** | **0.827** |

### PathMMU Multiple-Choice QA (Table 2 발췌)
| 모델 | PathMMU-test | PathMMU-test-tiny |
|---|---:|---:|
| InternVL2-8B | 43.68 | 44.86 |
| InternVL2.5-8B | 50.06 | 50.62 |
| InternVL3-8B | 54.07 | 50.80 |
| Llama-3.2V-11B-cot | 51.81 | 45.45 |
| Qwen2.5VL-7B | 41.18 | 43.20 |
| Patho-R1-7B (base) | 75.34 | 66.43 |
| **Patho-AgenticRAG** | **78.32** | **70.96** |
| 향상 (vs. base) | **+2.98pp** | **+4.53pp** |

세부 subset (Atlas / EduContent / PathCLS / PubMed / SocialPath)에서도 일관되게 SOTA.

### Yes/No VQA 및 전문가 QA (Table 3, 본문 §4 직접 인용)
> "Patho-AgenticRAG achieves +13.37% improvement on Quilt-VQA (75.80% vs. 64.72%) and +38.00% on MedXpertQA (60.00% vs. 22.00%) over Patho-R1. The largest margin appears on MedXpertQA, highlighting the importance of retrieval-augmented reasoning in knowledge-intensive tasks. On OmniMedVQA Bright Challenge, the model improves from 70.79% (Patho-R1) to 90.11%, a +19.32% increase."

| 모델 | Path-VQA | Quilt-VQA | MedXpertQA | OmniMedVQA Bright |
|---|---:|---:|---:|---:|
| InternVL2.5-8B | 60.06 | 49.78 | 64.78 | 22.22 |
| Patho-R1-7B (base) | 64.72 | 70.79 | 22.00 | 46.97 |
| **Patho-AgenticRAG** | **75.80** | **90.11** | **60.00** | **80.34** |
| 향상 (vs. base) | **+11.08pp** | **+19.32pp** | **+38.00pp** | **+33.37pp** |

### Ablation — 라우터 학습 전략 (Quilt-VQA 기준)
| 구성 | Quilt-VQA |
|---|---:|
| Patho-R1 (no router, no RAG) | 64.72% |
| +Qwen3 (raw router) | 60.93% (오히려 감소 — overcalling RAG) |
| +GRPO4k only | 60.93% |
| +SFT4k → GRPO400 | 미세 향상 |
| **+SFT400 → GRPO4k** | **75.80%** (+14.87% over GRPO-only) |

→ 논문 §4 주장:
> "These results suggest that SFT400 provides an effective 'cold start' that guides the policy initialization without compromising flexibility or generalization."

## 한계점
- **평가가 폐쇄형(closed-ended) 태스크에 한정** — Yes/No와 객관식 위주, 개방형 진단 추론(differential diagnosis) 미평가.
- **지식 베이스가 교과서 기반** → 최신 임상 가이드라인·연구 논문 미반영 (예: 최근 1년 내 신약).
- **교과서 커버리지의 도메인 불균형** — 19개 카테고리 중 일부는 소수 books에 의존 가능.
- **검색 지연·인프라 비용 미보고**: 150M+ 벡터 Milvus 인덱스 + multi-turn agentic 호출은 실용 deploy 시 latency 우려.
- **병리 도메인 외 일반화 미검증** — 동일 파이프라인이 방사선·안과·심전도에서 작동하는지 미증명.
- **GRPO 학습의 안정성**: ablation에서 GRPO-only는 base보다 성능 *하락*하는 경우 확인 — SFT cold-start 의존성 강함.
- **VRAG Agent의 multi-turn 호출 수가 가변** → 일관된 latency 보장 어려움.

## 관련 정보
- **논문 (arXiv)**: [arXiv:2508.02258](https://arxiv.org/abs/2508.02258)
- **AAAI 2026**: vol. 40, no. 35, pp. 29921–29929
- **GitHub**: [Wenchuan-Zhang/Patho-AgenticRAG](https://github.com/Wenchuan-Zhang/Patho-AgenticRAG)
- **DBLP**: [conf/aaai/ZhangGZZCZZYB26](https://dblp.org/rec/conf/aaai/ZhangGZZCZZYB26)
- **base model**: [Patho-R1-7B (Hugging Face)](https://huggingface.co/blackshow/Patho-R1)
- **Retrieval encoder**: [ColQwen2 (vidore)](https://huggingface.co/vidore/colqwen2-v1.0)
