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
## 🔨 Construction Methodology
**Step 1 — 데이터 출처 선정**
GeoGPT 라이브러리 코퍼스 중에서 1,000개의 오픈 액세스 지구과학 논문을 무작위 샘플링하여 초기 컨텍스트로 활용함.
**Step 2 — 구축 파이프라인**
RAGAS Test Set Generation 모듈 활용. 기저 LLM으로 gpt-4o를 사용하여 논문 텍스트 기반으로 질문-정답(QA) 쌍을 자동 생성함. 임베딩 기반 유사성 검색에는 text-embedding-3-small 모델을 병행 사용함.
**Step 3 — 품질 검증**
불완전하거나 손상된 항목을 수동으로 평가(Manual Review)하여 치명적 결함이 있는 62개의 예제를 제거함. "답이 문맥에 존재하지 않음" 식의 잘못 연결된 레퍼런스 정답에 대해서는 gpt-4o를 사용해 정답을 재생성(Regenerate)하여 평가 일관성을 보강함.
**Step 4 — 데이터셋 구성 및 공개**
총 938개의 최종 QA 쌍 완성 후 HuggingFace Dataset으로 공개함.
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
