---
notion_id: 355f2dcd-4912-8173-be88-d85ffb1b9127
title: GeoGPT-RAG Technical Report
bib_key: DBLP:journals/corr/abs-2509-09686
year: 2025
domain: earth
type: benchmark
venue: arXiv
paper_link: https://arxiv.org/abs/2509.09686v2
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# GeoGPT-RAG Technical Report

> arXiv | 2025 | benchmark | earth
## 📌 한 줄 요약
오픈 액세스 지구과학 학술 논문 1,000건을 바탕으로 GPT-4o 및 RAGAS 프레임워크를 활용해 자동 및 수동 검수로 구축된 938개 문항의 지구과학 RAG 검색 전문 벤치마크 데이터셋.
## 🎯 제작 배경
- **기존 벤치마크의 한계**: MTEB이나 BEIR와 같은 범용 정보 검색 벤치마크는 지질학, 석유 탐사 등 극도로 전문화된 어휘와 구조를 다루는 지구과학 분야의 언어 모델 정보 탐색 능력을 측정하기에는 부적합함.
- **필요성**: 고품질 레이블이 부족한 환경을 극복하고, RAG 시스템 개발에서 지구과학 검색 및 응답 성능을 객관적으로 계량화하기 위한 표준화된 측정 도구가 절실하게 필요했음.
## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — 소스 코퍼스 구성
  GeoGPT 라이브러리에서 오픈 액세스 지구과학 논문 1,000편 무작위 샘플링
  (석유 탐사, 지질학, 지구물리학 등 세부 분야 포함)

Step 2 — 자동 QA 쌍 생성 (RAGAS 프레임워크)
  ┌─ LLM: GPT-4o (질문·정답 생성)
  └─ Embedding: text-embedding-3-small (유사성 검색)

  생성 질문 유형 4종:
  ┌──────────────────────────────┬──────┐
  │ 유형                          │ 문항수 │
  ├──────────────────────────────┼──────┤
  │ Single-document fact-based   │  250 │
  │ Single-document inference    │  250 │
  │ Multi-document               │  188 │
  │ Conditional                  │  250 │
  ├──────────────────────────────┼──────┤
  │ 초기 생성 합계                │1,000 │
  └──────────────────────────────┴──────┘

Step 3 — 수동 품질 검증
  결함 있는 62개 제거 (잘못 연결된 정답 참조 포함)
  → 오답 참조 문항: GPT-4o로 정답 재생성

Step 4 — 최종 공개
  938개 QA 쌍 → HuggingFace Dataset 공개
```

> **주의**: GeoRAG-QA는 **open-ended free-text** 벤치마크. 정답은 MC 선택지가 아닌 문장 형태이며, 평가 메트릭은 Answer Recall (RAGAS 기반). Closed-form MC 벤치마크가 아님.
## 실제 문항 형식 예시

### 유형 A — Single-document fact-based (단일 문서 사실형)
> **Q.** What is the primary porosity type in carbonate reservoirs formed through dissolution processes?
>
> **A.** Vuggy porosity, formed when carbonate minerals are dissolved by acidic fluids, creating irregular pore spaces that can significantly enhance reservoir permeability.

### 유형 B — Inference QA (추론형)
> **Q.** Based on the seismic velocity contrast described in the study, what does a negative reflection coefficient at the target horizon indicate about the overlying formation?
>
> **A.** A negative reflection coefficient indicates that the overlying formation has higher acoustic impedance than the target, suggesting a transition from a harder to a softer rock unit, often associated with fluid-saturated porous formations.

### 유형 C — Multi-document (다중 문서 통합형)
> **Q.** How do the tectonic settings described across the cited studies differ in their influence on fault orientation and trap geometry for hydrocarbon accumulation?
>
> **A.** *(복수 논문에서 정보 통합 필요 — retriever가 여러 문서를 검색해야 함)*

> 평가 메트릭: **Answer Recall** (RAGAS) — 모델 답변이 정답 문장들을 얼마나 포함하는지 측정. 선택지 없음.

---

## 📥 Input (입력)
지구과학 전문 논문 텍스트 조각(Chunk)을 바탕으로 한 자연어 질의(Question).
<table header-row="true">
<tr>
<td>질문 유형</td>
<td>문항 수</td>
</tr>
<tr>
<td>Single-document, fact-based QA</td>
<td>250</td>
</tr>
<tr>
<td>Single-document inference QA</td>
<td>250</td>
</tr>
<tr>
<td>Multi-document QA</td>
<td>188</td>
</tr>
<tr>
<td>Conditional QA</td>
<td>250</td>
</tr>
</table>
## 📤 Output (출력 / 정답 형식)
모델이 생성한 텍스트 형태의 정답. 평가 지표: Answer Recall (RAGAS 기반), Top-K Recall (검색기 성능 측정용).
## 📊 주요 평가 결과
GeoGPT-RAG (GeoEmbedding) Top-K Recall: Top-1 0.908 / Top-3 0.945 / Top-5 0.950 / Top-8 0.959.
## ⚠️ 한계점
- GPT-4o가 기계적으로 역산하여 질문을 만들었으므로, 실제 연구 현장의 도메인 전문가가 백지에서 물어보는 직관적/모호한 형태의 질문 분포와는 다를 수 있음.
- 오픈 액세스 논문 1,000건만 샘플링하여 접근이 제한적인 고급 학술지 정보는 커버리지에서 누락될 가능성이 있음.
## 🔗 관련 정보
- 논문 링크: [https://arxiv.org/abs/2509.09686v2](https://arxiv.org/abs/2509.09686v2)
- HuggingFace Dataset: [https://huggingface.co/datasets/GeoGPT-Research-Project/GeoRAG-QA](https://huggingface.co/datasets/GeoGPT-Research-Project/GeoRAG-QA)
- **이 벤치마크를 사용한 논문:** GeoGPT-RAG Technical Report (arXiv 2025)
