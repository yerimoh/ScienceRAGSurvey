---
title: "Improving medical reasoning through retrieval and self-reflection with retrieval-augmented large language models"
bib_key: "DBLP:journals/bioinformatics/JeongSSK24"
year: 2024
domain: medical, bio
type: Method
venue: Bioinformatics (ISMB)
paper_link: https://doi.org/10.1093/bioinformatics/btae238
---
# Self-BioRAG: Retrieval + Self-Reflection for Medical Reasoning
> Bioinformatics (ISMB) 2024 | Method | medical · bio

## 한 줄 요약
Self-BioRAG는 "언제 검색할지"를 모델 스스로 판단하고(adaptive retrieval), MedCPT로 생의학 코퍼스에서 근거를 검색한 뒤, reflection token(RET/REL/SUP/USE)으로 근거의 관련성·지지 여부·유용성을 self-critique하여 최적 근거를 골라 답하는, Self-RAG를 생의학 도메인에 특화시킨 7B(및 13B) 의료 추론 프레임워크다.

## 시스템 구조 (Self-BioRAG Architecture)
Self-BioRAG는 세 가지 핵심 요소로 구성된다.

**(1) When-to-retrieve 판단 (Adaptive Retrieval).** 생성기 모델이 retrieval token(RET)을 직접 생성하여 검색 필요 여부를 결정한다. 정규화 확률 `p(retrieve=Yes) / (p(retrieve=Yes) + p(retrieve=No))` 가 임계값 δ=0.2를 넘으면 검색한다. 이를 통해 파라미터 지식만으로 답할 수 있는 질문에서는 검색을 건너뛰고, 필요한 경우에만 검색을 수행한다.

**(2) MedCPT Retriever + 생의학 코퍼스.** 검색기는 MedCPT로, PubMed 검색 로그의 255M query–article 쌍으로 대조학습(contrastive)된 생의학 전용 검색기다. 인덱싱 대상은 네 종류 생의학 코퍼스다(문서는 128단어 청크, 32단어 overlap으로 분할).

| Corpus | 문서 수 | 청크 수 |
|---|---|---|
| PubMed | 36,533,377 | 69,743,442 |
| PMC Full-text | 1,060,173 | 46,294,271 |
| Clinical Practice Guidelines | 35,733 | 606,785 |
| Medical Textbooks | 18 | 133,875 |

각 소스에서 top-k(k=10)씩 검색해 총 4k개 근거를 모은 뒤, reranking 모듈로 질의에 가장 관련 있는 최종 top-k 근거를 선별한다.

**(3) Reflection / Critique 토큰 (4종).** 모델이 생성하는 특수 토큰으로, 검색·근거평가·자기평가를 제어한다.

| Token | 입력 | 출력값 | 의미 |
|---|---|---|---|
| **RET** (Retrieve) | instruction (+output) | yes / no / continue | 검색이 필요한가 |
| **REL** (IsRel) | instruction, evidence | relevant / irrelevant | 근거가 유용한 정보를 담았는가 |
| **SUP** (IsSup) | instruction, evidence, output | fully / partially / no support | 답변 진술이 근거로 지지되는가 |
| **USE** (IsUse) | instruction, output | 5 / 4 / 3 / 2 / 1 | 출력이 질문에 얼마나 유용한가 |

**(4) 생성기(Generator).** LLaMA2 백본 기반의 Self-RAG 가중치를 초기값으로 fine-tuning한 7B 모델(및 13B 버전). 직접 LLaMA2를 학습시키는 것보다 Self-RAG 가중치에서 출발할 때 성능이 더 좋았다고 보고한다.

