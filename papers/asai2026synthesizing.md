---
notion_id: 355f2dcd-4912-81a8-a5b4-fd495696ea23
title: Synthesizing Scientific Literature with Retrieval-Augmented Language Models
bib_key: asai2026synthesizing
year: 2026
domain: bio, medical, physics
type: benchmark
venue: Nature
paper_link: https://doi.org/10.1038/s41586-025-10072-4
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Synthesizing Scientific Literature with Retrieval-Augmented Language Models

> Nature | 2026 | Benchmark | bio · medical · physics

## 한 줄 요약
컴퓨터과학·생의학·신경과학·물리학 4개 분야에 걸쳐 최초로 제안된 다학제 장문 문헌 합성 벤치마크. 2,967개 전문가 작성 질문과 다면적 자동+인간 평가 프로토콜 포함.

## 제작 배경
**기존 벤치마크의 한계**
- SciFact, QASA 등은 단일 분야 또는 단일 논문 기반 → 실제 문헌 리뷰 맥락과 괴리
- 기존 평가가 객관식/단답형에 그쳐 장문 합성 능력 미평가
- 장문 답변 평가의 어려움: 단일 레퍼런스 답변으로 모든 올바른 답 커버 불가
- 외부 검색 없이 제공된 논문만 사용하는 closed-set 방식 → 현실 반영 부족

**왜 이 벤치마크가 필요했는지**
- 연구자가 실제로 하는 문헌 리뷰는 수십 편의 최신 논문을 검색·종합하는 과정
- LLM의 인용 환각(78–90%) 문제를 정확히 측정할 도구 필요
- 인용 정확도(citation F1)를 핵심 지표로 포함한 벤치마크 부재

## 어떻게 만들었나 (Construction Methodology)
**전체 구성**: 기존 단일 논문 데이터셋 3개 + 신규 멀티 논문 데이터셋 4개

### 신규 멀티 논문 데이터셋 구축
**Step 1: 어노테이터 모집**
- Scholar-CS: CS 분야 PhD (교수·박사후연구원·연구과학자)
- Scholar-Bio/Neuro: 생의학/신경과학 PhD 6명 (현직 연구과학자·엔지니어)
- Scholar-Multi: CS(AI/ML/HCI), 생의학(bioimaging/genetics), 물리학(astrophysics/photonics/biophysics) PhD·박사후 연구원 (3년+ 경험, 1저자 논문 다수)
- IRB 면제 연구, 2024년 4월~10월 수집

**Step 2: Scholar-CS 구축 (Rubric 기반)**
```
CS 전문가 100개 질문 작성
       │  (여러 논문이 필요한 문헌 리뷰 질문)
       ▼
별도 어노테이터 2명이 웹 검색으로 Rubric 작성
       │  - "Must have" 항목 + "Nice to have" 항목
       │  - 각 항목마다 지지 인용문 4.4개
       │  - LLM 서비스 미사용 (초기 웹검색 단계)
       │  - Claude 3.5 Sonnet 등 4개 LLM 응답을 참조하여 Rubric 수정 가능
       ▼
Rubric 합의율: Pearson 상관계수 79.3 (general 포함) / 59.5 (전용 항목)
       │
       └─ 31개 전문가 장문 답변 (별도 어노테이터 풀)
```

**Step 3: Scholar-Bio/Neuro 구축**
- bioimaging, genetics, microbiology, neuromodulation 등 세부 분야 질문 수집
- 비용 문제로 질문만 수집 (답변 없음), Citation F1만 평가

**Step 4: Scholar-Multi 구축**
- 108개 질문 + 전문가 장문 답변 + 인용 포함
- 어노테이터당 평균 56분 소요 (답변 작성)
- LLM 미사용 지침, Google Scholar/Semantic Scholar만 허용
- 2024년 10월 이전 발표 논문 기준

**Step 5: 평가 파이프라인 개발**
- Rubric 평가: GPT-4o Turbo가 각 항목 충족 여부 채점 (annotation-driven 60% + general 40%)
- Citation F1: 인용 문장 단위 precision + recall → F1
- LLM judge (Prometheus v2): coverage, relevance, organization 5점 척도
- 인간-LLM judge 일치율: 3점 척도 기준 80%+ 일치

## Input (입력)
**데이터셋 개요**
| 데이터셋 | 형식 | 분야 | 크기 | 평가 |
|---|---|---|---|---|
| SciFact (기존) | Claim→Label | 생의학 | 208 | Accuracy, Citation |
| PubMedQA (기존) | Q→Yes/No | 생의학 | 843 | Accuracy, Citation |
| QASA (기존) | Q→Long-form | CS | 1,375 | ROUGE-L, Citation |
| **Scholar-CS** (신규) | Q→Long-form† | CS | 100 | Rubric, Citation |
| **Scholar-Bio** (신규) | Q→Long-form* | 생의학 | 1,451 | Citation |
| **Scholar-Neuro** (신규) | Q→Long-form* | 신경과학 | 1,308 | Citation |
| **Scholar-Multi** (신규) | Q→Long-form | CS+물리+생의학 | 108 | Citation, LLM, Expert |

