---
notion_id: 355f2dcd-4912-81a6-96a1-fb28e9797ce2
title: SQuAI - Scientific Question-Answering with Multi-Agent Retrieval-Augmented Generation
bib_key: DBLP:conf/cikm/BesrourHS025
year: 2025
domain: bio, chem, physics
type: benchmark
venue: CIKM
paper_link: https://doi.org/10.1145/3746252.3761471
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# unarXive (SQuAI Benchmark)

> CIKM | 2025 | Benchmark | physics, bio, chem

## 한 줄 요약
unarXive 2024의 방대한 arXiv 코퍼스를 바탕으로, LLaMA 3.3 70B를 활용해 합성 생성된 장문 형태(long-form)의 개방형 과학 QA 벤치마크. 총 1,000문항 (Simple 500개 + Expert 500개).

## 제작 배경
**기존 벤치마크의 한계**
- 기존 과학 QA 벤치마크(ScienceQA, PubMedQA 등)는 대부분 다중 선택형이거나 예/아니오, 짧은 단답형(factoid) 질문에 국한되어 있어 실제 연구 맥락과 괴리가 있음.
- 과학 도메인에서 자유 텍스트 형식의 설명적이고 긴 답변을 요구하는 개방형 질문(open-domain long-form scientific QA)을 평가할 수 있는 데이터셋 부족.

## 어떻게 만들었나 (Construction Methodology)
- **Step 1: 데이터 출처 선정**: 광범위한 과학 분야(컴퓨터 과학, 수학, 물리학 등)를 포괄하는 unarXive 2024 코퍼스(1991년~2024년 arXiv 전체 텍스트 230만 건)를 출처로 활용.
- **Step 2: Simple 서브셋 구축**: DeepEval 프레임워크 + LLaMA 3.3 70B Instruct를 사용하여 덜 복잡하고 일반적이며 비전문가에게 적합한 장문형 질문 500개를 합성 생성.
- **Step 3: Expert 서브셋 구축**: 동일한 모델과 프레임워크를 사용하여 출처 논문에서 도출해야 하는 상세한 증거와 기술적 지식을 요구하는 전문가용 질문 500개를 합성 생성.
- **Step 4: 데이터셋 구성 및 공개**: Q-A-E(Question-Answer-Evidence) 트리플렛 형태의 1,000문항을 구축하여 SQuAI 논문과 함께 공개.

## Input (입력)
| 서브셋 | 문항 수 | 특징 |
|---|---|---|
| unarXive Simple | 500개 | 덜 복잡하고 일반적. 비전문가를 위한 광범위한 질문. |
| unarXive Expert | 500개 | 구체적이고 기술적. 논문의 상세한 증거를 요구하는 질문. |

- 출처: unarXive 2024 내 개별 arXiv 논문
- 문항 형식: 개방형 장문 질문 (Long-form, open-domain)
- 도메인: 과학 전 분야 (컴퓨터 과학, 물리학, 수학 등)

## Output (출력 / 정답 형식)
| 항목 | 내용 |
|---|---|
| 출력 형태 | 인라인 인용([X]) 포함된 자유 텍스트 형태의 긴 답변 |
| 평가 지표 | Answer Relevancy, Contextual Relevancy, Faithfulness (각 0~1) |
| 특이사항 | 합성 참조 정답과의 직접 비교 지양 — 인용 증거와 생성 답변 간의 관계성을 직접 평가 |

**평가 지표 상세**
1. **Answer Relevancy**: 질문과 생성된 답변 간의 의미적 일치도.
2. **Contextual Relevancy**: 제공된 증거 구절이 답변에 얼마나 효과적으로 통합되었는지.
3. **Faithfulness**: 답변이 증거에 비추어 정확한지, 뒷받침되지 않는 주장이 없는지.

## 예시 문항
- **Q**: "What is quantum computing and how is it used in cryptography?"
- **A**: "Quantum computing uses qubits to perform computations based on quantum mechanics [1]. It has potential applications in cryptography, particularly for breaking classical encryption schemes [2]."
- 각 인용 번호([1], [2])에 대응하는 원본 논문의 citation context가 함께 매핑됨.

## 주요 평가 결과
| 접근법 | unarXive Simple | unarXive Expert |
|---|---|---|
| Standard RAG | 0.759 | 0.796 |
| SQuAI (Abstract) | 0.828 | 0.812 |
| SQuAI (Full Text) | **0.847** | **0.864** |

## 한계점
- 두 서브셋 모두 LLM(LLaMA 3.3 70B)으로 합성 생성되어 실제 인간 사용자의 복잡한 의도나 다양한 표현 방식을 완벽하게 반영하지 못할 가능성이 있음.

## 관련 정보
- 원 논문: [https://doi.org/10.1145/3746252.3761471](https://doi.org/10.1145/3746252.3761471)
- HuggingFace 데이터셋: [https://huggingface.co/datasets/ines-besrour/unarxive_2024](https://huggingface.co/datasets/ines-besrour/unarxive_2024)
- GitHub: [https://github.com/faerber-lab/SQuAI](https://github.com/faerber-lab/SQuAI)
- 이 벤치마크를 사용한 논문: SQuAI (CIKM 2025)