## 동작 파이프라인 (inference)
1. **입력:** instruction을 받는다.
2. **검색 필요 판단:** 모델이 RET 토큰을 생성, δ=0.2 기준으로 검색 여부 결정.
3. **조건부 검색:** 필요 시 MedCPT가 네 코퍼스 각각에서 top-10(총 4k개) 근거를 검색하고 reranking으로 최종 top-k 선별.
4. **문단별 critique / self-reflection:** 각 근거 후보에 대해 REL(관련성), SUP(지지도), USE(유용성) 토큰을 평가.
5. **근거 선택:** REL·SUP·USE의 정규화 확률을 가중합한 critique 점수가 가장 높은 근거를 선택(가중치는 추론 시 조정 가능).
6. **답변 생성:** 선택된 근거와 파라미터 지식을 결합하여 답을 생성.

## 학습 (Training)
**(1) Critic 모델 학습 (reflection 데이터 생성).** 약 120k 생의학 instruction 중 5,000개 샘플에 대해 GPT-4 API로 reflective token을 어노테이션하여 학습 데이터를 만든다(epoch 3, lr 2e-5). 이후 이 critic으로 전체 instruction에 reflection token을 자동 부착한다.

**(2) Generator 모델 학습 (instruction tuning).** Critic이 라벨링한 instruction을 필터링한 84,728개로 생성기를 학습한다. 답변과 reflection token을 함께 생성하도록 학습(epoch 5, lr 2e-5, A100 80GB×8, DeepSpeed stage 3, FlashAttention).

**(3) Instruction 데이터.** Mol-Instructions, MedInstruct, 자체 생성 생의학 instruction을 결합. 원본 122,349개를 필터링하여 최종 84,728개 사용.

## 주요 결과
**객관식(Multiple-Choice) QA — Accuracy(%)**

| Model | Params | MedQA | MedMCQA | MMLU-Med | Avg |
|---|---|---|---|---|---|
| LLaMA2 | 7B | 35.2 | 36.3 | 46.3 | 39.3 |
| RAG | 7B | 36.2 | 38.3 | 47.7 | 40.7 |
| Self-RAG | 7B | 31.2 | 36.5 | 45.7 | 37.8 |
| **Self-BioRAG** | **7B** | **43.6** | **42.1** | **53.9** | **46.5** |
| Self-BioRAG | 13B | 48.6 | 44.0 | 57.2 | 49.9 |

7B 오픈 모델 대비 평균 약 7.2%p 절대 향상.

**장문(Long-Form) QA — ROUGE (R1/R2/RL)**

| Model | LiveQA | MedicationQA |
|---|---|---|
| LLaMA2 | 8.8 / 1.9 / 6.2 | 5.7 / 1.2 / 4.4 |
| RAG | 11.5 / 2.3 / 11.1 | 9.8 / 1.3 / 4.8 |
| **Self-BioRAG** | **19.7 / 3.1 / 13.4** | **17.6 / 3.3 / 13.5** |

**Ablation (평균 정확도 영향).** reflection token 제거 −1.3%p, 생의학 코퍼스 제거 −2.9%p, MedCPT 검색기 제거 −4.4%p, 생의학 instruction 제거 −7.3%p(가장 큰 영향).

**Adaptive vs. 고정 전략(객관식 평균).** No-retrieval 44.8 / Always-retrieve 46.2 / **Adaptive 46.5**.

## 한계점
- 검색 코퍼스가 영어 PubMed/PMC/가이드라인/교과서에 한정되어 도메인·언어 일반화가 제한적이다.
- Critic 학습·평가가 GPT-4 어노테이션을 정답으로 삼아, GPT-4의 편향·오류가 reflection 품질에 전파될 수 있다.
- 객관식에서 7B는 GPT-4 등 대형 폐쇄형 모델에는 여전히 못 미치며, 검색 이득이 질문 유형에 따라 균일하지 않다.
- ROUGE 기반 장문 평가는 사실성·임상적 정확성을 직접 측정하지 못한다.

## 관련 정보
- arXiv: 2401.15269 (https://arxiv.org/abs/2401.15269)
- DOI: https://doi.org/10.1093/bioinformatics/btae238
- GitHub: https://github.com/dmis-lab/self-biorag
