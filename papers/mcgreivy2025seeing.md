---
title: "Seeing the Forest Through the Trees: Knowledge Retrieval for Streamlining Particle Physics Analysis"
bib_key: "mcgreivy2025seeing"
year: 2025
domain: physics
type: method
venue: arXiv preprint (arXiv:2509.06855)
paper_link: https://arxiv.org/abs/2509.06855
---
# Seeing the Forest Through the Trees: Knowledge Retrieval for Streamlining Particle Physics Analysis

> arXiv:2509.06855 | 2025 | method | physics
> McGreivy, Delaney, Beck, Williams — MIT (NSF AI Institute for AI and Fundamental Interactions, LHCb)

## 한 줄 요약
LHCb 코퍼스를 대상으로, 표준 RAG의 chunk fragmentation 한계를 극복하는 두 가지 구조화 검색 시스템 제안: **SCITREERAG**(논문 LaTeX 섹션 트리 + recursive attention-weighted 임베딩) + **SCIGRAPHRAG**(LLM-구축 Neo4j Knowledge Graph + NL→CYPHER). HFLAV에서 자동 생성한 **56개 평가 질의**로 검증, SCITREERAG가 baseRAG 대비 "poor" rating을 25% → 10%로 감소.

## 제작 배경
**표준 RAG의 세 가지 한계 (저자 분류, Sec. 1)**
1. **Accidental Semantic Similarity** — 키워드만 공유하는 무관 청크 검색
2. **Fragmented Context** — 청크 단위 concat이 논리적 관계 손상
3. **Lack of Global Knowledge** — 코퍼스 전반의 관계·패턴 검색 불가

**왜 이 시스템이 필요했는지**
- LHCb 협업: 수천 편 논문, 1,600명+ 협력자 — CERN open data 사용한 비전문가 분석 지원 필요
- LHC publications가 INSPIRE-HEP 등에 산재 → 종합적 cross-document synthesis 부재
- 신규 PhD 학생의 진입 장벽 완화

## 어떻게 만들었나 (Construction Methodology)

```
═══════════════════════════════════════════
[A] SCITREERAG — Local Knowledge Retrieval
═══════════════════════════════════════════
Step A1 — Tree 구축 (per article)
  sanitized LaTeX source 파싱
  abstract = root
  section/subsection = intermediate nodes
  paragraph / figure caption / table / equation = leaf nodes

Step A2 — Recursive LLM summary
  leaf summary = atomic content
  intermediate summary = recursive concat + summarize(children)
  root summary = abstract

Step A3 — Refined dense embedding
  각 노드 summary → paragraph embedding
  recursive attention-weighted refinement:
    동일 정보의 multi-level 표현 → robust signal 증폭
    word-choice / 환각 artifact 감쇠

Step A4 — Retrieval (Greedy tree traversal)
  abstract → section → subsection → leaf
  topically relevant section 우선
  같은 paper의 leaf nodes를 묶어 context에 추가

═══════════════════════════════════════════
[B] SCIGRAPHRAG — Global Knowledge Retrieval
═══════════════════════════════════════════
Step B1 — Per-article KG
  GPT-5 mini가 abstract → high-level KG (observable, decay, period)
  도메인 normalization: e.g., "Bs → µ+µ−" → "B(s)0 -> mu+ mu-"
  body text → systematic uncertainty + analysis methods 추출
  Entity types: 노란(decays) / 자주(observables) /
                연파랑(uncertainty) / 주황(methods)

Step B2 — Canonicalization (cross-document merge)
  TF-IDF(name) + semantic emb(description) → hybrid sim
  agglomerative clustering by type
  LLM-as-judge가 cluster 내 entity 병합 결정
  ex) "tracking efficiency in vertex" vs "in muon" → 분리 유지

Step B3 — NL → CYPHER 변환
  LLM이 schema + 3 few-shot examples 보고
  CYPHER expression 생성 (Neo4j)
  semantic similarity search (no exact string)

Step B4 — Query 실행 + LLM synthesis → NL answer

═══════════════════════════════════════════
[C] 평가 — HFLAV Eval Q&A (Sec. A.2)
═══════════════════════════════════════════
HFLAV 리포트 "Averages of b-hadron, c-hadron,
  τ-lepton properties as of 2023"
  ↳ LHCb corpus에 미포함 → 진정한 retrieval 평가
  ↳ 7개 chapter × 8 query = 56 queries
GPT-5 mini가 각 query에 대해 rubric 생성:
  Essential / Expert-level / Factual benchmarks 3-tier
LLM-as-judge로 grade {poor / satisfactory / good}
Human expert가 sub-sample 검증
```

## Input (입력)
- LHCb 코퍼스 (sanitized LaTeX source 사용)
- 사용자 자연어 질의 (b-hadron lifetime, Vcb, CP violation phase 등)
- HFLAV reference values (정량 benchmark)

