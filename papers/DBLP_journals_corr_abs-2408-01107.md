---
title: "BioRAG: A RAG-LLM Framework for Biological Question Reasoning"
bib_key: "DBLP:journals/corr/abs-2408-01107"
year: 2024
domain: bio, medical
type: Method
venue: arXiv 2024
paper_link: https://arxiv.org/abs/2408.01107
---
# BioRAG: A RAG-LLM Framework for Biological Question Reasoning

> arXiv 2024 | 2024 | Method | bio · medical

## 한 줄 요약
22,371,343편의 PubMed 초록을 색인하고, MeSH 분류 모델 + 도메인 임베딩 + 자체 평가(self-evaluation) 루프 + 외부 검색 도구(Gene/dbSNP/Protein/Genome 4개 NCBI API + 검색엔진 등 10개 외부 소스)를 결합한 5단계 반복 RAG 파이프라인. GeneTuring 9개 sub-task와 4개 의생물 QA 벤치마크에서 GeneGPT·NewBing·BioMistral·PMC-Llama 등 기존 BioLLM 및 SciRAG 시스템을 모두 능가한다.

## 제작 배경
**기존 접근법의 한계**
- Fine-tuned BioLLM (BioMistral, PMC-Llama 등)은 학습 시점의 지식만 보유 → 빠르게 진화하는 생명과학 분야에서 cutoff 문제 심각
- 단일 RAG 시스템 (GeneGPT)은 특정 API 호출(Gene, dbSNP)에만 특화되어 멀티-홉 추론 불가
- 일반 검색엔진 기반 RAG (NewBing)는 dbSNP, PubMed 같은 권위 있는 도메인 소스 접근 불가 → "BIORAG and GeneGPT achieve 100% accuracy in the gene SNP association sub-task, as both of them have access to the dbSNP database. However, NewBing has no access to the dbSNP database, thus it gets 0% accuracy in this task." (논문 p.7)

**왜 이 시스템이 필요한지**
- 학제 융합 연구에서는 분자 → 세포 → 조직 → 개체 수준을 가로지르는 다층 지식이 필요
- 단계별 추론(step-by-step reasoning) + 정보 부족 시 자동 외부 검색 전환이 가능한 closed-loop RAG 필요

## 어떻게 만들었나 (Construction Methodology)
**전체 5단계 파이프라인 (논문 Figure 2)**
```
[Input Question]
       │
       ▼
 ① Retriever Selection
   - 질문 유형 분석 → 어느 소스가 가장 적합한지 LLM이 결정
   - Internal (PubMed local) vs External (Gene/dbSNP/Protein/Genome/Crossref/Wikimedia/biorxiv 등)
       │
       ▼
 ② Query Pre-processing
   - 질의를 재작성 + MeSH topic tag 추출 (MMeSH = Llama3-8B fine-tuned)
   - 예: "innate vs adaptive immunity" → MeSH: [Adaptive Immunity, Animals, ...]
       │
       ▼
 ③ Retriever Execution
   - Internal: MeSH SQL filter + 임베딩 cosine 정렬
   - External: NCBI Entrez API 호출 / 검색엔진 호출
       │
       ▼
 ④ Self-Evaluation (← 핵심 루프)
   - LLM이 "검색 결과가 답변에 충분한가" 자체 판정
   - 불충분 시 ①로 되돌아가 다른 소스 재시도 (최대 15회)
       │
       ▼
 ⑤ Inference and Generation
   - 최종 답변 + 인용 출처 출력
```

### 핵심 구성 요소
**Internal Source: PubMed 22M 초록**
- 2024 PubMed baseline 전체 파싱
- HTML/링크/표 제거 후 22,371,343편의 고품질 abstract 청크 확보

**MMeSH (MeSH Classifier)**
- Llama3-8B fine-tuned with template: `"QUESTION: [.....] MeSH: [κ1, κ2, ...]"` (Figure 3)
- 예측된 MeSH terms로 SQL `filtered by: eq("MeSH", "Adaptive Immunity") or ...` 생성 (Figure 4)
- 1차 필터링 후 임베딩 유사도로 정렬

**Domain-Specific Embedding Model**
- AdamW, 2 epochs, PubMed 텍스트에 대해 도메인 적응
- 일반 임베딩 대비 생물학 전문 용어 분리력 향상

**External Sources (논문 Table)**
- NCBI Gene / dbSNP / Genome / Protein (4 entities × Entrez API)
- biorxiv (preprints)
- Wikimedia (개념 정의)
- Crossref (citation network)
- Search engine (general web)

**Customized 5-Prompt Chain (논문 Appendix)**
> "Prompt #1: To provide the most helpful and accurate response to the following Question: {Question}. You have been given descriptions..."
> "Prompt #2: Based on the RETRIEVAL METHODS you selected, and considering the Question and the Input Requirements..."
> "Prompt #4: Based on the RETRIEVAL RESULTS from the above steps, please evaluate whether the RESULTS support answering the..."
> "Prompt #5: Based on the RETRIEVAL RESULTS, perform a comprehensive reasoning and provide an answer to the Question."

## Input/Output
**Input**
- Biological question (free-form): nomenclature, genomic location, gene-disease association, functional analysis, protein-coding identification, multiple-choice biology/medicine questions

