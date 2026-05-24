---
notion_id: 355f2dcd-4912-815c-b521-d607762bcce7
title: Benchmarking Foundation Models with Retrieval-Augmented Generation in Olympic-Level Physics Problem Solving
bib_key: DBLP:conf/emnlp/ZhengZFZWPC25
year: 2025
domain: physics
type: Method
venue: EMNLP (Findings)
paper_link: https://aclanthology.org/2025.findings-emnlp.1196/
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Benchmarking Foundation Models with Retrieval-Augmented Generation in Olympic-Level Physics Problem Solving

> EMNLP (Findings) | 2025 | Method | physics
## 📌 한 줄 요약
Physics Olympiad 문제 풀이를 위한 최초의 멀티모달 RAG 벤치마크 **PhoPile**을 구축하고, 8개 foundation model × 7종 retriever 조합으로 RAG의 물리 추론 향상 가능성을 종합 평가한 연구.
## 🎯 연구 배경 및 동기
### 기존 방법의 한계점
- 기존 자연과학 데이터셋(SciQ, ScienceQA 등)은 초중고 수준의 단순 문제로 구성되어 전문가 수준의 물리 추론 벤치마킹에 부적합
- Foundation model들은 도메인 특화 전문 지식 부족, 잦은 환각(hallucination), 물리 법칙 적용의 일관성 부재 문제를 가짐
- Olympiad 수준 물리 문제는 다이어그램·그래프·수식을 필수적으로 포함하는 멀티모달 특성이 있으나, 기존 RAG 연구는 텍스트 위주
### 이 연구가 필요한 이유
- 수험생이 과거 유사 문제를 참고하여 새 문제를 푸는 방식(few-shot retrieval)을 AI에 적용하면 물리 추론 능력을 향상시킬 수 있다는 가설 검증 필요
- Olympiad 문제는 연도 간 유사 개념이 반복되므로 RAG의 효용이 기대됨
## 🏗️ 시스템 아키텍처
[image]
```javascript
[Physics Olympiad 문제 입력 (쿼리)]
        ↓
[Retriever] → PhoPile Corpus (2,662문제, 과거 연도)
        ↓ Top-k 유사 문제+해설 반환
[Generator (LLM/LMM)] ← k-shot 예시로 활용
        ↓
[생성된 풀이]
        ↓ (선택적)
[Reflection: GPT-4가 답안 재검토·수정]
        ↓
[GPT-4 Judge: 0/5/10점 step-wise + solution-level 채점]
```
## 🔑 핵심 모듈 상세 설명
### PhoPile 데이터셋
<table header-row="true">
<tr>
<td>구성 요소</td>
<td>내용</td>
</tr>
<tr>
<td>총 문제 수</td>
<td>3,052문제</td>
</tr>
<tr>
<td>Retrieval Corpus</td>
<td>2,662문제 (2018년 이전 출제분)</td>
</tr>
<tr>
<td>Test Set</td>
<td>390문제 (2019~2021년 출제분)</td>
</tr>
<tr>
<td>대회 출처</td>
<td>IPhO, APhO, EuPhO, NBPhO, RMPhO, AAPT, BPhO (7개)</td>
</tr>
<tr>
<td>모달리티</td>
<td>텍스트 + 이미지(다이어그램, 그래프, 수식)</td>
</tr>
</table>
### Retriever 목록
<table header-row="true">
<tr>
<td>유형</td>
<td>Retriever</td>
<td>특징</td>
</tr>
<tr>
<td>Text-only</td>
<td>BM25</td>
<td>어휘 기반 검색</td>
</tr>
<tr>
<td>Text-only</td>
<td>Contriever</td>
<td>비지도 학습 dense retriever</td>
</tr>
<tr>
<td>Text-only</td>
<td>DPR</td>
<td>Dense Passage Retriever</td>
</tr>
<tr>
<td>Text-only</td>
<td>DRAGON</td>
<td>다양한 증강 기반 dense retriever</td>
</tr>
<tr>
<td>Multimodal</td>
<td>VisualBERT 기반</td>
<td>이미지+텍스트 결합 임베딩</td>
</tr>
<tr>
<td>Multimodal</td>
<td>CLIP 기반</td>
<td>OpenAI 멀티모달 임베딩</td>
</tr>
<tr>
<td>Multimodal</td>
<td>BLIP 기반</td>
<td>부트스트래핑 언어-이미지 사전학습</td>
</tr>
</table>
### Generator 목록
<table header-row="true">
<tr>
<td>모델</td>
<td>유형</td>
<td>참고</td>
</tr>
<tr>
<td>GPT-3.5-turbo</td>
<td>LLM</td>
<td>OpenAI API</td>
</tr>
<tr>
<td>GPT-4</td>
<td>LLM</td>
<td>OpenAI API</td>
</tr>
<tr>
<td>GPT-4V</td>
<td>LMM</td>
<td>OpenAI API (Vision)</td>
</tr>
<tr>
<td>Gemini-Pro</td>
<td>LLM</td>
<td>Google API</td>
</tr>
<tr>
<td>Gemini-Pro-Vision</td>
<td>LMM</td>
<td>Google API (Vision)</td>
</tr>
<tr>
<td>ChatGLM</td>
<td>LLM</td>
<td>오픈소스</td>
</tr>
<tr>
<td>(기타 LLM 포함)</td>
<td>-</td>
<td>총 8개 모델</td>
</tr>
</table>
### GPT-4 Judge 평가 프레임워크
- **Step-wise 평가**: 풀이 과정 단계별 정확성 확인
- **Solution-level 평가**: 최종 답안 정확성 확인
- **점수 체계**: 0점(완전 오답) / 5점(부분 정답) / 10점(완전 정답)
- 참조 해설(reference solution)을 함께 제공하여 채점 근거로 활용
## 🧪 실험 및 평가
### 평가 태스크
- **PhoPile-Test**: 텍스트 전용 문제 390개
- **PhoPile(V)-Test**: 이미지 포함 문제 서브셋 (멀티모달 모델 평가용)
### 주요 결과
- RAG 통합 시 일부 모델에서 성능 향상 확인 (Gemini-Pro: RAG로 17.95%까지 향상)
- Text retriever 중 Contriever가 전반적으로 안정적 성능
- Multimodal retriever는 텍스트 위주 문제에서 오히려 노이즈 유발 가능
- Shot 수 증가(1→2→3-shot)가 항상 성능 향상을 보장하지 않음
- Reflection 메커니즘이 일부 모델에서 노이즈 완화에 효과적
## 💡 핵심 기여
1. Physics Olympiad 7개 대회 기반 **최초의 멀티모달 RAG 물리 벤치마크 PhoPile** 구축
2. LLM 4종 + LMM 4종, text retriever 4종 + multimodal retriever 3종 **종합 비교 실험**
3. 단계별(step-wise) + 최종 답안(solution-level) 이중 채점 **GPT-4 judge 프레임워크** 설계
4. 물리 추론에서 RAG의 효용과 한계에 대한 최초의 체계적 분석 제공
## ⚠️ 한계점
- 검색된 문제가 노이즈로 작용하여 성능을 오히려 낮추는 경우 존재
- 도메인 특화 파인튜닝 없이 범용 retriever만 사용 → 물리 특화 임베딩 부재
- GPT-4 judge 의존적 평가 → judge의 물리 전문성에 의존
- 영어 문제 중심 (일부 다국어 대회 문제 포함되나 주로 영어 번역본)
## 🔗 관련 연구 및 관련 정보
- **논문 링크**: [https://aclanthology.org/2025.findings-emnlp.1196/](https://aclanthology.org/2025.findings-emnlp.1196/)
- **arXiv**: [https://arxiv.org/abs/2510.00919](https://arxiv.org/abs/2510.00919)
- **관련 벤치마크**: SciQ (Welbl et al., 2017), ScienceQA (Lu et al., 2022), TheoremQA (Chen et al., 2023)
- **이 벤치마크(PhoPile)를 사용한 논문**: 본 논문 자체
