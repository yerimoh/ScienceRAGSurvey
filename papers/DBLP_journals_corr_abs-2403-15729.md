---
title: "Towards a RAG-based Summarization Agent for the Electron-Ion Collider"
bib_key: "DBLP:journals/corr/abs-2403-15729"
year: 2024
domain: physics
type: Method
venue: arXiv 2024
paper_link: https://arxiv.org/abs/2403.15729
---
# Towards a RAG-based Summarization Agent for the Electron-Ion Collider (RAGS4EIC)

> arXiv:2403.15729 | 2024 | Method | physics
> AI4EIC — EIC Collaboration (1,400명+ 물리학자, 38개국)

## 한 줄 요약
38개국 1,400명+ 물리학자가 참여하는 **EIC(Electron-Ion Collider)** 협업의 방대한 기관 문서·논문·데이터를 단일 벡터 DB에 인덱싱하고, LLM(GPT-3.5)으로 **인용이 풍부한 간결 요약**을 생성하는 LangChain 기반 RAG 에이전트. **RAGAS 점수 평가에서 Hallucination Frequency 2%, Context Entity Recall 98.7%** 달성.

## 제작 배경
**기존 접근법의 한계**
- 38개국 1,400명+ 물리학자가 참여하는 EIC 협업에서 다수 워킹 그룹 간 정보 큐레이션 조율이 어려움
- 신규 협력자·초기 경력 과학자가 방대한 EIC 데이터·문서를 이해하는 데 시간 집약적
- 실험과 데이터 수집 중 shift taker가 검토해야 하는 문서량이 초보자에게 압도적

**왜 이 시스템이 필요했는지**
- 시프트 근무 중 즉시 참조할 가상 보조원 필요
- 협업적 참여를 장려하고 신규 연구자 진입 장벽 완화
- LLM 환각(hallucination)을 인용 기반 응답으로 억제하여 신뢰성 확보

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 지식 베이스 구축 (Fig. 2)
  ┌─ 데이터 소스 : EIC 관련 wiki, run logs, PDFs, 미태깅 자료
  ├─ OCR + DL 모델로 텍스트화 (그림·이미지는 추출 한계)
  ├─ PDF Reader : PyPDF2 (그림 손실 발생)
  ├─ LaTeX Reader : LatexSplitter
  └─ Chunking : LangChain RecursiveCharacterTextSplitter

Step 2 — 벡터화 + 인덱싱
  Embedding model로 chunk → vector
  VectorDB 저장 (cf. 후속 jat2026retrieval에서 ChromaDB로 진화)

Step 3 — 온라인 추론 파이프라인 (Fig. 3)
  사용자 질문 + (cosine sim or MMR) 선택
       ↓
  decision chain (LLM이 KB 참조 필요 여부 판단)
       ↓
  필요 시 VectorDB에서 context + sources 검색
       ↓
  fine-tuned prompt template + 검색 컨텍스트 + 질문
       ↓
  GPT-3.5-turbo-1106 (LLM) — citation 포함 응답
       ↓
  GitHub markdown 포맷 출력 (syntactic LLM)

Step 4 — LLM-assisted 벤치마크 생성
  ┌─ 도메인: hep.ph / nucl-ex / ph-acc
  ├─ "annotator"가 arXiv 논문 선택 + claim 수 N 지정
  ├─ GPT-4.0이 (Question, Answer{claims, ideal_response, full_response}) 생성
  └─ annotator가 review·수정·등록
  → AI4EIC2023_DATASETS (50 questions × up to 3 claims)

Step 5 — 평가 (RAGAs framework)
  Standard metrics + RAGAs LLM-judge metrics (GPT-4)
