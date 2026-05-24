---
notion_id: 355f2dcd-4912-8112-afb6-d52236844811
title: Crowdsourcing Multiple Choice Science Questions
bib_key: DBLP:conf/aclnut/WelblLG17
year: 2017
domain: physics, chem, bio
type: benchmark
venue: Workshop on Noisy User-generated Text (WNUT)
paper_link: https://aclanthology.org/W17-4413/
originSessionId: e17a6512-257b-4eac-96cc-808523cf24a8
---
# Crowdsourcing Multiple Choice Science Questions

> WNUT @ EMNLP | 2017 | Benchmark | Domain: physics, chem, bio
---
## 📌 한 줄 요약
물리·화학·생물 분야의 **13,679개 4지 선다형 과학 문제**를 크라우드소싱으로 구축한 데이터셋. 대다수 문항에 정답 근거 단락(supporting evidence)이 함께 제공된다.
---
## 🎯 제작 배경
기존 과학 QA 데이터셋은 규모가 작거나 단일 도메인에 편향되는 문제가 있었다. Welbl et al. (2017)은 크라우드워커를 활용한 **대규모 도메인 특화 MCQ 생성 방법론**을 제안하고, 이를 통해 SciQ를 구축했다. 핵심 아이디어는 도메인 특화 코퍼스에서 문서를 자동 추천하고, 오답 선택지를 AI가 제안해 사람이 최종 검수하는 방식이다.
---
## 🔨 어떻게 만들었나 (Construction Methodology)
### Step 1 — 도메인 코퍼스 구축
- 물리, 화학, 생물 분야의 **교과서·학습 자료 텍스트 코퍼스**를 수집
- 각 문서에서 문제를 만들 수 있는 **핵심 문장(seed sentence)** 을 자동으로 추출
- 문서 선택 기준: 정보 밀도, 도메인 적합성
### Step 2 — 크라우드워커 문제 생성 파이프라인
```javascript
[도메인 코퍼스]
      ↓
[문서 자동 추천 (AI)] → 워커에게 관련 단락 제시
      ↓
[크라우드워커] → 질문 + 정답 작성
      ↓
[오답 선택지 자동 생성 (AI)] → 의미적으로 유사하지만 틀린 distractor 추천
      ↓
[크라우드워커] → distractor 검수 및 수정
      ↓
[최종 문항 완성]
```
**오답(distractor) 생성 방법:**
- 코퍼스에서 정답과 **의미적으로 유사한 단어/개념**을 자동으로 추출
- 단순 무작위 선택이 아닌, **혼동 가능한 오답**을 만들어 난이도 유지
### Step 3 — 품질 검증
- **Human validation:** 크라우드워커가 만든 문항을 다른 워커가 검수
- **Distinguishability test:** 사람이 크라우드소싱 문항과 원본 시험 문항을 구별할 수 없음을 실험으로 검증 → 품질이 실제 시험 수준임을 입증
- **Supporting evidence 제공:** 대부분 문항에 정답 근거 단락을 함께 제공하여 RAG 연구에 활용 가능하도록 설계
### Step 4 — 데이터셋 구성 및 공개
| 분할 | 수 |
| Train | 11,679 |
| Validation | 1,000 |
| Test | 1,000 |
| **합계** | **13,679** |

- AllenAI를 통해 오픈소스로 공개
- HuggingFace Datasets에서 `allenai/sciq`로 바로 사용 가능
---
## 📥 Input (입력)
| 항목 | 내용 |
| **출처** | 크라우드소싱 (Amazon Mechanical Turk) + 도메인 코퍼스 자동 추천 |
| **문항 형식** | 자연어 질문 + 4개 선택지 + (선택적) supporting evidence 단락 |
| **도메인** | 물리(Physics), 화학(Chemistry), 생물(Biology) |
| **총 문항 수** | 13,679개 |
| **분할** | Train 11,679 / Validation 1,000 / Test 1,000 |

### 제공 필드
| 필드 | 설명 |
| `question` | 과학 문제 텍스트 |
| `correct_answer` | 정답 선택지 텍스트 |
| `distractor1~3` | 오답 선택지 3개 |
| `support` | 정답 근거 단락 (대부분 문항에 포함) |

---
## 📤 Output (출력 / 정답 형식)
| 항목 | 내용 |
| **출력 형태** | 4개 선택지 중 정답 텍스트 선택 |
| **평가 지표** | Accuracy (정답률) |
| **특이사항** | `support` 단락을 컨텍스트로 제공하는 설정 vs. 제공하지 않는 설정 모두 가능 |

---
## 💡 예시 문항
### 예시 1 — 생물 (Biology)
> **Q.** What is the powerhouse of the cell?
> (A) Nucleus  (B) Ribosome  (C) Mitochondria  (D) Golgi apparatus
>
> **A.** (C) Mitochondria
>
> **Support:** *"The mitochondria are often referred to as the powerhouses of the cell because they generate most of the cell's supply of ATP, used as a source of chemical energy."*

### 예시 2 — 화학 (Chemistry)
> **Q.** What type of bond holds the two strands of DNA together?
> (A) Ionic bond  (B) Covalent bond  (C) Hydrogen bond  (D) Metallic bond
>
> **A.** (C) Hydrogen bond

### 예시 3 — 물리 (Physics)
> **Q.** Which law states that the pressure of a gas is inversely proportional to its volume at constant temperature?
> (A) Charles's Law  (B) Boyle's Law  (C) Avogadro's Law  (D) Gay-Lussac's Law
>
> **A.** (B) Boyle's Law
---
## 📊 주요 평가 결과 (HoneyComb 논문 기준)
| 모델 | Accuracy |
| HoneyBee (7B, 재료과학 특화) | 33.96% |
| GPT-3.5 | 90.69% |
| GPT-4 (baseline) | 90.84% |
| HoneyComb (GPT-4 기반) | **96.54%** |

> SciQ는 MaScQA 대비 난이도가 낮아 GPT-4 baseline도 ~91% 달성
---
## ⚠️ 한계점
- 크라우드소싱 특성상 문항 품질이 불균일할 수 있음
- 고등학교~학부 초반 수준의 난이도 (전문 연구 수준 아님)
- 재료과학 문항은 거의 없어 재료 분야 평가에 한계
- 텍스트 기반만 (이미지, 수식 없음)
---
## 🔗 관련 정보
- **논문:** [ACL Anthology, WNUT@EMNLP 2017](https://aclanthology.org/W17-4413/)
- **Hugging Face Dataset:** [https://huggingface.co/datasets/allenai/sciq](https://huggingface.co/datasets/allenai/sciq)
- **이 벤치마크를 사용한 논문:** HoneyComb (EMNLP Findings 2024), HiPerRAG (PASC 2025)