*질문만 존재 †Rubric 기반 정답 주석

**전문가 답변 특성 (Scholar-CS, 31개; Scholar-Multi, 108개)**
| | Scholar-CS | Scholar-Multi |
|---|---|---|
| 평균 답변 길이 | 424.3 tokens | – |
| 평균 인용 논문 수 | 7.1편 | – |
| Rubric 정확도 (human) | 54.0 | – |
| Citation Precision | 43.2% | 44.4% |
| Citation Recall | 40.1% | 41.5% |

## Output (출력 / 정답 형식)
**평가 지표 체계**
| 지표 | 방식 | 적용 |
|---|---|---|
| Rubric accuracy | GPT-4o Turbo 채점 (must/nice to have) | Scholar-CS |
| Citation F1 | 문장별 인용 precision × recall | 전 데이터셋 |
| LLM judge | Prometheus v2, coverage/relevance/organization 5점 | Scholar-Multi |
| Human pairwise | 전문가 16명, win/tie/lose | Scholar-Multi (108Q) |
| Human usefulness | 전문가 1–5점 → useful/neutral/not useful | Scholar-Multi |

## 예시 문항 (논문 Figure 3 / Figure 15 / Table 23 / Appendix E 직접 인용)

### 📘 단일 논문 — SciFact (Claim Verification, 생의학)
> **Claim**: "1,000 genomes project enables mapping of genetic sequence variation consisting of rare variants with larger penetrance effects than common variants."
>
> **Reference [1]**: *Rare Variants Create Synthetic Genome-Wide Associations*: "GWAS have identified at least 2,000 common variants ... rare causal mutations responsible for both hearing loss and sickle cell anemia create genome-wide significant synthetic associations..."
>
> **Expert verdict**: `true [1]` (claim supported)
> **평가 방식**: Accuracy + Citation F1

### 📘 단일 논문 — PubMedQA (Yes/No, 의학)
> **Q**: "Systematic use of patient-rated depression severity monitoring: is it helpful and feasible in clinical psychiatry?"
>
> **Reference [1]**: *Same-titled paper*: "STAR\*D emphasized the importance of measurement-based care for the treatment of depression ... PHQ-9 for monitoring depression severity was introduced in 19 diverse psychiatric practices..."
>
> **Expert answer**: `Yes [1]`
> **평가 방식**: Accuracy + Citation F1

### 📘 단일 논문 — QASA (Long-form 단답, AI/ML)
> **Q (about ShuffleNet 논문)**: "What are the side effects of group convolution?"
>
> **Reference [1] (ShuffleNet paper)**: "...larger group numbers result in more output channels for a given complexity constraint, which helps to encode more information, though it might also lead to degradation for an individual convolutional filter due to limited corresponding input channels..."
>
> **Expert answer**: "The side effects of group convolutions are: blocked flow of information between channel groups when multiple group convolutions are combined; and damaged individual convolution filters for each group due to decreased number of input channels [1]."
> **평가 방식**: ROUGE-L + Citation F1

---

### 📚 멀티 논문 — Scholar-CS Rubric 예시 ① (소프트웨어 보안)
> **Q**: "What are the best practices to protect software against vulnerabilities from third-party libraries?"
>
> **Must Have rubric**
> - Item-1: 신뢰할 수 있는 출처 (reliable source), 업데이트 모니터링, 코드 리뷰 등 예방 모범 사례 논의
>
> **Nice to Have rubric**
> - Item-1: 다양한 프로그래밍 언어에서 사용되는 유명 third-party library 사례 제시
>
> **Expert answer 발췌**
> > "Protecting software against vulnerabilities stemming from third-party libraries is a crucial aspect of software security [1] [2]. Below are best practices ... (1) Develop intelligent security tools to automatically detect and repair vulnerabilities ... (2) Applying formal verification methods to examine security properties as part of library test suites or continuous integration..."
>
> **평가 방식**: Rubric accuracy (GPT-4o-turbo 채점, must=가중치 큼) + Citation F1 + Coverage/Relevance/Organization (Prometheus v2 5점)

### 📚 멀티 논문 — Scholar-CS Rubric 예시 ② (Python 타입 추론)
> **Q**: "What publicly available datasets are typically used for evaluating type inference systems in Python?"
>
> **Most Important rubric**
> - 일반적인 type inference 시스템의 목표 정의 (도입부)
> - Python에서 자동 type inference의 중요성 강조
> - 평가 통합 접근의 필요성 + 평가 지표 (exact matches, missing types, accuracy 등)
> - **공개 데이터셋 열거 + 각 데이터셋 간단 설명**
>
> **Nice to Have rubric**
> - rule-based vs ML-based type inference 방법론 카테고리 설명
>
> **Supporting quotes 예시 (어노테이터 제공)**
> - "ManyTypes4Py: 5,382 Python projects with over 869,000 type annotations ... lightweight static analyzer pipeline to extract type information from ASTs"
> - "TypeEvalPy: 154 code snippets with 845 type annotations across 18 categories targeting various Python..."