```

## Input (입력)
- 벡터 DB: EIC institutional documents, arXiv 논문, run logs, wikis, technical design reports
- 사용자 질의: 자연어 (Streamlit web app: `rags4eic-ai4eic.streamlit.app`)
- 검색 설정: cosine similarity / MMR, top-k=20

## Output (출력 / 정답 형식)
- GitHub-markdown 형식 요약 + arXiv 인용
- LangSmith로 추적되는 inference trace

## 예시 문항 (논문 5장 평가 + Appendix A 직접 인용)

### 📘 벤치마크 데이터셋 생성 프로세스 (본문 그대로)
> "The 'annotator' chooses an arXiv paper (with an option for a random, unexplored selection), the total questions to generate, and the claims per question. GPT-4.0 then processes the paper's contents using a template to produce formatted Question and Answer pairs."

### 📘 데이터셋 구조 (각 Q는 N개의 "claims" 보유)
> "Each QA pair has a question with 'N' claims and a detailed json object which has detailed information about the answers. The json object contains the number of claims in the questions, the individual claims, ideal response to each of the individual claims, and a complete response involving all the claims."

### 📘 도메인 범위
> "The dataset selected for this research encompasses a variety of disciplines, ranging from hep.ph to nucl-ex to ph-acc" *(arXiv categorical codes in physics)*

### 📘 핵심 한계 (저자 직접 인용)
> "The RAG Agent's ability to provide accurate responses to inquiries decreases significantly when dealing with questions that involve physics equations (including special LaTeX characters)."

> 예시 사용 사례: Appendix A의 Fig. 4·5에서 "annotator" 인터페이스 + 추론 흐름이 시각화됨. 본문은 구체적 Q 텍스트를 인용하지 않으며, AI4EIC2023_DATASETS의 50개 Q×3 claim은 GitHub 코드에 분리 공개됨.

## 주요 평가 결과

**Standard Metrics (Table 2, 50Q × 3 claim)**

| Metric | 정의 | Score |
|---|---|---|
| Claim Recognition Rate | answered claims / total claims | **96.4 ± 3.4%** |
| Claim Accuracy Rate | correctly answered claims / recognized | 88.9 ± 8.3% |
| Source Citation Frequency | source-cited queries / total | 85.3 ± 5.0% |
| **Hallucination Frequency** | hallucinations / total queries | **2 ± 2%** |

**RAGAs LLM-as-judge (Table 3, GPT-4 평가)**

| Metric | Score |
|---|---|
| Faithfulness (markdown rendering correctness) | 87.4 ± 5.5% |
| Context Relevancy | 61.4 ± 4.3% |
| **Context Entity Recall** | **98.7 ± 1.2%** |
| Answer Relevance | 77.2 ± 2.3% |
| Answer Correctness | 72.3 ± 2.4% |

## 한계점 (저자 명시)
- **Context Relevancy 61.4%**: k=20 고정 검색으로 인해 redundant 정보가 많이 포함됨 (응답이 짧을 때 두드러짐)
- **물리 수식 처리 약점**: LaTeX 수식이 포함된 질문에서 정확도가 명백히 하락 → 더 나은 chunking 전략 필요
- **루팅 로직**: GitHub markdown rewriting을 위한 instruction-tuning 추가 필요
- **재현성**: LangSmith trace로 부분 해결, 그러나 LLM stochasticity로 인한 한계 남음
- **클라우드 호스팅 외부 KB 사용** → 미출판 사전 공개 데이터의 외부 전송 위험 (후속 jat2026retrieval에서 로컬 배포로 해결)

## 관련 정보
- **논문 (arXiv)**: [https://arxiv.org/abs/2403.15729](https://arxiv.org/abs/2403.15729)
- **웹 앱**: [https://rags4eic-ai4eic.streamlit.app](https://rags4eic-ai4eic.streamlit.app)
- **소스 코드**: [https://github.com/ai4eic/EIC-RAG-Project](https://github.com/ai4eic/EIC-RAG-Project)
- **AI4EIC2023_DATASETS**: GitHub 공개 (50Q × 3 claim)
- **후속 작업**: jat2026retrieval (arXiv:2604.02259) — 로컬 배포 LLaMA 기반 확장
