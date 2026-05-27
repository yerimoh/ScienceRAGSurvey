---
title: "BioASQ-QA: A manually curated corpus for Biomedical Question Answering"
bib_key: "krithara2023bioasq"
year: 2023
domain: medical, bio
type: benchmark
venue: Scientific Data (Nature)
paper_link: https://doi.org/10.1038/s41597-023-02068-4
---
# BioASQ-QA: A manually curated corpus for Biomedical Question Answering

> Scientific Data 2023 | Benchmark + Challenge Infrastructure | medical · bio

## 한 줄 요약
2012년부터 매년 운영되는 **BioASQ Challenge Task B의 누적 QA 데이터셋**. 21명의 생의학 전문가(EU 중심)가 직접 작성한 **4,721개 질문**(2022년 기준)과 함께 **관련 문서·스니펫·온톨로지 개념·RDF 트리플·exact answer·paragraph 단위 ideal answer**를 8단계 annotation 프로토콜로 제공. IR + QA + multi-document summarization을 동시 평가하는 유일한 의생물학 벤치마크.

---

## 어떻게 만들었나 (Construction Methodology)

```
BioASQ 인프라 = 전문가 team + Annotation tool + Assessment tool + Challenge

Step 0 — Expert team 구성 (2012~)
  └─ 21명 전문가 (cardio, psychiatry, pharmacology, drug repositioning,
     genomics, proteomics, clinical IR 등 광범위 커버)
  └─ 7명이 가장 활발히 기여
  └─ 매년 1인당 ~500 questions 목표

Step 1 — Question formulation (8단계 annotation 시작)
  ┌──────────────────────────────────────────────┐
  │ Question type 4종 선택:                       │
  │  · Yes/No                                    │
  │    e.g. "Do CpG islands colocalise with TSS?"│
  │  · Factoid (단일 entity 답)                  │
  │    e.g. "Which virus causes mononucleosis?"  │
  │  · List (entity 리스트)                      │
  │    e.g. "Which are the Raf kinase inhibitors?"│
  │  · Summary (1-paragraph 요약 필요)            │
  │    e.g. "How does dabigatran affect aPTT?"   │
  └──────────────────────────────────────────────┘
  ⚠ 가이드라인: PubMed 쿼리로 10~60개 article 회수 가능 범위 내,
                 controversial 질문 회피, 반드시 biomedical 도메인

Step 2 — Relevant concept 선정 (synonym/broader/narrower 포함)

Step 3 — Information retrieval (PubMed advanced query)
   ↓ 다양한 쿼리 가능 (실험적으로 "many roads lead to Rome")

Step 4 — 충분한 article 집합 선정
Step 5 — Text snippet 추출 (full sentence 단위, 다중 article 허용)
Step 6 — Query revision (Step 2-5 반복; 답 못 찾으면 question 폐기)

Step 7 — Exact answer
  · Yes/No → "yes" / "no"
  · Factoid → entity name + synonym 모두
  · List → entity 리스트 + 각 element의 synonym
  · Summary → blank (Step 8에서 통합)

Step 8 — Ideal answer (1-paragraph)
  반드시 Step 5의 snippet 기반 (전문가 사견 금지),
  rephrase/shorten/order 자유, 다른 전문가가 읽기 좋게 작성

[Post-challenge] Assessment phase:
  Expert가 자신이 만든 질문에 대한 system 답을 review,
  → 누락된 relevant doc/snippet은 gold dataset에 추가 → dataset 품질 점진 개선
```

---

## 데이터 소스 (Drug-Target-Disease triangle)

| 축 | 리소스 | 규모 |
|---|---|---|
| **Drugs** | **Jochem** (Joint Chemical Dictionary — UMLS+MeSH+ChEBI+DrugBank+KEGG+HMDB+ChemIDplus 통합) | — |
| **Targets** | **Gene Ontology** (cellular component / molecular function / biological process) | — |
|  | **UniProt SwissProt** (manual review) | >500k sequences |
| **Diseases** | **Disease Ontology** (MeSH/ICD/NCI/SNOMED/OMIM 통합 매핑) | ~8,000 diseases |
| **Documents** | **MEDLINE/PubMed** (abstracts only since BioASQ-4, 2016) | >34M citations |
| **Indexing** | **MeSH** (16 trees) | ~30,200 descriptors |
| ~~Linked Data~~ | ~~Linked Life Data~~ (10B statements) — *abandoned recent editions* | — |

---

## 데이터셋 누적 성장 (BioASQ Challenge 1~10)

| 년도 | Challenge | 누적 질문수 | 평균 #docs/Q | 평균 #snippets/Q |
|---|---|---|---|---|
| 2012 | BioASQ-1 (proof-of-concept) | 10 | – | – |
| 2013 | BioASQ-2 | 310 | 14.28 | 18.71 |
| 2014 | BioASQ-3 | 810 | 13.45 | 13.30 |
| 2015 | BioASQ-4 | 1,307 | 13.00 | 17.86 |
| 2016 | BioASQ-5 | 1,799 | 11.86 | 20.38 |
| 2017 | BioASQ-6 | 2,251 | 12.01 | 14.76 |
| 2018 | BioASQ-7 | 2,747 | 11.14 | 13.91 |
| 2019 | BioASQ-8 | 3,243 | 10.15 | 12.92 |
| 2020 | BioASQ-9 | 3,742 | 9.43 | 12.33 |
| 2021 | BioASQ-10 | 4,234 | 9.22 | 12.24 |
| **2022** | **(current)** | **4,721** | **8.58** | **11.36** |