---

### 🧬 멀티 논문 — Scholar-Bio 예시 (Inspiring Paper 기반)
> **Q**: "How does CRISPR/Cas9 compare to other gene-editing technologies in terms of efficiency and precision?"
>
> **Inspiring Paper**: Sajeesh et al. 2006. *CRISPR/Cas9 gene-editing: Research technologies, clinical applications and ethical considerations*
>
> **Inspiring abstract**: "Gene therapy carries the potential to treat more than 10,000 human monogenic diseases ... The repurposing of CRISPR/Cas9, an ancient bacterial immune defense system, into a gene-editing technology has armed researchers with a revolutionary tool..."
>
> Scholar-Bio는 비용 문제로 **질문만 수집**, expert answer 없이 **Citation F1만 평가**.

---

### ⚛️ 멀티 논문 — Scholar-Multi 예시 (Physics: levitated optomechanics)
> **Q**: "What are ways to cool the centre-of-mass (CoM) motion of levitated nanoparticles?"
>
> **Expert-written answer 발췌 (인용 포함)**
> > "For levitated nanoparticles, cooling their motional degrees of freedom—especially to the quantum ground state—is of great importance ... Currently, the most commonly used cooling method is **feedback cooling** [Tongcang Li et al. 2011]. By measuring the real-time position of the levitated nanoparticle, its instantaneous velocity can be determined, allowing for the application of a feedback cooling scattering force in the opposite direction of the velocity ... cooled from room temperature to 1.5 mK [Tongcang Li 2011], or even to the ground state in cryogenic environments [Novotný 2021]. An alternative method involves levitating the nanosphere in an **optical cavity and cooling via coherent scattering** [Deli´c 2018]. The trapping laser is red-detuned from the optical resonance at the CoM motional frequency ... cool the CoM motion to temperatures as low as 1 K [Deli´c 2018] and to the ground-state [Anonymous 2020]. A more recent proposal, known as **cold damping**, ... adjusts the spatial position of the optical traps using an acousto-optic deflector (AOD) [Vijayan 2022]..."
>
> **Fine-grained scores**: Org 5.0 | Rel 5.0 | Cov 4.0
>
> **OpenScholar-GPT4o answer 발췌 (비교용)**
> > "Cooling the centre-of-mass (CoM) motion of levitated nanoparticles is crucial for advancing experiments in levitated optomechanics ... One prominent approach is **cavity-assisted optomechanical cooling**, where the CoM motion is cooled via coherent scattering of light into an optical cavity ... [Windey 2018] ... achieve minimal temperatures in the millikelvin regime for pressures around 10⁻⁵..."
>
> **평가 방식**: Citation F1 + Coverage/Relevance/Organization (Prometheus v2 + 16 human experts) + Pairwise win/tie/lose

## 주요 평가 결과
**Scholar-CS (Rubric accuracy + Citation F1)**
| 모델 | Rubric Acc. | Citation F1 |
|---|---|---|
| GPT-4o (no retrieval) | 45.0 | 0.1 |
| PaperQA2 | 45.6 | 48.0 |
| Perplexity Pro | 40.0 | – |
| OpenScholar-8B | **51.1** | 47.9 |
| OpenScholar-GPT-4o | **57.7** | 39.5 |
| Human expert | 54.0 | 43.2/40.1 (P/R) |

**전문가 인간 평가 (Scholar-Multi, Win rate vs human experts)**
| 모델 | Win | Tie | Lose | Usefulness |
|---|---|---|---|---|
| GPT-4o | 31.9% | 13.8% | 54.2% | 69.7% |
| OpenScholar-8B | 50.8% | 12.3% | 36.9% | 72.1% |
| OpenScholar-GPT-4o | **70.0%** | 6.8% | 23.2% | **80.0%** |

## 한계점
- 전문가 어노테이션 비용으로 evaluation set이 소규모 (Scholar-CS 110, Scholar-Multi 108)
- Rubric 평가가 길이·스타일에 민감 → LLM이 부가 설명 추가로 점수 과부풀 가능
- Citation precision/recall이 문장 수준으로 인접 문장 지지를 미인정하는 경우 있음
- CS·생의학·물리학 편중 → 사회과학 등 타 분야 일반화 제한
- Static benchmark → 공개 후 train set 오염 위험

## 관련 정보
- **논문**: [https://doi.org/10.1038/s41586-025-10072-4](https://doi.org/10.1038/s41586-025-10072-4)
- **arXiv 프리프린트**: [https://arxiv.org/abs/2411.14199](https://arxiv.org/abs/2411.14199)
- **데이터**: [https://github.com/AkariAsai/ScholarQABench/tree/main/data](https://github.com/AkariAsai/ScholarQABench/tree/main/data)
- **평가 코드**: [https://github.com/AkariAsai/ScholarQABench](https://github.com/AkariAsai/ScholarQABench)
- **이 벤치마크를 사용한 RAG 논문**: OpenScholar (Nature 2026)
