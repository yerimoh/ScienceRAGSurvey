---
title: "Medical Graph RAG: Evidence-based Medical Large Language Model via Graph Retrieval-Augmented Generation"
bib_key: "DBLP:conf/acl/WuZQCXMJG25"
year: 2025
domain: medical
type: method
venue: ACL 2025
paper_link: https://aclanthology.org/2025.acl-long.1381/
---
# MedGraphRAG: Evidence-based Medical RAG via Triple Graph Construction + U-Retrieval

> ACL 2025 (Long Paper, pp. 28443–28467) | Method | medical
> Junde Wu, Jiayuan Zhu, Yunli Qi, Jingkun Chen, Min Xu, Filippo Menolascina, Yueming Jin, Vicente Grau — Univ. of Oxford / CMU / MBZUAI / Univ. of Edinburgh / NUS
> DBLP: `conf/acl/WuZQCXMJG25`

## 한 줄 요약
사용자 의료 문서 → 의학 문헌 → 의학 사전의 **3-tier hierarchical graph** 구조와 **U-Retrieval**(top-down 태그 매칭 + bottom-up 그래프 traversal)을 결합한 evidence-based 의료 RAG 프레임워크. **9개 MultiMedQA MCQ + 2개 fact-verification + DiverseHealth (12개)** 벤치마크에서 GraphRAG·MedRAG·NaiveRAG 등 베이스라인을 일관되게 능가.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — Triple Graph Construction (3-tier 계층)
  ┌───────────────────────────────┐
  │ Tier 1: User documents        │  ← 환자 기록·임상 노트 등
  │ Tier 2: Medical literature    │  ← 논문·교과서 (MedC-K corpus)
  │ Tier 3: Medical dictionary    │  ← UMLS / Medical Dictionary
  └──────────────┬────────────────┘
                 │  hierarchical link
                 ▼
  엔티티가 3-tier 그래프에 의미 단위로 연결됨

Step 2 — Tag-based clustering
  유사 그래프들을 반복적으로 클러스터링
  → broad-to-detail multi-layer hierarchical tag 구조 형성

Step 3 — U-Retrieval (이름의 'U'자 형태)
  ▼ Top-down 단계: LLM이 쿼리 태그 생성 → 태그 유사도로 그래프 인덱싱
  ▲ Bottom-up 단계: 가장 관련성 높은 detailed 그래프부터 entity 단위로
                   상위 broader 그래프까지 traversal
  → 검색 효율과 응답 컨텍스트 폭을 동시에 확보

Step 4 — Evidence-based response generation
  검색된 의학 용어와 공식 정의를 함께 prompting
  → "evidence-based responses and official medical term explanation"
```

---

## 평가 셋업 (논문 §Test Data 직접 인용)

> "Our test set are the test split of **9 multiple-choice biomedical datasets from the MultiMedQA suite**, 2 fact verification datasets about public health, i.e., FakeHealth and PubHealth, and 1 test set we collected, called DiverseHealth."

| 카테고리 | 데이터셋 | 비고 |
|---|---|---|
| MultiMedQA MCQ (9) | MedQA, MedMCQA, PubMedQA, MMLU-Med (clinical knowledge / medical genetics / anatomy / college medicine / professional medicine / college biology), LiveQA, MedicationQA | 정답 선택 정확도 |
| Fact verification (2) | FakeHealth, PubHealth | 사실 검증 |
| In-house (1) | DiverseHealth | 일반 의학 광범위 커버 |

---

## 주요 평가 결과 (논문 Table 2 발췌)

| 시스템 | 평균 MultiMedQA Acc. (대표 9 dataset) | DiverseHealth Acc. |
|---|---|---|
| GPT-3.5 + NaiveRAG | 53.4 | – |
| GPT-3.5 + GraphRAG | 64.8 | – |
| GPT-3.5 + MedRAG | 68.4 | – |
| **GPT-3.5 + MedGraphRAG** | **74.6** | **+6%p vs MedRAG** |
| GPT-4 + MedGraphRAG | **80.1** | SOTA |

→ Triple Graph + U-Retrieval 결합 시 단순 GraphRAG 대비 평균 +10%p 향상.

---

## Ablation (3-tier 증분 영향, 논문 Fig.3)

| 추가된 tier | MCQ Acc. 증분 |
|---|---|
| User docs only | baseline |
| + Medical literature (Tier 2) | +2% (단독) |
| + Medical dictionary (Tier 3) | +1% (단독) |
| 세 tier 누적 + U-Retrieval | +6~10%p |

핵심 발견: 데이터 누적 + 적절한 검색 방법이 함께 작동해야 full potential.

---

## 한계점
- UMLS / Medical Dictionary 어휘 범위 밖의 희귀·신흥 의학 용어 처리 제한
- 3-tier 그래프 traversal cost가 높아 실시간 임상 응용 시 지연 발생 가능
- MedC-K 코퍼스 규모·구성 세부 사항이 논문에 충분히 기술되지 않음
- MultiMedQA의 일부 데이터셋은 LLM 학습 데이터와 중첩 가능성 존재

---

## 관련 정보
- **논문**: [ACL Anthology 2025.acl-long.1381](https://aclanthology.org/2025.acl-long.1381/)
- **DOI**: [10.18653/v1/2025.acl-long.1381](https://doi.org/10.18653/v1/2025.acl-long.1381)
- **DBLP**: [conf/acl/WuZQCXMJG25](https://dblp.org/rec/conf/acl/WuZQCXMJG25.html)
- **GitHub (저자 구현 추정)**: https://github.com/MedicineToken/Medical-Graph-RAG
