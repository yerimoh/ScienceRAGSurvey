---
title: "HoneyComb: A Flexible LLM-Based Agent System for Materials Science"
bib_key: DBLP:conf/emnlp/ZhangSHML24
year: 2024
domain: material
type: Method
venue: Findings of EMNLP 2024
paper_link: https://doi.org/10.18653/v1/2024.findings-emnlp.192
---
# HoneyComb: A Flexible LLM-Based Agent System for Materials Science

> Findings of EMNLP 2024 (pp. 3369–3382) | Method | material
> Zhang, Su, Huang, Ma, Li — various affiliations
> DBLP: `conf/emnlp/ZhangSHML24`

## 한 줄 요약
재료과학 문헌에서 큐레이션한 구조적 지식 베이스(MatSciKB)와 Materials Project API 도구 모음(ToolHub)을 **Inductive Tool Construction** 방식으로 구축하고, 적응형 retriever가 태스크에 따라 지식 검색 vs. 도구 실행을 선택하는 재료과학 전용 LLM 에이전트 시스템.

---

## 어떻게 만들었나 (Construction Methodology)

```
Step 1 — MatSciKB 구축 (지식 소스)
  재료과학 논문·교재에서 신뢰할 수 있는 지식 추출
  구조화된 텍스트 형식으로 큐레이션
  (구체적 문서 수·청크 수는 논문 미기재)

Step 2 — ToolHub 구축 (계산 도구)
  Inductive Tool Construction (ITC) 방법:
  ┌─ Materials Project API 등 재료과학 도구 탐색
  ├─ LLM이 도구 설명·파라미터 자동 파싱
  ├─ 태스크별 하위 도구로 분해 (Decompose)
  └─ 중복/불필요 도구 정제 (Refine)
  결과: 재료과학 전용 API 툴 컬렉션

Step 3 — 적응형 Retriever 설계
  입력 쿼리 분석:
  ├─ 사실적 질문 (factual) → MatSciKB 의미론적 검색
  └─ 계산 요청 (computation) → ToolHub API 실행

Step 4 — 평가 벤치마크 설정
  ┌──────────────┬────────────────────────────────────┐
  │ 벤치마크      │ 설명                                │
  ├──────────────┼────────────────────────────────────┤
  │ MaScQA       │ GATE 재료과학 기출 650문항           │
  │ SciQ         │ 크라우드소싱 과학 MCQ 13,679문항     │
  │ MP 물성 태스크│ LLaMP 프로토콜(체적 탄성률·밴드갭 등)│
  └──────────────┴────────────────────────────────────┘
```

---

## 실제 태스크 예시

### 사실형 질문 (MatSciKB 경로)
> **Q.** What is the crystal structure of perovskite BaTiO₃?
>
> **HoneyComb 처리**: MatSciKB 검색 → "BaTiO₃: 페로브스카이트 구조, 입방정계(Pm3m), a=4.01Å" → 답변 생성

### 계산 요청 (ToolHub 경로)
> **Q.** What is the formation energy of Fe₂O₃ according to Materials Project?
>
> **HoneyComb 처리**: ToolHub → MP API 호출(mp-19770) → ΔH_f = −2.03 eV/atom → 답변 생성

---

## 주요 평가 결과

**MaScQA (Accuracy)**
| 모델 | Accuracy |
|---|---|
| HoneyBee-7B (재료과학 특화 SFT) | 33.96% |
| GPT-4 (바닐라) | ~62% |
| **HoneyComb (GPT-4 + MatSciKB + ToolHub)** | **79.07%** |

**SciQ (Accuracy)**
| 모델 | Accuracy |
|---|---|
| GPT-3.5 | 90.69% |
| GPT-4 (바닐라) | 90.84% |
| **HoneyComb (GPT-4 기반)** | **96.54%** |

**LLaMP 체적 탄성률 평가 (MAE, 낮을수록 좋음)**
| 모델 | MAE |
|---|---|
| GPT-4 (바닐라) | 41.225 |
| **HoneyComb (ToolHub → MP API)** | HoneyComb 수준으로 대폭 감소 |

---

## 한계점
- MatSciKB의 구체적 규모(항목 수, 커버리지)가 논문에 명시되지 않음
- ToolHub는 Materials Project API 가용성에 의존 (서비스 중단 시 취약)
- 재료과학 이외 도메인 확장성 미검증
- 특정 세부 분야(폴리머, 나노소재) 커버리지 불균형 가능성

---

## 관련 정보
- **논문**: [EMNLP Findings 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.192)
- **arXiv**: [arXiv:2409.00135](https://arxiv.org/abs/2409.00135)
- **DBLP**: [conf/emnlp/ZhangSHML24](https://dblp.org/rec/conf/emnlp/ZhangSHML24)