## Output (출력)
- SCITREERAG: 트리 traversal 결과 청크 + LLM 응답
- SCIGRAPHRAG: KG 서브그래프 + CYPHER 결과 + NL synthesis

## 예시 문항 (논문 본문 + Appendix A.2·B.2 직접 인용)

### 📘 HFLAV Eval Example Query ① — b-hadron lifetime
> "What are the most precise measurements of b-hadron lifetimes performed by LHCb, and how do the systematic uncertainties in these measurements compare across different decay channels and methodologies?"

### 📘 HFLAV Eval Example Query ② — |Vcb|
> "What is LHCb's most precise measurement of |Vcb| from exclusive semileptonic B decays, and how does it compare to the inclusive determination? What are the dominant sources of theoretical and experimental uncertainty in the exclusive approach?"

### 📘 HFLAV Eval Example Query ③ — Polarization fractions
> "Which B0 decay mode has been most useful for studying polarization fractions in vector-vector final states, and what are the LHCb results?"

### 📘 SCIGRAPHRAG Example — Query γ (Sec. 4)
> **Q**: "What decay channel should I use to measure the CP violating phase γ? What sources of systematic uncertainty will dominate my analysis?"
>
> **SCIGRAPHRAG Response (verbatim)**:
> > "Use a combination of tree-level B → D(∗)h modes plus the time-dependent Bs → D∓s K± channel. Practically this means including B± → DK± and B± → Dπ± (with D → KSππ, KSKK, K±π∓, K±π∓π±π∓, 3- and 4-body final states), B± → D∗K±, B0 → DK∗0/± and B0 → DK+π− (GLW/ADS/GGSZ-type approaches) ... combining these channels is the route taken in recent LHCb determinations and gives the best precision on γ [2010.08483, 2410.21115, 2209.03692, 2412.14074]. The dominant systematic uncertainties will be external hadronic inputs and model/theory assumptions: uncertainties on D-decay hadronic parameters (rXD, δXD, κXD, CP-even fractions F+ for multi-body modes) ..."
>
> **LLM-as-judge 결과**: SCIGRAPHRAG = "good", SCITREERAG/RAG = "satisfactory" (저자 동의)

### 📘 SCIGRAPHRAG Example — Query ∆ms (Sec. B.2)
> **Q**: "Which decay provides the most precise measurement of the B0s eigenstate oscillation frequency, ∆ms? What are the dominant systematic uncertainties for that measurement?"
>
> **응답 발췌**: *"the recent LHCb result quoted in the context gives ∆ms = 17.7683 ± 0.0051 (stat) ± 0.0032 (syst) ps−1 from B0s → D−s π+ [2104.04421]; earlier LHCb measurements on the same channels report compatible values with larger uncertainties (e.g. 17.768 ± 0.023 ± 0.006 [1304.4741])"*

## 주요 평가 결과 (Sec. 4, Sec. B.1)

**LLM-as-judge Quality Grades (HFLAV 56-Q, context 8k/16k/32k 평균)**

| System | "poor" 비율 | "satisfactory + good" 비율 |
|---|---|---|
| BaseRAG (표준) | 25% | ~42% |
| SCITREERAG (no diffusion) | 20% | >50% |
| **SCITREERAG + diffusion** | **10%** | **>50%** |

> 저자 결론: "SCITREERAG demonstrates modest but consistent improvements over BaseRAG ... receiving 'poor' ratings only 10% of the time compared to 25% for RAG."

**KG Canonicalization 검증 (Fig. 1)**
- Query γ: 17개 "CKM Angle gamma" entity들이 단일 entity로 올바르게 병합
- Query ∆ms: 4개의 중복 "Delta m_s" entity 발견 → **불완전 entity resolution** 사례 (저자 명시)

## 한계점
- **수치 표준 벤치마크 부재**: P@k, MRR 같은 IR metric 미사용 (LLM-as-judge만)
- SCIGRAPHRAG는 **work in progress** — KG 구축·NL→Cypher 신뢰성 미흡
- Schema가 좁게 정의(particle physics analysis) → 일반화 미검증
- Human expert validation은 sub-sample만, full evaluation 미시행
- LHCb 코퍼스에 한정 — ATLAS/CMS/ALICE로의 transferability 미검증
- KG 구축은 article별 1회성 upfront cost지만 GPT-5 mini API 비용 누적

## 관련 정보
- **논문**: [arXiv:2509.06855](https://arxiv.org/abs/2509.06855)
- **저자 소속**: MIT (NSF AI Institute for AI and Fundamental Interactions)
- **사용 LLM**: GPT-5 mini (KG 구축), embedding model (DPR / SciBERT 계열, 본문 미명시)
- **평가 reference**: HFLAV 2023 report (Banerjee et al. 2024) — LHCb 코퍼스에 미포함
- **KG 도구**: Neo4j (CYPHER query language)
- **코드 공개**: workshop camera-ready 버전에서 공개 예정