**Output**
- 자연어 답변 + (선택) 인용 출처
- 9 sub-task의 경우: gene symbol (예: "ARHGEF26"), location (chromosome band), Yes/No 또는 MCQ 정답

## 예시 사례
### 예시 ① — Gene Alias Task (GeneTuring; 논문 Figure 6)
> **Query**: "What is the official gene symbol of SGEF?"
>
> **BioRAG 실행 로그**
> > Thought: I can use the Gene tool to find the official gene symbol of SGEF.
> > Query Preprocessing → "SGEF"
> > Retriever Selection → Gene (NCBI)
> > Retriever Execution And Result:
> > "Official Symbol: ARHGEF26"
> > "Name: Rho guanine nucleotide exchange factor 26"
> > "Other Aliases: CSGEF, HMFN1864, SGEF"
> > Self-Evaluation: "The necessary information has been obtained to form an answer."
> > Inference and Generation: "The official gene symbol for SGEF is ARHGEF26."
>
> **NewBing 비교**: "The official gene symbol for SGEF is SGEF (Src homology 3 domain-containing Guanine nucleotide Exchange Factor)." → **오답** (NewBing은 Wikipedia 스니펫만 조회)
>
> **GeneGPT 비교**: Entrez API 호출은 성공하지만 alias 처리 미흡

### 예시 ② — Multi-hop Gene-Disease Reasoning (Figure 7)
> **Query**: "What are genes related to B-cell immunodeficiency?"
>
> **BioRAG 다단계 실행**
> > Step 1: Retriever Selection = Gene → "Official Symbol: TOP2B, Other Aliases: BILU, TOPIIB, top2beta"
> > Self-Evaluation: "Use the PubMed tool to conduct further searches on genes and diseases." (1차 결과 불충분 → 외부 점프)
> > Step 2: Retriever Selection = PubMed → "B cell development is a highly... Topoisomerase 2β (TOP2B) introduces..."
> > MeSH Mapping = Immunoglobulin G1 Fragments
> > 최종 답변: TOP2B 등 관련 유전자 목록

### 예시 ③ — College Biology MCQ (Figure 5)
> **Question (litter size in rodents)** → BioRAG
> > Retriever Selection: PubMed Search → "Parental investment and litter size in rodents"
> > MeSH Mapping: Parental Behavior, Rodentia
> > Self-Evaluation: "Small litter sizes in rodents may be an adaptation to their specialized diet, requiring more parental investment."
> > Output: "Option B: High parental investment"

## 주요 평가 결과
**Table 1 — GeneTuring (9 sub-tasks, accuracy %)**
| Sub-task | GPT-3.5 | Llama-70B | BioMistral | GeneGPT | NewBing | **BioRAG** |
|---|---|---|---|---|---|---|
| Gene_alias | – | – | – | 98 | – | **100** |
| SNP_location | – | – | – | 100 | 0 | **100** |
| Gene_disease_association | – | – | – | 0 | 8 | **71** |
| Protein-coding genes | – | – | – | 40 | 80 | **100** |
| Gene_name_conversion | – | – | – | 66 | 32 | **71** |
| Functional analysis | 5 | 48 | 94 | 0 | 0 | **98** |
| Gene_alias (variant col) | – | – | – | – | – | **100** |

**Table 2 — Biological QA 벤치마크 (accuracy %)**
| Dataset | GPT-3.5 | Llama-70B | BioMistral | PMC-Llama | GeneGPT | NewBing | **BioRAG** |
|---|---|---|---|---|---|---|---|
| MedMCQA | 54 | 51 | 71 | 56 | 49 | 55 | **73** |
| Medical Genetics | 74 | 51 | 67 | 28 | 67 | 88 | **88** |
| College Biology | 73 | 75 | 88 | 30 | 67 | 71 | **90** |
| College Medicine | 65 | 61 | 70 | 23 | 51 | 78 | **78** |

**핵심 인사이트**
- BioRAG는 nomenclature/genomic location 같은 API 의존 task에서 GeneGPT와 동률 100%
- gene-disease association처럼 reasoning이 필요한 task에서는 GeneGPT(0%) > NewBing(8%) ≪ **BioRAG(71%)**

## 한계점
- Self-evaluation 루프 최대 15회 고정 → 깊은 multi-hop 질의에서 조기 종료 위험
- 22M PubMed 인덱싱 + Llama3-70B 추론 비용 매우 큼
- MeSH는 의생물 외 분야(화학, 재료 등)에는 적용 불가
- 외부 API 의존 → NCBI/Crossref 가용성 실패 시 fallback 미정의
- 추론 chain이 길어질수록 prompt 토큰 비용 폭증

## 관련 정보
- **논문 (arXiv)**: [https://arxiv.org/abs/2408.01107](https://arxiv.org/abs/2408.01107)
- **저자 소속**: Zhejiang University, OPPO Research, ETH Zürich
- **벤치마크**: GeneTuring (Hou & Ji 2023), MedMCQA, MMLU subset (Medical Genetics, College Biology, College Medicine)
- **기본 LLM**: Llama3-70B
- **K×O 분류**: K1.O1 (PubMed 문헌) + K2.O1 (NCBI 큐레이션 DB) — 다중 소스 결합 패턴
