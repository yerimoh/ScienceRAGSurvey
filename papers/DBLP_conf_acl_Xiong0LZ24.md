---
notion_id: 355f2dcd-4912-8123-adc6-fa02ef47607e
title: Benchmarking Retrieval-Augmented Generation for Medicine
bib_key: DBLP:conf/acl/Xiong0LZ24
year: 2024
domain: medical, bio
type: benchmark
venue: ACL (Findings)
paper_link: https://aclanthology.org/2024.findings-acl.372
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# MIRAGE / MEDRAG: Benchmarking Retrieval-Augmented Generation for Medicine

> ACL Findings 2024 | Benchmark + Toolkit | medical · bio

## 한 줄 요약
의료 RAG 시스템 평가를 위한 벤치마크 **MIRAGE**(7,663 MC 문항)와 표준화된 툴킷 **MEDRAG**를 함께 제안. 5개 의료 QA 데이터셋을 통합하여 Zero-shot + Question-Only Retrieval 조건에서 retriever·corpus·LLM 조합을 체계적으로 비교한다.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 소스 데이터셋 선정
  └─ 생의학 분야에서 널리 쓰이는 5개 MC QA 데이터셋 선택
     (MMLU-Med / MedQA-US / MedMCQA / PubMedQA* / BioASQ-Y/N)

Step 2 — 전처리 (공정한 RAG 평가를 위한 정보 제거)
  └─ Gold supporting context 완전 제거
     (RAG가 스스로 찾아야 하는 조건 강제)
  └─ PubMedQA: 주어진 abstractcontext 500개 모두 제거
  └─ 모든 문항 → Zero-shot + Question-Only Retrieval(QOR) 설정

Step 3 — 통합 및 통계 검증
  ┌──────────────┬───────┬──────────┬──────────────────┐
  │ 데이터셋      │ 문항수 │ 선택지수 │ 출처             │
  ├──────────────┼───────┼──────────┼──────────────────┤
  │ MMLU-Med     │ 1,089 │ 4지      │ 의학 전문 시험   │
  │ MedQA-US     │ 1,273 │ 4지      │ USMLE 문제       │
  │ MedMCQA      │ 4,183 │ 4지      │ 인도 의학 입시   │
  │ PubMedQA*    │   500 │ 3지      │ 연구 논문 추론   │
  │ BioASQ-Y/N   │   618 │ 2지      │ 생의학 전문가    │
  ├──────────────┼───────┼──────────┼──────────────────┤
  │ MIRAGE 합계  │ 7,663 │ 2–4지    │                  │
  └──────────────┴───────┴──────────┴──────────────────┘

Step 4 — MedCorp 코퍼스 구축 (검색 대상)
  PubMed (23.9M) + StatPearls (9.3K) + Textbooks (18권)
  + Wikipedia (6.5M) → 총 30.4M 문서 / 54.2M 스니펫
  청크: LangChain RecursiveCharacterTextSplitter (최대 1,000자 / 평균 221 토큰)

Step 5 — MEDRAG 툴킷으로 평가 표준화
  검색기 4종(BM25 / Contriever / SPECTER / MedCPT)
  × 코퍼스 5종 × LLM 6종 → 체계적 조합 비교
```

---

## 실제 문항 형식 예시

### 유형 A — MMLU-Med / MedQA-US (4지 선다)
> **Q.** A 45-year-old man presents with crushing substernal chest pain radiating to the left arm. ECG shows ST-segment elevation in leads II, III, and aVF. Which coronary artery is most likely occluded?
>
> (A) Left anterior descending  
> (B) Left circumflex  
> (C) **Right coronary artery** ← 정답  
> (D) Left main coronary artery
>
> *평균 질문 길이: 177 tokens (MedQA-US)*

### 유형 B — MedMCQA (4지 선다, 짧은 형식)
> **Q.** Drug of choice for status epilepticus is:
>
> (A) Phenytoin  (B) Phenobarbitone  (C) **Diazepam** ← 정답  (D) Carbamazepine
>
> *인도 의학 입시(AIIMS/NEET PG) 스타일 — 평균 26 tokens*

### 유형 C — PubMedQA* (3지 선다, 연구 추론)
> **Q.** Does the administration of low-dose aspirin reduce the risk of colorectal cancer?
>
> (A) **Yes** ← 정답  (B) No  (C) Maybe
>
> *원래 함께 제공된 PubMed abstract를 MIRAGE에서 제거 → RAG가 직접 검색해야 함*

### 유형 D — BioASQ-Y/N (2지 선다)
> **Q.** Is BRCA1 involved in DNA double-strand break repair?
>
> (A) **Yes** ← 정답  (B) No
>
> *생의학 전문가 제작, 평균 17 tokens*

---

## 주요 평가 결과

| LLM | CoT 단독 | MEDRAG (MedCorp+RRF-4) | 향상 |
|---|---|---|---|
| GPT-4 | 73.44% | **79.97%** | +6.53%p |
| GPT-3.5 | 60.69% | 71.57% | +10.88%p |
| Mixtral 8×7B | 61.42% | 69.48% | +8.06%p |
| MEDITRON-70B | 57.04% | 60.18% | +3.14%p |
| PMC-LLaMA-13B | 36.82% | 46.52% | +9.70%p |

**핵심 발견:** GPT-3.5+MEDRAG가 CoT-only GPT-4에 근접 → 좋은 검색기가 LLM 크기를 상당 부분 대체

---

## 한계점
- Vanilla RAG (single-step) 아키텍처에 국한 — Active RAG / multi-hop retrieval 평가 없음
- PubMed Central 전문, 임상 FAQ 등 더 넓은 소스 제외
- 모든 문항이 객관식 → Open-ended 의료 RAG 성능 측정 불가

---

## 관련 정보
- **논문**: [ACL Anthology](https://aclanthology.org/2024.findings-acl.372)
- **GitHub (MEDRAG)**: [https://github.com/Teddy-XiongGZ/MedRAG](https://github.com/Teddy-XiongGZ/MedRAG)
- **GitHub (MIRAGE)**: [https://github.com/Teddy-XiongGZ/MIRAGE](https://github.com/Teddy-XiongGZ/MIRAGE)
- **이 벤치마크를 사용한 논문**: MEDRAG (본 논문), BIORAG (arXiv 2024), RAG² (NAACL 2025)
