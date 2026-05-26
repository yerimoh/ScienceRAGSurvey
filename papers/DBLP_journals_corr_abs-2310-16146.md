---
notion_id: 355f2dcd-4912-81ab-8019-d5f032ffdba0
title: CLINFO.AI - An Open-Source Retrieval-Augmented Large Language Model System for Answering Medical Questions Using Scientific Literature
bib_key: DBLP:journals/corr/abs-2310-16146
year: 2024
domain: medical
type: benchmark
venue: PSB
paper_link: https://arxiv.org/abs/2310.16146
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# CLINFO.AI: An Open-Source Retrieval-Augmented Large Language Model System for Answering Medical Questions Using Scientific Literature

> arXiv | 2023 | Benchmark | medical

## 한 줄 요약
PubMed 체계적 문헌 고찰(Systematic Review, SR)에서 추출한 질문과 해당 SR의 결론을 정답(Gold Standard)으로 매핑하여 만들어진 200문항 규모의 의료분야 검색+요약 평가 벤치마크.

## 제작 배경
**기존 벤치마크의 한계**
- 기존 QA 데이터셋은 의학적 필요성을 반영하지 못하거나, RAG 모델의 '정보 검색 역량(IR)'과 '요약 역량(Summarization)'을 결합하여 평가하기 어려웠음.

**필요성**
- 시스템이 수많은 논문 속에서 정말로 '적절한(관련성 높은)' 논문을 잘 찾아왔는지, 그리고 그걸 사람(의학 전문가)처럼 잘 통합했는지 검증할 Gold Standard이 필요.

## 어떻게 만들었나 (Construction Methodology)
**Step 1: 데이터 출처 선정**
- 임상의들이 정책 결정 및 근거 중심 의학을 위해 사용하는 '체계적 문헌 고찰(SR)'을 기준으로 삼음
- 인간 전문가가 이미 문헌을 싹 필터링하고 결론을 도출해 둔 자료이기 때문

**Step 2: 구축 파이프라인**
1. Entrez API로 PubMed에 접근하여 다양한 의학 하위 분야의 Systematic Review 검색
2. 제목(Title)에 명시적인 '질문(물음표)' 형태가 포함된 논문만 필터링

**Step 3: 품질 검증**
- 2명의 인간 평가자(저자)가 질문을 수동으로 검토하고, 질문과 직결되는 내용만 남도록 초록의 Results와 Conclusions 섹션 텍스트를 정제하여 '정답(Answer)'으로 구축

**Step 4: 데이터셋 구성**
- 최종적으로 200개의 (Question, Answer, Context, References, Date) 형태를 지닌 쌍 생성 완료

## Input (입력)
- **출처**: PubMed 내 Systematic Review 문헌
- **문항 형식**: Open QA Format (제목에 등장하는 질문)

**제공 필드 테이블**
| 필드명 | 설명 |
|---|---|
| Question | SR 논문의 제목(질문 형태) |
| Answer | Results/Conclusion 단락 정제 텍스트 |
| Context | 논문의 Introduction 기반 정보 |
| References | SR에서 참조한 논문들의 PubMed IDs |
| Topic / Subtopic | 의료 전문과목 및 세부분야 |
| Published Date | 논문 출판일 |

## Output (평가 지표)
- **출력 형태**: 질문에 대한 직접적인 서술형 답변 (Abstractive Summary)
- **정답(Answer) 출처**: 해당 SR의 'Results' 및 'Conclusion' 단락 텍스트
- **평가 지표**:
	- IR: Precision, Recall
	- Summarization: Source-Augmented 평가 (UniEval, COMET, CTC) 및 Source-Free 평가 (BERTScore, ROUGE-L, METEOR 등)

## 예시 문항
- **Q (Input)**: Does high-grade dysplasia/carcinoma in situ of the biliary duct margin affect the prognosis of extrahepatic cholangiocarcinoma? (담도 절제 연의 고등급 이형성증/상피내암이 간외 담관암의 예후에 영향을 미치는가?)
- **A (Answer 유사)**: 문헌의 증거는 혼재되어 있으나, 일부 부정적인 예후 또는 국소 재발의 높은 빈도와 연관될 수 있음. 마진에 침윤성 암종이 있는 것이 더 강력한 나쁜 예후 인자임.

## 주요 평가 결과 (Unrestricted 기준)
| 시스템/모델 | UniEval Overall |
|---|---|
| GPT-4 (Baseline) | 0.860 |
| Elicit | 0.713 |
| Statpearls SS | 0.728 |
| **Clinfo.ai Synthesis & TL;DR** | **0.840** |

## 한계점
- 의학이 계속 발전하므로, 해당 질문에 대한 "정답(Systematic Review의 결론)"이 최신 연구로 인해 바뀌었을 수 있다는 점 (이 때문에 Date 기준으로 Restricted, Source Dropped 등의 복잡한 평가 룰을 추가해야 했음).
- 자동화된 LLM 평가 지표에 의존하여 구축됨.

## 관련 정보
- **논문**: [https://arxiv.org/abs/2310.16146](https://arxiv.org/abs/2310.16146)
- **DBLP**: [https://dblp.org/rec/journals/corr/abs-2310-16146.html](https://dblp.org/rec/journals/corr/abs-2310-16146.html)
- **이 벤치마크를 사용한 논문**: Clinfo.ai (PSB 2024)

---

## ⚠️ 팩트체크 노트 (survey §O1 Long-form citation Grounding)

**Basis**: arXiv:2310.16146 본문 직접 인용 (PDF 본문 grep, abstract 아님)

main.tex `\subsubsection{Long-form citation Grounding}` 단락이 Clinfo.AI를 "citation precision/recall/F1, faithfulness per claim" 평가 사례로 묶은 것은 부정확하다. **Clinfo.AI는 IEEE 형식 인용을 포함한 합성문을 생성하지만, 평가는 요약 품질 metric 기반**이며 인용 단위 grounding metric을 보고하지 않는다.

| Claim (survey) | Evidence (paper body, verbatim) | Status |
|---|---|---|
| "paragraph with citations per claim" (생성 측면) | "structured list of article summaries ... constructing a [synthesis] ... relying on the structured list of citations to reference and accurately attribute each finding" + "construct their citations in the IEEE format" | ✅ |
| "citation precision, recall, F1" | Table 1 SA metrics: **UniEval, COMET, CTC**; Table 2 SF: **BERTScore, ROUGE-L** | ❌ (citation-level이 아닌 summary-quality) |
| "per-sentence grounding 평가" | "Step (2) is evaluated based on **precision and recall**. Considering the set of all documents D, RET(D, k) denotes the [retrieved set]..." → **문서 검색 P/R**이지 문장 단위 인용 P/R 아님 | ❌ |
| "faithfulness per claim" | 명명된 metric 아님 (paper 어디에도 없음) | ❌ |

**Verdict**: ⚠️ **PARTIAL** — 임상 영역 paragraph synthesis 시스템으로 인용하는 것은 정확하지만, 평가 방법론을 citation-level metric으로 묘사한 것은 사실 오류. Survey에서 Clinfo.AI를 언급할 때 평가가 UniEval/BERTScore/ROUGE 기반임을 명시하거나, citation-level metric 예시에서는 제외할 것.

**Survey 수정안**: factcheck_o1_longform.md의 proposed corrected paragraph 참조.