> ⚠ 추세: 평균 doc/snippet 수 점진 감소 — Sufficient set 정책(BioASQ-4부터)으로 "최소한"의 evidence만 요구.

---

## 도메인 적합성 판단 예시 (논문 Section 'Annotation process', verbatim)

> **Q1 (REJECTED):** *"Which are the differences between Hidden Markov Models (HMMs) and Artificial Neural Networks (ANNs)?"*
> · 일반 ML 비교 — 직접적인 biomedical 적용 명시 없음 → 거부.
>
> **Q2 (ACCEPTED):** *"Which are the uses of Hidden Markov Models (HMMs) in gene prediction?"*
> · "gene prediction"이라는 biomedical 응용을 명시 → 채택.

→ BioASQ는 명확한 biomedical 적용이 있는 질문만 허용하며, controversial하거나 답이 없는 의학 논쟁은 회피.

## 검색 단계 verbatim 예시 (Tables 1-3 in paper)

### Step 3 PubMed Query (Q: "Do CpG islands colocalise with transcription start sites?")
> 관련 용어 추출: "CpG Island", "transcription start site", + synonym "Transcription Initiation Site"
> PubMed Advanced Query: `"CpG Island" AND "transcription start site"`
>
> 회수된 article 예시 (Table 1):
> · *"Putative Zinc Finger Protein Binding Sites Are Over-Represented in the Boundaries of Methylation-Resistant CpG Islands in the Human Genome"*
> · *"CpG Islands: Starting Blocks for Replication and Transcription"*

### Step 5 Text Snippet 예시 (Table 2)
> *"A common explanation for the G+C rise that is seen here in the mammalian profile in the proximity of the TSS is the presence of CpG islands, ..."*

### Step 8 Ideal Answer (Table 3, verbatim)
> *"Yes. It is generally known that the presence of a CpG island around the TSS is related to the expression pattern of the gene. ..."*

## 실제 인스턴스 예시 (JSON format)

```json
{
  "id": "52bf1b0a03868f1b06000009",
  "body": "Do CpG islands colocalise with transcription start sites?",
  "type": "yesno",
  "documents": [
    "https://www.ncbi.nlm.nih.gov/pubmed/838566", ...
  ],
  "snippets": [
    {"text": "A common explanation for the G+C rise that is seen
              here in the mammalian profile in the proximity of
              the TSS is the presence of CpG islands, ...",
     "document": "...", "beginSection": "abstract",
     "offsetInBeginSection": 122, "offsetInEndSection": 272}, ...
  ],
  "concepts": ["https://www.disease-ontology.org/api/metadata/DOID:893", ...],
  "triples": [{"s":"...","p":".../name","o":"Wilson_disease"}, ...],
  "ideal_answer": ["Yes. It is generally known that the presence
                    of a CpG island around the TSS is related to
                    the expression pattern of the gene. ..."],
  "exact_answer": "yes"
}
```

---

## 평가 메트릭 (Task B)

| Phase | 평가 대상 | 메트릭 |
|---|---|---|
| **Phase A** | Document retrieval | MAP, Mean Precision/Recall/F-measure |
|  | Snippet retrieval | MAP, Mean Precision/Recall/F-measure |
|  | Concept retrieval | (동일) |
|  | RDF triple retrieval | (동일) |
| **Phase B** | Exact answer (Yes/No) | **Macro F1** (BioASQ-6부터 공식 / Accuracy 병기) |
|  | Exact answer (Factoid) | Mean Reciprocal Rank, Strict/Lenient Accuracy |
|  | Exact answer (List) | Mean F1 |
|  | Ideal answer | 1–5 manual scoring × 4 criteria (recall / precision / repetition / readability) |

---

## 한계점
- **English only** — 다국어 의생물학 QA 불가.
- **연 1회 업데이트** — PubMed에 분당 2편 등록되는 환경에 비해 최신 문헌 반영 지연.
- **Abstract only** (BioASQ-4부터): full-text PMC 활용 안 함 → 표·그림 등 abstract 외 정보 평가 불가.
- **Linked Life Data 폐기** → RDF triple 평가축은 사실상 비활성.
- **Expert 편향**: 21명 중 유럽 비중 압도 → 글로벌 임상 다양성 부족 가능.
- **Controversial 질문 회피 정책**: 명확한 답이 없는 의학 논쟁은 의도적으로 제외 → real-world 임상 의사결정 시나리오 일부 누락.

---

## 관련 정보
- **논문**: [Scientific Data 10:170 (2023)](https://doi.org/10.1038/s41597-023-02068-4)
- **공식 사이트**: [bioasq.org](http://bioasq.org)
- **데이터 다운로드**: [participants-area.bioasq.org](http://participants-area.bioasq.org)
- **이 벤치마크를 사용하는 주요 후속 작업**:
  - MEDRAG/MIRAGE (Xiong et al., ACL 2024) — BioASQ-Y/N 618 질문을 MC 형식으로 재구성
  - AlzheimerRAG (Lahiri & Hu, MAKE 2025) — cross-modal 평가에 사용
  - PubMedQA의 비교 대상 (Jin et al., EMNLP-IJCNLP 2019)
